# Output schema

## Local record

```json
{
  "url_key": "string",
  "original_url": "string",
  "physical_row": 0,
  "input_fingerprint": "string",
  "metadata_decision": {"status":"crime | noncrime | needs_article","reason":"string","confidence":0.0,"evidence":["string"]},
  "location_assessment": {"status":"assumed_us | confirmed_us | confirmed_non_us | unresolved_foreign_hint","evidence":["string"]},
  "article": {"status":"not_needed | fetched | fetch_failed | infrastructure_error","final_url":"string|null","content_hash":"string|null","text_path":"string|null","error_type":"string|null","error_detail":"string|null"},
  "good_categories": {"Main Category Name":["Subcategory Name"]},
  "bad_categories": {"Bad Category Name":["Bad Subcategory Name"]},
  "unmapped_candidates": [{"parent_category":"string","candidate_name":"string","evidence":"string","confidence":0.0}],
  "unmapped_bad_candidates": [{"parent_category":"string","candidate_name":"string","evidence":"string","confidence":0.0}],
  "case_stage": "incident | investigation | alert | arrest | charge | plea | trial | conviction | sentencing | appeal | update | unknown",
  "allegation_status": "suspected | alleged | charged | admitted | convicted | dismissed | acquitted | undetermined",
  "evidence_spans": ["string"],
  "confidence": 0.0,
  "needs_review": false,
  "selection_outcome": "not_run | winner_candidate | excluded | needs_review",
  "selection_reason": "string|null",
  "taxonomy_version": "string",
  "policy_version": "string",
  "readback_verified": false
}
```

## Sheet rendering

Classifier output columns:

```text
K Crime Status
L Good Categories
M Bad Categories
N Article Check Attempted (existing header may still say Needs Article)
O Evidence
P Unmapped Candidates
```

Only A:D are read as source columns, and only K:P are written by the classifier. The former confidence column was deleted, shifting evidence to O and unmapped candidates to P. Columns L and M each render one line per distinct category; subcategories under one category are comma-separated. Column N is a persistent article-attempt indicator: render `Yes` when the final local `article.status` is `fetched`, `fetch_failed`, or `infrastructure_error`; valid reused saved article text counts as `fetched`. Render `-` only for `not_needed`. `Yes` therefore means the workflow attempted the article path, not necessarily that text was obtained. A failed attempt requires `needs_review: true`; retain its diagnostics locally and include concise failure evidence in O when useful for manual intervention. A completed classification must not clear a prior `Yes`. The numeric confidence remains local only and has no Sheet destination. For every classifier field in K:P with no value, the Sheet display value is `-`; local structured records may retain empty strings/nulls. The dash is a display sentinel and must not be interpreted as a category, subcategory, or evidence. Codes are local metadata only and must not appear in user-facing cells.

`crime` records must have at least one supported Good Category or Bad Category. If neither side has a supported parent, `needs_review` must be true and at least one good or bad unmapped parent candidate with evidence must be present. A supported parent may be rendered without a subcategory; preserve the missing subcategory candidate and set `needs_review: true` rather than forcing a neighboring label. `noncrime` records normally have empty Good Categories locally and `-` in the Sheet; Bad Categories may still be recorded when supported. `needs_article` may have candidate categories but must not be presented as final.

Column P renders both unmapped arrays, one candidate per line:

```text
Good parent: Proposed Parent — concise evidence/review note
Good subcategory under Supported Parent: Proposed Subcategory — concise evidence/review note
Bad parent: Proposed Parent — concise evidence/review note
Bad subcategory under Supported Parent: Proposed Subcategory — concise evidence/review note
```

Use only the applicable prefix. Any nonempty good or bad unmapped array requires `needs_review: true`. Optional `case_stage`, `allegation_status`, and location clues are populated only from readily available evidence; missing optional detail does not by itself trigger article fetching.
