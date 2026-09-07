# Context lifecycle and subagent delegation

The host controller must manage skill context separately from ordinary chat history.

## Activation

Call `scripts/activation_registry.py activate` once per session and skill. It records the skill content hash, resource inventory, and a `protected_context` marker. If the same skill hash is activated again in the same session, treat it as `already_active` and do not inject the entrypoint a second time.

The host should preserve the activated entrypoint and its identifying wrapper through context compaction. The registry marker is evidence for the host; it does not itself change the host's compaction algorithm.

## Delegation

Use `scripts/worker_protocol.py build` to create one envelope per worker. A delegated worker receives:

- its role and stage;
- only its assigned physical rows and input artifact;
- the run-scoped preflight receipt and effective capability intersection;
- the skill entrypoint plus only the references listed for that role;
- symbolic allowed tools that the runtime adapter must map to real tools;
- required result fields and forbidden actions.

The host must launch the worker with the envelope's tool allowlist, not with the controller's full tool set. It must not give a worker the full spreadsheet, full taxonomy, unrelated article text, or other workers' outputs unless the envelope explicitly requires them.

After completion, run `scripts/worker_protocol.py validate` before merging the result. Reject results with mismatched worker identity, rows outside scope, duplicate rows, unapproved capabilities, or unauthorized actions.

## Host responsibilities

The skill package can generate the registry and envelopes, but only the host can enforce:

1. protected skill content during compaction;
2. actual tool allowlists for a subagent session;
3. user consent prompts at the host permission layer;
4. isolation between worker sessions.

If the host cannot provide those controls, run the stages in the controller and fail closed on envelope or receipt violations; do not claim that a file-based manifest is a security sandbox.
