# **Crime News Classification Taxonomy**

*A multi-label specification for identifying criminal case types from large news-link datasets*

***Version 1.0 | September 2026***

# How the classifier should work

**Purpose: **Identify every crime category supported by the article. This first-stage model is for recognition and routing—not for deciding whether a case is interesting, usable, footage-rich, or suitable for publication.

**Core rule: **Use multi-label classification. Assign one or more substantive offense labels, then add any supported context labels, victim/offender attributes, event-stage labels, and confidence. Never force a story into only one bucket when several crimes are materially alleged.

## Four classification axes

| **Axis** | **Meaning** |
| --- | --- |
| **A. Substantive offense** | What allegedly happened: homicide, assault, theft, fraud, DUI, drugs, arson, kidnapping, sexual offense, robbery, burglary, etc. |
| **B. Context / relationship** | Who or what enabled it: family/relationship, employee/workplace, juvenile offender, school/institution, elder/vulnerable victim, or hate/bias. |
| **C. Event stage** | What kind of news update it is: incident, investigation, missing alert, body discovery, arrest, charge, indictment, plea, trial, conviction, sentencing, appeal, release, or cold-case update. |
| **D. Certainty / status** | Whether conduct is alleged, suspected, charged, admitted, proved/convicted, dismissed, acquitted, or undetermined. |

## Non-negotiable decision rules

- Classify from the article text, headline, subheadline, captions, and structured metadata—not from a single keyword.

- Require an alleged criminal act or an official criminal/suspicious investigation. Do not turn accidents, civil disputes, policy stories, or vague misconduct into crime.

- Separate the suspect's attributes from the victim's. A teen victim does not make the case Teen Crime; a teacher victim does not make it Employee Crime.

- Do not infer guilt. Preserve allegation language and record case status separately from category.

- Classify conduct, not merely charges. Charge names vary by state; map facts and synonymous statutes to the shared taxonomy.

- When a crime results in death, assign Homicide/Death plus the causal offense/context when supported.

- When a news story contains several separate incidents, classify each incident separately if the data pipeline permits; otherwise union the supported labels and flag multi_incident=true.

- When information is insufficient, route the record to manual review rather than guessing or forcing it into an unrelated category.

## Recommended output object

```yaml
primary_offenses: [one or more taxonomy codes]
context_labels: [zero or more context codes]
offender: {age, age_group, juvenile_status, role, relationship_to_victim}
victim: {age, age_group, vulnerable_status, role, relationship_to_offender}
incident: {date, location, jurisdiction, setting, vehicle_involved, weapon_type, injury, fatality}
case_stage: incident | investigation | alert | arrest | charge | plea | trial | conviction | sentencing | appeal | update
allegation_status: suspected | alleged | charged | admitted | convicted | dismissed | acquitted | undetermined
confidence: 0.00–1.00
evidence_spans: [short article phrases supporting each label]
needs_review: true | false
```

# Category index

**1. Child Neglect, Endangerment & Child Abuse**  —  CHILD_MALTREATMENT

**2. Family, Domestic & Relationship Cases**  —  FAMILY_RELATIONSHIP

**3. Teen & Juvenile-Involved Crime**  —  JUVENILE_TEEN

**4. Theft, Fraud & Financial Crime**  —  THEFT_FRAUD

**5. Traffic, DUI & Vehicle Crime**  —  TRAFFIC_VEHICLE

**6. Employee, Workplace & Occupational Crime**  —  EMPLOYEE_WORKPLACE

**7. Homicide, Suspicious Death & Body Discovery**  —  HOMICIDE_DEATH

**8. Resisting, Evading, Obstruction & Public Disturbance**  —  PUBLIC_ORDER_OBSTRUCTION

**9. Assault, Weapons & Violent Crime**  —  ASSAULT_WEAPONS_VIOLENCE

**10. Drugs & Narcotics**  —  DRUGS_NARCOTICS

**11. Kidnapping, Abduction, Unlawful Restraint & Missing Persons**  —  KIDNAPPING_MISSING

**12. Arson, Vandalism & Destruction of Property**  —  ARSON_DESTRUCTION

**13. Robbery, Burglary, Trespass & Home Invasion**  —  ROBBERY_BURGLARY_ENTRY

**14. Cybercrime, Digital Crime & Identity Abuse**  —  CYBER_DIGITAL

**15. Stalking, Harassment, Threats & Protection-Order Violations**  —  STALKING_HARASSMENT

**16. Human Trafficking, Smuggling & Exploitation**  —  TRAFFICKING_SMUGGLING

**17. Elder & Vulnerable Adult Abuse or Exploitation**  —  ELDER_VULNERABLE_ABUSE

**18. Hate Crime, Bias & Extremism**  —  HATE_BIAS_EXTREMISM

**19. School, Institutional & Public-Facility Crime**  —  SCHOOL_INSTITUTION_CONTEXT

# 1. Child Neglect, Endangerment & Child Abuse

**Machine label: **CHILD_MALTREATMENT

**Definition: **Any alleged act or omission by a parent, guardian, caregiver, household member, institution, or other person that harms a minor or creates an unreasonable risk of physical, emotional, sexual, medical, or developmental harm. The category covers both completed injury and dangerous exposure, even when the child is not injured.

## Include

- Physical abuse: hitting, beating, burning, shaking, choking, poisoning, unlawful restraint, or inflicting injury on a child.

