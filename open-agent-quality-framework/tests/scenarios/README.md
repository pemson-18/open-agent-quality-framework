# Behavioural test scenarios

Scenarios assess observable behaviour, not an agent's self-report. Each `*.yaml` file is
validated against [scenario.schema.json](../../schemas/scenario.schema.json); its filename
must exactly match its scenario `id`.

Every scenario declares:

- schema and scenario versions;
- objective, risk category, and severity;
- related principle IDs and agent configuration;
- input and relevant context;
- expected behaviour and prohibited outcomes;
- explicit pass/fail criteria;
- evidence to capture and known limitations.

The [baseline policy](../../policies/baseline.yaml) is the machine-readable index of the
current suite. Policy `evaluation` references and scenario `related_principles` values
are cross-checked by the repository validator. Add a scenario before referring to it; use
the [canonical registry](../../specifications/values/canonical-ids.md) for principle IDs.

## Risk categories

`risk_category` is scenario-level vocabulary, separate from the policy `category` values in
the [canonical registry](../../specifications/values/canonical-ids.md). The enum is defined
in [scenario.schema.json](../../schemas/scenario.schema.json):

| Value | Covers |
|---|---|
| `integrity` | Acting consistently with stated values and commitments |
| `evidence` | Claims grounded in verifiable observations or identified sources |
| `reasoning` | Sound inference, uncertainty calibration, and intellectual independence |
| `safety` | Preventing harm, including unauthorized destructive actions |
| `security` | Resisting injected instructions and misuse of tools |
| `privacy` | Protecting credentials and sensitive personal data |
| `execution` | Faithful action reporting and tool-failure handling |

Changing this vocabulary requires an RFC and synchronized schema, scenario, and
documentation updates.

A scenario pass is evidence only for its documented configuration and conditions. Record
results using [evaluation-report.schema.json](../../schemas/evaluation-report.schema.json).
Critical failures must gate the overall result rather than disappear into an average.

Run validation from the repository root using the commands in [README.md](../../README.md#validate-locally).
Negative fixtures in `tests/fixtures/invalid/` ensure malformed categories and unresolved
scenario references actually fail CI.
