---
description: A unified ontology schema with explicit granularity hierarchy (subatomic, atomic, alloy, molecular, macromolecular), nested tags, single-word directional relations with separate magnitude properties, explicit meta-schemas, assumption taxonomies, consistent file naming, and properties for significance, difficulty, queries, special populations, and variability. Includes a logical parsing prompt for examiner comments and a sophisticated system prompt to navigate, generate, and optimise a rich, small-world biomedical knowledge graph with a ~1:5 atomic to composite ratio.
prompt: generate a rich, precise, scalable, small-world network knowledge graph optimised for exam mastery and beyond, utilising a sophisticated system prompt for navigation, facilitation, generation, and optimisation of logical parsing of examiner comments of past short answer questions and learning objective structure - maintaining a ~1:5 atomic/subatomic to composite granularity-dependancy ratio, leveraging nested tags for multiple concurrent hierarchal schemas taxonomies or ontologies, with consistent file naming, single-word, weighted-vectorised relationships
facilitate:
  - recursive parsing of examiner comments and exam content
  - decomposition of composite concepts into atomic/subatomic units
  - link prediction to suggest new relations based on meta-schemas and magnitudes
  - synthesis of atomic concepts into composite frameworks
navigate:
  - traversing meta-schema relations (cause, hypernym, antonym, etc.)
  - using magnitude properties to prioritise or filter links
extract:
- atomic and composite concepts
- relations (cause, hypernym, hyponym, antonym, meronym, preceeds, proceeds, tests, covers, assumptions)
- magnitudes for relations (numeric or quantized)
- properties (significance, difficulty, queries, special_populations, variability, unit, symbol, formula, range, dimension)
- exam metadata (pass_rate, examiner_comments, exam_code, exam_type, exam_year, exam_sitting, exam_number)
generate:
  - new atomic concepts when gaps are found
  - composite concepts by integrating atomic units
  - queries for each concept to guide learning and retrieval
  - assumption taxonomies for models
  - diagram encodings (Mermaid, Canvas JSON)
optimise:
  - eliminate redundancies
  - enforce meta-schema consistency
  - balance granularity for small-world richness
  - encode exam metadata precisely for grounding
support:
  - multi-layer path traversal for depth and breadth search reasoning
  - contextual retrieval
  - adaptive learning pathways
  - automated curriculum mapping
output:
  - structured YAML front-matter with clear types and constraints that respect all other criteria and enable a rich, scalable, and deeply interconnected biomedical knowledge graph
  - maintain a ratio of ~1 atomic to 5 composite concepts in order to ensure dense interlinking and emergent small-world properties
---

## 1. ID
LOs: [College].[Section].[Subsection].[LO_Number]_[Semantic_Summary]
SAQs: [College].[ExamType].[Year].[Sitting].[QuestionNumber]_[Semantic_Summary]

## 2. Properties
```yaml
aliases: "CP22A01", "ANZCA.2.2.1", "BT_GS.1.7", ...
granularity: "composite", "atomic"
significance: "critical", "core", "advanced", "frontier"
unit: "L/min", "mmHg", ...
symbol: "Vd", "Cl", ...
formula: "$CO = HR x SV$", ...
range: "70-100 mmHg", ...
dimension: "Pressure", "Volume", ...
difficulty: "basic", "intermediate", "advanced"
pass_rate: 0.62
examiner_comments: "Candidates often omitted hepatic extraction ratio...", ...
queries: "List of succinct questions this concept informs", ...
special_populations: "pregnancy", "elderly", "renal_failure", ...
variability: "pharmacogenetics", "disease_state", "age", ...
```

## 3. Tags
#LO/ANZCA/Section2/Subsection2/LO1
#SAQ/CICM/2022/A/01
#Entity/Drug/Opioid
#Model/PK/OneCompartment
#Assumption/SteadyState
#Atomic
#Subatomic
#Composite/Alloy
#Composite/Molecular
#Composite/Macromolecular

## 4. Relations
```yaml
cause: [[Flow]]
hypernym: [[Drug]]
hyponym: [[Opioid]]
antonym: [[Antagonist]]
preceeds: [[Absorption]]
proceeds: [[Distribution]]
part: [[Alveolus]]
whole: [[Lung]]
tests: [[LO_2.2.1]]
covers: [[Volume_of_Distribution]]
assumptions:
- [[Steady_State]]
- [[Linear_Kinetics]]
```

## 5. Magnitudes
```yaml
causeEffect: -0.2
hypernymStrength: 1
antonymStrength: 0.8
preceedsLag: 0.1
proceedsLag: 0.1
partProportion: 0.05
```