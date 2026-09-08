# Bad-Category Taxonomy

Status: provisional local taxonomy for the separate bad-category output. It is based on the keyword clues in the `bad categories` Sheet tab. Keywords are hints, not automatic decisions.

Bad categories are editorial-routing flags. They do not mean `noncrime`, and they do not replace factual crime categories. A record may receive both factual categories and one or more bad categories.

## Rendering and decision rules

- Use full names; one bad primary category per line; comma-separated subcategories on that line.
- Start with crime/noncrime recognition, then evaluate bad categories.
- Use title, URL slug, and description first; fetch only when unresolved.
- Require article context for weak terms such as `sex`, `sexual`, `porn`, `convicted`, `officer`, or `suicide`.
- Assign multiple bad categories when multiple themes are materially central.
- Preserve `unmapped_bad_candidates` when a supported bad family lacks a maintained subcategory.
- A supported bad parent may stand alone when no maintained subcategory fits; record the subcategory gap for manual review instead of forcing a nearby label.
- Keep allegation, charge, conviction, administrative finding, lawsuit, and commentary status distinct.

## 1. Suicide / Self-Harm

**Use for:** stories primarily about suicide, attempted suicide, suicidal crisis, self-harm, or self-inflicted death.

**Subcategories:** Completed / Suspected Suicide; Attempted Suicide / Suicidal Crisis; Self-Harm / Self-Inflicted Injury; Self-Inflicted Death.

**Clues:** `suicide`, `suicidal`, `killed himself`, `killed herself`, `took his own life`, `took her own life`, `self harm`, `self-harm`, `self inflicted`, `self-inflicted`.

**Boundary:** Do not infer suicide from an ambiguous self-inflicted injury, accident, or disputed cause.

## 2. Court / Sentencing Stories

**Use for:** stories mainly about trial, plea, verdict, conviction, acquittal, sentencing, resentencing, or appeal rather than a new incident.

**Subcategories:** Trial / Court Proceedings; Plea / Admission; Verdict / Conviction; Acquittal / Dismissal Outcome; Sentencing / Resentencing; Appeal / Post-Conviction Review.

**Clues:** `sentenced`, `sentencing`, `prison sentence`, `life sentence`, `convicted`, `conviction`, `found guilty`, `pleaded guilty`, `guilty plea`, `verdict`, `acquitted`, `acquittal`, `resentenced`, `appeal denied`, `appeal rejected`, `on trial`, `trial begins`.

**Boundary:** A passing court reference does not make the article a court story.

## 3. Prison / Jail-Only Incidents

**Use for:** incidents where custody or the correctional facility is the central setting.

**Subcategories:** Facility Disturbance / Riot / Lockdown; Inmate-on-Inmate Violence; Inmate Death / Custody Death; Contraband / Custody Escape.

**Clues:** `prison riot`, `jail riot`, `inmate-on-inmate`, `prison fight`, `jail fight`, `prison stabbing`, `inmate killed`, `inmate death`, `prison lockdown`, `jail contraband`, `escape from prison`, `escape from jail`.

**Boundary:** Arrest or booking into jail alone is not a jail-only incident.

## 4. Animal-Related Stories

**Use for:** stories where an animal or wildlife matter is materially involved as a victim, target, subject, instrument, contraband, or central part of the alleged operation.

**Subcategories:** Animal Cruelty / Abuse; Animal Neglect / Hoarding; Animal Fighting; Wildlife / Hunting Violation; Commercial Animal Operation; Animal Torture.

**Clues:** `animal cruelty`, `animal abuse`, `animal neglect`, `animal hoarding`, `dog fighting`, `dogfighting`, `cockfighting`, `illegal hunting`, `poaching`, `puppy mill`, `animal torture`.

**Boundary:** This category is additive. Assign it even when human assault, child endangerment, fraud, weapons, organized contraband smuggling, or another category is also supported. Do not assign it for an incidental animal mention, such as a police dog merely being present without material animal-related conduct.

## 5. White-Collar / Corporate Crime

**Use for:** stories mainly about financial, business, market, accounting, tax, healthcare-billing, or corporate criminal conduct.

**Subcategories:** Securities / Investment / Market Fraud; Tax / Accounting / Financial Reporting Fraud; Corporate / Commercial Fraud; Healthcare Fraud; Antitrust / Market Conduct.

**Clues:** `securities fraud`, `insider trading`, `investment fraud`, `Ponzi scheme`, `stock manipulation`, `market manipulation`, `tax fraud`, `tax evasion`, `accounting fraud`, `corporate fraud`, `corporate bribery`, `kickback`, `Medicare fraud`, `Medicaid fraud`, `healthcare fraud`, `antitrust`.

**Boundary:** Confirm an intentional financial or corporate scheme; ordinary billing disputes and failed businesses are not enough.