- Neglect: inadequate food, shelter, hygiene, clothing, supervision, education, or safe living conditions; children found alone, wandering, in filth, or living with accessible hazards.

- Medical neglect: withholding necessary treatment, failing to obtain urgent care, or intentionally misusing medication.

- Endangerment: leaving a child in a hot/cold vehicle; exposing a child to drugs, firearms, violence, dangerous animals, impaired driving, reckless pursuits, manufacturing drugs, or unsafe adults.

- Abandonment, unlawful desertion, failure to protect, permitting abuse, or knowingly leaving a child with a dangerous caregiver.

- Caregiver intoxication or incapacitation when it leaves a child unsupervised or at risk.

- Institutional abuse or neglect at a daycare, school, foster home, residential facility, camp, medical facility, or juvenile placement.

- Child exploitation that is not primarily sexual: forced labor, using a child to commit crimes, or financially exploiting a minor.

- Infant-related cases such as unsafe abandonment, suspicious injuries, failure to thrive, or substance exposure, when alleged criminal conduct is involved.

## Exclude / boundary

**Do not classify here: **Ordinary parenting disputes, poverty alone, lawful discipline with no allegation of abuse, accidental childhood injury with no negligence allegation, and child-custody litigation without alleged criminal conduct. Child death must also receive Homicide/Death Investigation when the death is criminal or suspicious.

## Common language signals

**Examples: **child abuse, child neglect, endangering the welfare of a child, contributing to the delinquency of a minor, failure to protect, abandoned child, left alone, filthy conditions, malnourished, failure to thrive, hot car, unsafe home, daycare abuse, foster parent, shaken baby, accessible drugs/firearm.

## Overlap and multi-label rule

**Apply with: **Apply Child Maltreatment whenever the victim is under 18 and the story alleges abuse, neglect, abandonment, exploitation, or dangerous exposure. Add Family/Relationship if the accused is family/household; Employee Crime if the accused acted through a paid caregiver, teacher, coach, daycare, or institutional role; Drugs, DUI, Weapons, Assault, or Homicide as applicable.

# 2. Family, Domestic & Relationship Cases

**Machine label: **FAMILY_RELATIONSHIP

**Definition: **A cross-cutting context label for alleged crimes arising between current or former intimate partners, spouses, dating partners, relatives, co-parents, household members, or people in a close personal relationship. It describes the relationship surrounding the crime; it is not a substitute for the actual offense.

## Include

- Domestic assault, strangulation, stalking, coercive control, threats, property destruction, or weapon use involving partners or household members.

- Crimes by or against spouses, ex-spouses, dating partners, ex-partners, parents, children, siblings, grandparents, in-laws, co-parents, or household residents.

- Custody-related interference, parental kidnapping, violation of protection orders, and confrontations during child exchanges.

- Family murder, attempted murder, suspicious family death, murder-suicide, or intimate-partner homicide.

- Relationship-motivated retaliation, jealousy, breakup violence, revenge property damage, or stalking.

- Criminal financial exploitation or theft involving relatives or intimate partners when the relationship is materially relevant.

## Exclude / boundary

**Do not classify here: **A crime merely occurring inside a residence, unrelated crimes committed by roommates with no relationship context, and stories that only mention the suspect has a family. Do not assign solely because the victim and suspect know each other socially.

## Common language signals

**Examples: **domestic violence, boyfriend, girlfriend, husband, wife, ex, partner, dating, co-parent, custody, mother, father, son, daughter, sibling, family member, household member, protection order, restraining order.

## Overlap and multi-label rule

**Apply with: **Always pair with the underlying offense: Assault, Homicide, Kidnapping, Stalking/Harassment, Theft/Fraud, Child Maltreatment, or Arson/Destruction.

# 3. Teen & Juvenile-Involved Crime

**Machine label: **JUVENILE_TEEN

**Definition: **A cross-cutting age label for crime stories in which an alleged offender is under 18, is explicitly called a juvenile/minor/teen, or is prosecuted in juvenile court. If the system wants broader youth coverage, a configurable extension may include 18- or 19-year-olds, but the default legal rule should be under 18 unless the article clearly uses juvenile status.

## Include

- Juvenile arrests, citations, petitions, detention, diversion, probation violations, or charges.

- Teen suspects in violent, property, vehicle, school, drug, weapons, cyber, or public-order offenses.

- Groups of minors or mixed-age groups when at least one alleged offender is a juvenile.

- Cases transferred or certified for adult prosecution, if the accused was a minor at the time of the alleged offense.

- School-related crimes committed by students when criminal conduct—not merely discipline—is alleged.

## Exclude / boundary

**Do not classify here: **Cases where only the victim is a teen (use a victim-age tag instead), generic references to 'young people,' adult suspects aged 18–19 unless your business rule deliberately includes them, and school discipline without alleged criminal conduct.

## Common language signals

**Examples: **juvenile, minor, teen, teenager, 13-year-old through 17-year-old, juvenile court, youth offender, tried as an adult, student arrested.

## Overlap and multi-label rule

**Apply with: **Always pair with the substantive offense(s). Keep separate fields for offender_age and victim_age so a teen victim is not mistaken for a teen offender.

# 4. Theft, Fraud & Financial Crime

**Machine label: **THEFT_FRAUD

**Definition: **Offenses involving taking, retaining, converting, obtaining, or controlling money, property, services, data, benefits, or something of value without lawful authorization, or obtaining value through deception, misrepresentation, forgery, abuse of trust, or concealment.

