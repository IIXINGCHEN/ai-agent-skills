# AI Agent Skills

语言: [English](README.md) | [中文](README.zh-CN.md)

面向 AI 编码智能体的可复用、证据驱动技能包。

本仓库为 Claude Code、Codex 风格智能体，以及通用 agent-skill 运行时提供一套偏生产级的软件交付技能系统。它定义了一条完整的软件交付生命周期：从项目初始化、PRD、实施计划、执行、代码审查、审查修复、二次审查、多角度审查，到提交准备、推送准备和完成门禁。

## 标准生命周期

```text
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete
```

请按任务需要选择最小充分子集，不要强制执行不需要的阶段。

## 本仓库提供什么

- `CLAUDE.md`：Claude Code 入口规则。
- `AGENTS.md`：Codex / Codex-style agents 入口规则。
- `agent-skills/`：可复用技能。
- `references/`：共享调用、路由、证据、输出和模板契约。
- `evals/`：路由、阻塞状态、对抗用例和输出契约评估。
- `manifest.json`：技能包元数据。
- `agents/interface.yaml`：跨智能体接口元数据。

## 仓库结构

```text
.
├── CLAUDE.md
├── AGENTS.md
├── README.md
├── README.zh-CN.md
├── manifest.json
├── agents/
│   └── interface.yaml
├── agent-skills/
│   ├── lifecycle-orchestrator/
│   ├── project-init/
│   ├── prd-authoring/
│   ├── implementation-planning/
│   ├── plan-execution/
│   ├── verification-gate/
│   ├── code-review-primary/
│   ├── review-fix-loop/
│   ├── code-review-secondary/
│   ├── multi-angle-review/
│   ├── git-commit-readiness/
│   ├── git-push-readiness/
│   ├── completion-gate/
│   └── ...
├── references/
│   ├── skill-routing-table.md
│   ├── lifecycle-evidence-ledger.md
│   ├── review-push-lifecycle.md
│   ├── lifecycle-workflow.md
│   ├── output-templates.md
│   ├── issue-evidence-contract.md
│   ├── strict-review-profile.md
│   ├── prd-template.md
│   └── commands-fusion-map.md
└── evals/
    ├── trigger_cases.json
    ├── route_cases.json
    ├── adversarial_route_cases.json
    ├── blocked_cases.json
    ├── no_route_cases.json
    └── output_contract_cases.json
```

## 技能列表

### 生命周期技能

| Skill | 用途 |
|---|---|
| `lifecycle-orchestrator` | 编排完整生命周期。 |
| `project-init` | 分析项目初始化、依赖、运行时、环境和命令。 |
| `prd-authoring` | 创建或优化产品需求文档（PRD）。 |
| `implementation-planning` | 将任务或 PRD 转换为实施计划。 |
| `plan-execution` | 按已批准计划进行小步、可验证执行。 |
| `verification-gate` | 防止在未验证时声称完成。 |
| `execution-reporting` | 生成基于证据的执行报告。 |
| `completion-gate` | 判定 Done、Done with accepted risks 或 Blocked。 |

### 审查链路技能

| Skill | 用途 |
|---|---|
| `code-review-primary` | 实施后的第一轮证据驱动代码审查。 |
| `review-fix-loop` | 逐项修复已确认的审查问题。 |
| `code-review-secondary` | 修复后的独立二次审查。 |
| `multi-angle-review` | 多视角审查：空间、垂直链路、逆向追踪、安全、数据、错误处理、测试和推送准备。 |

### 审查视角技能

| Skill | 用途 |
|---|---|
| `spatial-review` | 审查文件结构、导入、路径、配置和架构边界。 |
| `vertical-call-chain-review` | 审查 UI / API / service / data 调用链。 |
| `reverse-trace-review` | 从失败或结果反向追踪根因。 |
| `security-review` | 审查认证、输入、密钥、注入、路径、SSRF 和依赖风险。 |
| `data-integrity-hardening` | 确保真实数据源和 schema 一致性。 |
| `error-handling-hardening` | 审查 API / 文件 / 数据库 / 网络 / 配置 / 输入等真实失败场景。 |

