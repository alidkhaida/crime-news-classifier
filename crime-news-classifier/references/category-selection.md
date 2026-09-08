# Category Selection Rules

Use this file with `primary-taxonomy.md`. It contains the decision procedure; the taxonomy file contains the maintained labels.

## Decision sequence

1. Determine `crime`, `noncrime`, or `needs_article` from title, URL slug, and description before opening the article. At the same time, note explicit or credible foreign-location signals; otherwise use the U.S. routing default without fetching solely for geography.
2. Identify the alleged conduct, affected person/property, offender context, case stage, and allegation status.
3. Select every maintained primary category materially supported by the evidence.
4. Select only subcategories supported by the same evidence. A keyword is a candidate signal, not proof. A supported parent may stand alone when no maintained subcategory fits.
5. Record evidence phrases and confidence locally.
6. Preserve good and bad unmapped candidates separately. Any parent or subcategory gap sets `needs_review: true`; never replace it with a neighboring label.

## Efficient stopping rule

- Stop at metadata when category and subcategory are adequately supported.
- Fetch the original article only for category ambiguity, conflicting clues, a taxonomy gap that text may resolve, or a credible foreign-location hint.
- Do not fetch only to determine optional case stage, allegation status, jurisdiction, arrest/custody status, footage availability, or later inclusion-policy facts.
- When an article is fetched, retain its available clues and saved text for later skills; do not expand this stage into deep research or outside-source investigation.

## Context rules

- Add family/relationship when the relationship affects access, motive, victim selection, or conduct.
- Add juvenile-involved crime only when the alleged offender's under-18 or juvenile status is explicit.
- Add employee/workplace, school/institutional, elder/vulnerable, or child-neglect context only when the duty, access, setting, or vulnerability materially shapes the offense.
- Add hate/bias only when statements, symbols, target selection, official allegations, charges, or other evidence supports motive.
- Add cybercrime only when the computer, account, platform, communication, or data system is central—not merely mentioned.
- Add the Bad Category `Animal-Related Stories` whenever an animal or wildlife matter is materially involved. It is additive with human-directed and contraband categories; skip only incidental animal mentions.

## Common separations

- Homicide is for criminal, suspicious, attempted-killing, or unresolved criminal-death facts; accidental, natural, or confirmed-suicide facts do not automatically qualify.
- Kidnapping is not synonymous with missing person; require unlawful taking, movement, concealment, or restraint. Preserve missing-person status when the cause is unknown.
- Robbery requires force, threat, or intimidation connected to taking property. Burglary requires unlawful entry or remaining with criminal intent. Trespass is unlawful presence without enough evidence of another intended crime.
- Drugs require supported controlled-substance conduct; past use, suspected intoxication, or lawful medication is insufficient.
- Forced trafficking/exploitation requires force, fraud, coercion, control, forced labor, debt bondage, abuse of vulnerability, or an explicit trafficking/exploitation allegation. Child commercial sexual exploitation qualifies; voluntary adult commercial sex does not.
- Noncoercive paid human smuggling or unlawful migration transport is a Bad Category under `Excluded`. Forced or exploitative movement belongs under Human Trafficking, Forced Labor & Exploitation.
- Organized contraband smuggling is a Good Category only when an organized illegal-goods movement or concealment operation is central; ordinary possession or transport stays with the specific offense category.
- Add Kidnapping alongside trafficking only when unlawful taking, movement, concealment, confinement, or restraint is independently supported.
- Court-stage language should describe the article's main subject. A passing reference to a conviction or sentence does not make the article a court/sentencing story.

## Rendering

Render categories with full names, one primary category per line, and comma-separated subcategories on that line. Render a supported parent without a trailing colon when no maintained subcategory fits. Render `-` in a Sheet category cell when no category is assigned; keep local structured emptiness separate. In column N, render `Yes` for any attempted article path, including failure. Render evidence in O and prefix unmapped entries in P with `Good:` or `Bad:` plus a concise evidence/review note. Confidence remains local and has no Sheet column. Never expose legacy codes. Keep final inclusion/exclusion policy separate from category classification.
