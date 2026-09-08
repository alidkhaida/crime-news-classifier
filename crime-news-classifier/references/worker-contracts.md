# Worker contracts and permissions

The controller owns the run ledger, physical-row mapping, URL cache, stage transitions, final aggregation, and worker result joins. Workers are narrow and non-overlapping.

## Preflight gate

Before dispatch, the controller must have a valid run-scoped receipt from `scripts/preflight.py`. It verifies the receipt for the exact stage, capability, tab, and physical row bounds. A missing, expired, denied, or scope-mismatched receipt blocks the operation.

The effective worker permissions are:

`approved capabilities from receipt ∩ worker role allowlist ∩ current stage requirements`

The worker receives no other tools or data. A receipt does not itself grant OS, connector, browser, or network access; runtimes should enforce those permissions independently. If runtime enforcement is unavailable, the controller must fail closed and reject unauthorized worker outputs or side effects.

## Permission matrix

| Worker | Local read | Local write | Article/network | Sheets read | Sheets write | AI decision |
|---|---|---|---|---|---|---|
| Controller | config, state, manifests | run state, receipts | no direct fetch by default | metadata and bounded ranges | only when explicitly authorized | orchestration only |
| Sheet worker | assigned range payload | receipts only | no | exact assigned tab/range | exact assigned output range only | no |
| Metadata worker | assigned row payload, taxonomy index | none | no | no | no | crime gate/candidates |
| Article-fetch worker | assigned URLs, fetch config | article text, manifest | assigned URLs only | no | no | no |
| Category worker | assigned record, relevant taxonomy excerpts | none | no | no | no | categories/subcategories |
| Bad-category worker | assigned record, bad taxonomy excerpts | none | no | no | no | bad categories/subcategories |
| Policy worker | completed record, policy rules | none | no | no | no | final selection only |
| Taxonomy worker | grouped unmapped candidates | taxonomy proposals only | no | no | no | merge/new-candidate recommendation |

Workers must never broaden their inputs or tools. A worker result is not proof until the controller validates row identity, URL identity, required fields, and status consistency.

## Tool allowlists

When the runtime supports per-worker tool selection, apply these allowlists:

- `sheet_worker`: `mcp__codex_apps__google_drive_get_spreadsheet_metadata`, `mcp__codex_apps__google_drive_get_spreadsheet_cells`, `mcp__codex_apps__google_drive_get_spreadsheet_range`, and `mcp__codex_apps__google_drive_batch_update_spreadsheet`. No web tools and no arbitrary Sheet search.
- `metadata_worker`: local deterministic scripts and its assigned payload only. No web tools, Drive tools, or Sheet tools.
- `article_fetch_worker`: the configured article-fetch route or `web__run` for assigned URLs only. No Sheet tools and no classification references beyond fetch identity instructions.
- `category_worker`: local read-only reference access and its assigned payload only. No web tools, Drive tools, or Sheet tools.
- `bad_category_worker`: local read-only access to `references/bad-taxonomy.md` and its assigned payload only. No web tools, Drive tools, or Sheet tools.
- `policy_worker`: local read-only access to `references/policy-boundary.md` and completed records only. No web tools or Sheet tools.
- `taxonomy_worker`: local read-only taxonomy and candidate-ledger access, with proposal-file write access only. No web tools or Sheet tools.
- `controller`: local state/manifest tools and read-only Sheet metadata/range tools for orchestration; delegate Sheet mutation to `sheet_worker`.

If the runtime cannot enforce an actual tool allowlist, treat this matrix as a hard behavioral contract and have the controller reject outputs that contain unauthorized external actions.

## Sheet worker contract

Allowed: spreadsheet metadata, exact bounded source reads, current target reads, exact writes when authorized, exact readback, and verification receipts.

Forbidden: article classification, broad tab scans, guessed tab names, writes outside the configured tab/range, and treating API success as verification.

Required write sequence:

1. Resolve spreadsheet ID, visible tab title, and sheet ID from metadata.
2. Read source cells, K:P headers, and target cells immediately before the write. Confirm the live headers match the configured output mapping.
3. Preflight row count, six-column K:P width, semantic header order, physical row order, and target identity. Stop on any header or position mismatch.
4. Write one precise K:P rectangle using the current post-deletion layout.
5. Reread the exact written K:P range and source identity cells.
6. Save `readback_verified` or a row-specific conflict.

Sheet rendering rules: column N writes `Yes` when the controller's final local record has `article.status: fetched`, `fetch_failed`, or `infrastructure_error`; valid reused cached article text counts as `fetched`. It writes `-` only for `not_needed`. N records that the article path was attempted, not that it necessarily succeeded, and must not be cleared merely because classification is complete. Column O is evidence and P is unmapped candidates. The deleted confidence field has no Sheet column; confidence stays local.

## Metadata worker contract

Input: physical row, URL, title, description, URL slug, and relevant category index.

Output: `crime`, `noncrime`, or `needs_article`; candidate categories; evidence phrases; confidence; routing reason; and an inexpensive location assessment based on title, description, and URL slug.

It must not infer detailed facts absent from metadata. It may use an explicit URL slug clue, but a vague slug is not proof. In the absence of a credible foreign-location signal it uses the U.S. routing default without requesting an article solely for geography.

## Article-fetch worker contract

Input: only rows marked `needs_article` for category ambiguity/conflict/gap or credible foreign-location hints, and their original URLs. Missing optional case-stage or future-policy facts are not fetch reasons.

Output: fetch manifest, final URL, status, content hash, saved text path, identity checks, and failure or infrastructure-error details. A `fetch_failed` or `infrastructure_error` result must set `needs_review: true` so column N can show the attempted check while manual intervention remains explicit.

It must not turn blocked access, DNS failure, browser failure, or rate limiting into an article decision.

## Category worker contract

Input: metadata result or saved article text, relevant category references, and output schema.

Output: all supported Good Categories, context categories, subcategories, readily available case stage/allegation/location clues, evidence spans, confidence, and good unmapped candidates.

Main categories are additive. A formal charge is evidence, not a limit on factual category assignment.

The category worker must fail closed on taxonomy gaps: it must not select a neighboring or “closest” parent merely to avoid a blank category. A supported parent may stand alone; if its subcategory is missing, retain the parent, set `needs_review: true`, and add an unmapped subcategory candidate with evidence. Human Trafficking, Forced Labor & Exploitation requires force, fraud, coercion, control, forced labor, debt bondage, abuse of vulnerability, child commercial exploitation, or an explicit trafficking/exploitation allegation. Organized Contraband Smuggling requires an organized illegal-goods movement or concealment operation, not ordinary possession or transport.

## Bad-category worker contract

Input: the assigned record, metadata or saved article evidence, and the relevant sections of `references/bad-taxonomy.md`.

Output: every supported Bad Category and bad subcategory, bad evidence phrases, confidence, and `unmapped_bad_candidates` when a supported bad family lacks a maintained subcategory. It assigns `Animal-Related Stories` whenever animal or wildlife involvement is material, even when human-directed crime also supports other categories; incidental mentions do not qualify. It applies `Excluded: Out of US` only from affirmative incident-location evidence and uses `Excluded: Noncoercive Human Smuggling / Unlawful Migration Transport` when organized human movement is supported without trafficking/exploitation evidence.

It must not change `crime_status`, Good Categories, source fields, or final selection outcome. It must not infer a bad category from a keyword alone.

## Policy and taxonomy contracts

The policy worker outputs separate `selection_outcome` and `selection_reason`; it must not delete or replace factual categories.

The taxonomy worker outputs candidate merge, candidate new subcategory, or retain-as-rare; it must not silently promote candidates.
