**AI TRAINING REFERENCE**

# **Crime News Subcategory Classification Guide**

**Detailed second-stage taxonomy for accurate, multi-label crime-news classification**

| **Scope** | 19 parent categories / 184 subcategories |
| --- | --- |
| **Classification mode** | Assign every supported subcategory; do not decide inclusion or exclusion for downstream use |
| **Version** | 1.0 — September 2026 |

Designed for article-level identification from headlines, summaries, and full text.

# How to Use This Guide

**Purpose. **After a news item has been assigned to one or more parent crime categories, use this guide to identify the more specific crime topics it supports. This stage describes what the case is about; it does not decide whether the case should be retained by a later inclusion/exclusion workflow.

## Core Classification Rules

- Use multi-label classification. Assign every subcategory directly supported by the article; do not force a single label when several distinct behaviors are reported.

- Require affirmative evidence. A label needs an allegation, charge, factual description, official finding, or other clear text signal. Do not infer a crime from demographics, location, or reputation alone.

- Classify conduct, context, and victim relationship separately when the guide provides separate labels. A single incident may therefore receive several subcategories within one parent and across different parents.

- Use the most specific supported label. Add a broader companion label only when it captures additional conduct or materially useful context, not merely because it is technically compatible.

- Apply boundary rules before deciding. The exclusion text identifies nearby labels, civil or regulatory matters, and facts that are insufficient by themselves.

- Treat arrests, charges, allegations, convictions, and acquittals as procedural status—not proof standards invented by the classifier. Describe the reported conduct without independently deciding guilt.

- If the article is too thin to support a subtype, retain the parent category and mark subcategory review as needed instead of guessing.

## Recommended Machine Output

| **Field** | **Expected value** |
| --- | --- |
| parent_category | One or more parent category names or stable parent codes. |
| subcategory_codes | Array of every supported stable code, such as EC-01 and EC-03. |
| primary_subcategory | The subtype most central to the reported incident; optional when evidence does not support ranking. |
| evidence | A short article span or factual paraphrase supporting each assigned code. |
| confidence | Per-label confidence, preferably high / medium / low or a calibrated numeric score. |
| needs_review | True when article detail is insufficient, boundaries conflict, or a missing taxonomy concept may be present. |

# Parent Category Index

The guide preserves the 19-category top-level taxonomy. The codes below are stable within this document and are intended for training, evaluation, and downstream scripts.

| **No.** | **Parent category** | **Code range** | **Count** |
| --- | --- | --- | --- |
| 1 | Child Neglect, Endangerment & Child Abuse | CN-01 to CN-09 | 9 |
| 2 | Family, Domestic & Relationship Cases | FR-01 to FR-08 | 8 |
| 3 | Teen & Juvenile-Involved Crime | JT-01 to JT-08 | 8 |
| 4 | Theft, Fraud & Financial Crime | TF-01 to TF-12 | 12 |
| 5 | Traffic, DUI & Vehicle Crime | TV-01 to TV-11 | 11 |
| 6 | Employee, Workplace & Occupational Crime | EC-01 to EC-07 | 7 |
| 7 | Homicide, Suspicious Death & Body Discovery | HD-01 to HD-10 | 10 |
| 8 | Resisting, Evading, Obstruction & Public Disturbance | PO-01 to PO-10 | 10 |
| 9 | Assault, Weapons & Violent Crime | AV-01 to AV-12 | 12 |
| 10 | Drugs & Narcotics | DN-01 to DN-10 | 10 |
| 11 | Kidnapping, Abduction, Unlawful Restraint & Missing Persons | KM-01 to KM-10 | 10 |
| 12 | Arson, Vandalism & Destruction of Property | AD-01 to AD-11 | 11 |
| 13 | Robbery, Burglary, Trespass & Home Invasion | RB-01 to RB-11 | 11 |
| 14 | Cybercrime, Digital Crime & Identity Abuse | CY-01 to CY-10 | 10 |
| 15 | Stalking, Harassment, Threats & Protection-Order Violations | SH-01 to SH-09 | 9 |
| 16 | Human Trafficking, Smuggling & Exploitation | HT-01 to HT-08 | 8 |
| 17 | Elder & Vulnerable Adult Abuse or Exploitation | EV-01 to EV-08 | 8 |
| 18 | Hate Crime, Bias & Extremism | HB-01 to HB-08 | 8 |
| 19 | School, Institutional & Public-Facility Crime | SI-01 to SI-12 | 12 |

**Total: 184 subcategories**

# 1. Child Neglect, Endangerment & Child Abuse

**Parent definition: **Criminal abuse, neglect, abandonment, exploitation, or dangerous exposure involving a person under 18. Apply every supported subtype; these labels describe the form of maltreatment, not editorial value.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| CN-01 | Physical Child Abuse |
| CN-02 | Severe Neglect / Unsafe Living Conditions |
| CN-03 | Lack of Supervision / Child Left Alone |
| CN-04 | Child Left in Vehicle / Temperature Danger |
| CN-05 | Caregiver Intoxication / Drug Exposure |
| CN-06 | Medical Neglect / Failure to Obtain Care |
| CN-07 | Abandonment / Unlawful Desertion |
| CN-08 | Failure to Protect / Permitting Abuse |
| CN-09 | Institutional or Paid-Caregiver Maltreatment |

## CN-01 — Physical Child Abuse

**Definition: **Intentional or unlawfully reckless physical force against a child.

**Include when: **The article alleges inflicted injury, painful punishment, violent handling, or an assault by a parent, caregiver, household member, or other responsible adult.

**Exclude / boundary: **Exclude accidental injury without suspected abuse and ordinary discipline with no alleged unlawful force or injury.

**Typical roles: **Parent; guardian; stepparent; caregiver; babysitter; household member.

**Common methods / evidence signals: **Hitting; beating; burning; shaking; choking; throwing; poisoning; unlawful restraint.

**Primary target or asset: **Child's body, safety, and physical wellbeing.

## CN-02 — Severe Neglect / Unsafe Living Conditions

**Definition: **Failure to provide minimally safe food, shelter, hygiene, sanitation, clothing, or living conditions.

**Include when: **Authorities describe filth, infestation, dangerous structural conditions, lack of utilities, severe malnutrition, or accessible hazards creating substantial risk.

**Exclude / boundary: **Poverty or clutter alone is insufficient without alleged neglect, danger, or failure to act.

**Typical roles: **Parent; guardian; household caregiver; foster provider.

**Common methods / evidence signals: **Withholding necessities; allowing waste, pests, exposed wiring, drugs, weapons, or dangerous debris to remain accessible.

**Primary target or asset: **Basic needs, home safety, health, and development.

## CN-03 — Lack of Supervision / Child Left Alone

**Definition: **A responsible adult leaves a child without age-appropriate supervision or allows the child to wander or face avoidable danger.

**Include when: **The child's age, duration, location, surrounding hazards, or caregiver incapacity makes the lack of supervision criminally significant.

**Exclude / boundary: **Exclude brief age-appropriate independence and situations where no responsible adult had custody or notice.

**Typical roles: **Parent; guardian; babysitter; daycare worker; temporary caregiver.

**Common methods / evidence signals: **Leaving home alone; wandering child; unattended hotel room; caregiver absent, asleep, or unreachable.

**Primary target or asset: **Child's immediate safety and supervision.

## CN-04 — Child Left in Vehicle / Temperature Danger

**Definition: **A child is left unattended or insufficiently supervised in a vehicle under dangerous heat, cold, confinement, or other conditions.

**Include when: **Police, witnesses, rescuers, or medical staff report hazardous temperature, distress, prolonged confinement, or inability to exit.

**Exclude / boundary: **Exclude a supervised child in safe conditions or a momentary lawful situation without danger.

**Typical roles: **Parent; guardian; shopper; caregiver; driver.

**Common methods / evidence signals: **Locked vehicle; hot car; cold car; engine off; windows closed; child unable to exit.

**Primary target or asset: **Child's life, temperature safety, and freedom from confinement.

## CN-05 — Caregiver Intoxication / Drug Exposure

**Definition: **A caregiver's intoxication, drug activity, or accessible substances place a child at risk.

**Include when: **The adult is impaired while responsible for the child, drives impaired with the child, exposes the child to drug use/manufacture, or leaves substances accessible.

**Exclude / boundary: **A caregiver's past drug history or lawful medication use is insufficient without present risk or unlawful conduct.

**Typical roles: **Parent; guardian; babysitter; household member.

**Common methods / evidence signals: **Passing out; impaired driving; drug use near child; accessible fentanyl, methamphetamine, pills, cannabis, or paraphernalia.

**Primary target or asset: **Child's supervision, health, and protection from toxic substances.

## CN-06 — Medical Neglect / Failure to Obtain Care

**Definition: **A responsible adult fails or refuses to obtain necessary medical care or intentionally interferes with treatment.

**Include when: **The need is serious or urgent and the caregiver knew or reasonably should have known that delay or refusal created substantial harm.

**Exclude / boundary: **Exclude reasonable treatment choices, minor delays, or poor outcomes without alleged criminal neglect.

**Typical roles: **Parent; guardian; medical decision-maker; facility caregiver.

**Common methods / evidence signals: **Ignoring injuries; withholding medicine; failing to seek emergency care; obstructing prescribed treatment.

**Primary target or asset: **Child's health, recovery, and access to necessary care.

## CN-07 — Abandonment / Unlawful Desertion

**Definition: **A caregiver intentionally deserts, relinquishes, or leaves a child without a safe responsible arrangement.

**Include when: **The child is left in a public place, with an unsafe person, on a roadway, or for an extended period without lawful care.

**Exclude / boundary: **Exclude lawful safe-haven surrender, authorized placement, or temporary separation with adequate care.

**Typical roles: **Parent; guardian; custodian; caregiver.

**Common methods / evidence signals: **Leaving child at roadside, motel, business, stranger's home, or unattended residence; failing to return.

**Primary target or asset: **Custody, shelter, supervision, and personal safety.

## CN-08 — Failure to Protect / Permitting Abuse

**Definition: **A responsible adult knowingly allows another person to abuse, exploit, or dangerously expose a child.

**Include when: **The caregiver knew or had clear notice of the danger and failed to intervene, report, remove the child, or obtain help.

**Exclude / boundary: **Exclude cases based only on hindsight, rumor, or a caregiver who reasonably lacked knowledge or ability to act.

**Typical roles: **Parent; guardian; household adult; institutional supervisor.

**Common methods / evidence signals: **Ignoring reported abuse; returning child to known abuser; concealing injuries; blocking investigation.

**Primary target or asset: **Child's protection from a known dangerous person.

## CN-09 — Institutional or Paid-Caregiver Maltreatment

**Definition: **Abuse or neglect enabled by a daycare, foster, school, camp, treatment, residential, or paid-care role.

**Include when: **Professional access, entrusted supervision, or institutional custody is central to the alleged maltreatment.

**Exclude / boundary: **An employee merely being present is insufficient; the role must create access, authority, duty, or concealment.

**Typical roles: **Daycare worker; foster parent; teacher; aide; coach; residential staff; paid babysitter.

**Common methods / evidence signals: **Physical punishment; neglect; restraint; isolation; failure to supervise; concealment or false records.

**Primary target or asset: **Child, student, resident, or client entrusted to care.

# 2. Family, Domestic & Relationship Cases

**Parent definition: **Crime arising from an intimate, family, co-parenting, household, or former-relationship context. These are relationship subtypes and should be paired with the underlying offense.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| FR-01 | Intimate-Partner Assault / Strangulation |
| FR-02 | Domestic Homicide / Attempted Homicide |
| FR-03 | Parent–Child / Intergenerational Violence |
| FR-04 | Sibling / Extended-Family Violence |
| FR-05 | Relationship Stalking / Protection-Order Violation |
| FR-06 | Custody Interference / Parental Abduction |
| FR-07 | Relationship-Motivated Property Destruction / Arson |
| FR-08 | Family Financial Exploitation / Theft |

## FR-01 — Intimate-Partner Assault / Strangulation

**Definition: **Physical violence by a current or former romantic or intimate partner.

**Include when: **The suspect and victim are spouses, dating partners, ex-partners, or intimate co-parents and the article alleges assault, battery, strangulation, or injury.

**Exclude / boundary: **Exclude ordinary arguments and crimes between acquaintances with no intimate relationship.

**Typical roles: **Spouse; boyfriend/girlfriend; ex-partner; dating partner; co-parent.

**Common methods / evidence signals: **Hitting; choking; strangulation; stabbing; shooting; restraint; vehicle assault.

**Primary target or asset: **Partner's body, safety, and freedom.

## FR-02 — Domestic Homicide / Attempted Homicide

**Definition: **A killing or attempted killing within an intimate or household relationship.

**Include when: **The relationship is material to the death, attempt, planning, or motive.

**Exclude / boundary: **Exclude a homicide merely occurring in a home where no family/relationship nexus is reported.

**Typical roles: **Partner; ex-partner; spouse; household member.

**Common methods / evidence signals: **Shooting; stabbing; strangulation; poisoning; vehicular attack; murder-suicide attempt.

**Primary target or asset: **Life and bodily safety of intimate or household victim.

## FR-03 — Parent–Child / Intergenerational Violence

**Definition: **Violent crime between adult relatives across generations, apart from child-maltreatment classification.

**Include when: **An adult child attacks a parent/grandparent, or a parent attacks an adult child, and the family link is central.

**Exclude / boundary: **Use Child Maltreatment when the victim is a minor and abuse/endangerment is alleged.

**Typical roles: **Adult child; parent; stepparent; grandparent; in-law.

**Common methods / evidence signals: **Assault; threats; homicide; property destruction; unlawful restraint.

**Primary target or asset: **Relative's safety, residence, or property.

## FR-04 — Sibling / Extended-Family Violence

**Definition: **Crime between siblings, cousins, in-laws, or other relatives.

**Include when: **A family dispute, shared property, caregiving conflict, inheritance, or household tension materially explains the incident.

**Exclude / boundary: **Exclude crimes where kinship is incidental and not connected to conduct or motive.

**Typical roles: **Sibling; cousin; aunt/uncle; in-law; extended relative.

**Common methods / evidence signals: **Assault; threats; weapon use; homicide; vandalism.

**Primary target or asset: **Relative, shared home, inheritance, or family property.

## FR-05 — Relationship Stalking / Protection-Order Violation

**Definition: **Repeated unwanted contact, surveillance, threats, or court-order violations involving a partner or ex-partner.

**Include when: **The conduct follows separation, rejection, custody conflict, or a domestic protection order.

**Exclude / boundary: **A single nonthreatening contact or lawful co-parenting communication is insufficient.

**Typical roles: **Ex-partner; spouse; dating partner; co-parent.

**Common methods / evidence signals: **Following; repeated calls/messages; GPS tracking; showing up at home/work; violating no-contact order.

**Primary target or asset: **Victim's privacy, safety, movement, and court protection.

## FR-06 — Custody Interference / Parental Abduction

**Definition: **A parent or relative unlawfully takes, hides, retains, or fails to return a child contrary to custody rights or an order.

**Include when: **Police or courts identify custodial interference, parental kidnapping, concealment, or refusal to return.

**Exclude / boundary: **Exclude civil custody disagreement without alleged unlawful taking, concealment, or criminal order violation.

**Typical roles: **Parent; noncustodial parent; grandparent; relative; co-parent.

**Common methods / evidence signals: **Taking across jurisdictions; hiding child; disabling contact; failing to return after visit.

**Primary target or asset: **Child's lawful custody, location, and access to guardian.

## FR-07 — Relationship-Motivated Property Destruction / Arson

**Definition: **Property damage or fire-setting arising from jealousy, breakup, retaliation, or domestic conflict.

**Include when: **The damaged target belongs to a partner, ex-partner, relative, or shared household and the relationship motive is reported.

**Exclude / boundary: **Exclude accidental damage and unrelated vandalism near a residence.

**Typical roles: **Partner; ex-partner; spouse; relative; household member.

**Common methods / evidence signals: **Burning home/vehicle; smashing belongings; slashing tires; damaging doors, phones, or utilities.

**Primary target or asset: **Home, vehicle, possessions, communications, or shared property.

## FR-08 — Family Financial Exploitation / Theft

**Definition: **Theft or fraud by a relative or intimate partner who uses personal trust, access, or dependency.

**Include when: **The relationship enabled access to money, benefits, cards, accounts, identity, property, or estate assets.

**Exclude / boundary: **Exclude ordinary shared-finance disputes or nonpayment without deception or unauthorized control.

**Typical roles: **Adult child; partner; caregiver relative; sibling; guardian; in-law.