## Include

- Larceny, shoplifting, retail theft, package theft, mail theft, cargo theft, organized retail theft, theft by deception, possession of stolen property, and fencing stolen goods.

- Embezzlement, misappropriation, skimming, payroll theft, expense fraud, check theft, invoice fraud, procurement fraud, and misuse of business/customer funds.

- Identity theft, account takeover, credit/debit card fraud, check fraud, forgery, counterfeit money or documents, benefits fraud, insurance fraud, tax fraud, mortgage fraud, investment fraud, charity fraud, and elder financial exploitation.

- Scams and confidence schemes: impersonation, romance scams, tech-support scams, contractor scams, phishing, gift-card schemes, lottery scams, and fraudulent fundraising.

- Theft of services, utility theft, fare evasion when treated as a crime story, and unlawfully using another person's credentials or property.

- Auto theft and vehicle-part theft can receive this label plus Vehicle Crime.

## Exclude / boundary

**Do not classify here: **Robbery when force or threat is the defining conduct (use Robbery plus Theft/Fraud if desired); burglary when unlawful entry is central (use Burglary); civil contract/payment disputes without alleged criminal deception; misplaced property; and data breaches without alleged theft or fraud.

## Common language signals

**Examples: **stole, theft, shoplifting, embezzled, defrauded, scam, forged, counterfeit, identity theft, unauthorized charges, skimming, misappropriated, took money, fraudulent, stolen checks, benefits fraud, financial exploitation.

## Overlap and multi-label rule

**Apply with: **Add Employee Crime for occupational access/authority; Cybercrime when computers, accounts, networks, or digital deception are essential; Elder/Vulnerable Adult Abuse for targeted exploitation; and Vehicle Crime for stolen vehicles/catalytic converters.

# 5. Traffic, DUI & Vehicle Crime

**Machine label: **TRAFFIC_VEHICLE

**Definition: **Criminal or arrest-level conduct involving the operation, possession, theft, alteration, or misuse of a motor vehicle, or serious violations of roadway laws. This includes impaired and reckless driving, criminal crashes, pursuits, and vehicle-specific property offenses.

## Include

- DUI/DWI/OWI, drug-impaired driving, refusal-related arrests where criminal, open-container offenses linked to driving, and driving while intoxicated with a child passenger.

- Reckless driving, excessive-speed crimes, street racing, stunt driving, road rage involving a vehicle, hit-and-run/leaving the scene, vehicular assault, and vehicular homicide.

- Police pursuits, fleeing/eluding in a vehicle, ramming police or civilian vehicles, and using a vehicle as a weapon.

- Driving while suspended/revoked, no valid license, habitual traffic offender cases, unlawful vehicle registration/VIN/title activity, license-plate theft or concealment, and odometer fraud.

- Vehicle theft, carjacking, joyriding, catalytic-converter theft, chop shops, stolen vehicle possession, and vehicle burglary; use additional property/violent labels as appropriate.

- Commercial vehicle crimes, smuggling using vehicles, dangerous loads, and serious criminal violations by bus, rideshare, delivery, or truck drivers.

## Exclude / boundary

**Do not classify here: **Routine collisions with no alleged crime, traffic congestion, civil citations not treated as crime news, vehicle recalls, and crimes merely occurring near or inside a car when the vehicle is incidental.

## Common language signals

**Examples: **DUI, DWI, OWI, impaired driver, drunk driving, reckless driving, vehicular homicide, hit-and-run, fled a traffic stop, pursuit, stolen car, carjacking, road rage, suspended license, street racing, rammed cruiser, vehicle burglary.

## Overlap and multi-label rule

**Apply with: **Vehicular death receives Homicide/Death Investigation or a more specific Fatal Traffic tag; carjacking receives Robbery; auto theft receives Theft/Fraud; pursuits may also receive Resisting/Evading; drugs or weapons discovered during a stop receive their own labels. Do not classify every story containing the word 'driver' as vehicle crime—require alleged unlawful vehicle-related conduct.

# 6. Employee, Workplace & Occupational Crime

**Machine label: **EMPLOYEE_WORKPLACE

**Definition: **A cross-cutting context label for alleged crimes in which employment, professional duties, workplace access, occupational authority, entrusted property, customers, patients, students, clients, or employer resources materially enabled, motivated, concealed, or formed part of the conduct.

## Include

- Employee theft, embezzlement, payroll manipulation, refund/discount abuse, cash skimming, inventory theft, data theft, time-sheet fraud, procurement kickbacks, or misuse of company cards/accounts.

- Crimes against customers, patients, residents, students, passengers, clients, or employers committed through job access or professional trust.

- Caregiver, nurse, doctor, teacher, coach, clergy, law-enforcement, security, contractor, postal, delivery, rideshare, bank, retail, government, or licensed-professional misconduct when the role is essential to the alleged crime.

- Workplace violence, threats, sabotage, arson, stalking, or retaliation tied to current or former employment.

- Official corruption, bribery, falsifying records, evidence theft, misuse of databases, and abuse of public office in the course of duty.

- Former employees when their prior access, credentials, insider knowledge, grievance, or entrusted property materially connects to the offense.

## Exclude / boundary

**Do not classify here: **Any story that merely uses words such as employee, worker, manager, driver, nurse, teacher, or workplace. Exclude crimes unrelated to the person's job; victim-only occupation mentions; incidents happening at a workplace where employment is incidental; and ordinary HR misconduct that is not alleged to be criminal.

