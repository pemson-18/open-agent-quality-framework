# Contributing

Thank you for considering a contribution to OAQF.

## Before contributing

- Read [README.md](README.md) and [SKILL.md](SKILL.md).
- Search existing issues and discussions to avoid duplicate work.
- Use the [RFC template](.github/ISSUE_TEMPLATE/rfc.md) for substantial normative,
  terminology, schema, evaluation, or conformance changes.

## What makes a good contribution?

- Clear definitions that avoid ambiguity.
- Requirements with observable or testable outcomes.
- Scenarios with explicit expected and prohibited outcomes.
- Evidence, rationale, relevant prior art, and stated limitations.
- Compatibility with model- and framework-independent use.
- Proportionate requirements that do not add ceremony to trivial low-risk work.

## Normative language

Use these terms consistently:

- **MUST / MUST NOT:** mandatory requirement.
- **SHOULD / SHOULD NOT:** recommended practice; deviations need a reason.
- **MAY:** optional capability or practice.

Do not use normative terms casually. Explain how a requirement can be evaluated. Do not
turn examples or conformance descriptions into certification claims.

## Registry, policy, and scenario changes

- Choose new IDs and categories from the [canonical registry](specifications/values/canonical-ids.md).
  A new category requires synchronized registry, schema, specification, and test updates.
- Add a schema-valid scenario before referencing its ID from a policy.
- Keep scenario filenames identical to their IDs and update related principle IDs together.
- Use `extends` for profile composition and avoid duplicate IDs in the effective profile.
- Set `critical` severity only where failure must gate the overall result; do not hide it
  in an aggregate score.

## Validation

Create a project-local virtual environment and run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --requirement requirements-validation.txt
.venv/bin/python scripts/validate_repository.py
```

Validation covers JSON Schema shape, profile inheritance, unique effective principle IDs,
scenario and report references, report summary counts, critical-failure gates, and local
Markdown links. Negative fixtures ensure invalid categories and dangling scenario IDs fail.
The same checks run in pull-request CI; update schemas, policies, scenarios, and docs together.

## Pull requests

Include:

1. The problem being addressed.
2. The proposed change.
3. Rationale and relevant prior work.
4. Compatibility or migration implications.
5. Validation output, scenarios, or other supporting evidence.
6. Known limitations and untested paths.

Do not claim tests or evaluations ran unless they actually ran and results were inspected.
See the [RFC template](.github/ISSUE_TEMPLATE/rfc.md) for substantial proposals.

## Conduct

Be respectful, evidence-oriented, and open to correction. Critique ideas and implementations,
not people. Disclose relevant conflicts of interest in evaluations and governance decisions.
