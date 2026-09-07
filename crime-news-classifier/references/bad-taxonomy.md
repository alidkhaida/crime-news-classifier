# Bad-Category Taxonomy

Status: provisional local taxonomy for the separate bad-category output. It is based on the keyword clues in the `bad categories` Sheet tab. Keywords are hints, not automatic decisions.

Bad categories are editorial-routing flags. They do not mean `noncrime`, and they do not replace factual crime categories. A record may receive both factual categories and one or more bad categories.

## Rendering and decision rules

- Use full names; one bad primary category per line; comma-separated subcategories on that line.
- Start with crime/noncrime recognition, then evaluate bad categories.
- Use title, URL slug, and description first; fetch only when unresolved.
- Require article context for weak terms such as `sex`, `sexual`, `porn`, `convicted`, `officer`, or `suicide`.
- Assign multiple bad categories when multiple themes are materially central.
- Preserve `unmapped_bad_candidate` when a supported bad family lacks a maintained subcategory.
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

## 4. Animal-Only Stories

**Use for:** stories mainly about animal harm or animal-related violations without a material human-directed crime.

**Subcategories:** Animal Cruelty / Abuse; Animal Neglect / Hoarding; Animal Fighting; Wildlife / Hunting Violation; Commercial Animal Operation; Animal Torture.

**Clues:** `animal cruelty`, `animal abuse`, `animal neglect`, `animal hoarding`, `dog fighting`, `dogfighting`, `cockfighting`, `illegal hunting`, `poaching`, `puppy mill`, `animal torture`.

**Boundary:** Do not use Animal-Only when human assault, child endangerment, fraud, weapons, or another human-directed crime is the material center.

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

## 7. Prostitution / Sex Trafficking

**Use for:** stories mainly about commercial sex, prostitution, pimping, pandering, brothels, or human sex trafficking.

**Subcategories:** Prostitution / Commercial Sex; Pimping / Pandering / Brothel Operation; Human Sex Trafficking.

**Clues:** `brothel`, `commercial sex`, `pimp`, `pimping`, `pandering`, `prostitute`, `prostitution`, `sex worker arrest`, `human sex trafficking`, `sex trafficking`, `sexual trafficking`.

**Boundary:** Do not infer trafficking from prostitution or sex-worker language alone; require force, fraud, coercion, exploitation, transport, recruitment, or another trafficking fact.

## 8. Sexual Crimes / Exploitation

**Use for:** stories mainly about sexual assault, sexual abuse, child exploitation, CSAM, grooming, statutory sexual conduct, or related sexual misconduct.

**Subcategories:** Rape / Sexual Assault; Child Sexual Abuse / Exploitation; Indecent / Lewd / Statutory Sexual Conduct; Sexual Content / Pornography when the context establishes an offense or exploitation.

**Clues:** `child exploitation`, `CSAM`, `grooming a minor`, `indecent assault`, `indecent liberties`, `lewd conduct`, `molest`, `molestation`, `molested`, `porn`, `pornography`, `rape`, `raped`, `rapist`, `statutory rape`.

**Boundary:** Generic sexual language, pornography references, or consensual adult conduct do not establish a bad category without crime or exploitation context.

## Overlap rules

- Court / Sentencing may coexist with the underlying factual crime when the article is primarily a procedural update.
- Prison / Jail-Only may coexist with assault, homicide, weapons, or contraband categories when both are material.
- Officer Misconduct may coexist with a criminal category when the administrative or civil-liability issue is independently material.
- Prostitution / Sex Trafficking and Sexual Crimes / Exploitation may both apply when commercial sex/trafficking and abuse/exploitation are independently supported.
- Suicide / Self-Harm may coexist with criminal conduct only when both are materially covered.