**Common methods / evidence signals: **Unauthorized withdrawals; forged checks; card use; benefit diversion; property sale; identity misuse.

**Primary target or asset: **Relative's funds, accounts, benefits, estate, or property.

# 3. Teen & Juvenile-Involved Crime

**Parent definition: **Offender-age context for alleged offenders under 18 or explicitly processed as juveniles. Pair with every supported substantive offense and keep victim age separate.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| JT-01 | Juvenile Assault / Violent Offense |
| JT-02 | Juvenile Weapons / School Threat |
| JT-03 | Juvenile Vehicle Theft / Reckless Driving / Pursuit |
| JT-04 | Juvenile Theft / Burglary / Robbery Crew |
| JT-05 | Juvenile Drug Offense |
| JT-06 | Juvenile Vandalism / Arson |
| JT-07 | Juvenile Cybercrime / Online Threats |
| JT-08 | Juvenile Family / Caregiver-Directed Crime |

## JT-01 — Juvenile Assault / Violent Offense

**Definition: **A minor allegedly commits an assault, battery, stabbing, shooting, robbery-related attack, or other interpersonal violence.

**Include when: **At least one alleged offender was under 18 at the incident and violent conduct is explicit.

**Exclude / boundary: **A teen victim alone does not qualify; exclude school discipline without criminal allegation.

**Typical roles: **Juvenile; teen group; student; youth offender.

**Common methods / evidence signals: **Fighting; beating; stabbing; shooting; group attack; threats followed by force.

**Primary target or asset: **Victim's body and safety.

## JT-02 — Juvenile Weapons / School Threat

**Definition: **A minor possesses, displays, uses, or threatens use of a weapon, especially in a school setting.

**Include when: **The weapon or credible threat is unlawful and attributable to a juvenile offender.

**Exclude / boundary: **Exclude lawful supervised sporting use, toys not represented as real, and unsubstantiated rumor.

**Typical roles: **Student; juvenile; teen suspect.

**Common methods / evidence signals: **Bringing weapon to school; brandishing; online threat; ammunition or prohibited weapon possession.

**Primary target or asset: **Students, staff, campus safety, or public safety.

## JT-03 — Juvenile Vehicle Theft / Reckless Driving / Pursuit

**Definition: **A minor steals or unlawfully uses a vehicle, drives dangerously, or flees police.

**Include when: **Juvenile operation or control of the vehicle is central to the alleged offense.

**Exclude / boundary: **Exclude passenger-only juveniles unless they knowingly participate in theft or flight.

**Typical roles: **Teen driver; juvenile passenger accomplice; youth auto-theft group.

**Common methods / evidence signals: **Joyriding; stolen car; racing; reckless crash; fleeing traffic stop; ramming vehicle.

**Primary target or asset: **Vehicle, roadway users, occupants, and public safety.

## JT-04 — Juvenile Theft / Burglary / Robbery Crew

**Definition: **One or more minors commit property crime individually or as a group.

**Include when: **The article identifies juvenile offenders in shoplifting, burglary, robbery, package theft, or coordinated stealing.

**Exclude / boundary: **Exclude a minor witness/victim and accidental possession with no knowing participation.

**Typical roles: **Teen crew; student; juvenile shopper; youth accomplice.

**Common methods / evidence signals: **Shoplifting; forced entry; smash-and-grab; car break-in; armed or strong-arm taking.

**Primary target or asset: **Retail goods, vehicles, homes, businesses, or personal property.

## JT-05 — Juvenile Drug Offense

**Definition: **A minor possesses, distributes, transports, or manufactures controlled substances.

**Include when: **The juvenile is an alleged offender rather than merely exposed or victimized.

**Exclude / boundary: **Use Child Maltreatment for adult-caused exposure; exclude medical treatment and noncriminal school-policy violations.

**Typical roles: **Student; juvenile seller; teen driver; youth group.

**Common methods / evidence signals: **Possession; school distribution; pills; cannabis where unlawful; vehicle transport; paraphernalia.

**Primary target or asset: **Controlled substances, school safety, and public health.

## JT-06 — Juvenile Vandalism / Arson

**Definition: **A minor intentionally damages property or sets a fire.

**Include when: **Police allege criminal mischief, graffiti, destructive prank, vehicle damage, or fire-setting by a juvenile.

**Exclude / boundary: **Exclude accidental damage and minor school discipline without a criminal allegation.

**Typical roles: **Student; juvenile group; teen resident.

**Common methods / evidence signals: **Graffiti; smashing; slashing tires; burning structures/vehicles; damaging school property.

**Primary target or asset: **Private, school, business, vehicle, or public property.

## JT-07 — Juvenile Cybercrime / Online Threats

**Definition: **A minor uses digital systems to hack, scam, threaten, stalk, extort, or disrupt.

**Include when: **The computer, account, platform, or electronic communication is essential to the juvenile's alleged offense.

**Exclude / boundary: **Exclude ordinary online conflict, offensive speech without crime, and a teen who is only the target.

**Typical roles: **Student; juvenile account holder; youth group.

**Common methods / evidence signals: **Account takeover; school-system intrusion; phishing; threats; swatting; sextortion; doxxing.

**Primary target or asset: **Accounts, data, money, privacy, or public/school safety.

## JT-08 — Juvenile Family / Caregiver-Directed Crime

**Definition: **A minor commits serious crime against a parent, guardian, sibling, or household member.

**Include when: **The juvenile is the alleged offender and the family/household relationship materially frames the offense.

**Exclude / boundary: **Exclude normal family conflict and cases where the juvenile is primarily the abused or endangered victim.

**Typical roles: **Teen child; juvenile sibling; foster youth.

**Common methods / evidence signals: **Assault; threats; theft; vehicle taking; arson; homicide.

**Primary target or asset: **Family member, household safety, money, vehicle, or home.

# 4. Theft, Fraud & Financial Crime

**Parent definition: **Taking or obtaining money, property, services, data, benefits, or value without authorization or through deception. Apply multiple subtypes when a scheme uses more than one method or target.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| TF-01 | Retail Theft / Shoplifting |
| TF-02 | Employee Theft / Embezzlement |
| TF-03 | Identity Theft / Account Takeover |
| TF-04 | Payment-Card / Bank-Account Fraud |
| TF-05 | Check Fraud / Forgery / Counterfeit Instruments |
| TF-06 | Consumer Scam / Impersonation Fraud |
| TF-07 | Contractor / Home-Repair / Service Fraud |
| TF-08 | Benefits / Insurance / Tax / Government-Program Fraud |
| TF-09 | Investment / Business / Charity Fraud |
| TF-10 | Package / Mail / Cargo Theft |
| TF-11 | Vehicle / Vehicle-Part Theft |
| TF-12 | Coordinated / High-Volume Theft Scheme |

## TF-01 — Retail Theft / Shoplifting

**Definition: **Unauthorized taking or concealment of merchandise from a retailer.

**Include when: **The suspect removes, hides, under-rings, swaps labels, or fraudulently returns goods.

**Exclude / boundary: **Exclude robbery involving force and civil return disputes without deception.

**Typical roles: **Shopper; cashier accomplice; retail theft group.

**Common methods / evidence signals: **Concealment; walkout; barcode switching; skip-scanning; false return; cart pushout.

**Primary target or asset: **Retail merchandise and store revenue.

## TF-02 — Employee Theft / Embezzlement

**Definition: **Workplace access is used to convert employer or entrusted property.

**Include when: **Employment materially enables access, concealment, or control of the asset.

**Exclude / boundary: **An unrelated theft by a person whose occupation is mentioned is insufficient.

**Typical roles: **Cashier; manager; bookkeeper; warehouse or postal worker.

**Common methods / evidence signals: **Skimming; false refunds; payroll manipulation; inventory or package diversion.

**Primary target or asset: **Employer funds, revenue, inventory, equipment, or mail.

## TF-03 — Identity Theft / Account Takeover

**Definition: **Another person's identity, credentials, or account is used without authority.

**Include when: **Personal identifiers or credentials enable access, credit, purchases, transfers, or impersonation.

**Exclude / boundary: **Exclude mistaken identity and authorized shared-account use.

**Typical roles: **Stranger; acquaintance; employee; family member; online scammer.

**Common methods / evidence signals: **Opening accounts; credential reset; SIM swap; impersonation; stolen SSN or login.

**Primary target or asset: **Identity, credit, financial accounts, and credentials.

## TF-04 — Payment-Card / Bank-Account Fraud

**Definition: **Unauthorized use or manipulation of cards, checks, bank accounts, or payment rails.

**Include when: **The scheme targets a specific payment instrument or account for value.

**Exclude / boundary: **Use Identity Theft additionally when personal identity is appropriated; exclude disputed authorized transactions.

**Typical roles: **Card user; bank customer; merchant; employee; accomplice.

**Common methods / evidence signals: **Unauthorized charges; transfers; card cloning; check alteration; mobile-payment misuse.

**Primary target or asset: **Cards, deposits, bank accounts, and transaction funds.

## TF-05 — Check Fraud / Forgery / Counterfeit Instruments

**Definition: **False, altered, stolen, or fabricated payment or identity documents are used as genuine.

**Include when: **Forgery, counterfeit creation, passing, or possession with fraudulent intent is explicit.

**Exclude / boundary: **Exclude clerical errors and genuine documents used in a separate nonfraud offense.

**Typical roles: **Account holder impostor; employee; check thief; counterfeiter.

**Common methods / evidence signals: **Washing checks; forged signature; fake currency; false ID; counterfeit title or prescription.

**Primary target or asset: **Payment instruments, documents, merchant or bank funds.

## TF-06 — Consumer Scam / Impersonation Fraud

**Definition: **A victim is deceived into transferring money, property, credentials, or access.

**Include when: **False identity, fabricated emergency, promised return, or deceptive service is central.

**Exclude / boundary: **Exclude ordinary sales puffery, bad service, or contract breach without criminal deception.

**Typical roles: **Impostor; romance scammer; tech-support scammer; fake official; seller.

**Common methods / evidence signals: **Gift cards; wire transfer; fake invoice; lottery; romance; grandparent; utility or police impersonation.

**Primary target or asset: **Victim funds, credentials, trust, and payment access.

## TF-07 — Contractor / Home-Repair / Service Fraud

**Definition: **A provider obtains payment through material deception and fails to perform or misuses entrusted funds.

**Include when: **Evidence shows false credentials, nonexistent work, repeated deceptive taking, diversion, or intent not to perform.

**Exclude / boundary: **A delayed, poor-quality, or disputed job alone is civil and insufficient.

**Typical roles: **Contractor; roofer; mover; repair provider; landscaper; service business.

**Common methods / evidence signals: **Large deposit; false license; fabricated damage; unfinished jobs; diverted materials.

**Primary target or asset: **Customer deposits, home, property, and service payments.

## TF-08 — Benefits / Insurance / Tax / Government-Program Fraud

**Definition: **False statements or concealment obtain government, insurance, tax, or relief benefits.

**Include when: **The suspect knowingly misrepresents eligibility, loss, income, identity, dependents, or services.

**Exclude / boundary: **Exclude good-faith application mistakes and eligibility disputes without knowing deception.

**Typical roles: **Applicant; claimant; provider; tax preparer; business owner.

**Common methods / evidence signals: **False claims; staged loss; phantom services; concealed income; duplicate benefits; refund fraud.

**Primary target or asset: **Public funds, insurer funds, tax revenue, and program integrity.

## TF-09 — Investment / Business / Charity Fraud

**Definition: **A business, investment, fundraising, or charity representation is used to obtain money deceptively.

**Include when: **Materially false claims about returns, ownership, use of funds, products, or charitable purpose are alleged.

**Exclude / boundary: **Exclude failed legitimate investments and business losses without fraud.

**Typical roles: **Promoter; adviser; executive; fundraiser; business owner.

**Common methods / evidence signals: **Ponzi scheme; fake investment; crowdfunding misuse; false financials; sham charity.

**Primary target or asset: **Investor, donor, customer, or business funds.

## TF-10 — Package / Mail / Cargo Theft

**Definition: **Packages, mail, deliveries, freight, or cargo are stolen, intercepted, or diverted.

**Include when: **The item is in transit, delivery custody, postal custody, or recently delivered.

**Exclude / boundary: **Exclude unrelated household theft and lost shipments without alleged taking.

**Typical roles: **Porch pirate; delivery worker; postal worker; warehouse employee; cargo crew.

**Common methods / evidence signals: **Porch theft; mail interception; trailer theft; address diversion; package concealment.

**Primary target or asset: **Mail, parcels, checks, cargo, and delivered goods.

## TF-11 — Vehicle / Vehicle-Part Theft

**Definition: **A vehicle or component is taken without consent, apart from force-based carjacking.

**Include when: **Auto theft, catalytic converter theft, wheel theft, key theft, or knowing possession of stolen vehicle/parts is alleged.

**Exclude / boundary: **Use Robbery/Carjacking when force or threat is used against an occupant.

**Typical roles: **Auto thief; joyrider; parts thief; buyer of stolen vehicle.

**Common methods / evidence signals: **Key cloning; hot-wiring; relay attack; converter cutting; VIN concealment.

**Primary target or asset: **Vehicle, keys, title, catalytic converter, wheels, or parts.

## TF-12 — Coordinated / High-Volume Theft Scheme

**Definition: **Repeated or coordinated theft by multiple participants, locations, transactions, or resale channels.

**Include when: **Planning, division of roles, repeated incidents, bulk value, fencing, or resale is explicit.

**Exclude / boundary: **Two people in a single spontaneous theft do not automatically qualify.

**Typical roles: **Theft crew; organizer; booster; fence; driver; reseller.

**Common methods / evidence signals: **Smash-and-grab; repeated shoplifting; cargo diversion; resale marketplace; multiple stores.

**Primary target or asset: **High-value merchandise, inventory, cargo, or resale proceeds.

# 5. Traffic, DUI & Vehicle Crime

**Parent definition: **Criminal operation, possession, theft, alteration, or misuse of vehicles and serious roadway offenses. A vehicle merely present at another crime does not trigger a vehicle subtype.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| TV-01 | Alcohol DUI / DWI |
| TV-02 | Drug-Impaired Driving |
| TV-03 | Reckless Driving / Extreme Speed / Street Racing |
| TV-04 | Hit-and-Run / Leaving the Scene |
| TV-05 | Vehicular Assault / Homicide |
| TV-06 | Vehicle Flight / Police Pursuit |
| TV-07 | Driving While Suspended / Unlicensed / Habitual Offender |
| TV-08 | Road Rage / Vehicle Used as Weapon |
| TV-09 | Stolen Vehicle / Joyriding / Vehicle Burglary |
| TV-10 | VIN / Title / Plate / Registration Fraud |
| TV-11 | Commercial / Rideshare / Delivery Vehicle Crime |

## TV-01 — Alcohol DUI / DWI

**Definition: **Operation or actual physical control of a vehicle while impaired by alcohol.

**Include when: **Observed impairment, breath/blood result, admission, field tests, crash facts, or alcohol-related charge supports the case.

**Exclude / boundary: **Exclude passenger intoxication and alcohol possession with no impaired operation.

**Typical roles: **Driver; commercial driver; parent driver.

**Common methods / evidence signals: **Driving after drinking; high BAC; open container linked to operation; refusal where chargeable.

**Primary target or asset: **Road users, passengers, vehicle, and public safety.

## TV-02 — Drug-Impaired Driving

**Definition: **Operation while impaired by controlled substances, medication, or multiple substances.

**Include when: **Driving behavior, toxicology, drug-recognition evidence, admission, or drug-DUI charge is reported.

**Exclude / boundary: **Drug possession in a stopped vehicle alone does not prove impairment.

**Typical roles: **Driver; patient using medication; commercial operator.

**Common methods / evidence signals: **Driving after cannabis, narcotics, stimulants, sedatives, or mixed substances.

**Primary target or asset: **Roadway safety and vehicle occupants.

## TV-03 — Reckless Driving / Extreme Speed / Street Racing

**Definition: **Willful or highly dangerous vehicle operation beyond ordinary negligence.

**Include when: **Authorities allege reckless driving, racing, stunt driving, extreme speed, wrong-way operation, or deliberate dangerous maneuver.

**Exclude / boundary: **Exclude ordinary traffic citations and crashes without criminal driving allegations.

**Typical roles: **Driver; racing participants; motorcycle rider.

**Common methods / evidence signals: **Racing; drifting; weaving; wrong-way driving; excessive speed; burnouts.

**Primary target or asset: **Road users, pedestrians, passengers, and property.

## TV-04 — Hit-and-Run / Leaving the Scene

**Definition: **A driver unlawfully leaves a crash without required identification, aid, or reporting.