## Common language signals

**Examples: **employee accused of stealing, used customer information, on duty, while working, company funds, employer's account, former employee used credentials, caregiver charged, teacher arrested for conduct with student, postal worker stole mail, contractor defrauded client.

## Overlap and multi-label rule

**Apply with: **Always pair with an underlying offense. The classifier should require an occupational nexus: job access, job authority, entrusted assets, workplace target, on-duty conduct, professional victim relationship, or employment-linked motive.

# 7. Homicide, Suspicious Death & Body Discovery

**Machine label: **HOMICIDE_DEATH

**Definition: **Stories involving an intentional, reckless, negligent, or suspicious death; an attempted killing; discovery or concealment of human remains; or an active death investigation where criminality has not yet been resolved.

## Include

- Murder, capital/first-/second-degree murder, manslaughter, negligent homicide, felony murder, attempted murder, solicitation or conspiracy to kill, and murder-for-hire.

- Fatal shootings, stabbings, beatings, strangulations, poisonings, fires, child deaths, domestic killings, and deaths caused by vehicles when alleged criminal conduct is involved.

- Bodies or human remains found in homes, vehicles, trunks, water, wooded areas, dumpsters, containers, shallow graves, or public spaces.

- Concealment, dismemberment, disposal, tampering with remains, abuse of a corpse, or failure to report a death.

- Suspicious, unexplained, unattended, or in-custody deaths reported as investigations, even before charges, with a status tag distinguishing confirmed homicide from undetermined death.

- Cold cases, reopened death investigations, unidentified remains, and arrests or convictions tied to prior killings.

## Exclude / boundary

**Do not classify here: **Natural deaths with no criminal/suspicious angle, routine obituaries, nonfatal assaults, animal deaths, and purely civil wrongful-death claims. Overdose deaths belong here only when the story alleges homicide, poisoning, criminal supply resulting in death, or a suspicious death investigation.

## Common language signals

**Examples: **murder, homicide, manslaughter, killed, slain, fatal, dead, body found, remains discovered, death investigation, suspicious death, attempted murder, concealed a corpse, unidentified remains.

## Overlap and multi-label rule

**Apply with: **Add the relevant method/context label—Weapons, Assault, Domestic/Family, Child Maltreatment, Arson, Drugs, Traffic, Robbery, or Missing Persons. Track status separately: body discovery, suspicious/undetermined, attempted homicide, confirmed homicide, charged, convicted.

# 8. Resisting, Evading, Obstruction & Public Disturbance

**Machine label: **PUBLIC_ORDER_OBSTRUCTION

**Definition: **Offenses involving interference with police, courts, emergency responders, or public order, including resistance, flight, obstruction, disorderly behavior, unlawful public disruption, and certain nuisance offenses.

## Include

- Resisting arrest, obstructing an officer, fleeing on foot, evading detention, escape, failure to comply, providing false identifying information, and interfering with an investigation or arrest.

- Vehicle flight and pursuits (also Vehicle Crime), barricades, standoffs, and unlawful refusal to exit when charged as obstruction/resistance.

- Disorderly conduct, breach of peace, public intoxication, affray/fighting in public, riot-related offenses, unlawful assembly, disturbing the peace, aggressive public behavior, and certain harassment or menacing offenses.

- Misuse of 911, false alarms, bomb threats, swatting, interference with firefighters/EMS, tampering with evidence, witness intimidation, and obstruction of justice when connected to an immediate incident.

- Trespass when the central story is refusal to leave or disruption; add Property/Trespass if maintained separately.

## Exclude / boundary

**Do not classify here: **Mere criticism of police, lawful protest, noncriminal mental-health crisis, passive presence, ordinary rudeness, or an arrest where no resistance/obstruction is alleged. Do not infer resistance simply because force was used by officers.

## Common language signals

**Examples: **resisted arrest, obstructed, fled from officers, refused commands, disorderly conduct, breach of peace, public intoxication, disturbance, barricaded, standoff, false name, tampering with evidence, interfering with police.

## Overlap and multi-label rule

**Apply with: **Pair with the precipitating crime. Vehicle pursuits receive Traffic/Vehicle. Assaults on officers receive Assault.

# 9. Assault, Weapons & Violent Crime

**Machine label: **ASSAULT_WEAPONS_VIOLENCE

**Definition: **Non-homicide crimes involving actual, attempted, or threatened physical harm; unlawful force; serious intimidation; or possession, display, discharge, or use of a weapon. Because assault and weapons are distinct concepts, the data model should ideally preserve separate sublabels even if they roll up to one general category.

## Include

- Simple, aggravated, felonious, and sexualized-but-nonsexual assault; battery; serious bodily injury; stabbing, shooting, beating, choking/strangulation, poisoning, maiming, torture, or assault with a vehicle.

- Attempted assault, credible threats of violence, menacing, brandishing, terroristic threats, intimidation, and pointing or firing a weapon.

- Unlawful firearm possession, prohibited-person possession, concealed-carry violations, illegal modification, ghost guns, stolen firearms, machine-gun devices, unlawful discharge, and weapons trafficking.

- Knife, blunt object, explosive, chemical agent, vehicle, or other dangerous-weapon offenses.

- Mass-violence plots, active-shooter incidents, bomb threats with credible weapon conduct, and attacks on police, healthcare workers, teachers, transit workers, or other victims.

## Exclude / boundary

