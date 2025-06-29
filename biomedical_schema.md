---
# core_metadata?: Required metadata for all entities, NO nested properties, typically parsed from note content:
title (Required, concise identifier follwed by primary hierarchal ontology. For SAQ/LO - {SuccinctLabel}_{College}.{Exam}.{EntityType}.{Year/Section}.{Sitting/Subsection (if applicable)}.{SAQ/LO Number} e.g. "CompartmentModels_CICM.PEX.LO.B.i", "CompartmentModels_ANZCA.PEX.LO.2.2.1", "MilrinoneVsDobutamine_CICM.PEX.SAQ.25.A.09", "N2OforGA_ANZCA.PEX.SAQ.23.A.02". For principles, models, concepts, equations, objects - {SuccinctDomainLabel}.{DecreasingAtomicity}...{AtomicConceptName}): string 
aliases? (Required for LO/SAQ, array, Alternative identifiers, symbols or homonyms, including UID and codes, may include [{Description}, {SuccinctLabel}, {College.Exam.EntityType.Year/Section.Sitting/Subsection.SAQ/LO Number}, {LO_Code}] e.g., ["Discuss the advantages and disadvantages of using nitrous oxide as part of a general anaesthetic.", "N2OforGA", "ANZCA.PEX.SAQ.23.A.02", "BT_GS_1.27"]): string
entity_type?(Required, enum, Primary hierarchal ontology type): [LO, SAQ, axiom, principle, concept, equation, model, structure, object]
significance? (Required, array, Succinct but nuanced integration of relevance to other entities based on all metadata and relationships): string
description?: (Required, array, Succinct description of the entity that broadly answers all queries): string
tags?: (Required, array, Nested tags for all alternative hierarchal ontologies, allowing non-linear schemas representation through simultaneous categorisations, ensure this nested list is unified across all entities and refined e.g., [ANZCA/PEX/LO/12_Pain/3_Pharmacology/2_OpioidsMechanism, CICM/PEX/LO/K_NervousSystem/4_PainPharmacology/i_PainManagementPharmacology, Pharmacology/Pharmacodynamics/Mechanism/IntrinsicActivity/PartialAgonist]): string
queries?: (Required, array, List of questions informed by this entity): string
# exam_metadata?: Required metadata for SAQ/LOs, Optional otherwise, object, NO nested properties, typically parsed from note content:
college? (Required, enum, Institution through which the exam was administered): [ANZCA, CICM]
exam? (Required, enum, Primary/First Part vs Final/Second Part): [PEX, FEX]
section? (Required, enum, Section of the syllabus pertaining to the SAQ or LO, must include both ANZCA and CICM): [F - Respiratory System, 5 - Respiratory System]
subsection? (Optional, enum, Subsection of the syllabus pertaining to the SAQ or LO, e.g. [Cardiac Output, Pharmacodynamics]): string
lo? (Required if LO, enum, Learning objective number, e.g. [1.1, 1.2, 1.3]): string
sitting? (Required if SAQ, enum, Exam sitting March/April vs September/October [A, B]): string
year? (Required if SAQ, integer, Exam year, e.g. 2022): number
question_number? (Required if SAQ, integer, Question number for SAQs): number
pass_rate? (Required if SAQ, number, Normalised proportion of candidates passing from 0-1, e.g. 0.62 is 62% pass_rate): number
difficulty_level? (Required if SAQ, enum, Difficulty level of the question derived by pass_rate trisection, e.g. 'basic', 'intermediate', 'advanced'): string
ec_expected? (Required if SAQ (if expected standard or required domain knowledge was explained in examiner comments), array, Examiner comments explaining expected standard or required domain knowledge to pass the question. e.g. 'Candidates were expected to demonstrate relevant knowledge on the pharmacodynamics and pharmacokinetics of nitrous oxide'): string
ec_credit? (Required if SAQ (if extra credit was explained in examiner comments), array, Examiner comments explaining any extra credit awarded for the question. e.g. 'Candidates were awarded extra credit for noting that nitrous oxide is a potent vasodilator'): string
ec_errors? (Required if SAQ (if common errors were explained in examiner comments), array, Examiner comments explaining any common errors or problems made routinely by candidates in the question. e.g. 'Candidates often incorrectly identified the mechanism of action of nitrous oxide as a partial agonist'): string
# concept_metadata?: Required metadata for concepts - principles, models, equations etc, object, Optional otherwise, NO nested properties, typically parsed from note content, varying by entity_type
symbol? (Required if universally known within domain, string, Symbolic representation, e.g., 'Vd', 'Cl'): string
granularity? (Required, enum, Granularity of the concept): [subatomic, atomic, molecular, macromolecular]
atomic?: (Required, boolean, True if the concept has atomic granularity - represents the smallest exam-relevant concept, e.g., SI units): boolean
dependency_ratio?: (Required, number of composite concepts which are derived from this entity (helps derive optimal atomic:composite ratio which increases small-world network connectivity - ideally aiming for 0.1-0.2, with 5-10 composite concepts for every atomic concept)): number
dimension? (Required if variable, Otherwise optional, string, Physical dimension, e.g., 'Pressure', 'Volume'): string
key_formula? (Required if equation or model, Otherwise optional, string, Mathematical formula, e.g., 'CO = HR x SV'): string
units (standardised_units, SI_units, dimensional_units)?: string, Measurement unit, e.g., 'L/min (L/min/m2, d2/w/t)', 'mmHg'
normal_range (standardised_range)? (Required if variable, Otherwise optional, string, Typical value range, e.g., '5L/min (70ml/kg/min)'): string
key_examples? (Optional, array, principle examples of the entity): string
interesting_factoids? (Optional, array, Interesting factoids, e.g., 'The heart is the only muscle that can regenerate itself', 'The human body contains enough DNA to stretch from the Earth to the moon and back 100 times'): string
# relation_metadata?: Optional metadata for all entities, but strongly recommended. Defines connections between related entities. NO nested properties, typically parsed from note content:
causes? (Required if mechanism, Optional otherwise, array, IDs of concepts (must be internal links) that this concept directly causes, e.g., ["[[CardiacOutput]]", "[[ForceOfContraction]]"]): string
causes_magnitude? (Optional, object, Strength values for causal relationships, e.g., {1.15 x [[StrokeVolume]]}): string
causes_description? (Optional, object, Explanations of causal relationships, e.g., {"Directly increases [[StrokeVolume]] by 15%"}): string
assumes? (Required if model, Optional otherwise, array, IDs of axiomatic assumptions that this concept presupposes): string
assumes_confidence? (Required if model, Optional otherwise, object, Confidence levels for assumptions, e.g., {'Concept_A': 0.9}): string
determines? (Required if mechanism or model, Optional otherwise, array, IDs of concepts that this concept directly influences or calculates): string
determines_formula? (Required if mechanism or model, Optional otherwise, object, Mathematical relationships, e.g., {'Flow': 'Q = ΔP/R'}): string
hypernym? (Required if non-atomic, Optional otherwise, array, IDs of broader concepts that encompass this concept (is-a relationship)): string
hyponym? (Required if atomic, Optional otherwise, array, IDs of more specific concepts contained within this concept (has-a relationship)): string
antonym? (Optional but strongly recommended, array, IDs of concepts with opposing or contradictory meanings): string
precedes? (Optional, array, IDs of concepts that temporally or logically come before this concept): string
precedes_timeframe? (Optional, object, Optional temporal relationship descriptions, e.g., {'Concept_B': '2-3 minutes'}): string
follows? (Optional, array, IDs of concepts that temporally or logically come after this concept): string
follows_timeframe? (Optional, object, Optional temporal relationship descriptions, e.g., {'Concept_C': 'immediate'}): string
# integration_metadata?: Optional metadata for all entities, but strongly recommended, object, NO nested properties, typically parsed from note content:
special_populations? (Optional, array, Relevant populations, e.g., 'pregnancy', 'elderly'): string
variability? (Optional, array, Sources of variation with explanations, e.g., 'pharmacogenetics (2D6 polymorphism leads to rapid metabolism of tramadol)', 'age (closing capacity decreases by 5% per decade after 40 years of age)': string
physicochemical_considerations? (Optional, array, Physicochemical integration e.g. 'ion-channel gating', 'drug-receptor interaction'): string
measurement_considerations? (Optional, array, Measurement integration e.g. 'blood pressure', 'pulse oximetry'): string
physiology_considerations? (Optional, array, Physiological integration e.g. 'cardiorenal', 'hepatopulmonary', 'neurogastric'): string
pharmacokinetics_considerations? (Optional, array, Pharmacokinetic integration e.g. 'absorption', 'distribution'): string
pharmacodynamics_considerations? (Optional, array, Pharmacodynamic integration e.g. 'antibacterial', 'antiviral'): string
---
