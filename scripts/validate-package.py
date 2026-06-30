#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"ERROR: PyYAML is required to validate YAML frontmatter: {exc}")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_LIFECYCLE = (
    "init → PRD → plan → execute → code review → review fix loop → second review "
    "→ multi-angle review → commit readiness → push → complete"
)
CONFIRMED_ISSUE_FIELDS = [
    "Severity",
    "Category",
    "File",
    "Symbol / route / config",
    "Evidence",
    "Root cause",
    "Minimal fix",
    "Verification",
    "Risk",
]
ALLOWED_EVAL_KEYS = {
    "case",
    "expected",
    "expected_mode",
    "expected_output",
    "expected_route",
    "expected_skills",
    "input",
    "must_include",
    "must_not_route",
    "reason",
    "required_reason",
}
REQUIRED_SKILL_SECTIONS = [
    "# Skill:",
    "## Purpose",
    "## When to Use",
    "## Do Not Use When",
    "## Procedure",
    "## Output",
]

REQUIRED_TOOL_PATHS = [
    "scripts/validate-package.py",
    "scripts/route-validate.py",
    "scripts/lifecycle-state-machine.py",
    "scripts/output-guard.py",
    "scripts/verify-skill.py",
]
REQUIRED_SCHEMA_PATHS = [
    "schemas/confirmed-issue.schema.json",
    "schemas/destructive-action.schema.json",
    "schemas/lifecycle-ledger.schema.json",
    "schemas/route-decision.schema.json",
    "schemas/skill.schema.json",
]

