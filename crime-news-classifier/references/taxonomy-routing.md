# Taxonomy Routing

Use the compact maintained local references as the runtime taxonomy:

- `references/primary-taxonomy.md` — the 19 maintained primary labels and compact subcategory index.
- `references/category-selection.md` — decision sequence, context rules, boundaries, and rendering.
- `references/bad-taxonomy.md` — the separate provisional bad-category labels and subcategory index.

The files under `archive/` are legacy or provenance material. Do not use them for category or subcategory selection. Load `references/policy-boundary.md` only for the separate final inclusion/exclusion stage.

Priority is: current user instruction, then these compact local operational references. If an approved source changes, update the local references deliberately and record the taxonomy version; do not silently mix old archive labels with current labels.

When no maintained subcategory fits, keep the supported parent and save an unmapped subcategory candidate. When no maintained parent fits, leave categories empty, set `needs_review: true`, and preserve an unmapped candidate. Never substitute a neighboring parent merely to avoid review.
