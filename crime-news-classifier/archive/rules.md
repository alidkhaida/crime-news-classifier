# News Category Rules

Apply in order with precision over recall. A case normally qualifies only as a
discrete US police/crime incident with confirmed arrest, charge, capture, or
custody. Stronger exclusions override an arrest.

## Decision order

1. Outside the US -> `out of US`
2. Severe sexual/exploitation conduct under the test below -> `sexual case`
3. High-profile or qualifying political/federal/financial case -> its exclusion
4. No single qualifying incident:
   - multiple unrelated incidents of the same crime type -> `aggregate story`
   - not a crime-related incident covered by this project -> `general news`
5. Genuinely accidental incident with no alleged criminal conduct or
   enforcement -> `accident / non-crime`
6. Check for confirmed arrest, charge, capture, or custody; regardless of the
   result, continue through steps 7–9 before deciding inclusion
7. Suspect died before arrest with no arrested co-suspect ->
   `suspect died / no arrest`
8. Trivial, citation-only, or weak enforcement -> its matching exclusion
9. Court, sentencing, trial, or old-case story -> normally a court exclusion
10. Otherwise include a useful incident-level police/public-record lead

## Approved inclusion reasons

`arrest happened`, `arrests happened`, `arrest/charge`, `charged`,
`suspect in custody`, `suspect captured`, `taken into custody`,
`underlying arrest`, `arrest/bodycam`, `police encounter`

## Other exclusion definitions

- `out of US`: incident occurred outside the United States. Incident location,
  not publisher location, controls.
- `popular/high-profile`: celebrity, major-athlete, nationally notorious, or
  saturated case.
- `political/federal`: unsuitable political or nonfinancial federally involved
  case.
- `general news`: policy, trend, statistics, warning, awareness, opinion,
  memorial, anniversary, or broad reaction with no discrete qualifying incident.
- `aggregate story`: multiple unrelated same-type incidents; multiple suspects,
  victims, locations, or charges within one incident are not aggregate.
- `victim follow-up`: remembrance, recovery, fundraiser, funeral, memorial, or
  “seeks answers,” unless it is the only useful source for an underlying arrest.
- `suspect not found`: suspect is wanted, sought, at large, fled, escaped, or
  clearly not captured. This takes precedence over `no arrest` when both apply.
- `no arrest`: source explicitly establishes that no arrest occurred.
- `unable to access`: inaccessible after fallbacks, or an identity warning
  proves the fetched page is wrong.
- `not enough info`: original article was fetched/read but remains undecidable.
- `suspect died / no arrest`: source identifies the deceased as the suspect and
  no co-suspect was arrested; never infer this from a death mention.
- `accident / non-crime`: genuinely accidental, noncriminal fire, drowning,
  shooting, animal attack, or industrial accident; crashes use **Vehicular cases**.
- `court update`: sentencing, conviction, plea, trial, appeal, or routine
  procedural update.
- `old case / court`: retrospective old case with no useful new arrest event.
- `minor / weak case`: trivial misconduct, minor school incident, simple
  possession, or low-value enforcement.
- `citation only`: citation without custodial arrest or a stronger incident.

## Fraud and financial cases

Fraud type and dollar amount never control; agencies and a specific, potentially
recorded enforcement encounter do.

- Any federal involvement—including FBI, IRS, DOJ, Secret Service, or another
  federal authority—requires exclusion: `federal/financial` for financial cases,
  `political/federal` otherwise.
- Use `federal/financial` for a broad document-based scheme lacking a named
  local/state agency and requestable arrest, search, traffic stop, store response,
  seizure, or suspect encounter. Unclear agency or bodycam possibility also
  requires this exclusion.
- A nonfederal case may qualify if a named local/state agency and identifiable
  enforcement encounter are present, with most or all of: a discrete incident,
  identified suspect, arrest/charge, physical enforcement, and reasonably
  requestable footage.

## Sexual cases

Judge the alleged conduct, not headlines, tags, or isolated words such as
“sexual,” “lewd,” “inappropriate,” “child,” or “predator.” Read the underlying
facts when such wording is vague.

Use `sexual case` when the current or underlying incident involves rape or
attempted rape; sexual assault/battery; molestation or completed sexual abuse;
forced, coerced, violent, genital, or physically invasive sexual contact; direct
sexual exploitation; production/recording through actual child abuse;
prostitution, solicitation, or commercial sex; trafficking; incest or severe
intrafamilial abuse; sexual-purpose kidnapping/confinement; or homicide/violent
assault involving serious sexual abuse; or comparable serious, completed,
forced, abusive, or physically invasive sexual conduct.

This exclusion overrides arrest, local agency/bodycam access, and parallel
offenses. Never relabel it as homicide, kidnapping, child neglect, employee
misconduct, domestic violence, or another category.

When no severe act was completed, lower-impact, nonviolent, or primarily
non-contact conduct continues through normal selection. Examples include:

- exposure or public lewdness without victim contact; voyeurism, hidden cameras,
  or upskirting;
- inappropriate/nude images or messages; possession-only and AI-generated image
  allegations require fact review, while production through direct child abuse
  always excludes;
- decoy/minor meetings, luring, asking a minor on a date or to remove clothing,
  or similar conduct without completed sexual contact;
- limited touching not described as molestation, sexual assault/battery,
  coercive or genital contact, or direct abuse; and predatory conduct stopped
  before a severe offense.

Minor involvement alone does not exclude; completed sexual assault, molestation,
sexual battery, or direct sexual abuse of a minor always does. Incidental sexual
wording, unrelated priors, and background references do not disqualify the
current incident. Vague title/description evidence must follow the `needs_article`
flow in `SKILL.md`. Only after an accessible original article is reviewed, if
facts remain unclear and a serious sexual offense may have occurred, use
`sexual case`; an `access_error` remains `unable to access`.

## Arrest and custody

Positive proof includes arrested, booked, charged, jailed, in custody,
apprehended, captured, surrendered, taken into custody, or indicted. Wanted,
searching, at large, fled, escaped, no arrests, or unidentified are negative;
`accused`, `suspected`, `identified`, and `person of interest` are not proof.
When title/description are inconclusive, request the original article before
using `unable to access` or `not enough info`. `infrastructure_error` is not a
category; return it without classification.

### Vehicular cases

- Use `accident / non-crime` only for a genuinely accidental crash with no
  alleged crime or enforcement; the words “crash” or “accident” do not control.
  Reckless/aggressive driving, extreme speeding, DUI, hit-and-run, fleeing
  police, vehicular homicide, or similar conduct follows normal crime rules;
  include when arrest/charge/capture/custody requirements are met.
- DUI is strong when arrest/charge is confirmed, especially fatal, wrong-way,
  pedestrian, child-victim, serious-injury, bizarre-conduct, or pursuit cases.
  `Suspected DUI` alone is insufficient.
- Hit-and-run: arrested/charged/indicted -> candidate to include; still sought
  or fled -> `suspect not found`.
- Pursuit: captured/arrested -> candidate to include; escaped or wanted ->
  `suspect not found`.

## Court and special cases

- A court story may use `underlying arrest` only when it is the sole useful lead
  to a strong, distinctive underlying arrest.
- Serious juvenile arrests may qualify, including murder, shooting, arson,
  armed robbery, kidnapping, and serious pursuit/DUI. Minor misconduct ->
  `minor / weak case`.
