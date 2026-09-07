# Target configuration

The version-controlled default target is `config/target.json`.

It contains the spreadsheet identity, default visible tab, and source/output column contract. It deliberately does not contain a default row range. Every run must receive explicit physical rows from the user, such as `15-26`.

An explicit user-provided spreadsheet, tab, or column range overrides the default for that run and must be recorded in the preflight receipt. Do not modify `SKILL.md` to change targets.

The configuration contains no OAuth tokens, cookies, browser state, or other credentials. Keep authentication in the Codex/Google connector environment.
