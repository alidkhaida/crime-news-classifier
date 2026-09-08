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
- The private default target is stored in ignored `config/target.local.json`, with `config/target.example.json` as the shareable template; physical rows remain mandatory per run, and explicit user targets override the default only for that run.

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

### 2026-09-08 — category-stage boundaries and routing

- Stable: treat U.S. location as the metadata routing default; do not fetch every article for geography. Review the original article only for a credible foreign-location hint, and assign `Excluded: Out of US` only from affirmative incident-location evidence.
- Stable: forced/coercive human trafficking, forced labor, and exploitation are Good Categories. Noncoercive paid human smuggling is `Excluded: Noncoercive Human Smuggling / Unlawful Migration Transport`; voluntary adult commercial sex is `Prostitution / Commercial Sex`.
- Stable: organized smuggling of illegal goods is the separate Good Category `Organized Contraband Smuggling` and is additive with supported Drugs, Weapons, Theft, or other substantive categories.
- Stable: a supported good or bad parent may stand without a subcategory. Preserve missing good and bad parent/subcategory candidates separately, render both in column Q with evidence notes, and set `needs_review: true`; never force a neighboring label.
- Stable: category classification stops when metadata or the assigned original article supplies enough category evidence. Missing optional policy, stage, allegation, location, arrest, custody, or footage details do not trigger deep research; later selected-category policy skills may reuse saved article text and perform their own research.

### 2026-09-08 — animal routing and Sheet attempt history

- Stable: assign the Bad Category `Animal-Related Stories` whenever animal or wildlife involvement is material. It is additive with supported human-directed, contraband, or other categories; incidental animal mentions do not qualify.
- Stable: column N renders `Yes` whenever the article path was attempted, whether it succeeded (`fetched`) or failed (`fetch_failed` or `infrastructure_error`). Failures require `needs_review: true` and retained diagnostics for manual intervention.
- Stable: confidence remains in local structured records for routing and audit. Column O renders `-` and is not used for confidence output.

### 2026-09-08 — post-deletion Sheet layout correction

- Stable: the user deleted the former Sheet confidence column. The classifier now writes one contiguous K:P range: K crime status, L Good Categories, M Bad Categories, N article attempted, O evidence, and P unmapped candidates. The prior instruction to render a dash in the old confidence column is superseded; confidence remains local and has no Sheet destination.
