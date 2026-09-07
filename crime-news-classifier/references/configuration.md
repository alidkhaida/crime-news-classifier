# Target configuration

The shareable template is `config/target.example.json`. The actual spreadsheet target belongs in the ignored local file `config/target.local.json`.

The local file contains the spreadsheet identity, default visible tab, and source/output column contract. It deliberately does not contain a default row range. Every run must receive explicit physical rows from the user, such as `15-26`.

An explicit user-provided spreadsheet, tab, or column range overrides the default for that run and must be recorded in the preflight receipt. Do not modify `SKILL.md` to change targets.

The example file contains no private target. The local configuration contains no OAuth tokens, cookies, browser state, or other credentials; keep authentication in the Codex/Google connector environment. Do not commit `target.local.json`.