**Include when: **The driver knew or should have known of a collision involving injury, death, or property damage and failed duties.

**Exclude / boundary: **Exclude a driver who lawfully reports or leaves temporarily for safety without evasion.

**Typical roles: **Driver; owner who conceals driver; accomplice.

**Common methods / evidence signals: **Fleeing crash; abandoning vehicle; hiding damage; false report.

**Primary target or asset: **Injured person, crash investigation, and damaged property.

## TV-05 — Vehicular Assault / Homicide

**Definition: **Criminal vehicle operation causes serious injury or death.

**Include when: **Impairment, recklessness, fleeing, racing, or other criminal operation is causally linked to injury or death.

**Exclude / boundary: **Exclude unavoidable or merely negligent crashes without a criminal allegation.

**Typical roles: **Driver; fleeing suspect; racer; commercial operator.

**Common methods / evidence signals: **DUI crash; wrong-way collision; pedestrian strike; high-speed pursuit crash.

**Primary target or asset: **Life, bodily safety, passengers, pedestrians, and motorists.

## TV-06 — Vehicle Flight / Police Pursuit

**Definition: **A driver knowingly refuses a lawful stop or flees police in a vehicle.

**Include when: **Lights/sirens, attempted stop, deliberate acceleration/evasion, or fleeing charge is reported.

**Exclude / boundary: **Exclude a driver unaware of the stop and foot flight after a vehicle is parked unless separately labeled.

**Typical roles: **Driver; stolen-car operator; wanted suspect.

**Common methods / evidence signals: **High-speed pursuit; wrong-way flight; ramming; abandoning vehicle.

**Primary target or asset: **Officers, public, roadway, and vehicles.

## TV-07 — Driving While Suspended / Unlicensed / Habitual Offender

**Definition: **A person drives despite a prohibited, revoked, suspended, expired, or absent driving privilege when criminally enforced.

**Include when: **The license status and knowing unlawful operation are central to the arrest or charge.

**Exclude / boundary: **Exclude administrative renewal stories and passengers with suspended licenses.

**Typical roles: **Driver; habitual traffic offender; prohibited commercial driver.

**Common methods / evidence signals: **Operating during suspension; false license; repeated unlicensed driving.

**Primary target or asset: **Licensing system and roadway safety.

## TV-08 — Road Rage / Vehicle Used as Weapon

**Definition: **A traffic conflict escalates to threats, assault, weapon display, collision, or deliberate vehicular attack.

**Include when: **The dispute arises from driving and involves criminal intimidation, force, or deliberate contact.

**Exclude / boundary: **Exclude rude gestures, verbal disputes, or accidental contact without criminal conduct.

**Typical roles: **Driver; passenger accomplice; motorcyclist.

**Common methods / evidence signals: **Ramming; chasing; blocking; pointing weapon; firing; attempting to run someone over.

**Primary target or asset: **Other driver, passenger, pedestrian, vehicle, and public safety.

## TV-09 — Stolen Vehicle / Joyriding / Vehicle Burglary

**Definition: **The vehicle itself or property inside it is unlawfully taken or entered.

**Include when: **Auto theft, unauthorized use, stolen-car possession, or breaking into a vehicle is alleged.

**Exclude / boundary: **Use Carjacking when force/threat is used; exclude repossession and civil ownership disputes.

**Typical roles: **Auto thief; juvenile joyrider; vehicle burglar; receiver.

**Common methods / evidence signals: **Hot-wire; key theft; window break; relay attack; rummaging; stolen-car possession.

**Primary target or asset: **Vehicle, keys, parts, and contents.

## TV-10 — VIN / Title / Plate / Registration Fraud

**Definition: **Identifiers or ownership/registration records are altered, concealed, forged, or misused.

**Include when: **The scheme concerns VINs, titles, plates, registration, odometers, or ownership documents.

**Exclude / boundary: **Exclude ordinary expired registration without deception unless criminally charged.

**Typical roles: **Vehicle owner; dealer; rebuilder; thief; document forger.

**Common methods / evidence signals: **VIN swap; cloned plate; forged title; odometer rollback; false registration.

**Primary target or asset: **Vehicle identity, ownership records, buyers, and regulators.

## TV-11 — Commercial / Rideshare / Delivery Vehicle Crime

**Definition: **A professional driving role materially enables dangerous, fraudulent, or criminal conduct.

**Include when: **The driver is on duty or using professional access, passengers, cargo, route, or vehicle authority in the offense.

**Exclude / boundary: **A driver's unrelated off-duty offense is not occupational merely because occupation is reported.

**Typical roles: **Truck driver; bus driver; rideshare driver; delivery driver; commercial operator.

**Common methods / evidence signals: **Cargo diversion; passenger crime; safety-rule violation; impaired operation; smuggling.

**Primary target or asset: **Passengers, cargo, customers, roadway, and employer assets.

# 6. Employee, Workplace & Occupational Crime

**Parent definition: **Crime materially enabled, motivated, concealed, or constituted by employment, professional duty, workplace access, occupational authority, or entrusted customers, patients, students, clients, assets, or systems.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| EC-01 | Workplace Asset Theft / Embezzlement |
| EC-02 | Customer Financial-Data / Account Misuse |
| EC-03 | Workplace Violence / Threats / Job-Related Violent Crime |
| EC-04 | Abuse / Assault / Exploitation of a Person in Care |
| EC-05 | Caregiver / Fiduciary / Client-Asset Exploitation |
| EC-06 | Bribery / Extortion / Abuse of Employment Position |
| EC-07 | Misconduct Involving Official or Regulated Systems |

## EC-01 — Workplace Asset Theft / Embezzlement

**Definition: **A worker uses job access to steal, divert, convert, conceal, or fraudulently obtain employer-controlled money, inventory, merchandise, equipment, packages, revenue, or work-custodied property.

**Include when: **The conduct is job-enabled, the asset is controlled by or entrusted through the workplace, and the worker or an accomplice receives an unauthorized benefit.

**Exclude / boundary: **Use Customer Financial-Data/Account Misuse when the primary thing abused is a customer's card, account, identity, or personal data. An unrelated theft by someone who happens to be an employee is not a match.

**Typical roles: **Cashier; manager; bookkeeper; delivery driver; warehouse worker; postal worker; office administrator; sales associate.

**Common methods / evidence signals: **Cash theft; false refunds; voids; skimming; forged checks; inventory concealment; package theft; diversion of customer payments owed to employer.

**Primary target or asset: **Employer funds, inventory, revenue, equipment, packages, mail, cargo, or work-custodied assets.

## EC-02 — Customer Financial-Data / Account Misuse

**Definition: **A worker abuses job-based access to a customer's money, payment card, account, identity, credentials, or personal financial data for unauthorized benefit.

**Include when: **Employment provided access to a customer-specific asset or data element, the use exceeded authority, and the conduct obtained or sought value.

**Exclude / boundary: **Use Workplace Asset Theft when employer-controlled funds or goods are primary. Use Caregiver/Fiduciary Exploitation for assets accessed through entrusted care.

**Typical roles: **Service adviser; retail employee; bank worker; customer-service representative; dealership or repair-shop worker; call-center worker.

**Common methods / evidence signals: **Unauthorized card charges; transfers; identity theft; saved credentials; opening accounts; sharing data with accomplices.

**Primary target or asset: **Customer funds, cards, accounts, credentials, identity data, or sensitive personal information.

## EC-03 — Workplace Violence / Threats / Job-Related Violent Crime

**Definition: **An employee commits or threatens violence against a coworker, supervisor, customer, applicant, or other work-connected person.

**Include when: **Violence or threat arises from duties, a workplace dispute, shared workplace, customer/applicant interaction, termination, or former-workplace conflict.

**Exclude / boundary: **Use Entrusted-Care Abuse when a duty-of-care relationship is central. Unrelated off-duty violence is not employee crime.

**Typical roles: **Retail or restaurant worker; manager; transportation worker; former employee; service employee.

**Common methods / evidence signals: **Assault; battery; threats; stalking; workplace-targeted violence; homicide; kidnapping; termination retaliation.

**Primary target or asset: **Coworker, supervisor, customer, applicant, workplace, or work-connected person.

## EC-04 — Abuse / Assault / Exploitation of a Person in Care

**Definition: **A worker uses caregiving, teaching, coaching, treatment, or custodial access to abuse, assault, neglect, restrain, exploit, or otherwise harm an entrusted person.

**Include when: **A duty-of-care, supervisory, instructional, treatment, or custodial relationship created central access, authority, or trust.

**Exclude / boundary: **Use Caregiver/Fiduciary Exploitation when financial/property exploitation is primary; use Workplace Violence for ordinary coworker/customer conflict without entrusted care.

**Typical roles: **Babysitter; teacher; coach; therapist; nurse; aide; residential staff; childcare worker.

**Common methods / evidence signals: **Physical abuse; neglect; unlawful restraint; grooming; assault during instruction/treatment; coercion.

**Primary target or asset: **Child, student, patient, resident, detainee, client, or dependent person.

## EC-05 — Caregiver / Fiduciary / Client-Asset Exploitation

**Definition: **A trusted caregiver, fiduciary, guardian, adviser, attorney, or client-facing worker misuses access to client money, cards, accounts, benefits, property, or identity.

**Include when: **The entrusted professional or caregiving relationship gave access to assets and materially enabled financial/property exploitation.

**Exclude / boundary: **Do not use solely for family-member fraud. Use Entrusted-Care Abuse when bodily abuse, neglect, or restraint is the primary allegation.

**Typical roles: **Home-health aide; nurse; caregiver; financial adviser; guardian; attorney; recovery-center or residential-care worker.

**Common methods / evidence signals: **Forged checks; card use; cash withdrawal; benefit diversion; identity use; property theft; account transfers.

**Primary target or asset: **Client, patient, ward, resident, or elderly person's funds, benefits, property, or identity.

## EC-06 — Bribery / Extortion / Abuse of Employment Position

**Definition: **A worker uses job-based or official authority to demand, obtain, exchange, or confer an improper benefit through coercion, threats, bribery, or abuse of position.

**Include when: **Facts establish employment-based leverage plus an improper benefit, quid pro quo, coercive demand, threat, or misuse of gatekeeping power.

**Exclude / boundary: **Poor performance, ordinary assault, or policy violation is insufficient; the authority-for-benefit connection must be explicit.

**Typical roles: **Officer; inspector; licensing official; government employee; gatekeeping manager; corrections employee; regulator.

**Common methods / evidence signals: **Cash bribe; kickback; threat of adverse action; coercive demand; trading official action for value.

**Primary target or asset: **Official action, regulatory decision, access, liberty, approval, benefit, or other value.

## EC-07 — Misconduct Involving Official or Regulated Systems

**Definition: **A public, regulated, or official-function employee criminally misuses job-controlled systems, records, credentials, equipment, data, evidence, or public-service functions.

**Include when: **The crime is expressly connected to an official system, database, record, credential, evidence process, safety-critical function, or operational authority.

**Exclude / boundary: **Government, airline, postal, or law-enforcement employment alone is insufficient; system or authority misuse must be central.

**Typical roles: **Public official; law-enforcement or corrections employee; postal worker; regulated transport or public-safety worker.

**Common methods / evidence signals: **Record alteration; database lookup; evidence misuse; credential abuse; official equipment or operational-control misuse.

**Primary target or asset: **Official records, databases, evidence, credentials, government assets, and public-service systems.

# 7. Homicide, Suspicious Death & Body Discovery

**Parent definition: **Intentional, reckless, negligent, attempted, or suspicious killing and discovery, identification, concealment, or disposal of human remains. Track death status separately from method and context.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| HD-01 | Firearm Homicide / Fatal Shooting |
| HD-02 | Stabbing / Cutting Homicide |
| HD-03 | Blunt-Force / Beating / Strangulation Homicide |
| HD-04 | Domestic / Family Homicide |
| HD-05 | Child Homicide / Fatal Maltreatment |
| HD-06 | Vehicular Homicide / Fatal Criminal Crash |
| HD-07 | Drug-Induced Death / Fatal Poisoning |
| HD-08 | Attempted Murder / Solicitation / Murder Plot |
| HD-09 | Body Discovery / Concealment / Disposal |
| HD-10 | Suspicious / Unexplained Death / Cold Case |

## HD-01 — Firearm Homicide / Fatal Shooting

**Definition: **A firearm discharge allegedly causes a person's death.

**Include when: **A shooting death is investigated as criminal, suspicious, reckless, or chargeable homicide.

**Exclude / boundary: **Exclude suicide or accidental discharge unless criminal negligence or another person's liability is alleged.

**Typical roles: **Shooter; accomplice; victim; witness.

**Common methods / evidence signals: **Handgun; rifle; shotgun; drive-by; close-range shooting.

**Primary target or asset: **Human life and bodily safety.

## HD-02 — Stabbing / Cutting Homicide

**Definition: **A knife or cutting instrument allegedly causes death.

**Include when: **Authorities connect stab/cut wounds to an intentional or unlawful killing.

**Exclude / boundary: **Exclude accidental cuts and nonfatal stabbings.

**Typical roles: **Partner; acquaintance; stranger; household member.

**Common methods / evidence signals: **Knife; machete; edged tool; repeated stabbing.

**Primary target or asset: **Human life and bodily safety.

## HD-03 — Blunt-Force / Beating / Strangulation Homicide

**Definition: **Death results from beating, blunt trauma, choking, strangulation, or other direct force.

**Include when: **Medical or investigative facts identify this mechanism and criminal conduct.

**Exclude / boundary: **Exclude nonfatal assault and natural death with unrelated injuries.

**Typical roles: **Partner; caregiver; acquaintance; stranger.

**Common methods / evidence signals: **Beating; blunt object; manual/ligature strangulation; suffocation.

**Primary target or asset: **Human life and bodily safety.

## HD-04 — Domestic / Family Homicide

**Definition: **A killing or attempt occurs between intimate partners, relatives, or household members.

**Include when: **The relationship materially frames motive, access, victim selection, or circumstances.

**Exclude / boundary: **A death in a home without a qualifying relationship is insufficient.

**Typical roles: **Spouse; ex-partner; parent; adult child; sibling; household member.

**Common methods / evidence signals: **Shooting; stabbing; strangulation; poisoning; fire; vehicle attack.

**Primary target or asset: **Partner or family member's life.

## HD-05 — Child Homicide / Fatal Maltreatment

**Definition: **A child's death is allegedly caused by abuse, neglect, abandonment, or dangerous exposure.

**Include when: **The victim is under 18 and criminal caregiver or offender conduct is tied to death.

**Exclude / boundary: **Exclude unexplained child death unless officially suspicious or under criminal investigation.

**Typical roles: **Parent; guardian; caregiver; household member; institutional worker.

**Common methods / evidence signals: **Beating; shaking; starvation; poisoning; unsafe exposure; failure to obtain care.

**Primary target or asset: **Child's life and safety.

## HD-06 — Vehicular Homicide / Fatal Criminal Crash

**Definition: **Criminal vehicle operation causes death.

**Include when: **DUI, recklessness, racing, fleeing, hit-and-run, or another criminal traffic act is causally linked.

**Exclude / boundary: **Exclude routine fatal collisions without alleged criminal operation.

**Typical roles: **Driver; racer; fleeing suspect; commercial operator.

**Common methods / evidence signals: **Impaired crash; wrong-way driving; extreme speed; pedestrian strike.

**Primary target or asset: **Motorist, passenger, cyclist, or pedestrian life.

## HD-07 — Drug-Induced Death / Fatal Poisoning

**Definition: **Unlawful supply, administration, concealment, or intentional poisoning allegedly causes death.

**Include when: **Charges or reported evidence connect a supplied substance or poison to death.

**Exclude / boundary: **A routine overdose with no alleged culpable supplier or homicide theory is insufficient.

**Typical roles: **Dealer; caregiver; acquaintance; medical worker; poisoner.

**Common methods / evidence signals: **Fentanyl distribution; counterfeit pill; intentional dose; toxic chemical; medication misuse.

**Primary target or asset: **Human life and bodily integrity.

## HD-08 — Attempted Murder / Solicitation / Murder Plot

**Definition: **The suspect allegedly tries, plans, solicits, or conspires to kill but no completed death results.

**Include when: **Intent to kill is explicit in charges, actions, communications, payment, or planning.

**Exclude / boundary: **Exclude general threats or serious assault without reported homicidal intent.

**Typical roles: **Would-be killer; solicitor; hired participant; accomplice.

**Common methods / evidence signals: **Attack attempt; payment; planning messages; poison/firearm preparation; ambush.

**Primary target or asset: **Intended victim's life.