**Do not classify here: **Homicide as the sole label when a death occurred—add Homicide; lawful firearm possession; weapons merely mentioned as recovered property with no alleged offense unless possession itself is unlawful; and verbal arguments without threats or force.

## Common language signals

**Examples: **assault, battery, attacked, beat, stabbed, shot, strangled, choked, injured, threatened, menacing, brandished, firearm charge, prohibited possessor, illegal gun, discharged, weapon.

## Overlap and multi-label rule

**Apply with: **Add Domestic/Family, Robbery, Child Maltreatment, Hate/Bias, Weapons, Homicide, or Public Order as applicable. Where possible store separate flags: assault_present, threat_present, weapon_present, weapon_type, injury_severity.

# 10. Drugs & Narcotics

**Machine label: **DRUGS_NARCOTICS

**Definition: **Offenses involving unlawful possession, use, manufacture, cultivation, processing, prescription, distribution, sale, transport, importation, concealment, or diversion of controlled substances, drug paraphernalia, or regulated medications.

## Include

- Possession, possession with intent, trafficking, distribution, delivery, sales, conspiracy, controlled buys, stash houses, clandestine labs, cultivation, pill mills, and prescription fraud/diversion.

- Fentanyl, heroin, cocaine, methamphetamine, illicit pills, cannabis where unlawful, synthetic drugs, club drugs, inhalants, and unlawfully possessed prescription medication.

- Drug smuggling in vehicles, luggage, mail, cargo, prisons, schools, or across borders; body packing; concealment in food or products.

- Drug paraphernalia and precursor chemicals when charged; overdose-related prosecutions, drug-induced homicide, or poisoning when alleged.

- Caregiver/parent drug exposure that endangers a child, and employees diverting medication or drugs.

## Exclude / boundary

**Do not classify here: **Legal cannabis business coverage without alleged crime, general addiction/public-health stories, alcohol-only offenses (use DUI/Public Order where relevant), tobacco/vaping violations unless criminally charged, and drug references that are merely background.

## Common language signals

**Examples: **narcotics, controlled substance, fentanyl, cocaine, meth, heroin, pills, trafficking, possession with intent, drug bust, seized, overdose, paraphernalia, prescription fraud, smuggling.

## Overlap and multi-label rule

**Apply with: **Add Traffic for impaired driving or vehicle smuggling, Child Maltreatment for child exposure, Employee Crime for diversion through a job, Homicide for fatal poisoning/drug-induced death, and Weapons when separately alleged.

# 11. Kidnapping, Abduction, Unlawful Restraint & Missing Persons

**Machine label: **KIDNAPPING_MISSING

**Definition: **Stories involving taking, transporting, hiding, confining, holding, luring, or restraining a person without lawful consent, as well as disappearances and missing-person investigations where the cause may be criminal, endangered, or unknown.

## Include

- Kidnapping, abduction, false imprisonment, unlawful restraint, hostage-taking, confinement, luring, and ransom demands.

- Parental kidnapping, custodial interference, failure to return a child, and taking a child contrary to a custody order.

- Human trafficking when movement/control/exploitation is alleged; also apply Human Trafficking/Exploitation.

- Missing children, endangered adults, vulnerable missing persons, suspicious disappearances, Amber/Silver alerts, and long-term missing-person cases.

- Recovered or located missing persons, remains identified as a missing person, and arrests connected to a disappearance.

## Exclude / boundary

**Do not classify here: **A person temporarily unreachable with no official missing-person component, runaway stories with no police/public-safety angle, lawful custody changes, civil custody disagreements without alleged interference, and ordinary transportation of a consenting person.

## Common language signals

**Examples: **kidnapped, abducted, held against will, false imprisonment, hostage, missing, disappeared, endangered missing, Amber Alert, Silver Alert, custodial interference, lured, ransom.

## Overlap and multi-label rule

**Apply with: **Apply separate status: missing/unresolved, located safe, located deceased, suspected abduction, confirmed kidnapping. Add Homicide/Body Discovery if deceased, Trafficking if exploitative, Domestic/Family for relationship cases, and Child Maltreatment for child victims.

# 12. Arson, Vandalism & Destruction of Property

**Machine label: **ARSON_DESTRUCTION

**Definition: **Intentional, reckless, or criminally negligent burning, damaging, defacing, sabotaging, contaminating, or destroying real or personal property, infrastructure, vehicles, buildings, evidence, or public resources.

## Include

- Arson of homes, businesses, vehicles, churches, schools, government buildings, forests, or other property; attempted arson and possession/use of incendiary devices.

- Vandalism, criminal mischief, graffiti, smashing property, slashing tires, damaging utilities, infrastructure sabotage, and deliberate contamination.

- Explosion or bombing that primarily damages property; add Weapons/Violence when people are targeted or endangered.

- Domestic or workplace property destruction, insurance-motivated fires, riot damage, and burning evidence or a body.

- Tampering that creates a major safety risk, such as damaging rail, power, communications, water, or emergency equipment.

## Exclude / boundary

**Do not classify here: **Accidental fires with no alleged offense, weather damage, ordinary wear, lawful demolition, civil property disputes without criminal damage, and theft where property is taken but not damaged.

## Common language signals

**Examples: **arson, intentionally set fire, incendiary, Molotov cocktail, vandalism, criminal mischief, damaged, smashed, destroyed, defaced, graffiti, sabotage, slashed tires.

## Overlap and multi-label rule

