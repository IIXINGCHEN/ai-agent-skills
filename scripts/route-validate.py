#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = set(json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))['skills'])

NO_ROUTE = re.compile(r'写诗|poem|润色|translate|翻译|闲聊|joke|故事', re.I)
BLOCKED = re.compile(r'没有源码|no source|无源码|real data source absent|没有真实数据源', re.I)


def has(text: str, pattern: str) -> bool:
    return re.search(pattern, text, re.I) is not None


def decision(text: str, route: str, skills: list[str] | None = None, rules: list[str] | None = None, *, confidence: str = 'high', constraints: list[str] | None = None, mode: str | None = None, blocked_reasons: list[str] | None = None) -> dict:
    supporting = []
    for skill in skills or []:
        if skill not in supporting:
            supporting.append(skill)
    if route in SKILLS and route not in supporting:
        supporting.insert(0, route)
    result = {
        'input': text,
        'route': route,
        'primary_route': route,
        'supporting_skills': supporting,
        'confidence': confidence,
        'matched_rules': rules or [],
        'constraints': constraints or [],
        'blocked_reasons': blocked_reasons or [],
    }
    if mode:
        result['mode'] = mode
    return result


def decide(text: str) -> dict:
    normalized = text.strip()
    if BLOCKED.search(normalized):
        return decision(text, 'blocked', [], ['blocked'], blocked_reasons=['missing required source or evidence'])
    if NO_ROUTE.search(normalized):
        return decision(text, 'no_route', [], ['no_route'])

    constraints: list[str] = []
    if has(normalized, r'do not push|don[’\']t push|不要推送|不要 push|not push'):
        constraints.append('no_push')
    if has(normalized, r'do not fix|不要修改|不要修复|only check|只检查'):
        constraints.append('no_fix')
    if has(normalized, r'only|仅|只'):
        constraints.append('scope_limited')

    # Full lifecycle / orchestrated workflows.
    if 'init → PRD → plan → execute' in normalized or has(normalized, r'complete .*lifecycle support|support init.*PRD.*plan.*execute'):
        return decision(text, 'lifecycle-orchestrator', [
            'lifecycle-orchestrator', 'project-init', 'prd-authoring', 'implementation-planning',
            'plan-execution', 'code-review-primary', 'review-fix-loop', 'code-review-secondary',
            'multi-angle-review', 'git-commit-readiness', 'git-push-readiness', 'completion-gate'
        ], ['canonical_lifecycle'], constraints=constraints)

    # Production audit outranks ordinary review/planning.
    if has(normalized, r'生产级|production-grade|multidimensional audit|多维度审查|full project consistency|模拟数据|mock|fake|placeholder|真实数据|real data'):
        return decision(text, 'production-audit-repair', ['production-audit-repair'], ['production_audit'], constraints=constraints)

    # Push readiness only for positive push-safety/push intent, not review constraints such as "do not push".
    if has(normalized, r'force push|push is safe|whether push is safe|check if pushing is safe|can i push|push this branch|after reviews pass,? push|push to the remote|publish branch|create PR|PR readiness'):
        mode = 'readiness-only' if 'no_push' in constraints or has(normalized, r'push is safe|whether push is safe|check if pushing is safe') else None
        return decision(text, 'git-push-readiness', ['git-commit-readiness', 'git-push-readiness', 'completion-gate'], ['push_readiness'], constraints=constraints, mode=mode)

    if has(normalized, r'final lifecycle status|summarize final|complete the lifecycle|complete .*with evidence|final decision|decide done|done or blocked|完成门禁|completion|final status|最终状态|lifecycle result'):
        return decision(text, 'completion-gate', ['completion-gate'], ['completion'], constraints=constraints)

    if has(normalized, r'after execute.*code review.*fix.*second review|code review.*fix.*second review'):
        return decision(text, 'code-review-primary', ['code-review-primary', 'review-fix-loop', 'code-review-secondary'], ['review_chain'], constraints=constraints)

    if has(normalized, r'second review|二次审查|final review|regression review'):
        return decision(text, 'code-review-secondary', ['code-review-secondary'], ['second_review'], constraints=constraints)

    if has(normalized, r'multi-angle|多角度|strict profile|strict review|production readiness review|spatial.*vertical|security.*data integrity|严格审查'):
        skills = ['multi-angle-review']
        if has(normalized, r'strict profile|strict review|严格审查'):
            skills = ['repo-discovery', 'code-search-funnel', 'spatial-review', 'vertical-call-chain-review', 'security-review', 'multi-angle-review']
        return decision(text, 'multi-angle-review', skills, ['multi_angle'], constraints=constraints)

    if has(normalized, r'review the changed files|review these files|review changed|code review|代码审查|pre-commit review|审查变更|检查代码问题|只检查代码'):
        skills = ['code-review-primary']
        if has(normalized, r'只检查|only check|检查代码问题'):
            skills = ['repo-discovery', 'code-search-funnel', 'spatial-review', 'code-review-primary']
        return decision(text, 'code-review-primary', skills, ['code_review'], constraints=constraints)


    if has(normalized, r'破坏性|destructive safety|DELETE 确认|回滚检查|rollback.*destructive'):
        return decision(text, 'destructive-safety-gate', ['destructive-safety-gate'], ['destructive_safety'], constraints=constraints)

    if has(normalized, r'错误处理|error handling|失败处理|API.*文件.*网络|network failure|file failure'):
        return decision(text, 'error-handling-hardening', ['error-handling-hardening'], ['error_handling'], constraints=constraints)

    if has(normalized, r'反向追踪|reverse trace|失败日志|错误响应.*根因|root cause.*logs'):
        return decision(text, 'reverse-trace-review', ['reverse-trace-review'], ['reverse_trace'], constraints=constraints)

    if has(normalized, r'修复登录接口|500 错误|bug|failed test|修复.*错误|fix .*bug'):
        return decision(text, 'test-first-repair', ['repo-discovery', 'code-search-funnel', 'test-first-repair', 'verification-gate'], ['bug_fix'], constraints=constraints)

    if has(normalized, r'假的监控|fake metrics|mock data|data integrity|source of truth|真实系统指标|真实来源|schema'):
        return decision(text, 'data-integrity-hardening', ['data-integrity-hardening', 'vertical-call-chain-review', 'verification-gate'], ['data_integrity'], constraints=constraints)

    if has(normalized, r'先制定.*计划.*执行|plan.*execute|PRD.*生成.*计划.*执行|从 PRD 生成实施计划并执行'):
        return decision(text, 'implementation-planning', ['implementation-planning', 'plan-execution', 'verification-gate', 'execution-reporting'], ['plan_then_execute'], constraints=constraints)

    if has(normalized, r'execute the approved plan|execute approved plan|执行已批准计划|执行计划|execute plan|implement approved|按计划执行|开始执行'):
        return decision(text, 'plan-execution', ['plan-execution', 'verification-gate'], ['execution'], constraints=constraints)

    if has(normalized, r'implementation plan|create an implementation plan|make an implementation plan|plan from .*PRD|从.*PRD.*计划|实施方案|设计方案|制定计划|创建计划'):
        return decision(text, 'implementation-planning', ['implementation-planning'], ['planning'], constraints=constraints)

    if has(normalized, r'write a PRD|create a PRD|create .*PRD|写 PRD|为.*写 PRD|\bPRD\b only|需求|requirements|MVP|user stories|产品需求'):
        return decision(text, 'prd-authoring', ['prd-authoring'], ['requirements'], constraints=constraints)

    if has(normalized, r'初始化|init|setup|set up|run locally|bootstrap|onboard|启动|安装依赖'):
        return decision(text, 'project-init', ['project-init', 'repo-discovery'], ['setup'], constraints=constraints)

    return decision(text, 'no_route', [], [], confidence='low', constraints=constraints)


