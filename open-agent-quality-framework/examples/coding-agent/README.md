# Coding agent example

[profile.yaml](profile.yaml) demonstrates policy composition with `extends: baseline` and
adds software-specific requirements:

- Do not claim tests pass unless they ran and their results were inspected.
- Identify security-sensitive changes and explain relevant risks.
- Do not expose secrets in source files, logs, patches, or examples.
- Prefer minimal, maintainable changes without unrelated refactoring.
- Report untested paths and environmental limitations.
- Obtain authorization before destructive database, infrastructure, deployment, or repository-history operations.

[evaluation-report.example.json](evaluation-report.example.json) demonstrates the report
schema only. Its `status` is `illustrative`, and its limitations explicitly state that no
agent was evaluated; it is not an Evaluated or Enforced conformance claim.

This is an illustrative profile, not a tested adapter for any particular coding agent.
The validator resolves inherited principles and ensures that every scenario reference exists.
