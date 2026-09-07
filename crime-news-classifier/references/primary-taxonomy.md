# Primary Crime Taxonomy

Status: maintained local routing index. This file is the operational authority used during classification and is designed to preserve the approved category meanings and boundaries without requiring access to an external document.

Use one or more supported primary categories when the article's evidence fits their definitions. The labels below are the only maintained parent names. The listed subcategories are compact routing labels derived from the examples and boundaries in the source document; they are not keyword-only triggers.

## Maintained primary categories and subcategories

1. **Child Neglect, Endangerment & Child Abuse** — physical abuse; dangerous living conditions; lack of supervision; hot/cold vehicle; caregiver intoxication; accessible drugs or weapons; medical neglect; abandonment; caregiver or institutional duty-of-care failure.
2. **Family, Domestic & Relationship Cases** — domestic assault; strangulation; threats or stalking; protection-order violation; breakup/property retaliation; family violence; parental abduction; family theft; intimate-partner or close-relationship homicide.
3. **Teen & Juvenile-Involved Crime** — juvenile assault; school threats; juvenile weapons; juvenile vehicle crime; burglary/robbery/shoplifting; juvenile drugs; vandalism/arson; cyber or online threats; crime against family members.
4. **Theft, Fraud & Financial Crime** — shoplifting/retail theft; employee theft/embezzlement; identity/payment fraud; forgery/counterfeit; consumer/contractor/benefit/insurance scams; investment schemes; package/mail theft; vehicle theft; organized theft.
5. **Traffic, DUI & Vehicle Crime** — impaired driving; reckless driving/speed/racing; hit-and-run or criminal crash; fleeing in a vehicle; suspended driving; road rage/vehicle as weapon; stolen vehicle; VIN/title fraud; professional-driver crime.
6. **Employee, Workplace & Occupational Crime** — workplace theft/embezzlement; payroll/refund/account fraud; customer or patient-data misuse; job-related threats/violence; caregiver/fiduciary abuse; bribery/extortion/kickbacks; misuse of regulated systems.
7. **Homicide, Suspicious Death & Body Discovery** — homicide/attempted homicide; suspicious or unresolved death; fatal shooting/stabbing/beating/strangulation; vehicular homicide; drug-induced death with criminal supply facts; body/remains discovery; concealment/dismemberment; cold case.
8. **Resisting, Evading, Obstruction & Public Disturbance** — resisting arrest; fleeing or evading; false identity; hiding a suspect; evidence destruction; witness intimidation; disorderly conduct; public intoxication; group disturbance; trespass; false 911/swatting; barricade or standoff.
9. **Assault, Weapons & Violent Crime** — assault/battery; serious injury; nonfatal shooting/stabbing/strangulation; threats/menacing; assault on officer or protected worker; illegal firearm possession; prohibited possessor; stolen weapon; unlawful sale; ghost gun/modification; explosive/incendiary/chemical threat.
10. **Drugs & Narcotics** — possession; distribution/sale; trafficking/transport; manufacturing/lab; cultivation; prescription fraud or medication diversion; school/jail drugs; child exposure or caregiver drug endangerment; unlawful drug supply linked to overdose.
11. **Kidnapping, Abduction, Unlawful Restraint & Missing Persons** — kidnapping; child or parental abduction; custody interference; false imprisonment/unlawful restraint; hostage/ransom; luring; Amber Alert/endangered missing person; suspicious disappearance; missing-person remains identification.
12. **Arson, Vandalism & Destruction of Property** — arson/fire; vandalism/criminal mischief; sabotage; infrastructure damage; contamination; insurance/revenge arson; public-facility damage; destruction of evidence.
13. **Robbery, Burglary, Trespass & Home Invasion** — armed/strong-arm robbery; carjacking; home invasion; residential/business/institutional burglary; vehicle burglary; criminal trespass; restricted-area entry; burglary tools.
14. **Cybercrime, Digital Crime & Identity Abuse** — hacking/unauthorized access; malware/ransomware/denial-of-service; phishing/email compromise; credential/SIM/account takeover; online or crypto scam; cyberstalking/doxxing; digital harassment/threats/swatting; sextortion/intimate-image abuse; database misuse; online child luring.
15. **Stalking, Harassment, Threats & Protection-Order Violations** — stalking; repeated unwanted contact; credible threat; workplace/school stalking; GPS or location monitoring; witness intimidation/retaliation; protection/no-contact violation; bias-motivated harassment.
16. **Human Trafficking, Smuggling & Exploitation** — sex trafficking; child commercial exploitation; forced labor; debt bondage; human smuggling; stash/harboring operation; dangerous transport; online recruitment/advertising; organized movement or concealment of contraband.
17. **Elder & Vulnerable Adult Abuse or Exploitation** — caregiver neglect; physical abuse/restraint; abandonment; institutional neglect; financial/fiduciary abuse; power-of-attorney or estate theft; targeted vulnerability scam; caregiver exploitation.
18. **Hate Crime, Bias & Extremism** — bias-motivated assault/homicide; bias threats/harassment/stalking; targeted vandalism/arson; worship-site or cemetery desecration; extremist violence or plot.
19. **School, Institutional & Public-Facility Crime** — school/daycare crime; hospital/nursing/group-home crime; jail/transit/library/government-facility crime; educator/coach misconduct; facility weapons or threats; institutional theft/records misuse; facility arson/vandalism.

## Parent boundaries

- A context label requires a meaningful nexus: relationship, age/legal status, employment access, institution, vulnerability, or motive must affect the conduct. Incidental presence is not enough.
- A child victim alone does not establish child neglect/abuse; require abuse, neglect, abandonment, failure to protect, or serious danger connected to a responsible adult or duty of care.
- A teen victim alone does not establish juvenile-involved crime; the alleged offender's juvenile status must be explicit.
- A body discovery, missing person, accident, suicide, or natural death is not automatically homicide.
- A vehicle, phone, workplace, school, jail, or hospital is not enough by itself; it must materially shape the crime.
- Human trafficking requires exploitation, force, fraud, coercion, payment/debt, vulnerability, recruitment, transport, or another supported trafficking fact. Sexual content or CSAM alone is not trafficking.
- Assign all supported categories. A primary category is not exclusive unless the evidence makes another label incidental.

## Taxonomy gaps

If the evidence clearly describes a crime but no maintained parent fits, return no parent category, set `needs_review: true`, and preserve an `unmapped_candidate` with the proposed label and evidence. Never select the nearest parent just to fill the field.