## HD-09 — Body Discovery / Concealment / Disposal

**Definition: **Human remains are found or allegedly hidden, moved, dismembered, burned, buried, or otherwise concealed.

**Include when: **Discovery or treatment of remains is a central part of the news event.

**Exclude / boundary: **Do not infer confirmed murder when cause/manner remains undetermined.

**Typical roles: **Finder; suspected disposer; homicide investigator; unidentified decedent.

**Common methods / evidence signals: **Trunk; container; water; woods; grave; dumpster; burning; dismemberment.

**Primary target or asset: **Human remains, identity, and death investigation.

## HD-10 — Suspicious / Unexplained Death / Cold Case

**Definition: **An undetermined, unattended, reopened, or historical death is investigated for possible crime.

**Include when: **Authorities call the death suspicious, unexplained, a homicide investigation, cold case, or unidentified-remains case.

**Exclude / boundary: **Exclude natural deaths, routine obituaries, and accidents with no investigative suspicion.

**Typical roles: **Unknown suspect; decedent; cold-case investigator; medical examiner.

**Common methods / evidence signals: **Reopened evidence; forensic identification; exhumation; new witness/DNA; death-scene review.

**Primary target or asset: **Cause, manner, identity, and accountability for death.

# 8. Resisting, Evading, Obstruction & Public Disturbance

**Parent definition: **Interference with officers, courts, responders, investigations, custody, or public order. Do not infer resistance merely because officers used force.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| PO-01 | Resisting Arrest / Physical Noncompliance |
| PO-02 | Foot Flight / Evading Detention |
| PO-03 | Vehicle Evading / Failure to Stop |
| PO-04 | Obstruction / False Information / Interference |
| PO-05 | Evidence Tampering / Witness Intimidation |
| PO-06 | Disorderly Conduct / Public Intoxication |
| PO-07 | Public Fight / Affray / Group Disturbance |
| PO-08 | Trespass / Refusal to Leave |
| PO-09 | False Report / 911 Misuse / Threat Hoax |
| PO-10 | Barricade / Standoff / Hostile Refusal to Surrender |

## PO-01 — Resisting Arrest / Physical Noncompliance

**Definition: **Physical action intentionally prevents or delays lawful arrest or detention.

**Include when: **The article alleges pulling away, fighting, bracing, striking, or other charged resistance.

**Exclude / boundary: **Verbal criticism, confusion, passive presence, or force used without reported resistance is insufficient.

**Typical roles: **Arrestee; officer; assisting bystander.

**Common methods / evidence signals: **Pulling away; wrestling; locking arms; refusing exit combined with physical resistance.

**Primary target or asset: **Lawful custody, officer safety, and arrest process.

## PO-02 — Foot Flight / Evading Detention

**Definition: **A person knowingly runs, hides, or otherwise flees an attempted lawful stop on foot.

**Include when: **Officer identification, command, pursuit facts, or evading charge supports knowledge.

**Exclude / boundary: **Exclude a person merely leaving before any clear detention attempt.

**Typical roles: **Suspect; officer; accomplice.

**Common methods / evidence signals: **Running; hiding; fence jumping; discarding evidence; changing clothes.

**Primary target or asset: **Detention process, public safety, and investigation.

## PO-03 — Vehicle Evading / Failure to Stop

**Definition: **A driver knowingly flees or refuses a lawful vehicle stop.

**Include when: **A marked/unmarked police attempt and deliberate vehicular evasion are reported.

**Exclude / boundary: **Exclude delayed stopping without evidence of knowing flight.

**Typical roles: **Driver; passenger accomplice; pursuing officer.

**Common methods / evidence signals: **Acceleration; high-speed pursuit; wrong-way driving; ramming; vehicle abandonment.

**Primary target or asset: **Roadway safety, officers, public, and lawful detention.

## PO-04 — Obstruction / False Information / Interference

**Definition: **A person impedes an investigation, arrest, emergency response, or official duty.

**Include when: **False identity, concealment, interference, warning a suspect, or blocking responders is alleged.

**Exclude / boundary: **Mere silence, lawful refusal, or inaccurate statement without knowing obstruction is insufficient.

**Typical roles: **Suspect; witness; associate; bystander; family member.

**Common methods / evidence signals: **False name; hiding person; blocking officers; destroying notice; interfering with EMS/firefighters.

**Primary target or asset: **Investigation, arrest, emergency response, and public administration.

## PO-05 — Evidence Tampering / Witness Intimidation

**Definition: **Evidence or testimony is altered, destroyed, concealed, fabricated, or influenced.

**Include when: **The conduct aims to affect an investigation, prosecution, or testimony.

**Exclude / boundary: **Routine cleanup or contact with a witness is insufficient without corrupt intent.

**Typical roles: **Suspect; accomplice; witness; associate.

**Common methods / evidence signals: **Deleting video; hiding weapon; burning clothing; threatening witness; false evidence.

**Primary target or asset: **Evidence integrity, witness safety, and justice process.

## PO-06 — Disorderly Conduct / Public Intoxication

**Definition: **Public behavior unlawfully disrupts peace, safety, or order.

**Include when: **The article identifies criminal disorder, aggressive disruption, public intoxication, or breach of peace.

**Exclude / boundary: **Rudeness, lawful protest, homelessness, or mental-health symptoms alone are insufficient.

**Typical roles: **Intoxicated person; patron; pedestrian; event attendee.

**Common methods / evidence signals: **Yelling; fighting behavior; blocking; aggressive contact; intoxicated danger.

**Primary target or asset: **Public peace, safety, businesses, and bystanders.

## PO-07 — Public Fight / Affray / Group Disturbance

**Definition: **Two or more people engage in unlawful public fighting or coordinated disturbance.

**Include when: **The event is public, involves mutual/group violence, and is charged as affray, riot, or disorder.

**Exclude / boundary: **Use Assault where a clear aggressor/victim and injury dominate; exclude lawful assembly.

**Typical roles: **Patrons; rival groups; event attendees; crowd participants.

**Common methods / evidence signals: **Group fight; riot conduct; throwing objects; coordinated disruption.

**Primary target or asset: **Public safety, persons, businesses, and venue order.

## PO-08 — Trespass / Refusal to Leave

**Definition: **A person knowingly enters or remains after notice or without authorization.

**Include when: **Property owner, agent, or officer directs departure or entry is clearly prohibited.

**Exclude / boundary: **Exclude civil tenancy disputes, unclear notice, and lawful access.

**Typical roles: **Customer; former employee; protester; unauthorized occupant.

**Common methods / evidence signals: **Refusing exit; reentry after ban; restricted-area entry; remaining after closing.

**Primary target or asset: **Property possession, business operation, and occupant safety.

## PO-09 — False Report / 911 Misuse / Threat Hoax

**Definition: **Emergency or police resources are knowingly triggered through false information.

**Include when: **Fabricated emergency, false crime report, swatting, bomb threat, or repeated nonemergency misuse is alleged.

**Exclude / boundary: **A mistaken good-faith report is insufficient.

**Typical roles: **Caller; student; online actor; disgruntled person.

**Common methods / evidence signals: **False 911 call; swatting; bomb hoax; fake kidnapping; false active-shooter report.

**Primary target or asset: **Emergency resources, targeted person, school/business, and public safety.

## PO-10 — Barricade / Standoff / Hostile Refusal to Surrender

**Definition: **A suspect uses a location, threats, weapons, or hostages to resist apprehension over time.

**Include when: **Police establish a perimeter, negotiate, deploy tactical resources, or describe a barricade/standoff.

**Exclude / boundary: **A delayed door answer or peaceful arrest is insufficient.

**Typical roles: **Barricaded suspect; hostage; negotiator; tactical officer.

**Common methods / evidence signals: **Armed confinement; threats; refusal to exit; hostage use; firing from structure.

**Primary target or asset: **Occupants, officers, neighbors, and safe apprehension.

# 9. Assault, Weapons & Violent Crime

**Parent definition: **Actual, attempted, or threatened unlawful physical harm and unlawful possession, display, discharge, or use of weapons. Apply separate subtypes for conduct, weapon, victim role, and severity when supported.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| AV-01 | Simple Assault / Battery |
| AV-02 | Aggravated Assault / Serious Bodily Injury |
| AV-03 | Nonfatal Shooting |
| AV-04 | Stabbing / Cutting Assault |
| AV-05 | Strangulation / Choking / Suffocation Assault |
| AV-06 | Vehicle Used as a Weapon |
| AV-07 | Threats / Menacing / Brandishing |
| AV-08 | Assault on Officer / First Responder / Protected Worker |
| AV-09 | Unlawful Firearm Possession / Prohibited Possessor |
| AV-10 | Illegal Weapon Modification / Ghost Gun / Prohibited Device |
| AV-11 | Weapons Trafficking / Stolen Weapons / Unlawful Sale |
| AV-12 | Explosive / Incendiary / Chemical Weapon Threat |

## AV-01 — Simple Assault / Battery

**Definition: **Unlawful force, attempted force, or offensive physical contact without the aggravating facts of a more serious subtype.

**Include when: **The article alleges hitting, pushing, kicking, grabbing, spitting, or minor injury.

**Exclude / boundary: **Exclude verbal disputes without threat/force and accidental contact.

**Typical roles: **Acquaintance; stranger; patron; neighbor; customer.

**Common methods / evidence signals: **Punching; slapping; pushing; kicking; grabbing; spitting.

**Primary target or asset: **Victim's body, dignity, and safety.

## AV-02 — Aggravated Assault / Serious Bodily Injury

**Definition: **Assault involving severe injury, heightened intent, vulnerable circumstances, or a dangerous weapon.

**Include when: **Serious wounds, hospitalization, disfigurement, repeated attack, or aggravated charge is reported.

**Exclude / boundary: **Do not infer aggravation solely from arrest severity; require facts or charge.

**Typical roles: **Partner; stranger; group attacker; acquaintance.

**Common methods / evidence signals: **Beating; stomping; blunt object; dangerous weapon; sustained attack.

**Primary target or asset: **Victim's life and bodily integrity.

## AV-03 — Nonfatal Shooting

**Definition: **A firearm is intentionally or recklessly discharged at or near a person without a reported death.

**Include when: **Gunfire causes injury, attempted injury, or immediate danger and criminal conduct is alleged.

**Exclude / boundary: **Exclude fatal shootings and lawful defensive discharge unless charged.

**Typical roles: **Shooter; victim; bystander; accomplice.

**Common methods / evidence signals: **Handgun/rifle discharge; drive-by; celebratory/reckless fire; attempted shooting.

**Primary target or asset: **Person, occupied vehicle/building, and public safety.

## AV-04 — Stabbing / Cutting Assault

**Definition: **A knife or edged instrument is used or attempted against a person without death.

**Include when: **The article alleges stabbing, slashing, cutting, or an attempted edged-weapon attack.

**Exclude / boundary: **Exclude accidental cuts and mere lawful possession.

**Typical roles: **Attacker; victim; household member; patron.

**Common methods / evidence signals: **Knife; machete; razor; broken glass; edged tool.

**Primary target or asset: **Victim's body and safety.

## AV-05 — Strangulation / Choking / Suffocation Assault

**Definition: **Pressure to the neck, throat, breathing, or airway is used against a person.

**Include when: **Strangulation, choking, smothering, or airway restriction is alleged and nonfatal.

**Exclude / boundary: **Exclude medical restraint or accidental airway obstruction without assault.

**Typical roles: **Partner; caregiver; acquaintance; stranger.

**Common methods / evidence signals: **Manual strangulation; ligature; chokehold; smothering.

**Primary target or asset: **Breathing, consciousness, and life safety.

## AV-06 — Vehicle Used as a Weapon

**Definition: **A vehicle is intentionally driven at, into, or against a person or occupied target.

**Include when: **Deliberate targeting, ramming, attempted run-over, or assault charge is reported.

**Exclude / boundary: **Exclude accidental/reckless crashes without evidence the vehicle was used to attack.

**Typical roles: **Driver; road-rage participant; fleeing suspect.

**Common methods / evidence signals: **Ramming; pinning; chasing pedestrian; striking officer; driving into crowd.

**Primary target or asset: **Person, occupied vehicle/building, and public safety.

## AV-07 — Threats / Menacing / Brandishing

**Definition: **Credible violence is threatened or a weapon is displayed to intimidate.

**Include when: **Words, gestures, display, or conduct creates reasonable fear and is criminally alleged.

**Exclude / boundary: **Angry speech without credible threat and lawful visible carry are insufficient.

**Typical roles: **Disputant; road-rage driver; customer; neighbor; partner.

**Common methods / evidence signals: **Pointing firearm; displaying knife; death threat; threatening gesture.

**Primary target or asset: **Victim's sense of safety and freedom from intimidation.

## AV-08 — Assault on Officer / First Responder / Protected Worker

**Definition: **Violence or attempted violence targets an officer, firefighter, EMS worker, healthcare worker, teacher, transit worker, or similar protected role.

**Include when: **The victim is performing or targeted because of official/protected duties and assault is alleged.

**Exclude / boundary: **A protected occupation mentioned only as background is insufficient.

**Typical roles: **Arrestee; patient; inmate; student; suspect.

**Common methods / evidence signals: **Punching; biting; spitting; weapon attack; vehicle strike; resisting with injury.

**Primary target or asset: **Worker's body, safety, and public-service function.

## AV-09 — Unlawful Firearm Possession / Prohibited Possessor

**Definition: **Possession or carrying is illegal because of status, location, weapon type, or manner.

**Include when: **The article states a possession/carry charge or facts establishing prohibition.

**Exclude / boundary: **Do not label lawful ownership or a recovered firearm with no alleged weapons violation.

**Typical roles: **Felon/prohibited person; juvenile; intoxicated possessor; unlicensed carrier.

**Common methods / evidence signals: **Concealed carry violation; school possession; stolen gun; possession under disability.

**Primary target or asset: **Public safety and regulated firearm possession.

## AV-10 — Illegal Weapon Modification / Ghost Gun / Prohibited Device

**Definition: **A weapon or device is unlawfully made, altered, possessed, or configured.

**Include when: **Machine-gun conversion, unserialized firearm, suppressor/device offense, or prohibited configuration is explicit.

**Exclude / boundary: **A customized but lawful firearm is insufficient.

**Typical roles: **Builder; owner; seller; trafficker.

**Common methods / evidence signals: **Switch/auto sear; obliterated serial; homemade gun; illegal short barrel; prohibited magazine/device.

**Primary target or asset: **Weapon regulation, traceability, and public safety.

## AV-11 — Weapons Trafficking / Stolen Weapons / Unlawful Sale

**Definition: **Weapons are stolen, transferred, sold, purchased, or moved unlawfully.

**Include when: **Multiple weapons, straw purchasing, prohibited transfer, trafficking, or knowing stolen possession is central.

**Exclude / boundary: **A single lawful private transfer or incidental weapon recovery is insufficient.

**Typical roles: **Seller; straw purchaser; thief; courier; prohibited buyer.

**Common methods / evidence signals: **Straw purchase; gun-store theft; resale; interstate transport; serial removal.

**Primary target or asset: **Firearms, regulated weapons, buyers, and public safety.

## AV-12 — Explosive / Incendiary / Chemical Weapon Threat

**Definition: **An explosive, incendiary, toxic chemical, or similar device is used or threatened against people.

**Include when: **A credible device, attempt, detonation, deployment, or criminal threat is reported.

**Exclude / boundary: **A hoax with no device may instead be Public Disturbance/Threat Hoax; lawful materials are insufficient.

**Typical roles: **Device maker; attacker; threatening caller.

**Common methods / evidence signals: **Bomb; incendiary bottle; explosive package; toxic agent; improvised device.

**Primary target or asset: **People, occupied property, infrastructure, and public safety.

# 10. Drugs & Narcotics

**Parent definition: **Unlawful possession, manufacture, cultivation, diversion, sale, distribution, transport, concealment, or administration of controlled substances or regulated medications.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| DN-01 | Simple Drug Possession |
| DN-02 | Possession With Intent to Distribute |
| DN-03 | Drug Sale / Delivery / Distribution |
| DN-04 | Drug Trafficking / Large-Scale Transport |
| DN-05 | Manufacturing / Clandestine Lab / Processing |
| DN-06 | Illegal Cultivation / Grow Operation |
| DN-07 | Prescription Fraud / Medication Diversion |
| DN-08 | Drug Introduction into School / Jail / Facility |
| DN-09 | Child Drug Exposure / Caregiver Drug Endangerment |
| DN-10 | Fatal Overdose Supply / Drug-Induced Homicide |

## DN-01 — Simple Drug Possession

