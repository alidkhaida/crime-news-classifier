# Crime News Classifier Workflow Memory

This is local project memory for tested workflow decisions and observed edge cases. It is append-oriented. Current user instructions and the archived client documents always take precedence over this file.

## Stable workflow decisions

- Process title, URL slug, and description before opening an article.
- Use the URL as the cache lookup key while preserving the original URL.
- Fetch only records marked `needs_article` or explicitly refreshed.
- Main categories are additive; factual context is not erased because of the formal charge.
- Use human-readable category and subcategory names in Sheet output. Do not expose codes such as `CN-02`.
- Put each distinct primary category on its own line. Put multiple subcategories for one primary category on one comma-separated line.
- Preserve unmapped subcategory candidates for later taxonomy review.
- Keep factual classification separate from final inclusion/exclusion policy.
- Confidence is an operational routing/audit signal, not proof; retain it locally and during pilot Sheet testing.
- Every run requires a run-scoped permission receipt covering the exact tab, physical rows, stages, and capabilities; verify it before each worker dispatch or side effect. The receipt is a workflow gate, not a substitute for runtime tool ACLs.
- Delegated workers receive a generated envelope with a session-scoped skill context marker, role-specific references, assigned-row scope, effective capabilities, symbolic tools, and required result fields; validate the envelope-bound result before merging.
- The default target is stored in `config/target.json`; physical rows remain mandatory per run, and explicit user targets override the default only for that run.

## Confirmed pilot learnings

### 2026-09-07 — toddler firearm case

- The same article can belong to both `Assault, Weapons & Violent Crime` and `Child Neglect, Endangerment & Child Abuse`.
- The article supported `Unlawful Firearm Possession / Prohibited Possessor` and `Severe Neglect / Unsafe Living Conditions` because an adult left an unsecured weapon accessible to a toddler who died.
- Do not infer Homicide solely from an accidental death description.

### 2026-09-07 — unmapped subcategory

- Theft of a person’s ashes/cremains fit the Theft/Fraud main category but had no exact approved subcategory. Preserve `Theft of human remains/cremains` as an unmapped candidate.

### 2026-09-07 — worker and Sheet behavior

- The Sheet target was `test`; pilot writes were limited to exact requested physical ranges and reread after writing.
- Source columns A:D were preserved; pilot outputs used E:J.
- A first draft exposed a row-alignment risk, corrected by exact source/output rereads before finalizing.

## Open questions

- Whether production Sheets should retain the confidence column or keep it only in local state.
- Which unmapped candidates should be promoted after frequency and human review.
- Runtime-specific enforcement for per-worker tool allowlists.