errors: list[str] = []
warnings: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path):
    try:
        return json.loads(read_text(path))
    except Exception as exc:
        err(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return None


def load_yaml(path: Path):
    try:
        return yaml.safe_load(read_text(path))
    except Exception as exc:
        err(f"{path.relative_to(ROOT)} is not valid YAML: {exc}")
        return None


def extract_frontmatter(path: Path) -> dict | None:
    text = read_text(path)
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        err(f"{path.relative_to(ROOT)} is missing YAML frontmatter")
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except Exception as exc:
        err(f"{path.relative_to(ROOT)} has invalid YAML frontmatter: {exc}")
        return None
    if not isinstance(data, dict):
        err(f"{path.relative_to(ROOT)} frontmatter must be a mapping")
        return None
    return data


def validate_json_and_yaml() -> None:
    load_json(ROOT / "manifest.json")
    for path in sorted((ROOT / "evals").glob("*.json")):
        load_json(path)
    load_yaml(ROOT / "agents" / "interface.yaml")


def validate_skills() -> set[str]:
    skill_paths = sorted((ROOT / "agent-skills").glob("*/SKILL.md"))
    skill_names = {path.parent.name for path in skill_paths}

    for skill_dir in sorted((ROOT / "agent-skills").iterdir()):
        if skill_dir.is_dir():
            files = list(skill_dir.glob("SKILL.md"))
            if len(files) != 1:
                err(f"{skill_dir.relative_to(ROOT)} must contain exactly one SKILL.md")

    for path in skill_paths:
        rel = path.relative_to(ROOT)
        text = read_text(path)
        frontmatter = extract_frontmatter(path)
        if frontmatter:
            name = frontmatter.get("name")
            if name != path.parent.name:
                err(f"{rel} frontmatter name {name!r} must match directory {path.parent.name!r}")
            if not frontmatter.get("description"):
                err(f"{rel} frontmatter missing description")
            metadata = frontmatter.get("metadata")
            if not isinstance(metadata, dict):
                err(f"{rel} frontmatter missing metadata mapping")
            else:
                for key in ["maturity", "owner", "compatibility"]:
                    if key not in metadata:
                        err(f"{rel} metadata missing {key}")
        for section in REQUIRED_SKILL_SECTIONS:
            if section not in text:
                err(f"{rel} missing required section marker {section}")
        verify_path = path.parent / "verify.sh"
        contract_path = path.parent / "contract.json"
        if not verify_path.exists():
            err(f"{path.parent.relative_to(ROOT)} missing verify.sh")
        if not contract_path.exists():
            err(f"{path.parent.relative_to(ROOT)} missing contract.json")
        else:
            contract = load_json(contract_path)
            if isinstance(contract, dict):
                if contract.get("name") != path.parent.name:
                    err(f"{contract_path.relative_to(ROOT)} name must match skill directory")
                for key in ["preconditions", "postconditions", "verification"]:
                    if not isinstance(contract.get(key), list) or not contract.get(key):
                        err(f"{contract_path.relative_to(ROOT)} missing non-empty {key}")
    return skill_names


def validate_manifest(skill_names: set[str]) -> None:
    manifest = load_json(ROOT / "manifest.json")
    if not isinstance(manifest, dict):
        return
    manifest_skills = set(manifest.get("skills", []))
    if manifest_skills != skill_names:
        err(
            "manifest.skills must match agent-skills/*/SKILL.md; "
            f"missing={sorted(skill_names - manifest_skills)}, extra={sorted(manifest_skills - skill_names)}"
        )
    if manifest.get("canonical_lifecycle") != CANONICAL_LIFECYCLE:
        err("manifest.canonical_lifecycle does not match the package canonical lifecycle")
    for collection_key in ["references", "evals", "schemas", "tools", "tests"]:
        values = manifest.get(collection_key, [])
        if not isinstance(values, list):
            err(f"manifest.{collection_key} must be a list")
            continue
        for value in values:
            if not (ROOT / value).exists():
                err(f"manifest.{collection_key} references missing path {value}")
    for required in REQUIRED_TOOL_PATHS:
        if required not in manifest.get("tools", []):
            err(f"manifest.tools missing {required}")
    for required in REQUIRED_SCHEMA_PATHS:
        if required not in manifest.get("schemas", []):
            err(f"manifest.schemas missing {required}")
    runtime_guards = manifest.get("runtime_guards", {})
    if not isinstance(runtime_guards, dict):
        err("manifest.runtime_guards must be a mapping")
    else:
        for key in ["deterministic_route_validation", "lifecycle_state_machine", "output_fabrication_guard", "package_contract_validation"]:
            value = runtime_guards.get(key)
            if not value or not (ROOT / value).exists():
                err(f"manifest.runtime_guards.{key} references missing guard")
    skill_contracts = manifest.get("skill_contracts", {})
    if set(skill_contracts) != skill_names:
        err("manifest.skill_contracts must have one entry for every skill")
    else:
        for skill, contract in skill_contracts.items():
            for key in ["contract", "verify"]:
                value = contract.get(key) if isinstance(contract, dict) else None
                if not value or not (ROOT / value).exists():
                    err(f"manifest.skill_contracts.{skill}.{key} references missing path")


def validate_interface(skill_names: set[str]) -> None:
    interface = load_yaml(ROOT / "agents" / "interface.yaml")
    if not isinstance(interface, dict):
        return
    lifecycle = interface.get("lifecycle", {})
    if lifecycle.get("canonical") != CANONICAL_LIFECYCLE:
        err("agents/interface.yaml lifecycle.canonical is inconsistent")
    for phase, skill in lifecycle.get("phase_skills", {}).items():
        if skill not in skill_names:
            err(f"agents/interface.yaml phase {phase!r} references unknown skill {skill!r}")
    gates = lifecycle.get("cross_cutting_gates", {})
    for gate_name, gate in gates.items():
        skill = gate.get("skill") if isinstance(gate, dict) else None
        if skill not in skill_names:
            err(f"agents/interface.yaml cross_cutting_gates.{gate_name} references unknown skill {skill!r}")
    for required_gate in ["verification", "reporting"]:
        if required_gate not in gates:
            err(f"agents/interface.yaml missing cross_cutting_gates.{required_gate}")


def validate_entrypoints(skill_names: set[str]) -> None:
    for entrypoint in ["AGENTS.md", "CLAUDE.md"]:
        text = read_text(ROOT / entrypoint)
        for skill in sorted(skill_names):
            count = text.count(f"`{skill}`")
            if count != 1:
                err(f"{entrypoint} must list `{skill}` exactly once; found {count}")
        if CANONICAL_LIFECYCLE not in text:
            err(f"{entrypoint} missing canonical lifecycle string")


def validate_lifecycle_docs() -> None:
    for path in [
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "references" / "review-push-lifecycle.md",
        ROOT / "references" / "skill-routing-table.md",
        ROOT / "references" / "lifecycle-evidence-ledger.md",
    ]:
        if CANONICAL_LIFECYCLE not in read_text(path):
            err(f"{path.relative_to(ROOT)} missing canonical lifecycle string")

    minimal_subset = "init → PRD → plan → execute → verify → report"
    for path in sorted((ROOT / "references").glob("*.md")):
        text = read_text(path)
        if minimal_subset in text:
            lowered = text.lower()
            if "minimal" not in lowered or "subset" not in lowered:
                err(f"{path.relative_to(ROOT)} uses minimal lifecycle without labeling it as a subset")


def validate_output_contracts() -> None:
    output = read_text(ROOT / "references" / "output-templates.md")
    sections = {
        "audit_report": output.split("## audit_report", 1)[1].split("## blocked", 1)[0],
        "code_review_result": output.split("## code_review_result", 1)[1].split("## secondary_review_result", 1)[0],
    }
    for section_name, section_text in sections.items():
        for field in CONFIRMED_ISSUE_FIELDS:
            if f"- {field}:" not in section_text:
                err(f"references/output-templates.md {section_name} missing issue field `{field}`")
    contract = read_text(ROOT / "references" / "issue-evidence-contract.md")
    for field in CONFIRMED_ISSUE_FIELDS:
        if f"- {field}:" not in contract:
            err(f"references/issue-evidence-contract.md missing issue field `{field}`")


def _validate_schema_node(schema_path: str, node: object, location: str = "") -> None:
    if isinstance(node, dict):
        enum = node.get("enum")
        if enum is not None and (not isinstance(enum, list) or not enum):
            err(f"{schema_path} {location or '<root>'} has empty or invalid enum")
        if "const" in node and node.get("const") in (None, ""):
            err(f"{schema_path} {location or '<root>'} has empty const")
        required = node.get("required")
        properties = node.get("properties")
        if required is not None:
            if not isinstance(required, list) or not required:
                err(f"{schema_path} {location or '<root>'} required must be a non-empty list")
            elif isinstance(properties, dict):
                missing = [key for key in required if key not in properties]
                if missing:
                    err(f"{schema_path} {location or '<root>'} required keys missing from properties: {missing}")
        for key, value in node.items():
            _validate_schema_node(schema_path, value, f"{location}.{key}" if location else key)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            _validate_schema_node(schema_path, value, f"{location}[{index}]")


def validate_schemas_and_tools() -> None:
    for schema_path in REQUIRED_SCHEMA_PATHS:
        schema = load_json(ROOT / schema_path)
        if isinstance(schema, dict):
            for key in ["$schema", "$id", "type", "properties"]:
                if key not in schema:
                    err(f"{schema_path} missing {key}")
            _validate_schema_node(schema_path, schema)
            if schema_path == "schemas/destructive-action.schema.json":
                props = schema.get("properties", {})
                if props.get("first_confirmation", {}).get("const") != "DELETE":
                    err("destructive-action schema must require first DELETE confirmation")
                if props.get("second_confirmation", {}).get("const") != "DELETE":
                    err("destructive-action schema must require second DELETE confirmation")
    for tool_path in REQUIRED_TOOL_PATHS:
        path = ROOT / tool_path
        if not path.exists():
            err(f"missing tool {tool_path}")
        elif not path.read_text(encoding="utf-8").startswith("#!/usr/bin/env python3"):
            err(f"{tool_path} must be executable Python script with shebang")
    if not (ROOT / "tests" / "contract_tests.py").exists():
        err("missing tests/contract_tests.py")


def validate_evals(skill_names: set[str]) -> None:
    if not (ROOT / "evals" / "README.md").exists():
        err("evals/README.md is required to document eval case schemas")
    for path in sorted((ROOT / "evals").glob("*.json")):
        data = load_json(path)
        if not isinstance(data, list):
            err(f"{path.relative_to(ROOT)} top-level value must be a list")
            continue
        for index, case in enumerate(data):
            if not isinstance(case, dict):
                err(f"{path.relative_to(ROOT)} case[{index}] must be an object")
                continue
            unknown_keys = set(case) - ALLOWED_EVAL_KEYS
            if unknown_keys:
                err(f"{path.relative_to(ROOT)} case[{index}] has undocumented keys {sorted(unknown_keys)}")
            if case.get("expected_route") not in (None, "no_route") and case.get("expected_route") not in skill_names:
                err(f"{path.relative_to(ROOT)} case[{index}] references unknown expected_route {case.get('expected_route')!r}")
            if "expected_skills" in case:
                for skill in case["expected_skills"]:
                    if skill not in skill_names:
                        err(f"{path.relative_to(ROOT)} case[{index}] references unknown expected skill {skill!r}")


def main() -> int:
    validate_json_and_yaml()
    skill_names = validate_skills()
    validate_manifest(skill_names)
    validate_interface(skill_names)
    validate_entrypoints(skill_names)
    validate_lifecycle_docs()
    validate_output_contracts()
    validate_schemas_and_tools()
    validate_evals(skill_names)

    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        print(f"Validation failed: {len(errors)} error(s)")
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