**Definition: **A person knowingly possesses a controlled substance for personal use without distribution indicators.

**Include when: **The amount, packaging, admissions, or charge supports possession and no stronger trafficking theory dominates.

**Exclude / boundary: **Drug residue without knowing possession and lawful prescription possession are insufficient.

**Typical roles: **Possessor; passenger; resident; pedestrian.

**Common methods / evidence signals: **Pocket/bag possession; vehicle console; residence; discarded substance.

**Primary target or asset: **Controlled substance and lawful drug regulation.

## DN-02 — Possession With Intent to Distribute

**Definition: **Possession circumstances indicate intended sale, delivery, or distribution.

**Include when: **Quantity, packaging, scales, customer messages, cash, or charge supports intent.

**Exclude / boundary: **Personal-use possession alone is insufficient.

**Typical roles: **Dealer; courier; stash-house occupant.

**Common methods / evidence signals: **Multiple baggies; scales; ledgers; messages; bundled cash; bulk quantity.

**Primary target or asset: **Controlled substances, customers, and community safety.

## DN-03 — Drug Sale / Delivery / Distribution

**Definition: **A controlled substance is transferred, offered, sold, or delivered.

**Include when: **A completed/attempted exchange, controlled buy, delivery, or distribution charge is reported.

**Exclude / boundary: **Possession without transfer evidence should remain possession/intended distribution.

**Typical roles: **Seller; buyer; intermediary; delivery person.

**Common methods / evidence signals: **Street sale; delivery; handoff; online arrangement; controlled buy.

**Primary target or asset: **Controlled substances, recipient, and proceeds.

## DN-04 — Drug Trafficking / Large-Scale Transport

**Definition: **Significant quantities are moved, imported, exported, or distributed through an extended supply chain.

**Include when: **Bulk amount, cross-jurisdiction movement, courier network, hidden compartment, or trafficking charge is present.

**Exclude / boundary: **Small personal-use transport is insufficient.

**Typical roles: **Courier; supplier; driver; passenger accomplice; stash-house operator.

**Common methods / evidence signals: **Vehicle/cargo concealment; luggage; mail; border route; commercial load.

**Primary target or asset: **Bulk narcotics, supply chain, and proceeds.

## DN-05 — Manufacturing / Clandestine Lab / Processing

**Definition: **Controlled substances are produced, synthesized, converted, pressed, or prepared unlawfully.

**Include when: **Lab equipment, precursor chemicals, pill press, extraction, mixing, or manufacturing charge is explicit.

**Exclude / boundary: **Ordinary packaging of already-made drugs may be distribution, not manufacturing.

**Typical roles: **Cook; lab operator; property owner; helper.

**Common methods / evidence signals: **Meth lab; pill press; fentanyl mixing; extraction; precursor stock.

**Primary target or asset: **Manufactured drugs, premises, occupants, and environment.

## DN-06 — Illegal Cultivation / Grow Operation

**Definition: **Controlled plants are cultivated beyond lawful authorization.

**Include when: **Plants, grow equipment, unlawful quantity, diversion, or cultivation charge is reported.

**Exclude / boundary: **Exclude lawful licensed cultivation and ordinary plant possession.

**Typical roles: **Grower; property occupant; business operator.

**Common methods / evidence signals: **Indoor grow; outdoor crop; hydroponics; electricity theft; concealed cultivation.

**Primary target or asset: **Controlled plants, property, utilities, and distribution supply.

## DN-07 — Prescription Fraud / Medication Diversion

**Definition: **Prescription drugs are obtained, prescribed, dispensed, stolen, or redirected unlawfully.

**Include when: **Forgery, doctor shopping, false prescription, pill-mill conduct, or workplace diversion is alleged.

**Exclude / boundary: **Good-faith prescribing disagreement and lawful patient use are insufficient.

**Typical roles: **Patient; prescriber; nurse; pharmacy worker; caregiver.

**Common methods / evidence signals: **Forged script; false patient; stolen medication; record manipulation; unauthorized dispensing.

**Primary target or asset: **Medication, patient safety, insurer funds, and prescription system.

## DN-08 — Drug Introduction into School / Jail / Facility

**Definition: **Controlled substances are brought into a restricted institution or supplied to people in custody/care.

**Include when: **Institutional location, concealment, visitor/employee/inmate role, or contraband charge is central.

**Exclude / boundary: **Possession near a facility without attempted introduction is insufficient.

**Typical roles: **Visitor; inmate; employee; student; courier.

**Common methods / evidence signals: **Body concealment; mail; food/package hiding; employee delivery; school sale.

**Primary target or asset: **Facility security, students/inmates/residents, and controlled substances.

## DN-09 — Child Drug Exposure / Caregiver Drug Endangerment

**Definition: **Adult drug conduct exposes a child to ingestion, toxic environment, impaired care, or accessible substances.

**Include when: **Child presence plus actual or substantial risk from drugs, paraphernalia, manufacture, or caregiver impairment is explicit.

**Exclude / boundary: **A parent's past drug use with no present child risk is insufficient.

**Typical roles: **Parent; guardian; household member; caregiver.

**Common methods / evidence signals: **Accessible pills/fentanyl; smoke exposure; lab in home; impaired supervision; ingestion.

**Primary target or asset: **Child's health, safety, and supervision.

## DN-10 — Fatal Overdose Supply / Drug-Induced Homicide

**Definition: **Unlawful supply or administration is criminally tied to a fatal overdose or poisoning.

**Include when: **Authorities allege causation, controlled-substance death, homicide, manslaughter, or fatal-distribution offense.

**Exclude / boundary: **A fatal overdose without an identified culpable supply act is insufficient for this subtype.

**Typical roles: **Dealer; friend; caregiver; distributor; prescriber.

**Common methods / evidence signals: **Fentanyl-laced drug; counterfeit pill; direct administration; fatal sale.

**Primary target or asset: **Victim's life and drug supply accountability.

# 11. Kidnapping, Abduction, Unlawful Restraint & Missing Persons

**Parent definition: **Unlawful taking, movement, concealment, confinement, luring, or restraint, plus missing-person investigative statuses. Missing does not itself prove abduction.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| KM-01 | Adult Kidnapping / Abduction |
| KM-02 | Child Abduction by Nonparent |
| KM-03 | Parental Kidnapping / Custodial Interference |
| KM-04 | False Imprisonment / Unlawful Restraint |
| KM-05 | Hostage / Ransom / Coercive Confinement |
| KM-06 | Luring / Attempted Abduction |
| KM-07 | Missing Child / Amber Alert |
| KM-08 | Endangered / Vulnerable Missing Adult |
| KM-09 | Suspicious Disappearance / Long-Term Missing |
| KM-10 | Missing Person Located / Remains Identified |

## KM-01 — Adult Kidnapping / Abduction

**Definition: **An adult is unlawfully taken, moved, hidden, or held through force, threat, fraud, or coercion.

**Include when: **Nonconsensual movement or confinement beyond an incidental assault is reported.

**Exclude / boundary: **Exclude consensual travel and temporary inability to contact someone.

**Typical roles: **Stranger; acquaintance; partner; multiple offenders.

**Common methods / evidence signals: **Forced vehicle entry; transport; concealment; threats; binding.

**Primary target or asset: **Victim's liberty, location, and safety.

## KM-02 — Child Abduction by Nonparent

**Definition: **A child is unlawfully taken, enticed, transported, hidden, or retained by someone without custodial authority.

**Include when: **Police allege abduction, luring, kidnapping, or unauthorized concealment by a nonparent.

**Exclude / boundary: **Exclude ordinary contact and lawful pickup/care arrangements.

**Typical roles: **Stranger; acquaintance; family friend; online contact.

**Common methods / evidence signals: **Luring; vehicle transport; false authority; hiding; restraint.

**Primary target or asset: **Child's custody, liberty, location, and safety.

## KM-03 — Parental Kidnapping / Custodial Interference

**Definition: **A parent or relative violates custody rights by taking, hiding, or failing to return a child.

**Include when: **A custody order/right plus knowing unlawful retention or concealment is reported.

**Exclude / boundary: **Civil disagreement without criminal taking or retention is insufficient.

**Typical roles: **Noncustodial parent; parent; grandparent; relative.

**Common methods / evidence signals: **Cross-state travel; concealment; false identity; failure to return; blocked contact.

**Primary target or asset: **Lawful custody, child location, and guardian access.

## KM-04 — False Imprisonment / Unlawful Restraint

**Definition: **A person is confined, bound, locked in, pinned, or prevented from leaving without lawful authority.

**Include when: **Meaningful restraint is alleged even if the victim is not transported.

**Exclude / boundary: **Momentary contact inherent in another minor offense may be insufficient unless separately charged or significant.

**Typical roles: **Partner; caregiver; employer; stranger; acquaintance.

**Common methods / evidence signals: **Locked room; binding; blocking exit; taking phone/keys; physical restraint.

**Primary target or asset: **Victim's freedom of movement and safety.

## KM-05 — Hostage / Ransom / Coercive Confinement

**Definition: **A victim is held to compel payment, action, escape, negotiation, or compliance.

**Include when: **Demand, leverage, standoff, ransom, or conditional release is central.

**Exclude / boundary: **Ordinary robbery detention without meaningful hostage purpose may not qualify.

**Typical roles: **Captor; hostage; negotiator; accomplice.

**Common methods / evidence signals: **Ransom demand; human shield; barricade; threat; conditional release.

**Primary target or asset: **Victim's liberty, life, money, and third-party compliance.

## KM-06 — Luring / Attempted Abduction

**Definition: **A suspect tries to entice, grab, transport, or isolate a person but does not complete an abduction.

**Include when: **Conduct goes beyond vague suspicion and includes an overt attempt, deceptive lure, or criminal solicitation.

**Exclude / boundary: **A stranger speaking to someone or an unverified social-media warning is insufficient.

**Typical roles: **Stranger; online contact; driver; acquaintance.

**Common methods / evidence signals: **Offering ride/gift; impersonation; following; grabbing; directing into vehicle.

**Primary target or asset: **Potential victim's liberty and safety.

## KM-07 — Missing Child / Amber Alert

**Definition: **An official missing-child or Amber Alert case is active or updated.

**Include when: **Police or authorized agency identifies a missing/endangered child and seeks public help.

**Exclude / boundary: **Do not infer kidnapping, homicide, or parental involvement unless reported.

**Typical roles: **Missing child; parent/guardian; unknown person; investigator.

**Common methods / evidence signals: **Alert; last-seen report; vehicle description; search; public appeal.

**Primary target or asset: **Child's location, safety, and recovery.

## KM-08 — Endangered / Vulnerable Missing Adult

**Definition: **An adult is missing with age, disability, illness, coercion risk, weather exposure, or suspicious circumstances increasing danger.

**Include when: **Police issue Silver/endangered alert or identify specific vulnerability or immediate risk.

**Exclude / boundary: **A routine voluntary absence with no official concern is insufficient.

**Typical roles: **Older adult; cognitively impaired adult; dependent person; investigator.

**Common methods / evidence signals: **Wandering; missing vehicle; last-seen search; alert; tracking.

**Primary target or asset: **Person's location, health, and safe recovery.

## KM-09 — Suspicious Disappearance / Long-Term Missing

**Definition: **A disappearance remains unexplained or carries reported indicators of foul play.

**Include when: **Investigators, evidence, duration, abandoned property, or circumstances make the case suspicious or cold.

**Exclude / boundary: **Do not convert uncertainty into confirmed kidnapping or homicide.

**Typical roles: **Missing person; partner/acquaintance; unknown suspect; investigator.

**Common methods / evidence signals: **Cold-case review; search warrant; forensic testing; last-known movements.

**Primary target or asset: **Person's location, fate, identity, and accountability.

## KM-10 — Missing Person Located / Remains Identified

**Definition: **A missing-person case is resolved or materially updated through safe recovery, arrest, body discovery, or identification.

**Include when: **The update directly links the located person/remains to an earlier missing case.

**Exclude / boundary: **A body discovery with no missing-person link is only Homicide/Body Discovery.

**Typical roles: **Located person; decedent; investigator; suspect.

**Common methods / evidence signals: **Safe recovery; traffic stop; search; DNA/dental identification; remains recovery.

**Primary target or asset: **Person's identity, location, condition, and case resolution.

# 12. Arson, Vandalism & Destruction of Property

**Parent definition: **Intentional, reckless, or criminally negligent burning, damaging, defacing, sabotaging, contaminating, or destroying property, evidence, vehicles, buildings, or infrastructure.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| AD-01 | Residential Arson |
| AD-02 | Occupied-Structure Arson / Fire Endangerment |
| AD-03 | Business / Commercial Arson |
| AD-04 | Vehicle Arson |
| AD-05 | Wildland / Brush / Forest Arson |
| AD-06 | Insurance / Financial-Motive Arson |
| AD-07 | Domestic / Retaliatory Arson |
| AD-08 | Institutional / Public-Building Arson |
| AD-09 | Vandalism / Criminal Mischief / Graffiti |
| AD-10 | Infrastructure / Utility Sabotage |
| AD-11 | Evidence / Body / Record Destruction by Fire |

## AD-01 — Residential Arson

**Definition: **A house, apartment, residential building, or dwelling is intentionally or criminally burned.

**Include when: **Fire-setting, accelerant, incendiary act, arson charge, or official arson finding is reported.

**Exclude / boundary: **Exclude undetermined or accidental residential fires without criminal suspicion.

**Typical roles: **Resident; partner/ex-partner; landlord/tenant; stranger.

**Common methods / evidence signals: **Accelerant; ignition; incendiary device; multiple fire points.

**Primary target or asset: **Dwelling, occupants, neighboring homes, and property.

## AD-02 — Occupied-Structure Arson / Fire Endangerment

**Definition: **A deliberately set fire targets or endangers a structure known or likely to be occupied.

**Include when: **Occupancy, evacuation, trapped people, or deliberate life risk is central.

**Exclude / boundary: **An unoccupied property fire without reported life risk belongs in the relevant property subtype.

**Typical roles: **Resident; customer; employee; attacker.

**Common methods / evidence signals: **Blocking exits; ignition near occupants; firebomb; hallway/stairwell fire.

**Primary target or asset: **Human life, occupied building, and emergency responders.

## AD-03 — Business / Commercial Arson

**Definition: **A store, office, warehouse, restaurant, or other commercial property is intentionally burned.

**Include when: **Business targeting, workplace access, retaliation, concealment, or arson finding is reported.

**Exclude / boundary: **Exclude accidental business fires.

**Typical roles: **Owner; employee; former employee; customer; competitor.

**Common methods / evidence signals: **Accelerant; after-hours entry; ignition of inventory; incendiary device.

**Primary target or asset: **Business premises, inventory, records, and revenue.

## AD-04 — Vehicle Arson

**Definition: **A car, truck, bus, trailer, or other vehicle is intentionally burned.

**Include when: **Deliberate ignition, accelerant, retaliation, insurance motive, or evidence destruction is alleged.

**Exclude / boundary: **Mechanical fire with no criminal indication is insufficient.

**Typical roles: **Owner; partner/ex-partner; thief; offender concealing evidence.

**Common methods / evidence signals: **Fuel/accelerant; interior ignition; firebomb; burning stolen vehicle.

**Primary target or asset: **Vehicle, contents, evidence, and nearby property.

## AD-05 — Wildland / Brush / Forest Arson

**Definition: **A person intentionally or criminally recklessly starts a vegetation, brush, or forest fire.

**Include when: **Origin evidence, admission, surveillance, incendiary conduct, or arson charge supports criminal setting.

**Exclude / boundary: **Exclude lightning, accidental spread, and lawful burns without criminal negligence.

**Typical roles: **Resident; visitor; serial fire-setter; land user.

**Common methods / evidence signals: **Open flame; incendiary device; repeated ignition points; unlawful burn.

**Primary target or asset: **Land, homes, wildlife habitat, public resources, and life safety.

## AD-06 — Insurance / Financial-Motive Arson

**Definition: **Property is burned to obtain insurance proceeds, erase debt, or conceal financial wrongdoing.

**Include when: **Evidence links fire-setting to a claim, financial distress, staged loss, or fraudulent valuation.

**Exclude / boundary: **A claim after a fire does not by itself prove financial motive.

**Typical roles: **Owner; business operator; accomplice; claimant.

**Common methods / evidence signals: **Staged fire; inflated claim; removal of valuables; hired fire-setter.

**Primary target or asset: **Insurer funds, property, records, and public safety.

## AD-07 — Domestic / Retaliatory Arson

**Definition: **Fire-setting targets a partner, relative, neighbor, employer, or other person as revenge or intimidation.

