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
  "categories": {"Main Category Name":["Subcategory Name"]},
  "unmapped_candidates": [{"parent_category":"string","candidate_name":"string","evidence":"string","confidence":0.0}],
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

Recommended pilot columns:

```text
E Crime Status
F Categories
G Needs Article
H Confidence
I Evidence
J Unmapped Candidates
```

Column F renders one line per distinct main category. Subcategories under one category are comma-separated. Codes are local metadata only and must not appear in user-facing cells.

`crime` records should have at least one category or an explicit review reason. `noncrime` records normally have an empty category cell and a reason in evidence. `needs_article` may have candidate categories but must not be presented as final.
