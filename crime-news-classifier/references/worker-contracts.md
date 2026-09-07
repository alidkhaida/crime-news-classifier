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
| Policy worker | completed record, policy rules | none | no | no | no | final selection only |
| Taxonomy worker | grouped unmapped candidates | taxonomy proposals only | no | no | no | merge/new-candidate recommendation |

Workers must never broaden their inputs or tools. A worker result is not proof until the controller validates row identity, URL identity, required fields, and status consistency.

## Tool allowlists

When the runtime supports per-worker tool selection, apply these allowlists:

- `sheet_worker`: `mcp__codex_apps__google_drive_get_spreadsheet_metadata`, `mcp__codex_apps__google_drive_get_spreadsheet_cells`, `mcp__codex_apps__google_drive_get_spreadsheet_range`, and `mcp__codex_apps__google_drive_batch_update_spreadsheet`. No web tools and no arbitrary Sheet search.
- `metadata_worker`: local deterministic scripts and its assigned payload only. No web tools, Drive tools, or Sheet tools.
- `article_fetch_worker`: the configured article-fetch route or `web__run` for assigned URLs only. No Sheet tools and no classification references beyond fetch identity instructions.
- `category_worker`: local read-only reference access and its assigned payload only. No web tools, Drive tools, or Sheet tools.
- `policy_worker`: local read-only access to `references/policy-boundary.md` and completed records only. No web tools or Sheet tools.
- `taxonomy_worker`: local read-only taxonomy and candidate-ledger access, with proposal-file write access only. No web tools or Sheet tools.
- `controller`: local state/manifest tools and read-only Sheet metadata/range tools for orchestration; delegate Sheet mutation to `sheet_worker`.

If the runtime cannot enforce an actual tool allowlist, treat this matrix as a hard behavioral contract and have the controller reject outputs that contain unauthorized external actions.

## Sheet worker contract

Allowed: spreadsheet metadata, exact bounded source reads, current target reads, exact writes when authorized, exact readback, and verification receipts.

Forbidden: article classification, broad tab scans, guessed tab names, writes outside the configured tab/range, and treating API success as verification.

Required write sequence:

1. Resolve spreadsheet ID, visible tab title, and sheet ID from metadata.
2. Read source and target cells immediately before the write.
3. Preflight row count, column count, physical row order, and target identity.
4. Write one precise rectangular range.
5. Reread the exact written range and source identity cells.
6. Save `readback_verified` or a row-specific conflict.

## Metadata worker contract

Input: physical row, URL, title, description, URL slug, and relevant category index.

Output: `crime`, `noncrime`, or `needs_article`; candidate categories; evidence phrases; confidence; and routing reason.

It must not infer detailed facts absent from metadata. It may use an explicit URL slug clue, but a vague slug is not proof.

## Article-fetch worker contract

Input: only rows marked `needs_article` and their original URLs.

Output: fetch manifest, final URL, status, content hash, saved text path, identity checks, and infrastructure error details.

It must not turn blocked access, DNS failure, browser failure, or rate limiting into an article decision.

## Category worker contract

Input: metadata result or saved article text, relevant category references, and output schema.

Output: all supported substantive categories, context categories, subcategories, case stage, allegation status, evidence spans, confidence, and unmapped candidates.

Main categories are additive. A formal charge is evidence, not a limit on factual category assignment.

## Policy and taxonomy contracts

The policy worker outputs separate `selection_outcome` and `selection_reason`; it must not delete or replace factual categories.

The taxonomy worker outputs candidate merge, candidate new subcategory, or retain-as-rare; it must not silently promote candidates.
