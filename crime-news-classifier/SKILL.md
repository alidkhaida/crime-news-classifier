---
name: crime-news-classifier
description: Classify large news-link datasets with metadata-first crime routing, human-readable category/subcategory labels, targeted article review, local URL caching, taxonomy feedback, and verified Google Sheets writeback.
metadata:
  short-description: Metadata-first crime news classification
---

# Crime News Classifier

Use this skill for high-volume classification of news links into crime/noncrime status, substantive crime categories, matching subcategories, contextual labels, and future taxonomy candidates.

This is a classification and routing skill. It does not automatically decide whether a case is an editorial “winner” unless the user explicitly requests the separate final-policy stage.

## Non-negotiable boundaries

- Respect the exact physical row range supplied by the user. Never inspect, fetch, analyze, or write outside it.
- Treat the URL as the local cache key, while preserving the original URL unchanged.
- Read title, URL slug, and description before opening an article.
- Open only records marked `needs_article` or explicitly requested for refresh.
- Never convert network, DNS, browser, or fetcher failure into `noncrime`, `unable_to_access`, or a guessed category.
- Only the Sheet worker may modify Google Sheets. It must reread source and target cells, write the exact range, and reread the written cells.
- Preserve source columns and nonempty target values unless the user explicitly authorizes replacement.
- Main categories are additive. A contextual category may be assigned alongside the substantive offense.
- Use full human-readable category and subcategory names in user-facing output. Do not expose codes such as `CN-02`.
- Put each distinct primary category on its own line. Put multiple subcategories belonging to one primary category on the same line, separated by commas.
- Do not force a record into an existing subcategory. Save an `unmapped_candidate` with evidence when the taxonomy lacks a suitable match.
- Keep classification separate from final inclusion/exclusion policy.

## Progressive disclosure

Load only the material required for the current stage:

1. Load this file for routing and boundaries.
2. Load `references/configuration.md` and `config/target.json` when resolving the default spreadsheet target.
3. Load `references/worker-contracts.md` when delegating or coordinating workers.
4. Load `references/output-schema.md` before producing or validating results.
5. Load `references/taxonomy-routing.md` for category selection.
6. Load only the relevant category sections from the archived taxonomy and subcategory guide.
7. Load `references/policy-boundary.md` only for final inclusion/exclusion decisions.
8. Load `references/local-state.md` for cache, resume, version, and recovery work.
9. Load `memory/WORKFLOW_MEMORY.md` before a test or batch run; treat it as tested project context, not as authority over current user instructions or archived policy.
10. Run the permission preflight in `references/preflight.md` before any batch or worker dispatch.
11. Load `references/context-lifecycle.md` when activating the skill, managing compaction, or delegating workers.

Do not put the complete taxonomy or article text into every AI prompt. Local code narrows candidate categories first; AI receives only the record fields and relevant excerpts.

## Workflow

1. Activate this skill once per session using the activation registry; preserve its context marker through compaction.
2. Resolve the target from `config/target.json`, then apply any explicit user override for spreadsheet, tab, or columns. Require an explicit physical row range for every run.
3. Run the preflight and obtain a run-scoped receipt for the exact tab, rows, stages, and capabilities.
4. Build one least-privilege worker envelope per delegated stage.
5. Verify the receipt and envelope before every worker dispatch and every external or persistent side effect.
6. Read the bounded source range and current result range before changing anything.
7. Normalize each URL into `url_key`; retain `original_url`.
8. Check local state. Reuse an existing metadata result or saved article when URL, input fingerprint, taxonomy version, and policy version permit reuse.
9. Run the metadata pass on title, URL slug, and description.
10. Route each record to `crime`, `noncrime`, or `needs_article`.
11. Fetch only `needs_article` records and save fetched text and manifest locally.
12. Assign every supported substantive and contextual category, then map supported subcategories.
13. Capture confidence, evidence phrases, case stage, allegation status, and unmapped candidates.
14. Validate each worker result before merging; then save the complete result record before preparing Sheet values.
15. If writeback is authorized, have only the Sheet worker write the exact output range and verify it by reread.

## Worker routing

Use isolated workers when available:

- `sheet_worker`: metadata, bounded reads, exact writes, readback, and Sheet identity checks. It must not classify articles.
- `metadata_worker`: title/slug/description screening and candidate generation. It must not open URLs or write Sheets.
- `article_fetch_worker`: fetches only assigned URLs, records infrastructure failures, and saves article artifacts. It must not classify or write Sheets.
- `category_worker`: assigns categories/subcategories from the supplied record and relevant taxonomy excerpts. It must not fetch URLs or access Sheets.
- `policy_worker`: applies final client inclusion/exclusion rules only when requested. It must not erase category labels.
- `taxonomy_worker`: reviews unmapped candidates and proposes taxonomy additions or merges. It must not silently promote candidates.

Workers receive only their assigned row payload, relevant references, and controller-supplied state. The controller owns persistence, joins results by `url_key` and physical row, validates them, and decides whether the next stage is allowed.

Use `scripts/worker_protocol.py` to build and validate delegation envelopes. A worker is not considered delegated merely because its role is documented; the host must launch it with the envelope's effective tool allowlist and return its result for validation.

## Output rendering

Human-readable category cells use this shape:

```text
Assault, Weapons & Violent Crime: Nonfatal Shooting, Assault on Officer / First Responder / Protected Worker
Family, Domestic & Relationship Cases: Intimate-Partner Assault / Strangulation
```

Store structured JSON locally even when the Sheet receives a rendered text value.

## Validation and recovery

Before writeback, validate row count, physical-row identity, URL/title identity, category formatting, confidence bounds, required evidence, and status/category consistency. After writeback, reread the exact source and output ranges and record `readback_verified` per row.

Run `scripts/validate_result.py` against staged result JSON before using it for a Sheet write. Run `scripts/normalize_url.py` for deterministic cache-key generation.

If a worker fails, preserve the manifest and partial state. Resume only the failed stage. A taxonomy update should reclassify from saved article text without refetching.

The preflight receipt is a workflow gate, not a credential. If the runtime supports real per-worker tool ACLs, enforce the receipt there too. If it does not, the controller must refuse unauthorized stages and treat the worker contracts as hard behavioral boundaries.

After an explicitly requested test-learning update, append a concise dated entry to `memory/WORKFLOW_MEMORY.md`. Do not rewrite prior entries; record the evidence, decision, and whether the rule is provisional or stable.