## 6. Officer Misconduct / Administrative Stories

**Use for:** stories mainly about officer/department discipline, internal review, policy compliance, resignation, excessive-force litigation, or wrongful-arrest litigation.

**Subcategories:** Administrative Discipline / Employment Action; Administrative Leave / Internal Review; Policy / Procedure Violation; Resignation / Separation; Civil Rights / Excessive Force Lawsuit.

**Clues:** `officer suspended`, `officer fired`, `officer terminated`, `deputy suspended`, `trooper fired`, `police chief suspended`, `administrative leave`, `internal affairs investigation`, `internal investigation`, `policy violation`, `officer resigned`, `excessive force lawsuit`, `wrongful arrest lawsuit`.

**Boundary:** Administrative action is not proof of criminal conduct. Add the factual crime category separately when supported.

## 7. Prostitution / Commercial Sex

**Use for:** stories mainly about voluntary adult commercial sex, prostitution, solicitation, pimping, pandering, or brothel operations when the available evidence does not establish forced trafficking or exploitation.

**Subcategories:** Prostitution / Commercial Sex; Solicitation / Commercial-Sex Purchase; Pimping / Pandering / Brothel Operation.

**Clues:** `brothel`, `commercial sex`, `pimp`, `pimping`, `pandering`, `prostitute`, `prostitution`, `sex worker arrest`, `solicitation`, `purchased sex`.

**Boundary:** Do not infer trafficking from prostitution or sex-worker language alone. If force, fraud, coercion, control, debt bondage, abuse of vulnerability, or child commercial exploitation is supported, also use the Good Category `Human Trafficking, Forced Labor & Exploitation`. Do not describe a minor's commercial sexual exploitation as voluntary.

## 8. Sexual Crimes / Exploitation

**Use for:** stories mainly about sexual assault, sexual abuse, child exploitation, CSAM, grooming, statutory sexual conduct, or related sexual misconduct.

**Subcategories:** Rape / Sexual Assault; Child Sexual Abuse / Exploitation; Indecent / Lewd / Statutory Sexual Conduct; Sexual Content / Pornography when the context establishes an offense or exploitation.

**Clues:** `child exploitation`, `CSAM`, `grooming a minor`, `indecent assault`, `indecent liberties`, `lewd conduct`, `molest`, `molestation`, `molested`, `porn`, `pornography`, `rape`, `raped`, `rapist`, `statutory rape`.

**Boundary:** Generic sexual language, pornography references, or consensual adult conduct do not establish a bad category without crime or exploitation context.

## 9. Excluded

**Use for:** narrow category-stage routing facts that the user has explicitly designated as bad, without making the future final inclusion/exclusion decision.

**Subcategories:** Out of US; Noncoercive Human Smuggling / Unlawful Migration Transport.

**Out of US rule:** Treat U.S. location as the routing default when title, description, and URL slug contain no credible foreign-location signal. Do not open every article to verify country. Assign `Out of US` only when metadata or the original article affirmatively places the incident outside the United States; incident location controls, not publisher location, nationality, or outlet domain. A credible but unresolved foreign hint may trigger original-article review and `needs_review`, but not a guessed `Out of US` label.

**Human-smuggling rule:** Use `Noncoercive Human Smuggling / Unlawful Migration Transport` for paid or organized unlawful movement, concealment, harboring, or stash-house activity involving people when available evidence does not establish force, fraud, coercion, control, or exploitation. Forced or exploitative movement belongs in the Good Category `Human Trafficking, Forced Labor & Exploitation`.

**Boundary:** `Excluded` is a Bad Category flag only. It does not set `selection_outcome`, run the future policy stage, or erase any supported Good Category.

## Overlap rules

- Court / Sentencing may coexist with the underlying factual crime when the article is primarily a procedural update.
- Prison / Jail-Only may coexist with assault, homicide, weapons, or contraband categories when both are material.
- Officer Misconduct may coexist with a criminal category when the administrative or civil-liability issue is independently material.
- Prostitution / Commercial Sex and Sexual Crimes / Exploitation may both apply when commercial sex and a separate sexual offense or exploitation theme are independently supported.
- Human Trafficking, Forced Labor & Exploitation may coexist with Sexual Crimes / Exploitation when forced sexual exploitation and the sexual offense are independently material; do not add Prostitution / Commercial Sex merely because forced sex trafficking occurred.
- Animal-Related Stories may coexist with any supported Good or Bad Category whenever animal or wildlife involvement is material.
- `Excluded: Out of US` or `Excluded: Noncoercive Human Smuggling / Unlawful Migration Transport` may coexist with any independently supported category.
- Suicide / Self-Harm may coexist with criminal conduct only when both are materially covered.
