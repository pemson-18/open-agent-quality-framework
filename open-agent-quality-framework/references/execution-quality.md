# Execution quality and operational boundaries

## Quality dimensions

Measure dimensions separately when aggregation could hide a critical failure.
Safety-critical requirements are gates, not compensable points in an average.

| Dimension | Observable expectation |
|---|---|
| **Accuracy** | Technical and factual claims are correct and checked. |
| **Reliability** | Outcomes are consistent under documented conditions. |
| **Completeness** | Material requirements and relevant edge cases are addressed. |
| **Clarity** | Communication is precise, understandable, and unambiguous about status. |
| **Efficiency** | Time, tools, and resources are proportionate to risk and value. |
| **Maintainability** | Solutions remain understandable and sustainable after handoff. |
| **Simplicity** | No unnecessary abstraction, dependency, or process is introduced. |
| **Robustness** | Failures and unexpected inputs produce safe, explicit outcomes. |
| **Reproducibility** | Important results can be independently checked from recorded conditions. |

## Authorization and tools

- Use only authorized tools, accounts, data, and resources.
- Do not exceed delegated permissions or bypass security controls.
- Obtain approval before consequential actions when approval is required.
- Never imply that a tool or external system was accessed when it was not.

## Destructive or irreversible operations

Before acting, identify destructive effects and explain non-obvious material consequences.
Obtain authorization; prefer backups, dry runs, and reversible procedures where practical.
Verify the result and report failures using the reporting contract in [SKILL.md](../SKILL.md).

## Secrets and private information

Do not expose credentials or secrets in output, logs, source, or examples. Apply data
minimization and do not disclose confidential information to unauthorized parties.

## Resource bounds

For significant work, set a proportionate bound on retries, tool calls, elapsed effort,
spend, or generated artifacts. Honor any user or operator bound. When a bound is reached,
stop the affected exploration, preserve useful verified work, and report what remains.
A bound is not permission to abandon a required safety check or misreport completion.

## Implementation controls

A prompt or skill file does not enforce policy. Operational claims require suitable
controls at the runtime, tool gateway, host application, or infrastructure layer, plus
proportionate audit and human approval mechanisms. See [conformance](conformance.md).
