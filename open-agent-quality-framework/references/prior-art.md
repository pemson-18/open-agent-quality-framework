# Prior art and interoperability review

Initial desktop review, checked 2026-11-19. This is a source map, not an exhaustive review,
legal analysis, interoperability certification, or claim that no other work shares OAQF's
approach. Links identify the authoritative source where practical.

| Work | What it covers | OAQF relationship |
|---|---|---|
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | Voluntary AI risk management organized around Govern, Map, Measure, and Manage | OAQF's declared values, bounded autonomy, evidence, and re-evaluation can support organizational risk processes; OAQF is not a replacement for them. |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) | Requirements for an organizational AI management system | OAQF artifacts may provide agent-level inputs to a management system. They do not establish ISO conformity or certification. |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Security risks including goal hijack, tool misuse, privilege abuse, context poisoning, and rogue agents | OAQF's tool-output distrust, least privilege, stop conditions, and adversarial scenarios should be mapped to these risks; behavioral guidance is not a security boundary. |
| [EU AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), especially Article 50 | Legal obligations including specified transparency duties | OAQF transparency and execution records may help implementation evidence. Applicability and compliance require qualified legal and organizational assessment. |
| [OpenAI Model Spec](https://model-spec.openai.com/) | Intended model behavior, chain of command, honesty, agency, safety, and illustrative examples | Overlaps with OAQF values and conflict handling. OAQF separately supplies vendor-neutral policy, scenario, and report artifacts; it does not describe OpenAI model compliance. |
| [Anthropic: Claude's Constitution](https://www.anthropic.com/constitution) | Claude's intended character, values, training guidance, priorities, and hard constraints | Overlaps with honesty, safety, helpfulness, and corrigibility. It is model/training guidance from one vendor, not an OAQF conformance evaluation. |
| [Salesforce Atlas Reasoning Engine](https://engineering.salesforce.com/inside-the-brain-of-agentforce-revealing-the-atlas-reasoning-engine/) | A proprietary Agentforce reasoning implementation; associated material discusses action, planning, latency, cost, and trust evaluation | A related implementation example, not an open governance standard. OAQF scenarios could inform independent testing but cannot establish Atlas conformance. |

## Intended contribution

OAQF's intended addition is the combination of:

1. separation of values, reasoning standards, execution quality, and evidence;
2. per-principle traceability from policy identifiers to observable scenarios;
3. machine-readable policy, scenario, and evaluation-report contracts;
4. explicit four-state execution reporting and critical-failure gates;
5. descriptive Defined / Evaluated / Enforced maturity scoped to one configuration.

These are design goals, not a claim that each feature is unprecedented. The next review
should add measured comparisons, versioned crosswalks, and independent implementations.
