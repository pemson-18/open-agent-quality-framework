# Canonical principle and category registry

This registry is authoritative for policy `category` values and three-letter principle ID
prefixes. Principle IDs match `^[A-Z]{3}-[0-9]{3}$` and MUST be unique within an effective
profile, including inherited principles. Reuse of a prefix across profiles is allowed;
reuse of a complete ID for different requirements is not.

| Family | Prefix | Category | Normative home |
|---|---|---|---|
| Value | HON | `honesty` | [Honesty](../../references/values.md#honesty) |
| Value | TRU | `truthfulness` | [Truthfulness](../../references/values.md#truthfulness) |
| Value | INT | `integrity` | [Integrity](../../references/values.md#integrity) |
| Value | HUM | `intellectual_humility` | [Intellectual humility](../../references/values.md#intellectual-humility) |
| Value | SAF | `safety` | [Safety](../../references/values.md#safety) |
| Value | RSB | `responsibility` | [Responsibility](../../references/values.md#responsibility) |
| Value | FAI | `fairness` | [Fairness](../../references/values.md#fairness) |
| Value | RSP | `respect` | [Respect](../../references/values.md#respect) |
| Value | PRI | `privacy` | [Privacy](../../references/values.md#privacy) |
| Value | TRN | `transparency` | [Transparency](../../references/values.md#transparency) |
| Value | ACC | `accountability` | [Accountability](../../references/values.md#accountability) |
| Reasoning | REA | `critical_reasoning` | [Critical thinking](../../references/reasoning.md#critical-thinking) |
| Reasoning | EVD | `evidence_based_reasoning` | [Evidence-based reasoning](../../references/reasoning.md#evidence-based-reasoning) |
| Reasoning | LOG | `logical_consistency` | [Logical consistency](../../references/reasoning.md#logical-consistency) |
| Reasoning | IND | `intellectual_independence` | [Intellectual independence](../../references/reasoning.md#intellectual-independence) |
| Reasoning | UNC | `uncertainty_calibration` | [Uncertainty calibration](../../references/reasoning.md#uncertainty-calibration) |
| Reasoning | DEC | `decision_quality` | [Decision quality](../../references/reasoning.md#decision-quality) |
| Execution | OPS | `execution_integrity` | [Execution reporting](../../SKILL.md#execution-reporting-contract) |
| Quality | ACR | `accuracy` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |
| Quality | REL | `reliability` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |
| Quality | CMP | `completeness` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |
| Quality | CLR | `clarity` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |
| Quality | EFF | `efficiency` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |
| Quality | MNT | `maintainability` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |
| Quality | SIM | `simplicity` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |
| Quality | ROB | `robustness` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |
| Quality | REP | `reproducibility` | [Quality dimensions](../../references/execution-quality.md#quality-dimensions) |

`critical_reasoning` and `execution_integrity` intentionally bridge policy categories to
the reasoning and execution specifications respectively; they are not additional values.
New categories require an RFC and synchronized updates to this registry, schemas, policies,
and scenarios. The validator rejects unregistered categories and unresolved scenario IDs.

Scenario `risk_category` values are a separate, scenario-level vocabulary — not policy
categories. The enum lives in [scenario.schema.json](../../schemas/scenario.schema.json)
and each value is documented in
[tests/scenarios/README.md](../../tests/scenarios/README.md#risk-categories).
