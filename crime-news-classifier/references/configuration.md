# Target configuration

The shareable template is `config/target.example.json`. The actual spreadsheet target belongs in the ignored local file `config/target.local.json`.

The local file contains the spreadsheet identity, default visible tab, and source/output column contract. After deletion of the former confidence column, `output_columns` is K:P and `output_mapping` explicitly maps K crime status, L good categories, M bad categories, N article attempted, O evidence, and P unmapped candidates. Confidence exists only in local records. The config deliberately does not contain a default row range. Every run must receive explicit physical rows from the user, such as `15-26`.

Before each write, resolve live Sheet metadata and reread the current K:P headers. They must match the configured semantic order. Stop for correction or renewed authorization on a mismatch; never shift values based only on an old run artifact.

An explicit user-provided spreadsheet, tab, or column range overrides the default for that run and must be recorded in the preflight receipt. Do not modify `SKILL.md` to change targets.

The example file contains no private target. The local configuration contains no OAuth tokens, cookies, browser state, or other credentials; keep authentication in the Codex/Google connector environment. Do not commit `target.local.json`.
