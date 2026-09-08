# Taxonomy Routing

Current taxonomy version: `2026-09-08-category-v3`.

Use the compact maintained local references as the runtime taxonomy:

- `references/primary-taxonomy.md` — the 20 maintained primary labels and compact subcategory index.
- `references/category-selection.md` — decision sequence, context rules, boundaries, and rendering.
- `references/bad-taxonomy.md` — the separate provisional bad-category labels and subcategory index.

The files under `archive/` are legacy or provenance material. Do not use them for category or subcategory selection. Load `references/policy-boundary.md` only for the separate final inclusion/exclusion stage.

Priority is: current user instruction, then these compact local operational references. If an approved source changes, update the local references deliberately and record the taxonomy version; do not silently mix old archive labels with current labels.

When no maintained subcategory fits, keep the supported parent, save the missing good or bad subcategory candidate, and set `needs_review: true`. When no maintained parent fits, leave that category side empty, set `needs_review: true`, and preserve the proposed parent. A supported category on the other side still counts; never substitute a neighboring parent merely to avoid review.
