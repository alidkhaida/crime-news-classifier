# Permission preflight

Run a preflight before reading a Sheet, fetching an article, invoking a decision worker, writing local state, writing a Sheet, or changing taxonomy files.

Resolve the default spreadsheet and tab from `config/target.json`. The user must still provide explicit physical row bounds for every run. An explicit user target overrides the config for that run and must be reflected in the receipt.

## Capability meanings

| Capability | Allows | Does not allow |
|---|---|---|
| `sheet_read` | Read the configured spreadsheet metadata and exact physical range | Broad tab scans or Sheet writes |
| `sheet_write` | Write only the approved tab and exact output range | Replacing nonempty cells or writing another tab |
| `article_fetch` | Fetch only URLs assigned to the current run and marked `needs_article` | Search, crawling, or fetching unresolved rows |
| `ai_decision` | Use an AI worker for the approved classification stage | Letting AI fetch URLs or write Sheets |
| `local_state_read` | Read the local cache, manifests, and relevant references | Reading unrelated private files |
| `local_state_write` | Write run state, cache entries, receipts, and result records | Writing secrets or arbitrary paths |
| `taxonomy_write` | Add or update taxonomy proposals in the approved proposal file | Silently promoting a candidate to the production taxonomy |

## Required behavior

1. Build the smallest capability request from the requested stages. Classification-only does not imply `sheet_write`.
2. Show the user the spreadsheet ID, visible tab, exact physical rows, requested stages, capabilities, and whether article fetching may occur.
3. Ask for approval for each capability not already approved for this exact run scope. A write approval must name the destination tab and physical output range.
4. Save the result as a run-scoped receipt. The receipt must include the exact row bounds, approved capabilities, stages, skill version, and timestamp.
5. Before each stage, verify the receipt still covers the requested capability, tab, rows, and stage. Stop on denial, expiry, scope mismatch, or missing receipt.
6. Pass workers only their role allowlist intersected with the approved capabilities. A worker cannot grant itself additional capabilities.
7. Do not treat a network, connector, or authorization failure as a classification result.

The deterministic helper is `scripts/preflight.py`. Use `request` to create a receipt and `verify` immediately before a stage or side effect:

```bash
python3 scripts/preflight.py request \
  --receipt .classification_runs/RUN_ID/preflight.json \
  --run-id RUN_ID --config config/target.json \
  --start-row 2 --end-row 14 \
  --stages metadata,category \
  --grant sheet_read,local_state_read,local_state_write,ai_decision

python3 scripts/preflight.py verify \
  --receipt .classification_runs/RUN_ID/preflight.json \
  --capability ai_decision --stage category \
  --spreadsheet-id SHEET_ID \
  --tab test --start-row 2 --end-row 14
```

Use `--interactive` when the controller must ask in the terminal. Without `--grant` or `--interactive`, missing capabilities are denied. The receipt is an audit/control record; actual OS, connector, browser, and worker tool enforcement must be supplied by the runtime where available.
