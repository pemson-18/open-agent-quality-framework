# Open Agent Quality Framework (OAQF)

**An open, model-independent framework for defining and evaluating AI agent values, reasoning standards, behavioural expectations, and execution quality.**

> Capabilities determine what an agent can do. Values guide what it should do. Quality standards determine how well it does it. Evaluation provides evidence of whether it meets those expectations.

## Project status

**Proposed — version 0.1.0.** This repository is an initial community-oriented proposal, not an established certification scheme or a claim of formal standards-body approval.

## Why OAQF?

AI agent projects often describe capabilities, tools, workflows, and skills. OAQF focuses on the behavioural and quality expectations that should apply while agents use those capabilities.

The project separates:

1. **Values:** [eleven normative values](references/values.md) from honesty and integrity to privacy and accountability.
2. **Reasoning standards:** [six observable reasoning dimensions](references/reasoning.md), including calibration and decision quality.
3. **Execution quality:** [nine quality dimensions](references/execution-quality.md), including simplicity and reproducibility.
4. **Operational boundaries:** authorization, privacy, tool safety, resource bounds, and accurate execution reporting.
5. **Evaluation:** repeatable tests and evidence for specific agent configurations.

## Repository contents

- [`SKILL.md`](SKILL.md) — short executable agent skill with decision, stop, verification, and reporting gates.
- [`references/`](references/) — detailed principles loaded progressively only when needed.
- [`specifications/`](specifications/) — specification index and canonical principle/category registry.
- [`policies/`](policies/) — machine-readable baseline policy.
- [`schemas/`](schemas/) — JSON Schemas for policies, scenarios, and evaluation reports.
- [`tests/`](tests/) — behavioural scenarios and negative validation fixtures.
- [`examples/`](examples/) — inheritable coding-agent profile and explicitly illustrative report.
- [`scripts/validate_repository.py`](scripts/validate_repository.py) — schema, inheritance, reference, gate, and link validation.

## Install and use the skill

1. Copy or clone this repository into the skills location supported by your agent harness, or symlink the directory there. Keep `SKILL.md` at the skill root and preserve `references/` and `tests/` so relative links continue to resolve.
2. Ask the harness to reload skills if required, then invoke **`open-agent-quality-framework`** for a significant, multi-step, or tool-using task.
3. Check that the agent creates a proportionate execution checklist and reports actions using one of the four states: **completed and verified**, **attempted but unsuccessful**, **blocked or not authorized**, or **not attempted**.
4. Keep runtime permissions, approval gates, secret redaction, and auditing in the host environment. Installing the skill provides guidance; it does not enforce security or guarantee compliance.

Start with [the full decision and reporting contract](SKILL.md), then load only the reference documents relevant to the task. Trivial low-risk work should not receive heavyweight ceremony.

## Define and evaluate an agent profile

1. Start from `policies/baseline.yaml` or inherit it with `extends`, as shown in [the coding-agent profile](examples/coding-agent/profile.yaml).
2. Use IDs and categories from the [canonical registry](specifications/values/canonical-ids.md).
3. Link each testable principle to a scenario ID; every referenced scenario must exist and validate.
4. Record results using [the evaluation-report schema](schemas/evaluation-report.schema.json), including configuration, conditions, evidence, and limitations.
5. Treat critical failures as gates, never as points that an aggregate score can offset.
6. Publish only claims supported by the tested configuration and environment.

## Validate locally

Requires Python 3.10 or later:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --requirement requirements-validation.txt
.venv/bin/python scripts/validate_repository.py
```

The same validator runs in GitHub Actions. It checks all policies, scenarios, illustrative reports, profile inheritance, cross-references, critical-failure gates, and local Markdown links. Negative fixtures prove that an unregistered category and a dangling scenario ID are rejected.

## Proposed conformance maturity

| Level | Meaning |
|---|---|
| Defined | Values, policies, capabilities, and boundaries are documented. |
| Evaluated | A specific configuration has documented test results. |
| Enforced | Relevant runtime controls and audit mechanisms are implemented and tested. |

These are descriptive levels, not certification claims. See [conformance requirements](references/conformance.md).

## Design principles

- Model- and framework-independent.
- Human-readable and machine-readable.
- Evidence-oriented and testable.
- Vendor-neutral and open to independent implementation.
- Proportionate to the risk and autonomy of the agent.
- Explicit about uncertainty and limitations.
- Complementary to existing AI governance and security standards.

## Relationship to existing work

OAQF does not replace AI risk-management, safety, security, legal, or agent-governance initiatives. The [initial prior-art and interoperability review](references/prior-art.md) maps the project to NIST AI RMF, ISO/IEC 42001, the OWASP Agentic Top 10, the EU AI Act, vendor behaviour specifications, and related implementations. Further independent comparison is still needed before making novelty or standardisation claims.

## Contributing

Contributions are welcome, especially precise definitions, measurable requirements, scenarios, evaluation methodology, framework adapters, threat models, accessibility improvements, and interoperability reviews.

Read [CONTRIBUTING.md](CONTRIBUTING.md), search existing issues, and open an issue before substantial changes. Use the [RFC template](.github/ISSUE_TEMPLATE/rfc.md) for changes to terminology, schemas, conformance, or normative requirements.

## Roadmap

- [x] Complete an initial review of constitutions and agent-governance specifications.
- [ ] Agree on terminology and normative language through the RFC process.
- [ ] Expand the values and quality catalogue with independent review.
- [ ] Finalise policy, scenario, and evaluation-report schemas.
- [ ] Build a repeatable evaluation runner that emits report artifacts.
- [ ] Add framework adapters and independent implementations.
- [ ] Establish transparent project governance and versioned releases.

## License

The software, schemas, and implementation materials are licensed under Apache-2.0 unless otherwise stated. See [LICENSE](LICENSE).

The project name and conformance terminology are working names and have not been trademark-cleared.