### 发现、修复、Git 和安全技能

| Skill | 用途 |
|---|---|
| `repo-discovery` | 发现仓库结构、命令、配置和缺失证据。 |
| `code-search-funnel` | 在编辑前收敛真实变更面。 |
| `test-first-repair` | 用聚焦复现和验证处理高风险修复。 |
| `production-audit-repair` | 执行生产级多维度审查与修复。 |
| `git-commit-readiness` | 检查原子提交准备状态和提交信息。 |
| `git-push-readiness` | 检查推送准备状态，并且只在用户明确要求时推送。 |
| `destructive-safety-gate` | 破坏性操作前要求两次 `DELETE` 确认。 |

## 快速开始

使用完整生命周期：

```md
Use skill:
lifecycle-orchestrator

Lifecycle:
init → PRD → plan → execute → code review → review fix loop → second review → multi-angle review → commit readiness → push → complete

Task:
[describe requested outcome]
```

使用生产级审查与修复：

```md
Use skill:
production-audit-repair

Task:
Perform a production-grade multidimensional audit and repair of this project.

Constraints:
- Remove mock, fake, demo, random, placeholder, and guessed data.
- Use only real APIs, logs, system metrics, database records, configured services, or user-provided files.
- Modify only necessary code.
```

只做审查：

```md
Use skills:
- code-review-primary
- code-review-secondary
- multi-angle-review

Task:
Review the implemented changes and report confirmed issues only.
```

## 可执行契约层

本包以指令为核心，但关键承诺由可执行验证器约束：

- `scripts/validate-package.py` 验证包元数据、技能契约、schema、生命周期一致性、eval schema 和输出字段。
- `scripts/route-validate.py` 提供确定性路由检查，并可回放对抗式路由 eval。
- `scripts/lifecycle-state-machine.py` 验证结构化生命周期台账，阻止非法完成声明。
- `scripts/output-guard.py` 扫描生成报告中的缺失证据字段、不可验证路径引用和未验证完成声明。
- 每个 `agent-skills/*` 目录都包含 `verify.sh` 和 `contract.json`，使 skill 资产可被机械发现和测试。

## 安全模型

始终生效的规则：

- 不编造文件、命令、API、日志、数据、指标、测试结果或项目结构。
- 使用命令、路径、依赖、API 或数据源前必须验证。
- 不发明真实数据源。
- 优先使用最小安全变更。
- 不使用 `--no-verify`。
- 未明确要求时不执行 push。
- push 默认模式是 `readiness-only`。
- 破坏性操作必须经过 destructive safety gate。

## Push 策略

`git-push-readiness` 支持两种模式：

```text
readiness-only
execute-push
```

默认模式：

```text
readiness-only
```

只有当用户明确要求 push 时，才使用 `execute-push`。

禁止对以下分支执行强推：

```text
main
master
protected branches
```

## 路由与证据

使用：

```text
references/skill-routing-table.md
```

选择正确技能。

使用：

```text
references/lifecycle-evidence-ledger.md
```

在 `completion-gate` 前记录生命周期证据。

每个已确认问题应包含：

```text
file
symbol / route / config
evidence
root cause
minimal fix
verification
risk
```

## Evals

本包包含：

```text
evals/trigger_cases.json
evals/route_cases.json
evals/adversarial_route_cases.json
evals/blocked_cases.json
evals/no_route_cases.json
evals/output_contract_cases.json
```

这些 evals 用于检查：

- 技能路由是否正确
- no-route 行为是否正确
- blocked 状态是否正确
- 对抗用例是否被正确处理
- 输出契约是否完整

## 兼容性

面向：

```text
Claude Code
Codex-style agents
Generic agent-skills runtimes
```

## 版本

当前包版本：

```text
1.2.2
```

## License

本项目使用 MIT License。详见 [LICENSE](LICENSE)。