**Apply with: **Add Homicide/Assault for deaths or injuries, Domestic/Family or Employee Crime for context, Fraud for insurance schemes, Hate/Bias for targeted property, and Public Order for riot-related destruction.

# 13. Robbery, Burglary, Trespass & Home Invasion

**Machine label: **ROBBERY_BURGLARY_ENTRY

**Definition: **Crimes centered on taking property by force or threat, unlawfully entering or remaining in a structure/vehicle with criminal intent, invading an occupied place, or unlawfully entering property. These should not be collapsed into generic theft because force and entry patterns are operationally important.

## Include

- Robbery, armed robbery, strong-arm robbery, mugging, purse snatching involving force, commercial robbery, bank robbery, and carjacking.

- Burglary of homes, businesses, schools, storage units, construction sites, and vehicles; breaking and entering; attempted burglary; possession of burglary tools.

- Home invasion, occupied burglary, robbery inside a residence, and burglary crews.

- Criminal trespass, unlawful entry, refusing to leave private property when charged, and squatting-related criminal entry where applicable.

## Exclude / boundary

**Do not classify here: **Shoplifting with no force/entry, theft by an authorized occupant or employee without unlawful entry, civil landlord-tenant disputes, lawful entry followed by an unrelated offense unless burglary law is alleged, and vehicle theft without entry facts.

## Common language signals

**Examples: **robbery, robbed at gunpoint, mugged, carjacking, burglary, broke into, home invasion, forced entry, burglarized, trespassing, burglary tools.

## Overlap and multi-label rule

**Apply with: **Robbery also receives Theft/Fraud and Assault/Weapons if force or a weapon is present. Burglary often also receives Theft/Fraud. Vehicle burglary receives Traffic/Vehicle.

# 14. Cybercrime, Digital Crime & Identity Abuse

**Machine label: **CYBER_DIGITAL

**Definition: **Crime in which a computer, network, online account, digital platform, electronic communication, or data system is the target, essential instrument, or primary environment of the offense—not merely incidental communication.

## Include

- Hacking, unauthorized access, malware, ransomware, denial-of-service attacks, data theft, credential theft, SIM swapping, account takeover, and cyber extortion.

- Phishing, business-email compromise, online investment/romance scams, payment diversion, cryptocurrency fraud, marketplace fraud, and digital identity theft.

- Cyberstalking, doxxing, swatting arranged online, online threats, sextortion, nonconsensual intimate images, and unlawful surveillance.

- Computer-facilitated child exploitation, enticement, illegal material distribution, and trafficking recruitment.

- Misuse of employer/government databases, altering electronic records, digital evidence tampering, and insider data theft.

## Exclude / boundary

**Do not classify here: **A conventional crime merely discussed by text message or posted on social media, routine online arguments, platform-policy violations without alleged lawbreaking, and ordinary fraud that could occur without any meaningful digital component.

## Common language signals

**Examples: **hacked, ransomware, phishing, account takeover, data breach, malware, cyberstalking, online scam, cryptocurrency fraud, SIM swap, unauthorized database access, sextortion, doxxing.

## Overlap and multi-label rule

**Apply with: **Frequently pair with Theft/Fraud, Stalking/Harassment, Employee Crime, or Child Maltreatment.

# 15. Stalking, Harassment, Threats & Protection-Order Violations

**Machine label: **STALKING_HARASSMENT

**Definition: **Repeated or targeted conduct that causes fear, intimidation, substantial emotional distress, or unwanted surveillance/contact, including credible threats and violations of court-ordered no-contact protections.

## Include

- Stalking, cyberstalking, repeated unwanted contact, following, surveillance, tracking devices, threatening messages, targeted harassment, and intimidation.

- Violation of restraining, protective, no-contact, or anti-harassment orders.

- Threats to kill or injure, terroristic threats, threats against schools/public places, witness intimidation, and retaliation.

- Bias-motivated harassment and workplace or relationship stalking.

## Exclude / boundary

**Do not classify here: **One rude interaction without a criminal threat, lawful protest/criticism, noncriminal workplace conflict, and vague social-media hostility without a credible allegation or charge.

## Common language signals

**Examples: **stalking, harassing, repeated messages, threatened to kill, protection order violation, restraining order, no-contact order, tracking device, intimidated witness.

## Overlap and multi-label rule

**Apply with: **Add Domestic/Family, Cybercrime, Assault/Weapons, Employee Crime, or Hate/Bias as facts require.

# 16. Human Trafficking, Smuggling & Exploitation

**Machine label: **TRAFFICKING_SMUGGLING

**Definition: **Recruiting, transporting, harboring, obtaining, controlling, or exploiting people through force, fraud, coercion, abuse of vulnerability, or unlawful commercial arrangements; and organized movement of people or contraband across borders or jurisdictions.

## Include

- Sex trafficking, labor trafficking, forced labor, debt bondage, trafficking of minors, and exploitation through hotels, massage businesses, domestic work, agriculture, or online advertising.

- Migrant/human smuggling, harboring, stash houses, high-risk vehicle transport, and payment-based unlawful border movement.

- Organ trafficking or exploitation, document confiscation, coercive recruitment, and trafficking conspiracies.

- Contraband smuggling—drugs, weapons, currency, wildlife, stolen goods—when the smuggling operation is a central fact.

## Exclude / boundary

**Do not classify here: **Consensual adult movement without exploitation, immigration status alone, ordinary transportation crimes, and prostitution stories with no trafficking indicators unless local charges explicitly allege trafficking.

