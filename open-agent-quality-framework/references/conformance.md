# Evaluation and conformance

Evaluate observable behavior rather than relying only on an agent's self-description.
Use repeatable scenarios, edge cases, and adversarial tests; record configuration, test
conditions, evidence, limitations, and failures. Re-evaluate after material changes to
models, tools, policies, or configuration.

A passing evaluation is evidence about tested scenarios and a specific configuration,
not a guarantee of future behavior. Critical failures MUST NOT be hidden by aggregate scores.
See [evaluation-report.schema.json](../schemas/evaluation-report.schema.json).

## Descriptive maturity levels

### Defined

The configuration declares applicable values, policies, capabilities, and boundaries.
Evidence: versioned policy documents with resolvable identifiers.

### Evaluated

The specific configuration was tested against documented behavioral and quality scenarios.
Evidence: evaluation report identifying evaluator, configuration, conditions, results,
critical failures, and limitations.

### Enforced

Relevant operational controls are implemented and tested, including authorization
boundaries and auditability. Evidence: runtime-control tests and approval/audit records,
in addition to behavioral evaluation.

These levels are descriptive project concepts, not certification. Conformance applies
only to the tested configuration and environment and MUST identify who made the claim.

## Continuous improvement

Accept valid corrections, correct known errors, avoid documented repeated mistakes, and
reassess conclusions as evidence changes. Do not claim persistent learning or memory
unless that capability exists and was actually updated.
