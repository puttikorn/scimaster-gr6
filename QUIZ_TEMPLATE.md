# Knowledge Assessment Quiz: [Subject] Grade 6 (Midterm/Final Exam Suite)

<!--
╔══════════════════════════════════════════════════════════════════════╗
║  QUIZ TEMPLATE — SciMaster Gr.6 Platform                           ║
║  HOW TO USE: Replace placeholders in [square brackets] with actual   ║
║  content, then run: python3 parse_quiz.py to convert to JSON.        ║
╠══════════════════════════════════════════════════════════════════════╣
║  PRE-PARSE CHECKLIST                                                 ║
║  [ ] Replace [Subject] everywhere (e.g., English, Science, Math)      ║
║  [ ] Replace [XX] with Subject Code (e.g., ENG, SCI, MATH)            ║
║  [ ] Fill in Document Summary                                        ║
║  [ ] Fill in Learning Objectives                                     ║
║  [ ] Section A: Exactly 60 questions (Q1–Q60)                        ║
║  [ ] Section B: Exactly 30 questions (Q61–Q90)                       ║
║  [ ] Section C: Exactly 15 questions (Q91–Q105)                      ║
║  [ ] Section D: Exactly 10 questions (Q106–Q115)                     ║
║  [ ] MCQ options use "* A." with no leading space                    ║
╚══════════════════════════════════════════════════════════════════════╝
-->

---

## Document Summary ([Subject] Grade 6 Assessment Overview)

This document contains the complete curriculum summary and assessment items for [Subject] Grade 6, covering [N] main learning units:

### 1. Learning Unit N: [Unit Title 1]
* **[Subtopic 1]**: [Brief summary/description]
* **[Subtopic 2]**: [Brief summary/description]

### 2. Learning Unit N+1: [Unit Title 2]
* **[Subtopic 1]**: [Brief summary/description]
* **[Subtopic 2]**: [Brief summary/description]

---

## Learning Objectives Mapping

* **LO-[XX]1**: [Objective 1 — Remember / Understand Level]
* **LO-[XX]2**: [Objective 2 — Apply Level]
* **LO-[XX]3**: [Objective 3 — Analyze Level]
* **LO-[XX]4**: [Objective 4 — Evaluate / Create Level]

---

## Total Score Summary

| Section | Questions | Points/Question | Total Points |
|---------|-----------|-----------------|--------------|
| A: Multiple Choice (MCQ) | 60 | 1 | 60 |
| B: True / False (TF) | 30 | 1 | 30 |
| C: Scenario-Based | 15 | 2 | 30 |
| D: Short Answer | 10 | 3 | 30 |
| **Total** | **115** | — | **150** |
| **Passing Criteria (80%)** | — | — | **120** |

---

# Section A: Multiple Choice Questions (60 Questions)

<!--
RULES Section A:
- Q1–Q60 (60 Questions, 1 Point/Question)
- Options: "* A." must have no leading space (parser sensitive!)
- Answer: A | B | C | D only
- Difficulty Ratio: Easy ~30% / Medium ~50% / Hard ~20%
- LO Distribution: Balanced coverage across all LOs
-->

#### ข้อ 1
* **Topic**: [Topic / Lesson Title]
* **Learning Objective**: LO-[XX]1
* **Difficulty**: Easy
* **Prompt**: [Remember / Understand level question]
* A. [Option A]
* B. [Option B — ✓ Correct Answer]
* C. [Option C]
* D. [Option D]
* **Correct Answer**: B
* **Explanation**: [Explain why B is correct and A, C, D are incorrect]

#### ข้อ 2
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]1
* **Difficulty**: Easy
* **Prompt**: [Question]
* A. [Option A]
* B. [Option B]
* C. [Option C — ✓]
* D. [Option D]
* **Correct Answer**: C
* **Explanation**: [Explanation]

#### ข้อ 3
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]2
* **Difficulty**: Medium
* **Prompt**: [Application level question]
* A. [Option A — ✓]
* B. [Option B]
* C. [Option C]
* D. [Option D]
* **Correct Answer**: A
* **Explanation**: [Explanation]