## Common language signals

**Examples: **human trafficking, sex trafficking, labor trafficking, forced labor, smuggling migrants, stash house, harboring, transported for payment, coerced, exploited, trafficking ring.

## Overlap and multi-label rule

**Apply with: **Add Kidnapping, Child Maltreatment, Drugs, Weapons, or Vehicle Crime. Distinguish trafficking (exploitation) from smuggling (movement/service), although a case may involve both.

# 17. Elder & Vulnerable Adult Abuse or Exploitation

**Machine label: **ELDER_VULNERABLE_ABUSE

**Definition: **Abuse, neglect, abandonment, intimidation, sexual abuse, or financial exploitation of an older adult or a person whose disability, illness, dependency, or diminished capacity increases vulnerability.

## Include

- Caregiver neglect, unsafe living conditions, withholding care/medication, physical abuse, abandonment, and unlawful restraint.

- Theft, coercion, forged documents, misuse of power of attorney, fraudulent transfers, scams, and exploitation of benefits or bank accounts.

- Abuse in nursing homes, assisted living, group homes, hospitals, or private residences.

- Crimes by relatives, guardians, healthcare workers, contractors, or strangers who target vulnerability.

## Exclude / boundary

**Do not classify here: **Age alone with no abuse/exploitation nexus, legitimate financial decisions, poor outcomes without alleged misconduct, and ordinary theft where vulnerability is not materially relevant.

## Common language signals

**Examples: **elder abuse, vulnerable adult, dependent adult, exploited senior, caregiver neglect, nursing home abuse, power of attorney misuse, stole life savings.

## Overlap and multi-label rule

**Apply with: **Add Theft/Fraud, Employee Crime, Family/Relationship, Assault, or Homicide.

# 18. Hate Crime, Bias & Extremism

**Machine label: **HATE_BIAS_EXTREMISM

**Definition: **A cross-cutting motive/context label for alleged crimes motivated wholly or partly by bias against protected or targeted identity characteristics, or conducted in furtherance of violent extremist ideology.

## Include

- Bias-motivated assault, homicide, threats, harassment, vandalism, arson, stalking, or intimidation.

- Crimes targeting race, ethnicity, nationality, religion, disability, sexual orientation, gender, gender identity, or other protected status under relevant law.

- Desecration or attacks on houses of worship, cemeteries, community centers, or identity-linked property when bias is alleged.

- Domestic terrorism or extremist plots involving violence, credible threats, weapons, or destructive acts.

## Exclude / boundary

**Do not classify here: **Offensive speech alone where not criminal, demographic differences between suspect and victim without evidence of motive, political disagreement without criminal conduct, and speculative labeling not supported by authorities or facts.

## Common language signals

**Examples: **hate crime, bias-motivated, racial slur during attack, targeted because of, antisemitic, Islamophobic, anti-LGBTQ, white supremacist, extremist plot, domestic terrorism.

## Overlap and multi-label rule

**Apply with: **Always pair with the underlying offense such as Assault, Homicide, Threats, or Arson/Destruction. Store alleged_bias_basis and whether the label is official, alleged, or inferred from reported evidence.

# 19. School, Institutional & Public-Facility Crime

**Machine label: **SCHOOL_INSTITUTION_CONTEXT

**Definition: **A cross-cutting location/authority context for crime occurring in, directed at, or materially enabled by a school, daycare, hospital, care facility, jail, library, transit system, government building, or similar institution. Use only when institutional setting changes the nature, victims, access, or public-safety significance of the case.

## Include

- School threats, weapons at school, student assaults, educator misconduct, institutional abuse, library/public lewdness, hospital assaults, jail crimes, and attacks on public facilities.

- Crimes enabled by institutional access, supervision, custody, or entrusted duty.

- Threats, hoaxes, evacuations, vandalism, arson, or theft specifically targeting institutions.

## Exclude / boundary

**Do not classify here: **A suspect merely attended a school or once worked at an institution; a crime near a facility with no meaningful connection; and ordinary incidents where location is incidental.

## Common language signals

**Examples: **at school, campus, daycare, nursing home, hospital, jail, prison, library, transit station, government building, school resource officer.

## Overlap and multi-label rule

**Apply with: **Always pair with the substantive offense and relevant context tags such as Juvenile, Employee, Child Maltreatment, Assault/Weapons, or Public Order.

# Cross-category conflict rules

## Theft vs. robbery

**Rule: **Theft is taking property without force; robbery is taking or attempting to take through force, threat, or intimidation. Assign Robbery, and optionally the Theft/Fraud roll-up.

## Theft vs. burglary

**Rule: **Burglary centers on unlawful entry or remaining with criminal intent. The intended/completed theft may be an additional label.

## Vehicle theft vs. carjacking

**Rule: **Vehicle theft without confronting an occupant is Theft + Vehicle Crime. Taking a vehicle by force/threat is Robbery/Carjacking + Vehicle Crime + Assault/Weapons where supported.

## Assault vs. homicide

**Rule: **A fatal attack receives Homicide plus method/context labels. An attempted killing receives Homicide (attempted) plus Assault. Do not erase the violent method.

## Missing person vs. kidnapping

**Rule: **Missing is an investigative status; kidnapping requires evidence/allegation of unlawful taking or confinement. Do not infer abduction solely because someone is missing.

## Child victim vs. child maltreatment

