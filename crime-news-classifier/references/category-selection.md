# Category Selection Rules

Use this file with `primary-taxonomy.md`. It contains the decision procedure; the taxonomy file contains the maintained labels.

## Decision sequence

1. Determine `crime`, `noncrime`, or `needs_article` from title, URL slug, and description before opening the article.
2. Identify the alleged conduct, affected person/property, offender context, case stage, and allegation status.
3. Select every maintained primary category materially supported by the evidence.
4. Select only subcategories supported by the same evidence. A keyword is a candidate signal, not proof.
5. Record evidence phrases and confidence locally.
6. If no parent fits, fail closed with `needs_review: true` and an unmapped candidate.

## Context rules

- Add family/relationship when the relationship affects access, motive, victim selection, or conduct.
- Add juvenile-involved crime only when the alleged offender's under-18 or juvenile status is explicit.
- Add employee/workplace, school/institutional, elder/vulnerable, or child-neglect context only when the duty, access, setting, or vulnerability materially shapes the offense.
- Add hate/bias only when statements, symbols, target selection, official allegations, charges, or other evidence supports motive.
- Add cybercrime only when the computer, account, platform, communication, or data system is central—not merely mentioned.

## Common separations

- Homicide is for criminal, suspicious, attempted-killing, or unresolved criminal-death facts; accidental, natural, or confirmed-suicide facts do not automatically qualify.
- Kidnapping is not synonymous with missing person; require unlawful taking, movement, concealment, or restraint. Preserve missing-person status when the cause is unknown.
- Robbery requires force, threat, or intimidation connected to taking property. Burglary requires unlawful entry or remaining with criminal intent. Trespass is unlawful presence without enough evidence of another intended crime.
- Drugs require supported controlled-substance conduct; past use, suspected intoxication, or lawful medication is insufficient.
- Human trafficking is not inferred from prostitution, pornography, sexual conduct, or immigration status alone; require exploitation or trafficking facts.
- Court-stage language should describe the article's main subject. A passing reference to a conviction or sentence does not make the article a court/sentencing story.

## Rendering

Render categories with full names, one primary category per line, and comma-separated subcategories on that line. Never expose legacy codes. Keep final inclusion/exclusion policy separate from factual classification.