<!-- ★ COPY Q4–Q60 HERE (Duplicate #### ข้อ N block and change the number) -->
<!-- Q1–Q20   → Mainly LO-[XX]1 (Easy) -->
<!-- Q21–Q50  → LO-[XX]2, LO-[XX]3 (Medium) -->
<!-- Q51–Q60  → LO-[XX]3, LO-[XX]4 (Hard) -->

---

# Section B: True / False Questions (30 Questions)

<!--
RULES Section B:
- Q61–Q90 (30 Questions, 1 Point/Question)
- Field: "* **Statement**:" or "* **Prompt**:"
- Answer: True or False (Capitalized)
- Enclose statement in double quotes " "
- True ~15 items / False ~15 items
-->

#### ข้อ 61
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]1
* **Difficulty**: Easy
* **Statement**: "[Correct Statement]"
* **Answer**: True
* **Explanation**: [Explain why this statement is true]

#### ข้อ 62
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]2
* **Difficulty**: Easy
* **Statement**: "[False Statement]"
* **Answer**: False
* **Explanation**: [Explain why it is false and what the correct statement should be]

#### ข้อ 63
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]2
* **Difficulty**: Medium
* **Statement**: "[Statement requiring analysis before deciding]"
* **Answer**: True
* **Explanation**: [Explanation]

<!-- ★ COPY Q64–Q90 HERE -->

---

# Section C: Scenario-Based Questions (15 Questions)

<!--
RULES Section C:
- Q91–Q105 (15 Questions, 2 Points/Question)
- MUST contain "* **Scenario**:" — parser uses this field to render blue highlight box in UI
- Use "* **Question**:"
- Use "* **Answer**:" for expected model answer
- JS Grading Heuristic: >15 chars → 2pt, >0 chars → 1pt
-->

#### ข้อ 91
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]3
* **Difficulty**: Hard
* **Scenario**: [2-4 sentences scenario context e.g., "Student named... wants to... given that... Please help..."]
* **Question**: [Explanatory / Analytical question]
* **Answer**: [Expected model answer explaining core principles and reasoning]
* **Explanation**: [Additional explanation for learners]

#### ข้อ 92
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]3
* **Difficulty**: Hard
* **Scenario**: [Scenario Context]
* **Question**: [Question]
* **Answer**: [Expected Answer]
* **Explanation**: [Explanation]

#### ข้อ 93
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]4
* **Difficulty**: Hard
* **Scenario**: [Scenario Context]
* **Question**: [Question]
* **Answer**: [Expected Answer]
* **Explanation**: [Explanation]

<!-- ★ COPY Q94–Q105 HERE -->

---

# Section D: Short Answer Questions (10 Questions)

<!--
RULES Section D:
- Q106–Q115 (10 Questions, 3 Points/Question)
- Use "* **Prompt**:" or "* **Question**:"
- MUST contain "* **Expected Answer**:" — parser uses this field
- Do NOT use "* **Answer**:" (unlike Section C)
- JS Grading Heuristic: >20 chars → 3pt, >0 chars → 1pt
- Open-ended question requiring 3-5 sentences answer
-->

#### ข้อ 106
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]3
* **Difficulty**: Hard
* **Prompt**: [Open-ended question — Explain / Compare / Exemplify / Analyze]
* **Expected Answer**: [Expected key points e.g., "(1) Student should state that... (2) Provide examples of... (3) Explain the rationale..."]

#### ข้อ 107
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]4
* **Difficulty**: Hard
* **Prompt**: [Open-ended question]
* **Expected Answer**: [Expected Answer]

#### ข้อ 108
* **Topic**: [Topic Title]
* **Learning Objective**: LO-[XX]4
* **Difficulty**: Hard
* **Prompt**: [Open-ended question]
* **Expected Answer**: [Expected Answer]

<!-- ★ COPY Q109–Q115 HERE -->
<!-- Section D should cover all high-level LOs -->
<!-- Every item MUST have "Expected Answer", otherwise parser will skip the item -->
