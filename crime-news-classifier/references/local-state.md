# Local state and cache

Use a local SQLite database or equivalent durable store for high-volume runs. The primary lookup is `url_key`; always preserve `original_url`.

Recommended state tables:

```text
articles(url_key PRIMARY KEY, original_url, input_fingerprint, title, description,
         final_url, content_hash, text_path, fetch_status, fetched_at)
classifications(url_key, taxonomy_version, policy_version, result_json,
                classification_status, classified_at, PRIMARY KEY(url_key, taxonomy_version, policy_version))
row_receipts(run_id, physical_row, url_key, source_fingerprint, write_range,
             readback_verified, conflict_reason)
taxonomy_candidates(parent_category, normalized_candidate, evidence_count,
                    examples_json, status)
```

Cache rules:

- Skip metadata processing when URL and input fingerprint are unchanged and the relevant taxonomy version is already classified.
- Reclassify from saved text after a taxonomy change; do not refetch merely because labels changed.
- Refetch only when text is absent, fetch failed, refresh is explicitly requested, or the source changed under an explicit refresh policy.
- Keep different content hashes as versions; do not overwrite evidence silently.
- Different URLs may describe the same incident. URL caching is not duplicate-incident resolution.
- Persist manifests and partial results before any external write.

Use states such as `new`, `metadata_classified`, `needs_article`, `fetched`, `classified`, `needs_review`, `taxonomy_update_required`, `fetch_failed`, and `infrastructure_error`.