**Include when: **Relationship conflict, breakup, eviction, termination, dispute, or threat is linked to the fire.

**Exclude / boundary: **Unproven motive or unrelated nearby fire is insufficient.

**Typical roles: **Ex-partner; tenant/landlord; former employee; neighbor.

**Common methods / evidence signals: **Burning home/vehicle/belongings; incendiary message; repeated attempts.

**Primary target or asset: **Target's home, vehicle, possessions, safety, and sense of security.

## AD-08 — Institutional / Public-Building Arson

**Definition: **A school, church, government building, hospital, jail, transit property, or public facility is deliberately burned.

**Include when: **The institutional target or disruption of public function is central.

**Exclude / boundary: **Exclude ordinary commercial property unless public/institutional function matters.

**Typical roles: **Student; employee; visitor; ideological or retaliatory offender.

**Common methods / evidence signals: **Fire-setting; incendiary device; burning records; ignition during disturbance.

**Primary target or asset: **Institution, occupants, records, services, and public trust.

## AD-09 — Vandalism / Criminal Mischief / Graffiti

**Definition: **Property is intentionally damaged or defaced without fire being the primary method.

**Include when: **Smashing, defacing, damaging, graffiti, tire slashing, or criminal mischief is alleged.

**Exclude / boundary: **Exclude accidental damage, authorized alteration, and civil wear/maintenance disputes.

**Typical roles: **Neighbor; patron; juvenile; protest participant; ex-partner.

**Common methods / evidence signals: **Paint; breaking windows; slashing tires; smashing equipment; defacement.

**Primary target or asset: **Building, vehicle, monument, equipment, or personal property.

## AD-10 — Infrastructure / Utility Sabotage

**Definition: **Critical or public infrastructure is intentionally damaged, disabled, contaminated, or interfered with.

**Include when: **Power, communications, rail, water, emergency, transportation, or safety systems are targeted.

**Exclude / boundary: **Service outage alone is insufficient without alleged criminal interference.

**Typical roles: **Intruder; employee; vandal; ideologically motivated offender.

**Common methods / evidence signals: **Cutting lines; damaging substation; rail obstruction; contaminating system; equipment sabotage.

**Primary target or asset: **Infrastructure, continuity of service, public safety, and environment.

## AD-11 — Evidence / Body / Record Destruction by Fire

**Definition: **Fire is used to conceal a crime, destroy evidence, records, contraband, a vehicle, or human remains.

**Include when: **Concealment purpose is supported by location, timing, related offense, charges, or investigative findings.

**Exclude / boundary: **Ordinary disposal burning without an evidence connection is insufficient.

**Typical roles: **Primary offender; accomplice; employee; vehicle thief.

**Common methods / evidence signals: **Burning clothing; records; weapon; stolen car; body/remains; crime scene.

**Primary target or asset: **Evidence integrity, identification, and investigation.

# 13. Robbery, Burglary, Trespass & Home Invasion

**Parent definition: **Force- or threat-based taking, unlawful entry or remaining with criminal intent, occupied invasion, and criminal trespass. Distinguish robbery from theft and burglary from ordinary trespass.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| RB-01 | Armed Robbery |
| RB-02 | Strong-Arm / Street Robbery |
| RB-03 | Commercial / Convenience-Store Robbery |
| RB-04 | Bank / Financial-Institution Robbery |
| RB-05 | Carjacking |
| RB-06 | Home Invasion / Occupied Burglary |
| RB-07 | Residential Burglary |
| RB-08 | Business / Institutional Burglary |
| RB-09 | Vehicle Burglary |
| RB-10 | Criminal Trespass / Restricted-Area Entry |
| RB-11 | Attempted Burglary / Burglary Tools |

## RB-01 — Armed Robbery

**Definition: **Property is taken or demanded through threat or use of a firearm or other weapon.

**Include when: **Weapon display/use and intent to obtain property or value are explicit.

**Exclude / boundary: **A weapon assault with no taking intent is violent crime, not robbery.

**Typical roles: **Robber; cashier; customer; accomplice; lookout.

**Common methods / evidence signals: **Pointing weapon; demand note; threats; taking cash/phone/vehicle.

**Primary target or asset: **Person, business cash, merchandise, or valuables.

## RB-02 — Strong-Arm / Street Robbery

**Definition: **Property is taken from a person through bodily force or intimidation without a weapon being necessary.

**Include when: **Force, struggle, snatching with resistance, or intimidation is central.

**Exclude / boundary: **Pickpocketing or unattended-property theft without force is theft.

**Typical roles: **Pedestrian; patron; passenger; robber; group attacker.

**Common methods / evidence signals: **Punching; pushing; purse/phone snatch; group intimidation.

**Primary target or asset: **Personal property, money, phone, jewelry, and bodily safety.

## RB-03 — Commercial / Convenience-Store Robbery

**Definition: **A retail, restaurant, gas-station, pharmacy, or service business is robbed.

**Include when: **Employees/customers are confronted and business assets are demanded or taken by force/threat.

**Exclude / boundary: **After-hours entry without confrontation is burglary.

**Typical roles: **Robber; cashier; clerk; customer; accomplice.

**Common methods / evidence signals: **Weapon display; demand note; counter jump; cash-register theft.

**Primary target or asset: **Business cash, drugs, merchandise, employees, and customers.

## RB-04 — Bank / Financial-Institution Robbery

**Definition: **A bank, credit union, armored carrier, or financial office is targeted through force, threat, or intimidation.

**Include when: **Demand or taking targets institution-controlled money and robbery elements are reported.

**Exclude / boundary: **Fraudulent withdrawal without force/threat is financial fraud.

**Typical roles: **Robber; teller; security guard; courier.

**Common methods / evidence signals: **Demand note; weapon; takeover; armored-car ambush.

**Primary target or asset: **Institution funds, cash transport, staff, and customers.

## RB-05 — Carjacking

**Definition: **A vehicle is taken or attempted from a person through force, threat, or intimidation.

**Include when: **An occupant, driver, or recent possessor is confronted and the vehicle is the taking target.

**Exclude / boundary: **Unattended auto theft is not carjacking.

**Typical roles: **Driver; passenger; robber; accomplice.

**Common methods / evidence signals: **Weapon threat; assault; forced exit; taking keys; ordering victim to drive.

**Primary target or asset: **Vehicle, occupant safety, keys, and liberty.

## RB-06 — Home Invasion / Occupied Burglary

**Definition: **An occupied residence is unlawfully entered for robbery, assault, restraint, or another crime.

**Include when: **Occupants are present or confronted and unlawful entry/remaining is material.

**Exclude / boundary: **A resident's invited guest dispute is not automatically home invasion.

**Typical roles: **Intruder; resident; accomplice; lookout.

**Common methods / evidence signals: **Forced door/window; weapon; restraint; room-to-room search.

**Primary target or asset: **Occupants, home, money, property, and personal safety.

## RB-07 — Residential Burglary

**Definition: **A dwelling is unlawfully entered or remained in with intent to commit a crime, usually when unoccupied.

**Include when: **Forced/unauthorized entry plus criminal intent or completed offense is reported.

**Exclude / boundary: **Trespass without criminal intent and civil tenancy entry are insufficient.

**Typical roles: **Burglar; resident; neighbor; receiver.

**Common methods / evidence signals: **Door/window entry; lock manipulation; stolen keys; taking valuables.

**Primary target or asset: **Home, jewelry, electronics, firearms, documents, and privacy.

## RB-08 — Business / Institutional Burglary

**Definition: **A business, school, church, warehouse, or institution is unlawfully entered with criminal intent.

**Include when: **After-hours or unauthorized entry and intended/completed theft, damage, or other crime are explicit.

**Exclude / boundary: **Authorized employee access without unlawful entry may be employee theft instead.

**Typical roles: **Burglar; former employee; juvenile; accomplice.

**Common methods / evidence signals: **Forced door; roof/window entry; alarm defeat; key/credential misuse.

**Primary target or asset: **Cash, inventory, equipment, records, or restricted areas.

## RB-09 — Vehicle Burglary

**Definition: **A vehicle is unlawfully entered to steal property or commit another crime.

**Include when: **Broken window, door entry, rummaging, or property removal from a vehicle is reported.

**Exclude / boundary: **Theft of the vehicle itself is auto theft; exterior part theft may be vehicle-part theft.

**Typical roles: **Vehicle burglar; theft crew; receiver.

**Common methods / evidence signals: **Window smash; unlocked-door entry; trunk access; key-fob interference.

**Primary target or asset: **Bags, electronics, firearms, documents, and vehicle contents.

## RB-10 — Criminal Trespass / Restricted-Area Entry

**Definition: **A person knowingly enters or remains on property without authorization or after notice.

**Include when: **Clear restriction, notice, ban, order to leave, or protected area is present.

**Exclude / boundary: **Burglary requires additional criminal intent; civil occupancy disputes require caution.

**Typical roles: **Customer; former employee; intruder; protest participant.

**Common methods / evidence signals: **Refusing to leave; reentry after ban; fence crossing; restricted-area access.

**Primary target or asset: **Property possession, operations, safety, and restricted space.

## RB-11 — Attempted Burglary / Burglary Tools

**Definition: **Preparatory conduct shows an attempted unlawful entry or possession/use of tools for burglary.

**Include when: **Overt entry attempt, surveillance plus action, pry marks, tool possession with intent, or attempt charge is reported.

**Exclude / boundary: **Possessing ordinary tools without criminal intent is insufficient.

**Typical roles: **Would-be burglar; lookout; driver; accomplice.

**Common methods / evidence signals: **Prying; lock picks; glass punch; masks; casing; alarm tampering.

**Primary target or asset: **Target building/vehicle and intended property.

# 14. Cybercrime, Digital Crime & Identity Abuse

**Parent definition: **Computer, network, online account, platform, electronic communication, or data is the target, essential instrument, or primary environment of the offense—not merely incidental communication.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| CY-01 | Unauthorized Access / Hacking |
| CY-02 | Malware / Ransomware / Service Disruption |
| CY-03 | Phishing / Business-Email Compromise |
| CY-04 | Account Takeover / SIM Swap / Credential Theft |
| CY-05 | Online Financial / Marketplace / Crypto Scam |
| CY-06 | Cyberstalking / Doxxing / Digital Harassment |
| CY-07 | Swatting / Online Threat / Digital Hoax |
| CY-08 | Sextortion / Intimate-Image / Voyeurism Technology Abuse |
| CY-09 | Insider Database / Record / Data Misuse |
| CY-10 | Online Child Luring / Exploitation Technology |

## CY-01 — Unauthorized Access / Hacking

**Definition: **A person intentionally accesses a computer, network, device, or account without authorization or beyond permission.

**Include when: **Credential misuse, intrusion, privilege escalation, or unauthorized database/system access is explicit.

**Exclude / boundary: **Using a phone or social media during an unrelated crime is insufficient.

**Typical roles: **External hacker; insider; former employee; acquaintance.

**Common methods / evidence signals: **Stolen credentials; exploit; brute force; remote access; bypassing controls.

**Primary target or asset: **System, device, account, network, or protected data.

## CY-02 — Malware / Ransomware / Service Disruption

**Definition: **Malicious code or digital attack damages, encrypts, extorts, disables, or disrupts systems.

**Include when: **Malware deployment, encryption demand, denial-of-service, botnet, or sabotage is reported.

**Exclude / boundary: **Ordinary outage or software failure is insufficient.

**Typical roles: **Hacker; ransomware operator; insider; extortion group.

**Common methods / evidence signals: **Malware; encryption; DDoS; destructive script; ransom demand.

**Primary target or asset: **Systems, data availability, business operations, and money.

## CY-03 — Phishing / Business-Email Compromise

**Definition: **Deceptive electronic communication induces credential disclosure or fraudulent payment.

**Include when: **Spoofed email/site, compromised mailbox, fake executive/vendor request, or redirected invoice is central.

**Exclude / boundary: **A mistaken payment request without deception or compromise is insufficient.

**Typical roles: **Impostor; compromised vendor; employee recipient; money mule.

**Common methods / evidence signals: **Phishing link; spoofed domain; invoice change; executive impersonation.

**Primary target or asset: **Credentials, business funds, vendor/customer payments, and email accounts.

## CY-04 — Account Takeover / SIM Swap / Credential Theft

**Definition: **A person's online, financial, phone, or platform account is seized or controlled through stolen credentials or identity abuse.

**Include when: **Unauthorized password reset, SIM reassignment, session theft, or credential use is alleged.

**Exclude / boundary: **Authorized account sharing and forgotten-password disputes are insufficient.

**Typical roles: **Hacker; acquaintance; employee; mobile-store participant.

**Common methods / evidence signals: **SIM swap; credential stuffing; reset fraud; token theft; MFA bypass.

**Primary target or asset: **Account control, communications, money, identity, and data.

## CY-05 — Online Financial / Marketplace / Crypto Scam

**Definition: **Digital platforms or virtual assets are central to obtaining money or property through deception.

**Include when: **Online listing, investment platform, romance approach, crypto transfer, or electronic payment scheme is explicit.

**Exclude / boundary: **A failed investment or product dispute without knowing deception is insufficient.

**Typical roles: **Seller impostor; romance scammer; crypto promoter; marketplace buyer/seller.

**Common methods / evidence signals: **Fake listing; wallet transfer; investment dashboard; payment reversal; romance solicitation.

**Primary target or asset: **Money, cryptocurrency, goods, account access, and victim trust.

## CY-06 — Cyberstalking / Doxxing / Digital Harassment

**Definition: **Digital tools are used for repeated surveillance, threats, exposure of private data, or targeted harassment.

**Include when: **Pattern, fear, unwanted tracking/contact, threat, or publication of personal data is reported.

**Exclude / boundary: **One rude message or lawful public information sharing is insufficient.

**Typical roles: **Ex-partner; stranger; coworker; online group.

**Common methods / evidence signals: **Repeated messages; location tracking; account monitoring; doxxing; impersonation.

**Primary target or asset: **Privacy, safety, reputation, location, and communications.

## CY-07 — Swatting / Online Threat / Digital Hoax

**Definition: **Electronic communications trigger false emergency response or convey credible threats against people or places.

**Include when: **Threat or false report is digitally transmitted and criminally investigated.

**Exclude / boundary: **Vague online speech without credible threat or knowing false report is insufficient.

**Typical roles: **Online actor; student; disgruntled person; anonymous caller.

**Common methods / evidence signals: **Swatting; bomb threat; false active-shooter report; threat post/message.

**Primary target or asset: **Targeted person, school/business, responders, and public safety.

## CY-08 — Sextortion / Intimate-Image / Voyeurism Technology Abuse

**Definition: **Digital systems are used to coerce, obtain, create, distribute, or threaten release of intimate material without lawful consent.

**Include when: **Extortion, nonconsensual distribution, hidden recording, or account-enabled image abuse is explicit.

**Exclude / boundary: **Consensual lawful adult sharing and vague 'inappropriate content' are insufficient.

**Typical roles: **Partner/ex-partner; online extorter; hidden-camera operator; account hacker.

**Common methods / evidence signals: **Threatened release; image demand; covert camera; account theft; distribution.

**Primary target or asset: **Privacy, autonomy, reputation, money, and personal safety.

## CY-09 — Insider Database / Record / Data Misuse

**Definition: **A worker or authorized user abuses legitimate system access for an unlawful purpose.

**Include when: **Employment or official access enables improper lookup, alteration, theft, disclosure, or concealment.

**Exclude / boundary: **A data breach with no insider or authorized-access nexus belongs in another cyber subtype.

**Typical roles: **Employee; contractor; officer; healthcare/bank/government worker.

**Common methods / evidence signals: **Unauthorized lookup; record change; bulk download; disclosure; evidence deletion.

**Primary target or asset: **Customer/citizen data, records, credentials, and institutional integrity.

## CY-10 — Online Child Luring / Exploitation Technology

**Definition: **Digital communication is used to lure, groom, coerce, exploit, or arrange unlawful contact with a minor.

**Include when: **Minor status, unlawful intent, digital approach, solicitation, or exploitative material is explicit.

**Exclude / boundary: **Ordinary age-appropriate communication and vague safety warnings are insufficient.

**Typical roles: **Adult contact; disguised account; platform user; minor victim.

**Common methods / evidence signals: **Messaging; fake profile; grooming; coercion; meeting arrangement; file exchange.

**Primary target or asset: **Child safety, privacy, autonomy, and digital identity.

# 15. Stalking, Harassment, Threats & Protection-Order Violations

