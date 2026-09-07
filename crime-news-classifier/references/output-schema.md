# Output schema

## Local record

```json
{
  "url_key": "string",
  "original_url": "string",
  "physical_row": 0,
  "input_fingerprint": "string",
  "metadata_decision": {"status":"crime | noncrime | needs_article","reason":"string","confidence":0.0,"evidence":["string"]},
  "article": {"status":"not_needed | fetched | fetch_failed | infrastructure_error","final_url":"string|null","content_hash":"string|null","text_path":"string|null"},
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
N Needs Article
O Confidence
P Evidence
Q Unmapped Candidates
```

Only A:D are read as source columns and only K:Q are written by the current classifier. E:I and all other columns are outside the contract. Columns L and M each render one line per distinct category; subcategories under one category are comma-separated. Codes are local metadata only and must not appear in user-facing cells.

`crime` records should have at least one good category. The only exception is an unresolved good-taxonomy gap: `good_categories` must be empty, `needs_review` must be true, and `unmapped_candidates` plus an evidence/review reason must be present. Bad categories are independent editorial flags and may be present even when the good-category cell is empty. `noncrime` records normally have empty good categories; bad categories may still be recorded when supported. `needs_article` may have candidate categories but must not be presented as final.