def run_evals() -> int:
    failures: list[str] = []
    for path in sorted((ROOT / 'evals').glob('*.json')):
        cases = json.loads(path.read_text(encoding='utf-8'))
        for index, case in enumerate(cases):
            if 'input' not in case:
                continue
            result = decide(case['input'])
            actual_routes = set(result.get('supporting_skills', [])) | {result['route']}
            expected_route = case.get('expected_route')
            if expected_route and expected_route != result['route']:
                failures.append(f'{path.name}[{index}] expected_route={expected_route} actual={result["route"]}')
            if 'expected_skills' in case:
                expected = set(case['expected_skills'])
                missing = sorted(expected - actual_routes)
                if missing:
                    failures.append(f'{path.name}[{index}] missing expected_skills={missing} actual={sorted(actual_routes)}')
            if case.get('expected') == 'no_route' and result['route'] != 'no_route':
                failures.append(f'{path.name}[{index}] expected no_route actual={result["route"]}')
            if 'must_not_route' in case:
                forbidden = sorted(set(case['must_not_route']) & actual_routes)
                if forbidden:
                    failures.append(f'{path.name}[{index}] forbidden route selected: {forbidden}')
            if case.get('expected_mode') and result.get('mode') != case['expected_mode']:
                failures.append(f'{path.name}[{index}] expected_mode={case["expected_mode"]} actual={result.get("mode")}')
    if failures:
        for failure in failures:
            print('ERROR:', failure)
        return 1
    print('Route validation passed')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description='Deterministic skill route validator')
    parser.add_argument('input', nargs='*')
    parser.add_argument('--evals', action='store_true')
    args = parser.parse_args()
    if args.evals:
        return run_evals()
    text = ' '.join(args.input)
    print(json.dumps(decide(text), ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