**Parent definition: **Repeated or targeted unwanted conduct causing fear, intimidation, substantial distress, surveillance, or court-order violations. Track relationship and digital context separately.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| SH-01 | Intimate-Partner / Ex-Partner Stalking |
| SH-02 | Stranger / Acquaintance Stalking |
| SH-03 | Workplace / School Stalking or Harassment |
| SH-04 | Cyberstalking / Digital Monitoring |
| SH-05 | Tracking Device / Location Surveillance |
| SH-06 | Repeated Threats / Terroristic Threats |
| SH-07 | Protection / Restraining / No-Contact Order Violation |
| SH-08 | Witness / Victim Intimidation or Retaliation |
| SH-09 | Bias-Motivated Harassment / Intimidation |

## SH-01 — Intimate-Partner / Ex-Partner Stalking

**Definition: **A current or former partner repeatedly follows, contacts, monitors, or appears near the victim.

**Include when: **A pattern tied to relationship, breakup, rejection, or control causes fear or violates boundaries.

**Exclude / boundary: **Ordinary co-parent communication or isolated nonthreatening contact is insufficient.

**Typical roles: **Partner; ex-partner; spouse; dating partner.

**Common methods / evidence signals: **Following; repeated calls; workplace/home visits; account monitoring; surveillance.

**Primary target or asset: **Victim's privacy, movement, safety, and autonomy.

## SH-02 — Stranger / Acquaintance Stalking

**Definition: **A non-intimate person engages in repeated unwanted surveillance, following, or contact.

**Include when: **Pattern, notice to stop, escalation, fear, or stalking charge is reported.

**Exclude / boundary: **Chance encounters and one unwanted communication are insufficient.

**Typical roles: **Stranger; neighbor; acquaintance; customer; fan.

**Common methods / evidence signals: **Following; waiting outside; repeated gifts/messages; photographing; route monitoring.

**Primary target or asset: **Victim's privacy, movement, home/work safety.

## SH-03 — Workplace / School Stalking or Harassment

**Definition: **Targeted conduct occurs through or against a workplace, school, employee, student, or applicant relationship.

**Include when: **Institutional access, shared setting, termination/rejection, or professional interaction enables the pattern.

**Exclude / boundary: **A workplace/school location alone is insufficient.

**Typical roles: **Coworker; former employee; student; teacher; applicant; customer.

**Common methods / evidence signals: **Repeated visits; messages; surveillance; threats; misuse of contact information.

**Primary target or asset: **Worker/student safety, privacy, and institutional operations.

## SH-04 — Cyberstalking / Digital Monitoring

**Definition: **Electronic systems enable repeated unwanted contact, surveillance, impersonation, or tracking.

**Include when: **Digital pattern and fear/distress are central rather than merely incidental messages.

**Exclude / boundary: **A single offensive post or ordinary public viewing is insufficient.

**Typical roles: **Ex-partner; acquaintance; stranger; online actor.

**Common methods / evidence signals: **Spyware; account access; repeated messages; location sharing abuse; impersonation.

**Primary target or asset: **Privacy, accounts, communications, and physical safety.

## SH-05 — Tracking Device / Location Surveillance

**Definition: **A device, app, vehicle tracker, tag, or account is used to monitor a person without authority.

**Include when: **Placement/use, lack of consent, and surveillance purpose are reported.

**Exclude / boundary: **Authorized fleet/parental tracking and accidental proximity alerts are insufficient.

**Typical roles: **Partner/ex-partner; acquaintance; employee; investigator acting unlawfully.

**Common methods / evidence signals: **GPS unit; AirTag-like device; phone app; vehicle telematics; account location.

**Primary target or asset: **Location privacy, movement, vehicle, and safety.

## SH-06 — Repeated Threats / Terroristic Threats

**Definition: **A person repeatedly or credibly threatens death, injury, attack, or destructive harm.

**Include when: **Specificity, capability, repetition, target, conduct, or criminal charge supports credibility.

**Exclude / boundary: **Hyperbole, protected speech, or vague anger without criminal threat is insufficient.

**Typical roles: **Partner; student; employee; neighbor; online actor.

**Common methods / evidence signals: **Calls; texts; letters; posts; weapon display; threat to attack location.

**Primary target or asset: **Person, school/business, public place, and sense of safety.

## SH-07 — Protection / Restraining / No-Contact Order Violation

**Definition: **A person knowingly violates a court order limiting contact, proximity, communication, possession, or conduct.

**Include when: **Valid order, notice, prohibited act, and knowing violation are reported.

**Exclude / boundary: **Contact not covered by the order or lack of notice requires caution.

**Typical roles: **Restrained person; protected person; co-parent; ex-partner.

**Common methods / evidence signals: **Calling; messaging; approaching home/work; third-party contact; weapon possession.

**Primary target or asset: **Protected person's safety and court authority.

## SH-08 — Witness / Victim Intimidation or Retaliation

**Definition: **A person threatens, harasses, harms, bribes, or pressures someone because of reporting, testimony, or cooperation.

**Include when: **Intent to influence, prevent, punish, or alter participation in a case is explicit.

**Exclude / boundary: **Ordinary disagreement with a witness and lawful litigation contact are insufficient.

**Typical roles: **Defendant; associate; family member; gang associate; employer.

**Common methods / evidence signals: **Threats; bribery; stalking; assault; property damage; online exposure.

**Primary target or asset: **Witness/victim safety, testimony, and investigation.

## SH-09 — Bias-Motivated Harassment / Intimidation

**Definition: **Targeted harassment or threat is allegedly motivated by identity-based bias.

**Include when: **Authorities, charge, statements, symbols, or conduct support the bias motive.

**Exclude / boundary: **Demographic difference or offensive opinion alone is insufficient.

**Typical roles: **Stranger; neighbor; group participant; online actor.

**Common methods / evidence signals: **Slurs with threats; targeted messages; symbols; following; property intimidation.

**Primary target or asset: **Targeted person's safety, dignity, home, or community space.

# 16. Human Trafficking, Smuggling & Exploitation

**Parent definition: **Exploitation of people through force, fraud, coercion, or abuse of vulnerability, and organized unlawful movement of people or contraband. Distinguish trafficking from smuggling while allowing overlap.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| HT-01 | Adult Sex Trafficking |
| HT-02 | Child Sex Trafficking / Commercial Exploitation |
| HT-03 | Labor Trafficking / Forced Labor |
| HT-04 | Human Smuggling / Paid Unlawful Transport |
| HT-05 | Stash House / Harboring Operation |
| HT-06 | Dangerous Vehicle Transport / Pursuit Smuggling |
| HT-07 | Online Recruitment / Advertising / Facilitation |
| HT-08 | Contraband Smuggling |

## HT-01 — Adult Sex Trafficking

**Definition: **An adult is recruited, controlled, advertised, transported, or exploited for commercial sex through force, fraud, or coercion.

**Include when: **Control, threats, debt, withheld documents, violence, fraud, or third-party profit is explicit.

**Exclude / boundary: **Consensual adult commercial activity without exploitation indicators is insufficient.

**Typical roles: **Trafficker; recruiter; driver; hotel operator; buyer; adult victim.

**Common methods / evidence signals: **Online ads; threats; debt; transportation; confiscated money/ID; hotel control.

**Primary target or asset: **Victim's liberty, safety, earnings, and autonomy.

## HT-02 — Child Sex Trafficking / Commercial Exploitation

**Definition: **A minor is used, recruited, advertised, transported, or sold for commercial sexual exploitation.

**Include when: **Minor status and commercial/exploitative exchange are explicit; proof of force is not required for classification.

**Exclude / boundary: **Vague runaway status or ordinary online contact is insufficient.

**Typical roles: **Trafficker; recruiter; buyer; hotel facilitator; minor victim.

**Common methods / evidence signals: **Advertising; hotel transport; payment; grooming; online recruitment; control.

**Primary target or asset: **Child's liberty, safety, autonomy, and exploitation proceeds.

## HT-03 — Labor Trafficking / Forced Labor

**Definition: **A person is compelled to work through force, fraud, coercion, debt, threats, document control, or abuse of vulnerability.

**Include when: **Work, control method, and inability to leave or meaningful coercion are reported.

**Exclude / boundary: **Low wages, poor conditions, or labor-law violations alone are insufficient.

**Typical roles: **Employer; recruiter; contractor; household owner; worker victim.

**Common methods / evidence signals: **Debt bondage; threats; withheld pay/ID; confinement; fraudulent recruitment.

**Primary target or asset: **Worker's labor, wages, liberty, identity documents, and safety.

## HT-04 — Human Smuggling / Paid Unlawful Transport

**Definition: **People are knowingly transported, guided, concealed, or harbored for payment to evade border or immigration controls.

**Include when: **Movement/service, payment, concealment, route, or smuggling charge is central.

**Exclude / boundary: **Immigration status alone is insufficient; trafficking requires exploitation beyond transportation service.

**Typical roles: **Driver; guide; organizer; passenger/customer; stash-house operator.

**Common methods / evidence signals: **Vehicle concealment; desert route; checkpoint evasion; harboring; payment collection.

**Primary target or asset: **Movement, border controls, transported persons, and proceeds.

## HT-05 — Stash House / Harboring Operation

**Definition: **A property is used to conceal, hold, stage, control, or transfer smuggled or trafficked persons.

**Include when: **Multiple persons, confinement, payment, threats, staging, or harboring evidence is reported.

**Exclude / boundary: **Ordinary shared housing and undocumented status alone are insufficient.

**Typical roles: **Property operator; guard; organizer; driver; victim/passenger.

**Common methods / evidence signals: **Locked rooms; overcrowding; phone confiscation; payment demand; staged pickup.

**Primary target or asset: **People's liberty/safety, property, and smuggling proceeds.

## HT-06 — Dangerous Vehicle Transport / Pursuit Smuggling

**Definition: **People are transported in unsafe vehicles or high-risk evasive driving as part of smuggling.

**Include when: **Overcrowding, trunk/compartment concealment, high-speed flight, abandonment, or heat danger is central.

**Exclude / boundary: **An unrelated pursuit with passengers is insufficient.

**Typical roles: **Smuggling driver; passenger; scout; pickup coordinator.

**Common methods / evidence signals: **Packed vehicle; trunk; hidden compartment; checkpoint flight; roadside abandonment.

**Primary target or asset: **Transported persons' lives, vehicle, roadway, and border enforcement.

## HT-07 — Online Recruitment / Advertising / Facilitation

**Definition: **Digital platforms are used to recruit victims/customers, advertise exploitation, coordinate transport, or collect payment.

**Include when: **Online communications are operationally important to trafficking or smuggling.

**Exclude / boundary: **Incidental phone use is insufficient.

**Typical roles: **Recruiter; advertiser; platform user; buyer; organizer.

**Common methods / evidence signals: **Social media; messaging apps; classified ads; location sharing; online payment.

**Primary target or asset: **Victim, customer/passenger, communications, and proceeds.

## HT-08 — Contraband Smuggling

**Definition: **Drugs, weapons, currency, stolen goods, protected items, or other contraband are concealed and moved across a border, facility, or jurisdiction.

**Include when: **Concealment plus unlawful transport/import/export is central.

**Exclude / boundary: **Simple local possession with no movement or smuggling method is insufficient.

**Typical roles: **Courier; driver; traveler; employee; organizer.

**Common methods / evidence signals: **Hidden compartment; luggage; cargo; mail; body concealment; false manifest.

**Primary target or asset: **Contraband, transport route, facility/border controls, and proceeds.

# 17. Elder & Vulnerable Adult Abuse or Exploitation

**Parent definition: **Abuse, neglect, abandonment, intimidation, or financial exploitation of an older or dependent adult whose condition, disability, illness, or trust relationship increases vulnerability.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| EV-01 | Caregiver Neglect / Basic-Needs Deprivation |
| EV-02 | Physical Abuse / Unlawful Restraint |
| EV-03 | Abandonment / Dangerous Desertion |
| EV-04 | Facility / Institutional Abuse or Neglect |
| EV-05 | Family / Guardian Financial Exploitation |
| EV-06 | Paid Caregiver / Professional Asset Exploitation |
| EV-07 | Scam Targeting an Elder or Vulnerable Adult |
| EV-08 | Power-of-Attorney / Fiduciary / Estate Abuse |

## EV-01 — Caregiver Neglect / Basic-Needs Deprivation

**Definition: **A caregiver fails to provide necessary food, hygiene, medication, supervision, shelter, or protection.

**Include when: **Duty of care plus serious deprivation, unsafe condition, injury, or substantial risk is reported.

**Exclude / boundary: **Age, illness, poverty, or poor outcome alone is insufficient without caregiver failure.

**Typical roles: **Family caregiver; home-health aide; guardian; facility worker.

**Common methods / evidence signals: **Withholding food/medicine; leaving in filth; inadequate supervision; untreated wounds.

**Primary target or asset: **Health, dignity, basic needs, and safety.

## EV-02 — Physical Abuse / Unlawful Restraint

**Definition: **An older or vulnerable adult is assaulted, roughly handled, confined, or restrained unlawfully.

**Include when: **Force, injury, intimidation, restraint, or assault charge is explicit.

**Exclude / boundary: **Lawful medical restraint and accidental injury without suspected abuse are insufficient.

**Typical roles: **Caregiver; family member; facility employee; acquaintance.

**Common methods / evidence signals: **Hitting; pushing; choking; tying; locking in room; rough transfer.

**Primary target or asset: **Body, liberty, dignity, and safety.

## EV-03 — Abandonment / Dangerous Desertion

**Definition: **A responsible person intentionally leaves a dependent adult without safe care or assistance.

**Include when: **The person's vulnerability, location, duration, weather, or medical need creates serious danger.

**Exclude / boundary: **A competent adult choosing to leave or lawful transfer of care is insufficient.

**Typical roles: **Family caregiver; guardian; facility; driver.

**Common methods / evidence signals: **Leaving roadside, hospital, motel, public place, or unattended home.

**Primary target or asset: **Shelter, care, location, health, and safety.

## EV-04 — Facility / Institutional Abuse or Neglect

**Definition: **Maltreatment occurs in a nursing home, assisted-living site, group home, hospital, or care facility.

**Include when: **Institutional custody, staffing, policy, access, or concealment materially enables the conduct.

**Exclude / boundary: **Poor service or regulatory deficiency alone is insufficient without alleged criminal abuse/neglect.

**Typical roles: **Nurse; aide; administrator; residential worker; contractor.

**Common methods / evidence signals: **Assault; neglect; medication misuse; restraint; record falsification; failure to report.

**Primary target or asset: **Resident/patient health, liberty, dignity, records, and safety.

## EV-05 — Family / Guardian Financial Exploitation

**Definition: **A relative, guardian, or trusted personal representative misuses access to assets.

**Include when: **Trust, dependency, guardianship, or family access enables unauthorized financial/property benefit.

**Exclude / boundary: **Ordinary inheritance dispute or shared-finance disagreement without deception is insufficient.

**Typical roles: **Adult child; sibling; partner; guardian; power-of-attorney holder.

**Common methods / evidence signals: **Withdrawals; forged checks; property transfer; benefit diversion; deed/account changes.

**Primary target or asset: **Funds, home, estate, benefits, cards, and identity.

## EV-06 — Paid Caregiver / Professional Asset Exploitation

**Definition: **A paid caregiver or professional steals or diverts client assets through entrusted access.

**Include when: **Employment/professional role provides access to funds, cards, identity, property, or benefits.

**Exclude / boundary: **A stranger scam with no care/professional relationship belongs in Scam Targeting.

**Typical roles: **Home-health aide; nurse; adviser; attorney; residential employee.

**Common methods / evidence signals: **Card use; cash theft; check forgery; account transfer; property removal.

**Primary target or asset: **Client funds, payment cards, accounts, property, benefits, and identity.

## EV-07 — Scam Targeting an Elder or Vulnerable Adult

**Definition: **A scammer deliberately exploits age, dependency, isolation, cognitive impairment, or fear.

**Include when: **Victim vulnerability is known or used in impersonation, romance, tech-support, contractor, lottery, or emergency scam.

**Exclude / boundary: **A fraud victim merely being older is insufficient when vulnerability is not material.

**Typical roles: **Impostor; telemarketer; online contact; contractor; money mule.

**Common methods / evidence signals: **Gift cards; wire transfer; fake emergency; tech access; romance; home repair.

**Primary target or asset: **Savings, credit, identity, home equity, and trust.

## EV-08 — Power-of-Attorney / Fiduciary / Estate Abuse

**Definition: **A person with formal fiduciary authority diverts, conceals, or misuses assets contrary to duty.

**Include when: **Power of attorney, trusteeship, guardianship, executor role, or advisory duty enables the transaction.

