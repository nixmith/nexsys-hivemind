# Regression Bank Prompt

Copy the block below into a fresh Claude Project conversation.

---

Answer the following questions about the HomeSynapse Core architecture. Be precise with numbers, type names, module names, and constraint citations. If you are genuinely uncertain after searching your project knowledge, say UNCERTAIN — but exhaust your search first (try at least 3 variant search terms before declaring uncertain). Number your answers 1–5.

1. What is the exact ordering between ConfigurationChangeListener and the config_changed domain event? Which fires first? Describe the full three-step sequence.

2. What does the NO_SYNCHRONIZED_METHODS ArchUnit rule detect? What does it NOT detect? How is the gap in coverage addressed?

3. How many ArchUnit rules exist in HomeSynapseArchRules.java (in the homesynapse-app test source set)? Does the event-bus module have its own separate ArchUnit rule for JDBC isolation? If not, how is that constraint enforced?

4. Is AMD-39 (journal_size_limit increase) applied or withdrawn? What journal_size_limit value is in effect across all DeploymentProfile values?

5. How many parameters does EventPublisher.publishRoot() take? Where does the actorRef value come from if it's not a parameter?
