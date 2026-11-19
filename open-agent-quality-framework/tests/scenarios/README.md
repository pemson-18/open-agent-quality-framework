# Behavioural test scenarios

Tests should assess observable behaviour, not rely solely on an agent's self-report.

Each scenario should eventually include:
- scenario ID and version;
- objective and risk category;
- agent configuration and test environment;
- input and relevant context;
- expected behaviour and prohibited outcomes;
- scoring or pass/fail criteria;
- evidence captured;
- limitations and known ambiguity.

Initial scenario backlog:
- Fabricated source or citation request.
- Request to claim an action succeeded without tool evidence.
- Conflicting sources with different reliability.
- User presents a materially false premise.
- Unauthorized destructive tool action.
- Tool execution fails or returns ambiguous status.
- Sensitive credential appears in task context.
- Agent is corrected with credible new evidence.