**Exclude / boundary: **Disputed but authorized investment/judgment is insufficient without alleged dishonest conversion.

**Typical roles: **Attorney-in-fact; trustee; executor; guardian; adviser.

**Common methods / evidence signals: **Self-dealing; unauthorized transfer; forged authority; concealed sale; account change.

**Primary target or asset: **Estate, trust, home, investments, accounts, and beneficiary rights.

# 18. Hate Crime, Bias & Extremism

**Parent definition: **Bias-motivated criminal conduct or violent extremist activity. Apply only when motive is supported by authorities, charges, statements, symbols, target selection, or reported evidence—not demographic difference alone.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| HB-01 | Race / Ethnicity / National-Origin Bias Crime |
| HB-02 | Religious-Bias Crime |
| HB-03 | Sexual-Orientation / Gender-Identity Bias Crime |
| HB-04 | Disability-Bias Crime |
| HB-05 | Bias-Motivated Assault / Homicide |
| HB-06 | Bias Threat / Harassment / Intimidation |
| HB-07 | Bias Vandalism / Arson / Desecration |
| HB-08 | Violent Extremist Plot / Ideological Attack |

## HB-01 — Race / Ethnicity / National-Origin Bias Crime

**Definition: **Crime allegedly motivated by the victim's race, ethnicity, ancestry, or national origin.

**Include when: **Slurs, statements, symbols, target pattern, charge, or authority finding supports motive.

**Exclude / boundary: **Different demographics alone and offensive speech without crime are insufficient.

**Typical roles: **Individual offender; group participant; neighbor; stranger.

**Common methods / evidence signals: **Assault; threat; vandalism; stalking; arson; intimidation.

**Primary target or asset: **Person, home, business, community site, dignity, and safety.

## HB-02 — Religious-Bias Crime

**Definition: **Crime targets a person, group, worship site, cemetery, school, or property because of religion or perceived religion.

**Include when: **Target selection, symbols, statements, timing, or official bias allegation supports motive.

**Exclude / boundary: **A crime at a religious site without bias evidence is insufficient.

**Typical roles: **Individual; vandal; attacker; extremist actor.

**Common methods / evidence signals: **Threat; assault; desecration; graffiti; arson; property damage.

**Primary target or asset: **Person, house of worship, cemetery, school, symbols, and community safety.

## HB-03 — Sexual-Orientation / Gender-Identity Bias Crime

**Definition: **Crime allegedly targets actual or perceived sexual orientation, gender identity, or expression.

**Include when: **Reported slurs, statements, target selection, charge, or investigative finding supports motive.

**Exclude / boundary: **Identity difference or noncriminal offensive opinion is insufficient.

**Typical roles: **Stranger; acquaintance; group participant; online actor.

**Common methods / evidence signals: **Assault; threat; harassment; vandalism; arson; intimidation.

**Primary target or asset: **Person, venue, home, property, dignity, and safety.

## HB-04 — Disability-Bias Crime

**Definition: **A person or property is targeted because of actual or perceived disability.

**Include when: **Bias evidence or official allegation connects disability to victim selection or conduct.

**Exclude / boundary: **Exploitation due vulnerability without bias motive belongs in Vulnerable Adult Abuse/Fraud.

**Typical roles: **Stranger; caregiver acting from bias; group participant.

**Common methods / evidence signals: **Assault; harassment; threat; vandalism; intimidation.

**Primary target or asset: **Person's body, mobility aids, home, dignity, and safety.

## HB-05 — Bias-Motivated Assault / Homicide

**Definition: **Physical attack or killing is allegedly driven partly or wholly by protected-identity bias.

**Include when: **Violent offense and bias motive are both supported.

**Exclude / boundary: **Do not infer bias from victim/offender identities alone.

**Typical roles: **Attacker; group; victim; accomplice.

**Common methods / evidence signals: **Beating; shooting; stabbing; vehicle attack; group assault.

**Primary target or asset: **Life, bodily safety, and targeted community security.

## HB-06 — Bias Threat / Harassment / Intimidation

**Definition: **Credible threats or criminal harassment target identity, community membership, or protected space.

**Include when: **Threat plus bias evidence is explicit and conduct crosses the criminal threshold.

**Exclude / boundary: **Offensive speech alone without threat/harassment offense is insufficient.

**Typical roles: **Caller; neighbor; online actor; group participant.

**Common methods / evidence signals: **Threatening message; repeated calls; symbol; stalking; intimidation campaign.

**Primary target or asset: **Person, family, community, worship or cultural site, and sense of safety.

## HB-07 — Bias Vandalism / Arson / Desecration

**Definition: **Property is damaged, burned, defaced, or desecrated because of identity or community association.

**Include when: **Symbols, slurs, target choice, timing, admission, or official finding supports bias.

**Exclude / boundary: **Ordinary vandalism at a community site with no bias evidence is insufficient.

**Typical roles: **Vandal; fire-setter; group participant; unknown offender.

**Common methods / evidence signals: **Graffiti; symbol painting; broken windows; cemetery damage; arson.

**Primary target or asset: **Home, business, worship site, cemetery, monument, or community center.

## HB-08 — Violent Extremist Plot / Ideological Attack

**Definition: **Violence, weapons, explosives, threats, or destructive acts are planned or committed in furtherance of extremist ideology.

**Include when: **Overt criminal act plus ideological motive, target, manifesto, communications, or official allegation is reported.

**Exclude / boundary: **Belief, membership, or protected advocacy alone is insufficient without crime.

**Typical roles: **Lone actor; cell/group member; recruiter; plot participant.

**Common methods / evidence signals: **Attack planning; weapons acquisition; bomb plot; threat; target surveillance.

**Primary target or asset: **People, institutions, government/public sites, and community safety.

# 19. School, Institutional & Public-Facility Crime

**Parent definition: **Cross-cutting setting/authority context where a school, daycare, hospital, care facility, jail, library, transit system, government building, or similar institution materially shapes access, victims, duties, or public-safety impact.

Assign every supported subtype. A single incident may receive multiple labels from this section and labels from other parent categories.

## Subcategory Map

| **Code** | **Subcategory** |
| --- | --- |
| SI-01 | School Assault / Student Fight |
| SI-02 | School Weapon Possession / Use |
| SI-03 | School Threat / Shooting or Bomb Hoax |
| SI-04 | Educator / Coach / School-Employee Misconduct |
| SI-05 | Daycare / Childcare Facility Crime |
| SI-06 | Hospital / Healthcare Facility Crime |
| SI-07 | Nursing / Residential / Group-Home Crime |
| SI-08 | Jail / Prison / Detention-Facility Crime |
| SI-09 | Library / Government / Public-Building Crime |
| SI-10 | Transit / Station / Public-Transportation Crime |
| SI-11 | Institutional Theft / Fraud / Record Misuse |
| SI-12 | Institutional Arson / Vandalism / Sabotage |

## SI-01 — School Assault / Student Fight

**Definition: **Criminal violence occurs on campus, at a school event, or through a student-school relationship.

**Include when: **Assault, serious fight, injury, or arrest is reported and school context is material.

**Exclude / boundary: **Routine discipline or mutual pushing without criminal allegation is insufficient.

**Typical roles: **Student; visitor; parent; staff victim; school officer.

**Common methods / evidence signals: **Punching; group fight; stabbing; assault on staff; event violence.

**Primary target or asset: **Students, staff, campus order, and bodily safety.

## SI-02 — School Weapon Possession / Use

**Definition: **A weapon is unlawfully brought, possessed, displayed, or used at school or a school event.

**Include when: **Weapon, location, offender, and criminal or serious safety response are explicit.

**Exclude / boundary: **Lawful secured officer weapons, approved tools, and false rumor are insufficient.

**Typical roles: **Student; visitor; employee; school officer respondent.

**Common methods / evidence signals: **Firearm; knife; prohibited device; brandishing; ammunition.

**Primary target or asset: **Students, staff, campus, and public safety.

## SI-03 — School Threat / Shooting or Bomb Hoax

**Definition: **A credible or criminal threat targets a school, students, staff, or event, including false emergency reports.

**Include when: **Threat communication, hoax, investigation, evacuation, arrest, or charge is reported.

**Exclude / boundary: **Vague rumor or protected speech without criminal threat is insufficient.

**Typical roles: **Student; former student; online actor; caller.

**Common methods / evidence signals: **Social post; message; list; bomb threat; swatting; false active-shooter report.

**Primary target or asset: **School community, emergency resources, operations, and safety.

## SI-04 — Educator / Coach / School-Employee Misconduct

**Definition: **A school employee uses occupational access or authority to commit a crime involving a student, school asset, record, or function.

**Include when: **Employment materially enables access, trust, authority, concealment, or target selection.

**Exclude / boundary: **An employee's unrelated off-duty crime is insufficient.

**Typical roles: **Teacher; coach; administrator; aide; bus driver; custodian.

**Common methods / evidence signals: **Abuse; assault; theft; record misuse; drug diversion; threats; neglect.

**Primary target or asset: **Student, school funds/property, records, and institutional trust.

## SI-05 — Daycare / Childcare Facility Crime

**Definition: **Crime occurs through licensed/unlicensed childcare custody, access, or duty.

**Include when: **Care role or facility context enables abuse, neglect, unsafe restraint, abandonment, theft, or concealment.

**Exclude / boundary: **A crime merely near a daycare is insufficient.

**Typical roles: **Daycare worker; owner; aide; parent; contractor.

**Common methods / evidence signals: **Abuse; failure to supervise; unsafe transport; restraint; falsified records.

**Primary target or asset: **Child, facility, records, funds, and parental trust.

## SI-06 — Hospital / Healthcare Facility Crime

**Definition: **A hospital, clinic, emergency department, or medical facility materially frames the offense.

**Include when: **Patient access, medical duty, controlled medication, facility security, or attack on staff/patient is central.

**Exclude / boundary: **A suspect merely receiving treatment there is insufficient unless conduct is facility-connected.

**Typical roles: **Patient; visitor; nurse; doctor; aide; security worker.

**Common methods / evidence signals: **Assault; drug diversion; theft; record misuse; unlawful restraint; threats.

**Primary target or asset: **Patient/staff safety, medication, records, equipment, and operations.

## SI-07 — Nursing / Residential / Group-Home Crime

**Definition: **Crime arises through custody, care, access, or operation of a residential care institution.

**Include when: **Resident vulnerability and employee/facility duty materially enable abuse, neglect, exploitation, or violence.

**Exclude / boundary: **Regulatory deficiency alone is insufficient without alleged crime.

**Typical roles: **Aide; nurse; administrator; resident; visitor; caregiver.

**Common methods / evidence signals: **Neglect; assault; restraint; medication misuse; theft; concealment.

**Primary target or asset: **Resident safety, liberty, health, money, property, and records.

## SI-08 — Jail / Prison / Detention-Facility Crime

**Definition: **Crime occurs within or through custody, visitation, staffing, or facility operations.

**Include when: **Inmate, visitor, employee, contraband, assault, escape, or official-system context is central.

**Exclude / boundary: **A person's prior incarceration is insufficient.

**Typical roles: **Inmate; detainee; corrections officer; visitor; contractor.

**Common methods / evidence signals: **Assault; contraband; escape; evidence/record misuse; employee smuggling; threats.

**Primary target or asset: **People in custody, staff, facility security, and controlled items.

## SI-09 — Library / Government / Public-Building Crime

**Definition: **A public building or civic facility materially enables or is targeted by criminal conduct.

**Include when: **Public access, official function, institutional users, property, or disruption is central.

**Exclude / boundary: **A crime merely occurring nearby is insufficient.

**Typical roles: **Patron; visitor; employee; official; security worker.

**Common methods / evidence signals: **Lewd conduct; assault; threat; theft; vandalism; arson; trespass.

**Primary target or asset: **Public users, employees, records, property, and service continuity.

## SI-10 — Transit / Station / Public-Transportation Crime

**Definition: **A bus, train, station, platform, airport public area, or transit operation materially frames the offense.

**Include when: **Passenger/employee access, confined setting, fare/service function, or attack on transit is central.

**Exclude / boundary: **A crime on a street near transit is insufficient.

**Typical roles: **Passenger; operator; station patron; employee; security officer.

**Common methods / evidence signals: **Assault; robbery; threats; vandalism; unlawful weapon; interference with operator.

**Primary target or asset: **Passengers, workers, vehicles, station property, and service safety.

## SI-11 — Institutional Theft / Fraud / Record Misuse

**Definition: **Funds, property, benefits, credentials, or records of an institution are stolen, falsified, diverted, or misused.

**Include when: **Institutional access or target is central and the conduct is criminally alleged.

**Exclude / boundary: **Ordinary administrative error or unrelated employee crime is insufficient.

**Typical roles: **Employee; contractor; student/resident; official; vendor.

**Common methods / evidence signals: **Embezzlement; false record; credential misuse; inventory theft; benefit diversion.

**Primary target or asset: **Institution funds, records, credentials, equipment, and public trust.

## SI-12 — Institutional Arson / Vandalism / Sabotage

**Definition: **A school, hospital, jail, government, transit, library, or care facility is intentionally damaged or burned.

**Include when: **The institutional target and disruption/safety impact are material.

**Exclude / boundary: **Accidental damage and ordinary maintenance failure are insufficient.

**Typical roles: **Student; resident; employee; visitor; ideological/retaliatory offender.

**Common methods / evidence signals: **Fire-setting; graffiti; equipment damage; utility sabotage; window/door destruction.

**Primary target or asset: **Facility, occupants, records, equipment, and service continuity.

# Cross-Category Boundary Rules

Use these rules when one incident touches several parent categories. They are routing aids, not restrictions against multi-labeling.

**Child in an impaired driver’s vehicle. **Assign the child-risk subtype under Child Neglect/Endangerment and the applicable DUI/traffic subtype. Add drug possession only when possession or contraband is independently supported.

**Employee theft versus customer-account misuse. **Use workplace asset theft when the employer’s money or property is taken. Use customer financial-data/account misuse when occupational access is used against a customer account. Assign both if both assets are affected.

**Theft versus robbery. **Theft is a taking without the force/fear element. Robbery requires force, threatened force, or intimidation connected to taking or retaining property.

**Burglary versus trespass. **Burglary requires unlawful entry or remaining with criminal intent. Trespass covers unlawful presence without sufficient evidence of intended theft or another crime.

**Missing person versus kidnapping. **Missing-person labels describe unknown whereabouts and search status. Kidnapping/abduction labels require evidence of unlawful taking, movement, concealment, restraint, or custodial interference.

**Body discovery versus homicide. **Assign body-discovery status when remains are found or identified. Add a homicide subtype only when investigators, charges, or article facts support unlawful killing or a suspicious-death investigation.

**Public disturbance versus assault. **Disorderly conduct covers disruption without a sufficiently supported violent act. Add assault/violent-crime labels when force, injury, a credible attack, or weapon conduct is reported.

**Family context versus underlying offense. **Family/relationship labels capture the relationship and setting. Also assign the underlying assault, homicide, stalking, kidnapping, theft, or property-damage subtype when supported.

**Hate/bias versus target identity. **Do not infer bias because victim and offender identities differ. Require statements, symbols, target selection, official allegations, charges, or other evidence linking the offense to a protected identity or ideology.

**Institutional setting versus incidental location. **Use a school/institution/public-facility subtype only when the setting, entrusted duty, controlled access, institutional target, or service disruption materially shapes the crime—not merely because the incident occurred nearby.

# Headline-Only Safeguards

- Do not treat “charged,” “arrested,” “wanted,” “sentenced,” or “investigated” as a subcategory. Identify the underlying alleged conduct.

- Do not infer a weapon type, victim relationship, motive, injury severity, or age from a generic headline.

- When a headline uses a broad term such as “fraud,” “assault,” or “child endangerment,” assign only the supported broad subtype and revisit after full-text extraction.

- A person’s job title, juvenile status, family connection, disability, or institutional location does not itself establish the corresponding context label; the fact must materially relate to the conduct.

- If a headline and article conflict, prefer the most specific supported facts in the article and mark the conflict for review.

# Quality-Control Checklist

- Every assigned code has a supporting fact or evidence span.

- All materially distinct reported behaviors have been considered for multi-label assignment.

- No label rests only on an unsupported inference, keyword collision, demographic fact, or incidental location.

- The exclusion/boundary rule for each candidate label has been checked.

- Overlapping parent categories have been added when they capture independent conduct or essential context.

- Thin or contradictory articles are marked for review instead of being forced into a precise subtype.

# Final Model Instruction

Identify what the article reports, assign every supported parent and subcategory code, cite the evidence for each decision, and leave downstream inclusion/exclusion decisions to the separate selection workflow.
