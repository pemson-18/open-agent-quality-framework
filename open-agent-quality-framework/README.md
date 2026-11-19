# Open Agent Quality Framework (OAQF)

**An open, model-independent framework for defining and evaluating AI agent values, reasoning standards, behavioural expectations, and execution quality.**

> Capabilities determine what an agent can do. Values guide what it should do. Quality standards determine how well it does it. Evaluation provides evidence of whether it meets those expectations.

## Project status

**Proposed — version 0.1.0.** This repository is an initial community-oriented proposal, not an established certification scheme or a claim of formal standards-body approval.

## Why OAQF?

AI agent projects often describe capabilities, tools, workflows, and skills. OAQF focuses on the behavioural and quality expectations that should apply while agents use those capabilities.

The project separates:

1. **Values:** honesty, truthfulness, integrity, safety, responsibility, fairness, respect, and transparency.
2. **Reasoning standards:** critical thinking, evidence-based reasoning, logical consistency, and intellectual humility.
3. **Execution quality:** accuracy, reliability, completeness, clarity, efficiency, maintainability, and robustness.
4. **Operational boundaries:** authorization, privacy, tool safety, and accurate execution reporting.
5. **Evaluation:** repeatable tests and evidence for specific agent configurations.

## Repository contents

- [`SKILL.md`](SKILL.md) — reusable agent skill.
- [`specifications/`](specifications/) — human-readable value and quality specifications.
- [`policies/`](policies/) — example machine-readable policy.
- [`schemas/`](schemas/) — initial JSON Schema for policy validation.
- [`tests/`](tests/) — proposed behavioural test scenarios.
- [`examples/`](examples/) — example agent profiles.

## Quick adoption

An agent developer can start by:

1. Reviewing `SKILL.md`.
2. Selecting the principles relevant to the agent's use case.
3. Declaring applicable policies in YAML.
4. Translating requirements into observable tests.
5. Implementing runtime controls for permissions and safety.
6. Publishing evaluation results with configuration, test conditions, and limitations.

A skill or prompt provides behavioural guidance; it does not independently enforce security or guarantee compliance.

## Proposed conformance maturity

| Level | Meaning |
|---|---|
| Defined | Values, policies, capabilities, and boundaries are documented. |
| Evaluated | A specific configuration has documented test results. |
| Enforced | Relevant runtime controls and audit mechanisms are implemented and tested. |

These are proposed descriptive levels, not certification claims.

## Design principles

- Model- and framework-independent.
- Human-readable and machine-readable.
- Evidence-oriented and testable.
- Vendor-neutral and open to independent implementation.
- Proportionate to the risk and autonomy of the agent.
- Explicit about uncertainty and limitations.
- Complementary to existing AI governance and security standards.

## Relationship to existing work

OAQF does not aim to replace AI risk-management, safety, security, or agent-governance initiatives. It should map to and reuse relevant existing work where appropriate. The project needs a documented prior-art and interoperability review before claiming novelty or standardisation.

## Contributing

Contributions are welcome, especially:
- precise definitions and measurable behavioural requirements;
- test scenarios and evaluation methodology;
- framework adapters;
- threat models and failure analysis;
- accessibility, documentation, and interoperability improvements.

Open an issue before making substantial changes. Please include the problem, proposed change, rationale, compatibility implications, and how the change could be evaluated.

## Roadmap

- [ ] Review existing constitutions and agent-governance specifications.
- [ ] Agree on terminology and normative language.
- [ ] Expand the initial values and quality catalogue.
- [ ] Finalise machine-readable policy and evaluation schemas.
- [ ] Build a repeatable evaluation runner.
- [ ] Add framework adapters and independent implementations.
- [ ] Establish transparent project governance and an RFC process.

## License

The software, schemas, and implementation materials in this repository are licensed under Apache-2.0 unless otherwise stated. See [`LICENSE`](LICENSE).

The project name and conformance terminology are working names and have not been trademark-cleared.