**Rule: **A minor victim alone is insufficient. Apply Child Maltreatment when abuse, neglect, exploitation, abandonment, failure to protect, or dangerous exposure is alleged.

## Employee mentioned vs. employee crime

**Rule: **Require an occupational nexus. A delivery driver arrested for off-duty DUI is Vehicle Crime, not Employee Crime, unless job operation/access is material.

## Teen victim vs. teen offender

**Rule: **Teen Crime is an offender-age/context label. Track teen victims separately.

## Drug mention vs. drug crime

**Rule: **Past drug use or toxicology context is not enough. Require alleged unlawful possession, manufacture, sale, transport, diversion, or criminally relevant supply.

## Weapon present vs. weapon offense

**Rule: **A lawfully possessed weapon or incidental mention is not automatically Weapons Crime. Label when used, threatened, unlawfully possessed, trafficked, modified, or otherwise charged.

## Domestic location vs. domestic relationship

**Rule: **A crime inside a house is not automatically domestic violence. Require a qualifying personal/household relationship or a reported domestic classification.

## Public disturbance vs. mental-health crisis

**Rule: **Do not label crisis behavior as criminal unless the article alleges an offense, arrest, citation, or criminal investigation. Record crisis as a separate contextual attribute if needed.

## Arson vs. accidental fire

**Rule: **Require intentional/reckless criminal fire-setting or an official arson investigation; do not classify every structure fire as arson.

## Fraud vs. civil dispute

**Rule: **Require alleged deception, conversion, forgery, unauthorized use, or criminal charge/investigation; nonpayment or breach of contract alone is civil.

## Trafficking vs. smuggling

**Rule: **Trafficking centers on exploitation; smuggling centers on unlawful movement for a service/payment. They may overlap, but neither should be inferred from immigration status alone.

# Headline-only classification safeguards

**Default: **If only a headline and URL slug are available, assign labels only when the conduct is explicit. Reduce confidence and set needs_review=true for ambiguous roles, ages, relationships, or outcomes.

- Resolve grammatical role: distinguish suspect from victim, officer, witness, prosecutor, and person quoted.

- Treat 'charged,' 'accused,' 'arrested for,' and 'police say' as allegation/status markers—not proof.

- Do not classify from occupation words alone: driver, teacher, nurse, coach, worker, manager, employee, owner, clerk, or contractor.

- Do not classify from location words alone: school, workplace, home, bar, highway, hospital, library, store, or jail.

- Do not infer homicide from 'body found' unless the category permits Body Discovery/Suspicious Death; set death_status=undetermined when cause/manner is unknown.

- Do not infer kidnapping from 'missing,' employee misconduct from 'employee,' domestic violence from 'wife/husband,' or weapons crime from 'gun' without a criminal predicate.

- If the headline describes only a procedural update, inherit offense labels only when the underlying offense is stated in the headline/metadata or reliably linked case record.

# Negative / noncrime routing

**Why needed: **A complete classifier needs explicit destinations for links that are not new criminal incidents; otherwise the model will force them into crime buckets.

**NONCRIME_ACCIDENT: **Accidental fire, accidental injury, ordinary collision, missing property, or other event with no alleged offense.

**CIVIL_DISPUTE: **Lawsuit, contract dispute, custody litigation, eviction, employment dispute, or regulatory matter with no alleged crime.

**POLICY_GENERAL: **General crime trends, legislation, prevention advice, commentary, statistics, or agency policy—not a specific case.

**COURT_PROCEDURAL_ONLY: **Hearing, appeal, sentence administration, release, or lawsuit where the underlying crime is not identifiable from available text.

**DUPLICATE_UPDATE: **A repeated or follow-up article about a previously classified incident; link to the master case rather than count as a new case.

**INSUFFICIENT_INFORMATION: **Crime may be possible, but the available headline/snippet does not support a reliable category.

# Quality-control checklist

- At least one evidence phrase supports every assigned label.

- Every context label has a verified nexus, not a keyword coincidence.

- Offender and victim roles/ages are not reversed.

- Fatality, injury, weapon, vehicle, relationship, and employment attributes are captured separately.

- Missing-person status is not mistaken for confirmed kidnapping or homicide.

- Allegation/charge/conviction status is preserved.

- Multiple independent offenses receive multiple labels.

- Noncrime and duplicate updates are routed outside the new-case pool.

- Low-information records are reviewed rather than confidently overclassified.

- State-specific charge names are normalized to facts while original charge text is retained.

# Recommended hierarchy for implementation

**Person harm: **Homicide/Death; Assault/Weapons; Child Maltreatment; Kidnapping/Missing; Stalking/Threats; Elder/Vulnerable Abuse

**Property/economic: **Theft/Fraud; Robbery/Burglary/Entry; Arson/Destruction; Cyber/Digital; Vehicle property crime

**Regulated/enterprise: **Drugs/Narcotics; Trafficking/Smuggling

**Public order: **Resisting/Evading/Public Disturbance; serious traffic/DUI offenses

**Cross-cutting contexts: **Family/Relationship; Juvenile/Teen offender; Employee/Workplace; School/Institution; Hate/Bias

**Routing/status: **Noncrime; Duplicate Update; Insufficient Information; case stage; allegation status

# Final instruction to the model

**Identify what allegedly happened, who was involved, how they were connected, and what stage the case has reached. Assign every supported substantive and contextual label. Do not select stories for editorial value at this stage, do not infer unsupported facts, and do not let a single keyword override the full meaning of the headline or article.**
