import os

file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_Grammar_Gr6.md"
alt_file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_Grammar__Gr6.md"

header = """# Knowledge Assessment Quiz: English Grammar Grade 6 (Midterm & Final Assessment)

---

## Document Summary (English Grammar Grade 6 Curriculum & Assessment Summary)

This assessment document compiles comprehensive learning content and evaluation questions for English Grammar Grade 6, covering 5 core units:

### 1. Unit 1: Tenses & Subject-Verb Agreement
* **Tenses**: Present Simple, Present Continuous, Past Simple (Regular & Irregular verbs), Future Simple (will / be going to), and Present Perfect
* **Subject-Verb Agreement**: Rules for singular and plural subjects, compound subjects, expressions of quantity, indefinites (every, each, everyone, nobody), and 'neither...nor / either...or'

### 2. Unit 2: Parts of Speech (Nouns, Pronouns, Adjectives & Adverbs)
* **Nouns**: Countable vs Uncountable nouns, regular and irregular plural nouns, collective nouns, possessive nouns
* **Pronouns**: Subject, Object, Possessive Adjectives, Possessive Pronouns, Reflexive Pronouns, Relative Pronouns (who, which, that, where, whose)
* **Adjectives & Adverbs**: Modifiers, adverbs of manner/time/frequency/place, Comparative and Superlative degrees

### 3. Unit 3: Prepositions, Articles, Quantifiers & Conjunctions
* **Prepositions**: Prepositions of time (in, on, at, for, since, during) and place/direction (in, on, at, under, behind, next to, between, opposite)
* **Articles & Quantifiers**: Definite (the) and Indefinite (a, an) articles, zero article, Quantifiers (some, any, much, many, a few, a little, a lot of)
* **Conjunctions**: Coordinating (and, but, or, so) and Subordinating (because, although, if, when, while) conjunctions

### 4. Unit 4: Question Formation, Modals & Passive Voice
* **Questions & Tags**: Wh-questions, Yes/No auxiliary questions, Question Tags (positive/negative balance)
* **Modal Verbs**: Ability (can, could), Obligation & Prohibition (must, mustn't, have to), Advice (should, shouldn't), Permission & Possibility (may, might)
* **Passive Voice**: Active vs Passive Voice transformation in Present Simple and Past Simple (is/am/are/was/were + V.3)

### 5. Unit 5: Conditionals, Punctuation & Error Analysis
* **Conditionals**: Zero Conditional (general truths) and First Conditional (real future possibilities: If + Present Simple, Will + V.1)
* **Punctuation & Capitalization**: Commas, apostrophes (possession vs contraction), quotation marks, capital letters
* **Grammar Error Correction**: Identifying and fixing double negatives, subject-verb mismatches, misplaced modifiers, and commonly confused words (there/their/they're, your/you're, its/it's)

---

## Learning Objectives Mapping

* **LO-GRAM1**: Identification of parts of speech, tense structures, article rules, and punctuation marks (Remember / Understand)
* **LO-GRAM2**: Application of correct verb forms, subject-verb agreement, modal verbs, and prepositions (Apply)
* **LO-GRAM3**: Sentence structure analysis, active-to-passive conversion, question tag construction, and error detection (Analyze)
* **LO-GRAM4**: Sentence synthesis, editing and proofreading complex passages, conditional reasoning, and advanced grammar evaluation (Evaluate / Create)

---

## Total Score Summary

| Section | Questions | Points/Q | Total Points |
|---------|-----------|----------|--------------|
| A: Multiple Choice (MCQ) | 60 | 1 | 60 |
| B: True / False (TF) | 30 | 1 | 30 |
| C: Scenario-Based | 15 | 2 | 30 |
| D: Short Answer | 10 | 3 | 30 |
| **Total** | **115** | — | **150** |
| **Passing Score (80%)** | — | — | **120** |

---

# Section A: Multiple Choice Questions (4 Options)
"""

mcq_questions = [
    # 1-15: Tenses & Subject-Verb Agreement
    (1, "Tenses (Present Simple)", "LO-GRAM1", "Easy",
     "The Earth ________ around the Sun.",
     "revolve", "revolves", "revolved", "is revolving", "ข",
     "General scientific facts take Present Simple Tense with singular subject Earth -> revolves."),

    (2, "Tenses (Present Continuous)", "LO-GRAM1", "Easy",
     "Listen! Someone ________ on the front door.",
     "knock", "knocks", "is knocking", "knocked", "ค",
     "The signal word 'Listen!' indicates an action happening now -> Present Continuous (is knocking)."),

    (3, "Tenses (Past Simple)", "LO-GRAM2", "Medium",
     "She ________ her keys in the car yesterday afternoon.",
     "leave", "leaves", "left", "has left", "ค",
     "Past Simple signal word 'yesterday' requires V.2 of leave -> left."),

    (4, "Tenses (Future)", "LO-GRAM2", "Medium",
     "Look at those dark clouds! It ________ rain soon.",
     "will", "is going to", "rains", "is raining", "ข",
     "Predictions based on present evidence (dark clouds) use 'be going to' -> is going to."),

    (5, "Tenses (Present Perfect)", "LO-GRAM2", "Medium",
     "I ________ lived in Bangkok for five years.",
     "have", "has", "am", "was", "ก",
     "Present Perfect tense with Subject 'I' uses have + V.3 -> have lived."),

    (6, "Subject-Verb Agreement", "LO-GRAM2", "Medium",
     "Either Tom or his brothers ________ responsible for locking the gate.",
     "is", "are", "was", "be", "ข",
     "With 'either...or', the verb agrees with the closest subject 'his brothers' (plural) -> are."),

    (7, "Subject-Verb Agreement", "LO-GRAM2", "Medium",
     "Neither of the two books ________ interesting.",
     "is", "are", "were", "be", "ก",
     "'Neither of + plural noun' takes a singular verb -> is."),

    (8, "Subject-Verb Agreement", "LO-GRAM2", "Medium",
     "Bread and butter ________ my favorite breakfast.",
     "is", "are", "were", "being", "ก",
     "Bread and butter considered as a single compound meal takes a singular verb -> is."),

    (9, "Subject-Verb Agreement", "LO-GRAM2", "Medium",
     "Every boy and girl in the class ________ a textbook.",
     "have", "has", "having", "are having", "ข",
     "Subject modified by 'Every' takes a singular verb -> has."),

    (10, "Subject-Verb Agreement", "LO-GRAM3", "Hard",
     "A number of students ________ absent today, but the number of absent students ________ decreasing.",
     "is, is", "are, is", "is, are", "are, are", "ข",
     "'A number of' takes plural verb (are); 'The number of' takes singular verb (is)."),

    # 11-25: Parts of Speech (Nouns, Pronouns, Modifiers)
    (11, "Nouns (Plurals)", "LO-GRAM1", "Easy",
     "Choose the correct plural form of the word 'hypothesis'.",
     "hypothesises", "hypothesiss", "hypotheses", "hypothesi", "ค",
     "Nouns ending in -is change to -es in plural -> hypotheses."),

    (12, "Nouns (Uncountable)", "LO-GRAM1", "Easy",
     "Which of the following is an UNCOUNTABLE noun?",
     "Furniture", "Chair", "Table", "Desk", "ก",
     "Furniture is an uncountable category noun."),

    (13, "Pronouns (Reflexive)", "LO-GRAM2", "Medium",
     "The little boy fell down and hurt ________.",
     "him", "his", "himself", "he", "ค",
     "When subject and object are the same person, use reflexive pronoun -> himself."),

    (14, "Pronouns (Relative)", "LO-GRAM2", "Medium",
     "The girl ________ wallet was stolen called the police.",
     "who", "whom", "whose", "which", "ค",
     "Possessive relative pronoun referring to the girl's wallet -> whose."),

    (15, "Pronouns (Relative)", "LO-GRAM2", "Medium",
     "This is the university ________ my father studied engineering.",
     "which", "where", "that", "when", "ข",
     "Relative pronoun referring to a place where an action occurred -> where."),

    (16, "Adjectives & Adverbs", "LO-GRAM2", "Medium",
     "He speaks English very ________ because he practiced hard.",
     "fluent", "fluently", "more fluent", "fluency", "ข",
     "An adverb (fluently) modifies the verb speaks."),

    (17, "Comparatives", "LO-GRAM2", "Medium",
     "This puzzle is much ________ than the previous one.",
     "easy", "easier", "more easy", "easiest", "ข",
     "Two-syllable adjective ending in -y changes to -ier in comparative -> easier."),

    (18, "Superlatives", "LO-GRAM2", "Medium",
     "She is ________ student in our entire school.",
     "intelligent", "more intelligent", "the most intelligent", "most intelligent", "ค",
     "Superlative degree requires 'the most intelligent'."),

    (19, "Adverbs of Frequency", "LO-GRAM1", "Easy",
     "Where should the adverb 'always' be placed in this sentence: 'She (1) is (2) punctual (3) for work (4)'?",
     "Position (1)", "Position (2)", "Position (3)", "Position (4)", "ข",
     "Adverbs of frequency go AFTER verb 'to be' (is always punctual)."),

    (20, "Possessive Nouns", "LO-GRAM1", "Easy",
     "Which phrase shows correct possessive punctuation for plural boys?",
     "The boy's toys", "The boys' toys", "The boyses toys", "The boies' toys", "ข",
     "Plural regular nouns ending in -s take apostrophe after s -> boys'."),

    # 26-40: Prepositions, Articles & Conjunctions
    (21, "Prepositions of Time", "LO-GRAM1", "Easy",
     "We have been studying English ________ 2021.",
     "for", "since", "in", "during", "ข",
     "'since' is used with a specific starting point in time (2021)."),

    (22, "Prepositions of Time", "LO-GRAM1", "Easy",
     "They lived in London ________ three years.",
     "since", "for", "during", "at", "ข",
     "'for' is used with a duration/period of time (three years)."),

    (23, "Prepositions of Place", "LO-GRAM1", "Easy",
     "The cat is sleeping ________ the rug in front of the fireplace.",
     "in", "on", "at", "to", "ข",
     "Surfaces take preposition 'on' -> on the rug."),

    (24, "Articles", "LO-GRAM2", "Medium",
     "He is ________ honest man who always tells ________ truth.",
     "a, the", "an, the", "a, a", "an, a", "ข",
     "'honest' has silent 'h' (starts with vowel sound -> an); 'the truth' is a fixed idiom."),

    (25, "Articles (Zero Article)", "LO-GRAM2", "Medium",
     "________ Lead is a heavy metal.",
     "A", "An", "The", "No article (-)", "ง",
     "Uncountable nouns used in a general sense take no article."),

    (26, "Quantifiers", "LO-GRAM2", "Medium",
     "There are ________ books on the shelf, but not many.",
     "a little", "a few", "much", "any", "ข",
     "Countable plural nouns (books) in small quantity take 'a few'."),

    (27, "Quantifiers", "LO-GRAM2", "Medium",
     "Could you please add ________ sugar to my coffee?",
     "a few", "a little", "many", "few", "ข",
     "Uncountable nouns (sugar) in small quantity take 'a little'."),

    (28, "Conjunctions", "LO-GRAM2", "Medium",
     "________ it was raining heavily, we went out for a walk.",
     "Because", "Although", "So", "However", "ข",
     "Subordinating conjunction showing concession/contrast -> Although."),

    (29, "Conjunctions", "LO-GRAM2", "Medium",
     "Study hard, ________ you will fail the final examination.",
     "and", "but", "or", "so", "ค",
     "Conjunction 'or' expresses negative alternative outcome."),

    (30, "Conjunctions", "LO-GRAM3", "Hard",
     "Not only did he pass the exam, ________ he also won first prize.",
     "but", "and", "so", "or", "ก",
     "Correlative conjunction pair: 'Not only... but also'."),

    # 31-45: Questions, Modals & Passive Voice
    (31, "Question Tags", "LO-GRAM3", "Hard",
     "You haven't finished your homework yet, ________?",
     "have you", "haven't you", "do you", "don't you", "ก",
     "Negative main clause (haven't) takes positive tag -> have you?"),

    (32, "Question Tags", "LO-GRAM3", "Hard",
     "Let's go for a walk in the park, ________?",
     "will we", "shall we", "don't we", "aren't we", "ข",
     "Suggestions with 'Let's' take question tag 'shall we?'."),

    (33, "Question Tags", "LO-GRAM3", "Hard",
     "Nobody called while I was out, ________?",
     "did they", "didn't they", "did he", "didn't he", "ก",
     "'Nobody' makes clause negative and takes pronoun 'they' -> positive tag 'did they?'."),

    (34, "Modal Verbs (Prohibition)", "LO-GRAM2", "Easy",
     "You ________ smoke in the hospital. It is strictly prohibited.",
     "don't have to", "mustn't", "shouldn't", "needn't", "ข",
     "Strict legal prohibition uses 'mustn't'."),

    (35, "Modal Verbs (Lack of Obligation)", "LO-GRAM2", "Medium",
     "Tomorrow is Sunday. I ________ get up early.",
     "mustn't", "don't have to", "shouldn't", "can't", "ข",
     "Absence of necessity/obligation uses 'don't have to'."),

    (36, "Modal Verbs (Deduction)", "LO-GRAM3", "Hard",
     "He has been working all day without rest. He ________ be exhausted.",
     "must", "can't", "should", "might not", "ก",
     "Strong positive logical deduction uses 'must'."),

    (37, "Passive Voice (Present Simple)", "LO-GRAM3", "Hard",
     "English ________ in many countries around the world.",
     "speaks", "is spoken", "is speaking", "was spoken", "ข",
     "Present Simple passive: is + V.3 (is spoken)."),

    (38, "Passive Voice (Past Simple)", "LO-GRAM3", "Hard",
     "The telephone ________ by Alexander Graham Bell in 1876.",
     "invented", "was invented", "is invented", "were invented", "ข",
     "Past Simple passive singular object: was + V.3 (was invented)."),

    (39, "Active to Passive Conversion", "LO-GRAM3", "Hard",
     "Active: 'The chef prepares dinner.' -> Passive: 'Dinner ________ by the chef.'",
     "is prepared", "was prepared", "has prepared", "is preparing", "ก",
     "Present Simple active 'prepares' converts to passive 'is prepared'."),

    (40, "Active to Passive Conversion", "LO-GRAM3", "Hard",
     "Active: 'Somebody stole my bicycle.' -> Passive: 'My bicycle ________.'",
     "is stolen", "was stolen", "stole", "has stolen", "ข",
     "Past Simple active 'stole' converts to passive 'was stolen'."),

    # 41-60: Conditionals, Punctuation & Error Analysis
    (41, "Conditionals (Zero)", "LO-GRAM2", "Medium",
     "If you heat ice, it ________.",
     "melt", "melts", "will melt", "melted", "ข",
     "Zero conditional for general scientific facts: If + Present Simple, Present Simple -> melts."),

    (42, "Conditionals (First)", "LO-GRAM2", "Medium",
     "If she ________ hard, she will pass the exam.",
     "study", "studies", "studied", "will study", "ข",
     "First conditional: If + Present Simple (studies), Will + V.1."),

    (43, "Conditionals (First)", "LO-GRAM3", "Hard",
     "Unless you ________ now, you will miss the train.",
     "leave", "don't leave", "will leave", "left", "ก",
     "'Unless' means 'If... not', so it takes a positive verb form -> leave."),

    (44, "Punctuation (Commas)", "LO-GRAM1", "Easy",
     "Which sentence uses commas correctly in a list?",
     "I bought apples oranges and bananas.", "I bought apples, oranges, and bananas.", "I bought, apples, oranges, and bananas.", "I bought apples oranges, and bananas.", "ข",
     "Items in a list are separated by commas (Oxford comma before 'and')."),

    (45, "Punctuation (Apostrophes)", "LO-GRAM2", "Medium",
     "Choose the sentence with correct apostrophe usage for contractions.",
     "Its raining outside, so dont forget your umbrella.", "It's raining outside, so don't forget your umbrella.", "Its' raining outside, so dont' forget your umbrella.", "It'is raining outside, so do'nt forget your umbrella.", "ข",
     "It's = It is; don't = do not."),

    (46, "Confusing Words (its vs it's)", "LO-GRAM2", "Medium",
     "The cat licked ________ paws after eating ________ food.",
     "it's, it's", "its, its", "its, it's", "it's, its", "ข",
     "Possessive adjective is 'its' (without apostrophe)."),

    (47, "Confusing Words (there/their/they're)", "LO-GRAM2", "Medium",
     "________ going to visit ________ grandparents over ________.",
     "They're, their, there", "There, their, they're", "Their, they're, there", "They're, there, their", "ก",
     "They're = They are; their = possessive; there = location."),

    (48, "Confusing Words (your vs you're)", "LO-GRAM2", "Medium",
     "If ________ ready, we can start ________ exam now.",
     "your, your", "you're, your", "your, you're", "you're, you're", "ข",
     "you're = you are; your = possessive adjective."),

    (49, "Error Detection", "LO-GRAM3", "Hard",
     "Identify the grammatically INCORRECT part: 'She don't (A) like (B) playing (C) tennis (D).'",
     "don't (A)", "like (B)", "playing (C)", "tennis (D)", "ก",
     "Singular subject 'She' requires 'doesn't', not 'don't'."),

    (50, "Error Detection", "LO-GRAM3", "Hard",
     "Identify the grammatically INCORRECT part: 'One of my friend (A) is (B) coming (C) today (D).'",
     "friend (A)", "is (B)", "coming (C)", "today (D)", "ก",
     "'One of + plural noun' requires 'friends', not 'friend'."),

    (51, "Double Negatives", "LO-GRAM3", "Hard",
     "Which sentence correctly avoids a double negative?",
     "I don't know nothing about it.", "I don't know anything about it.", "I can't see no one.", "She didn't say nothing.", "ข",
     "Standard English avoids double negatives: 'I don't know anything'."),

    (52, "Direct vs Indirect Speech", "LO-GRAM3", "Hard",
     "Direct: He said, 'I am busy.' -> Indirect: He said that he ________ busy.",
     "is", "was", "has been", "had been", "ข",
     "Present Simple 'am' backshifts to Past Simple 'was' in indirect speech."),

    (53, "Direct vs Indirect Speech", "LO-GRAM3", "Hard",
     "Direct: 'Where do you live?' she asked. -> Indirect: She asked me where I ________.",
     "live", "lived", "do live", "did live", "ข",
     "Indirect questions use statement word order and backshift tense -> where I lived."),

    (54, "Gerunds vs Infinitives", "LO-GRAM2", "Medium",
     "She enjoys ________ fantasy novels in her free time.",
     "to read", "reading", "read", "reads", "ข",
     "The verb 'enjoy' is followed by a gerund (-ing form) -> reading."),

    (55, "Gerunds vs Infinitives", "LO-GRAM2", "Medium",
     "He decided ________ a new laptop for university.",
     "buying", "to buy", "buy", "bought", "ข",
     "The verb 'decide' is followed by an infinitive (to + V.1) -> to buy."),

    (56, "Used to + V.1", "LO-GRAM2", "Medium",
     "When I was a child, I ________ live in a small village.",
     "used to", "was used to", "use to", "am used to", "ก",
     "Past habits/states no longer true take 'used to + V.1'."),

    (57, "Sentence Parallelism", "LO-GRAM3", "Hard",
     "Choose the sentence with correct parallel structure.",
     "He likes swimming, running, and to bike.", "He likes swimming, running, and biking.", "He likes to swim, running, and biking.", "He likes swim, run, and bike.", "ข",
     "Parallel structure keeps matching grammatical forms (-ing, -ing, -ing)."),

    (58, "Capitalization Rules", "LO-GRAM1", "Easy",
     "Which word in the sentence requires capitalization: 'we will visit uncle sam in london next tuesday.'?",
     "Only London", "London and Tuesday", "We, Sam, London, and Tuesday", "All words", "ค",
     "Capitalize sentence start (We), proper names (Sam, London), and days (Tuesday)."),

    (59, "Causative Verbs", "LO-GRAM3", "Hard",
     "My mother made me ________ my bedroom before going out.",
     "clean", "to clean", "cleaning", "cleaned", "ก",
     "Causative verb 'make someone + bare infinitive' (clean)."),

    (60, "Conditionals (Wish/Hypothetical)", "LO-GRAM3", "Hard",
     "I wish I ________ more time to travel the world.",
     "have", "had", "will have", "am having", "ข",
     "Present wishes take Past Simple form -> had.")
]

tf_questions = [
    # 61-90 True/False
    (61, "Tenses", "LO-GRAM1", "Easy",
     "The Present Continuous Tense is used for habitual actions and general truths.",
     "False", "Incorrect. Present Simple is used for habits/truths; Present Continuous is for actions happening now."),

    (62, "Subject-Verb Agreement", "LO-GRAM1", "Easy",
     "Plural subjects require plural verbs (e.g., The dogs bark).",
     "True", "Correct. Subject-verb agreement requires matching numbers."),

    (63, "Nouns", "LO-GRAM1", "Easy",
     "The plural of 'mouse' is 'mouses'.",
     "False", "Incorrect. The irregular plural of mouse is 'mice'."),

    (64, "Nouns", "LO-GRAM1", "Easy",
     "Information, advice, and news are all uncountable nouns in English.",
     "True", "Correct. Information, advice, and news take singular verbs and cannot be pluralized with -s."),

    (65, "Pronouns", "LO-GRAM1", "Easy",
     "Reflexive pronouns end in '-self' (singular) or '-selves' (plural).",
     "True", "Correct. E.g., himself, themselves."),

    (66, "Adjectives & Adverbs", "LO-GRAM2", "Medium",
     "Adverbs modify verbs, adjectives, or other adverbs.",
     "True", "Correct. Definition of adverb functions."),

    (67, "Adjectives & Adverbs", "LO-GRAM1", "Easy",
     "The adverb form of 'good' is 'goodly'.",
     "False", "Incorrect. The adverb form of good is 'well'."),

    (68, "Prepositions", "LO-GRAM1", "Easy",
     "We use 'in' for specific times on the clock, e.g., 'in 5 o'clock'.",
     "False", "Incorrect. Specific clock times take 'at' (at 5 o'clock)."),

    (69, "Prepositions", "LO-GRAM1", "Easy",
     "We use 'on' for days of the week and specific dates (e.g., on Friday, on May 1st).",
     "True", "Correct. Days and dates take preposition 'on'."),

    (70, "Articles", "LO-GRAM1", "Easy",
     "We use 'an' before words that start with a consonant sound.",
     "False", "Incorrect. We use 'an' before VOWEL sounds (a, e, i, o, u)."),

    (71, "Articles", "LO-GRAM2", "Medium",
     "The definite article 'the' is used when referring to a specific noun known to the listener.",
     "True", "Correct. 'The' specifies known/unique items."),

    (72, "Quantifiers", "LO-GRAM2", "Medium",
     "We use 'many' with uncountable nouns in negative sentences.",
     "False", "Incorrect. We use 'much' with uncountable nouns (much water); 'many' is for countable nouns."),

    (73, "Conjunctions", "LO-GRAM1", "Easy",
     "The conjunction 'because' shows cause and reason.",
     "True", "Correct. 'Because' introduces clauses of reason."),

    (74, "Question Tags", "LO-GRAM3", "Hard",
     "A positive statement takes a positive question tag.",
     "False", "Incorrect. A positive statement takes a NEGATIVE tag (She is smart, isn't she?)."),

    (75, "Modal Verbs", "LO-GRAM2", "Medium",
     "The modal verb 'can' can express both ability and permission.",
     "True", "Correct. 'Can' expresses ability (I can swim) and permission (Can I leave?)."),

    (76, "Passive Voice", "LO-GRAM3", "Hard",
     "In passive voice, the object of the active sentence becomes the subject of the passive sentence.",
     "True", "Correct. Object -> Subject shift is fundamental to passive voice."),

    (77, "Conditionals", "LO-GRAM2", "Medium",
     "First conditional sentences express imaginary or impossible situations in the past.",
     "False", "Incorrect. First conditional expresses real/possible future situations. Past impossible is Third conditional."),

    (78, "Punctuation", "LO-GRAM1", "Easy",
     "An apostrophe is used to show possession and contraction.",
     "True", "Correct. E.g., Tom's book (possession) and don't (contraction)."),

    (79, "Confusing Words", "LO-GRAM2", "Medium",
     "'Their' is a contraction for 'they are'.",
     "False", "Incorrect. 'Their' is possessive. 'They're' is the contraction for 'they are'."),

    (80, "Gerunds & Infinitives", "LO-GRAM2", "Medium",
     "A gerund is a verb form ending in -ing that functions as a noun.",
     "True", "Correct. E.g., Swimming is good exercise."),

    (81, "Double Negatives", "LO-GRAM3", "Hard",
     "In standard English, using two negative words in the same clause is correct.",
     "False", "Incorrect. Double negatives (e.g., I don't know nothing) are grammatically incorrect in standard English."),

    (82, "Comparative Adjectives", "LO-GRAM2", "Medium",
     "The comparative form of 'bad' is 'worse'.",
     "True", "Correct. Irregular comparative: bad -> worse -> worst."),

    (83, "Subject-Verb Agreement", "LO-GRAM2", "Medium",
     "Indefinite pronouns like 'someone', 'everybody', and 'nobody' take plural verbs.",
     "False", "Incorrect. Indefinite pronouns ending in -one, -body, -thing take SINGULAR verbs."),

    (84, "Relative Pronouns", "LO-GRAM2", "Medium",
     "'Whose' is used to replace possessive adjectives for both people and things.",
     "True", "Correct. 'Whose' indicates possession in relative clauses."),

    (85, "Tenses", "LO-GRAM2", "Medium",
     "The Past Continuous Tense is formed with 'was/were + V.-ing'.",
     "True", "Correct. Past Continuous = was/were + V.-ing."),

    (86, "Prepositions", "LO-GRAM1", "Easy",
     "We say 'in night' when referring to late evening hours.",
     "False", "Incorrect. Time phrase is 'at night'."),

    (87, "Conjunctions", "LO-GRAM2", "Medium",
     "'Although' and 'despite' have similar meanings, but 'despite' is followed by a noun phrase, not a clause.",
     "True", "Correct. Although + clause; Despite + noun/gerund."),

    (88, "Modals", "LO-GRAM2", "Medium",
     "'Should' is used to express strong legal prohibition.",
     "False", "Incorrect. 'Should' expresses advice. Legal prohibition requires 'mustn't'."),

    (89, "Direct/Indirect Speech", "LO-GRAM3", "Hard",
     "When converting direct speech to indirect speech, Present Simple usually changes to Past Simple.",
     "True", "Correct. Tense backshifting rule."),

    (90, "Active/Passive Voice", "LO-GRAM3", "Hard",
     "Intransitive verbs (verbs without an object, like 'sleep' or 'arrive') can easily be made passive.",
     "False", "Incorrect. Intransitive verbs cannot form passive voice because they have no direct object.")
]

sc_questions = [
    # 91-105 Scenario
    (91, "Tense Conversion Scenario", "LO-GRAM3", "Hard",
     "Convert the following Present Simple narrative into Past Simple Tense: 'Every day, Paul wakes up early, eats breakfast, and catches the school bus. He studies hard and plays football with friends.'",
     "Question: Rewrite the entire narrative in Past Simple Tense.",
     "Past Simple Narrative: 'Yesterday, Paul woke up early, ate breakfast, and caught the school bus. He studied hard and played football with friends.'",
     "Explanation: Irregular verbs (wake->woke, eat->ate, catch->caught) and regular verbs (study->studied, play->played) backshift to Past Simple V.2."),

    (92, "Subject-Verb Agreement Correction Scenario", "LO-GRAM3", "Hard",
     "A student wrote this paragraph containing 3 subject-verb agreement errors: 'The group of students are studying in the library. Neither John nor his sister have their book. Everyone in the class need to submit their assignment.' Identify and correct the 3 errors.",
     "Question: Identify the 3 agreement errors and provide corrections.",
     "Error 1: 'group... are' -> 'group... IS' (collective noun group is singular).\\nError 2: 'Neither... sister have' -> 'Neither... sister HAS' (agrees with singular sister).\\nError 3: 'Everyone... need' -> 'Everyone... NEEDS' (indefinite pronoun is singular).",
     "Explanation: Collective nouns, neither...nor (closer subject), and 'Everyone' take singular verbs."),

    (93, "Active to Passive Voice Transformation Scenario", "LO-GRAM3", "Hard",
     "Transform these 2 active sentences into passive voice: 1) 'The architect designed the modern library.' 2) 'Volunteers clean the local beach every weekend.'",
     "Question: Provide the correct passive voice conversions.",
     "1) Passive: 'The modern library was designed by the architect.'\\n2) Passive: 'The local beach is cleaned by volunteers every weekend.'",
     "Explanation: 1) Past Simple passive = was + V.3; 2) Present Simple passive = is + V.3."),

    (94, "Direct to Indirect Speech Conversion Scenario", "LO-GRAM3", "Hard",
     "Convert the direct dialogue into reported speech: Teacher said to Mark: 'Why are you late today, and did you finish your homework?'",
     "Question: Rewrite the teacher's questions as reported speech.",
     "Reported Speech: 'The teacher asked Mark why he was late that day and if he had finished his homework.'",
     "Explanation: 1) Wh-question keeps wh-word with statement order and past tense (why he was late); 2) Yes/No question takes 'if/whether' with Past Perfect (if he had finished)."),

    (95, "Question Tag Construction Scenario", "LO-GRAM3", "Hard",
     "Construct the correct question tags for these 3 statements: 1) 'She can speak three languages, _____?' 2) 'They didn't see the movie, _____?' 3) 'You're coming to the party, _____?'",
     "Question: Provide the 3 matching question tags.",
     "1) 'can't she?' (Positive statement -> negative tag)\\n2) 'did they?' (Negative statement -> positive tag)\\n3) 'aren't you?' (Positive statement -> negative tag)",
     "Explanation: Match auxiliary verb, reverse polarity (positive/negative), use pronoun."),

    (96, "Relative Pronoun Combining Scenario", "LO-GRAM3", "Hard",
     "Combine each pair of sentences into one complex sentence using relative pronouns (who, which, whose): 1) 'The woman called the police. Her car was stolen.' 2) 'I read the book. It was recommended by my teacher.'",
     "Question: Combine the sentence pairs using relative clauses.",
     "1) 'The woman whose car was stolen called the police.' (whose = possessive)\\n2) 'I read the book which/that was recommended by my teacher.' (which/that = object/thing)",
     "Explanation: Use 'whose' for possessive relationship and 'which/that' for things."),

    (97, "First Conditional Application Scenario", "LO-GRAM3", "Hard",
     "Create 2 First Conditional sentences based on these situations: 1) Rain tomorrow -> Stay home. 2) Finish homework early -> Play video games.",
     "Question: Write 2 First Conditional (If + Present Simple, Will + V.1) sentences.",
     "1) 'If it rains tomorrow, we will stay home.'\\n2) 'If I finish my homework early, I will play video games.'",
     "Explanation: First Conditional pattern: If-clause (Present Simple) + Main clause (will + V.1)."),

    (98, "Preposition Selection Scenario", "LO-GRAM3", "Hard",
     "Fill in the correct prepositions of time and place: 'My brother was born ___ (1) 8:30 a.m. ___ (2) July 12th ___ (3) 2012 ___ (4) a hospital ___ (5) Bangkok.'",
     "Question: Provide the 5 correct prepositions in order.",
     "(1) at (specific time 8:30 a.m.)\\n(2) on (specific date July 12th)\\n(3) in (year 2012)\\n(4) in / at (hospital)\\n(5) in (city Bangkok)",
     "Explanation: at time, on date, in year, in city."),

    (99, "Error Proofreading & Editing Scenario", "LO-GRAM4", "Hard",
     "Proofread the passage and fix 4 grammar errors: 'Yesterday, Mary go (1) to the market and buy (2) some apples. She didn't had (3) enough money, so she borrow (4) $5 from her friend.'",
     "Question: List the 4 incorrect words and their corrections.",
     "1) 'go' -> 'went' (Past Simple V.2)\\n2) 'buy' -> 'bought' (Past Simple V.2)\\n3) 'had' -> 'have' (After didn't, use bare infinitive have)\\n4) 'borrow' -> 'borrowed' (Past Simple V.2)",
     "Explanation: Past narrative consistency and auxiliary didn't + bare infinitive."),

    (100, "Modal Verb Advice & Obligation Scenario", "LO-GRAM4", "Hard",
     "Write 3 sentences for a school safety rules poster using: 1) 'must' (rule), 2) 'mustn't' (prohibition), 3) 'should' (advice).",
     "Question: Formulate 3 distinct modal sentences.",
     "1) Must: 'Students must wear school uniforms every day.'\\n2) Mustn't: 'Students mustn't run in the hallways.'\\n3) Should: 'Students should eat healthy food during lunchtime.'",
     "Explanation: Must = obligation; Mustn't = prohibition; Should = advice."),

    (101, "Article Usage Scenario", "LO-GRAM3", "Hard",
     "Fill in the correct articles (a, an, the, or - for zero article): '___ (1) Sun is ___ (2) star. It gives us ___ (3) light and ___ (4) heat. ___ (5) Earth revolves around it.'",
     "Question: Provide the 5 correct articles.",
     "(1) The (unique celestial body)\\n(2) a (singular countable noun starting with consonant sound)\\n(3) - (uncountable noun in general sense)\\n(4) - (uncountable noun in general sense)\\n(5) The (unique planet)",
     "Explanation: The Sun, a star, light (no article), heat (no article), The Earth."),

    (102, "Gerund vs Infinitive Scenario", "LO-GRAM3", "Hard",
     "Choose the correct verb form (gerund -ing or infinitive to + V.1) for each sentence: 1) 'I stopped (to smoke / smoking) two years ago.' (ceased habit) 2) 'He stopped (to buy / buying) a newspaper on his way home.' (paused action to do another)",
     "Question: Select and explain the correct verb forms for both sentences.",
     "1) 'smoking' (stop + gerund = quit/cease habit permanently)\\n2) 'to buy' (stop + infinitive = pause current activity in order to perform another action)",
     "Explanation: Stop + gerund = terminate action; Stop + infinitive = pause to do something else."),

    (103, "Adjective Order Scenario", "LO-GRAM4", "Hard",
     "Arrange the adjectives in correct order (OSASCOMP: Opinion, Size, Age, Shape, Color, Origin, Material, Purpose): 'a / wooden / beautiful / old / round / table'.",
     "Question: Write the adjectives in correct standard English order.",
     "Correct Order: 'a beautiful old round wooden table'\\n(Opinion: beautiful -> Age: old -> Shape: round -> Material: wooden).",
     "Explanation: Adjective order: Opinion -> Size -> Age -> Shape -> Color -> Origin -> Material."),

    (104, "Punctuation & Capitalization Editing Scenario", "LO-GRAM4", "Hard",
     "Edit and rewrite this sentence with correct punctuation and capitalization: 'on monday mr brown said we will travel to paris france'",
     "Question: Rewrite the sentence with proper capitalization, comma, and quotation marks.",
     "Correct Sentence: 'On Monday, Mr. Brown said, \"We will travel to Paris, France.\"'",
     "Explanation: Capitalize On, Monday, Mr., Brown, We, Paris, France. Add comma after Monday and said, period after Mr, quotation marks around direct quote."),

    (105, "Confusing Homophones & Contractions Scenario", "LO-GRAM4", "Hard",
     "Complete the story with their/there/they're and its/it's: '___ (1) standing over ___ (2) with ___ (3) dog. ___ (4) a cute puppy, and ___ (5) tail is wagging fast.'",
     "Question: Supply the 5 correct homophones/contractions in order.",
     "(1) They're (They are)\\n(2) there (location)\\n(3) their (possessive)\\n(4) It's (It is)\\n(5) its (possessive)",
     "Explanation: They're = They are; there = place; their = possessive; It's = It is; its = possessive.")
]

sa_questions = [
    # 106-115 Short Answer
    (106, "12 Tenses Overview & Formulas", "LO-GRAM1", "Medium",
     "State the formulas and provide 1 example sentence for: 1) Present Simple, 2) Present Continuous, 3) Past Simple, 4) Future Simple (will).",
     "1) Present Simple: Subject + V.1(s/es) -> She drinks tea.\\n2) Present Continuous: Subject + is/am/are + V.-ing -> She is drinking tea.\\n3) Past Simple: Subject + V.2 -> She drank tea.\\n4) Future Simple: Subject + will + V.1 -> She will drink tea."),

    (107, "Subject-Verb Agreement Rules Summary", "LO-GRAM2", "Medium",
     "State 3 key Subject-Verb Agreement rules involving: 1) Singular vs Plural subjects, 2) 'Neither... nor', 3) Indefinite pronouns (everyone/nobody).",
     "1) Singular subjects take singular verbs; plural subjects take plural verbs (The dog runs / The dogs run).\\n2) With 'Neither A nor B', the verb agrees with subject B closest to it (Neither John nor his friends ARE coming).\\n3) Indefinite pronouns (everyone, nobody, somebody) always take singular verbs (Everyone IS ready)."),

    (108, "Passive Voice Transformation Rules", "LO-GRAM3", "Hard",
     "Explain the 3 main steps to convert an active sentence into a passive sentence. Convert: 'The mechanic fixed the red car.'",
     "Steps:\\n1) Move the active object to become the passive subject ('The red car').\\n2) Add verb 'to be' matching the active tense + V.3 of active verb ('was fixed').\\n3) Place active subject after 'by' ('by the mechanic').\\nResult: 'The red car was fixed by the mechanic.'"),

    (109, "Direct to Reported Speech Rules", "LO-GRAM3", "Hard",
     "Explain the tense backshift rules for converting Direct Speech to Reported Speech for: 1) Present Simple, 2) Present Continuous, 3) Past Simple. Convert: He said, 'I play tennis.'",
     "Backshift Rules:\\n1) Present Simple -> Past Simple\\n2) Present Continuous -> Past Continuous\\n3) Past Simple -> Past Perfect\\nConversion: Direct: He said, 'I play tennis.' -> Reported: He said that he played tennis."),

    (110, "Question Tag Construction Rules", "LO-GRAM3", "Hard",
     "Explain the 3 main rules for creating Question Tags. Provide 2 examples: 1 positive main clause, 1 negative main clause.",
     "Rules:\\n1) Balance polarity: Positive clause -> Negative tag; Negative clause -> Positive tag.\\n2) Use the same auxiliary/modal verb from the main clause.\\n3) Use a pronoun corresponding to the subject.\\nExamples:\\n1) Positive clause: 'She is a doctor, isn't she?'\\n2) Negative clause: 'They don't like coffee, do they?'"),

    (111, "Prepositions of Time & Place Summary (in, on, at)", "LO-GRAM2", "Medium",
     "Summarize the usage of 'in', 'on', and 'at' for both Time and Place with 1 example for each.",
     "Time:\\n- 'at': Specific clock time (at 5:00 p.m.)\\n- 'on': Specific day/date (on Monday, on July 4th)\\n- 'in': Month, year, season (in July, in 2026, in summer)\\nPlace:\\n- 'at': Specific point/address (at school, at 10 Main St)\\n- 'on': Surface/street name (on the table, on Sukhumvit Road)\\n- 'in': Enclosed space/city/country (in the room, in Bangkok, in Thailand)"),

    (112, "Conditionals (Zero & First) Comparison", "LO-GRAM3", "Hard",
     "Compare Zero Conditional and First Conditional regarding: 1) Function/Meaning, 2) Sentence Structure, 3) Provide 1 example sentence for each.",
     "1) Zero Conditional: Scientific facts/universal truths -> Structure: If + Present Simple, Present Simple. Example: If you freeze water, it turns to ice.\\n2) First Conditional: Real/possible future events -> Structure: If + Present Simple, Will + V.1. Example: If it rains tomorrow, I will take an umbrella."),

    (113, "Plural Noun Rules & Exceptions", "LO-GRAM2", "Medium",
     "Explain 4 rules for making nouns plural: 1) Regular -s, 2) -es for s/ch/sh/x, 3) -y to -ies, 4) Irregular plurals. Give 1 example for each.",
     "1) Regular: Add -s (book -> books)\\n2) End in s, ch, sh, x: Add -es (watch -> watches)\\n3) End in consonant + y: Change y to i + es (city -> cities)\\n4) Irregular: Change internal vowels/form (child -> children, foot -> feet)"),

    (114, "Countable vs Uncountable Nouns & Quantifiers", "LO-GRAM2", "Medium",
     "Differentiate Countable and Uncountable nouns. Specify which quantifiers (many, much, a few, a little) are used with each.",
     "1) Countable Nouns: Things that can be counted individually (e.g., apples, cars). Uses quantifiers 'many' and 'a few'.\\n2) Uncountable Nouns: Substances/concepts that cannot be counted individually (e.g., water, milk, information). Uses quantifiers 'much' and 'a little'."),

    (115, "Proofreading & Common Error Elimination", "LO-GRAM4", "Hard",
     "Explain how to identify and correct 3 common grammar errors: 1) Double negative, 2) Misplaced apostrophe in possessive vs contraction, 3) Subject-verb disagreement.",
     "1) Double Negative: Avoid using two negatives together (Change 'I don't know nothing' -> 'I don't know anything').\\n2) Apostrophe: Distinguish contraction (It's = It is) from possessive adjective (its = belonging to it).\\n3) Subject-Verb Agreement: Match verb number to subject (Change 'The list of items are long' -> 'The list of items IS long').")
]

# Build Markdown content
out = header

# Section A
for q in mcq_questions:
    num, topic, lo, diff, prompt, opt_a, opt_b, opt_c, opt_d, ans, exp = q
    out += f"""
#### ข้อ {num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Question**: {prompt}
* ก. {opt_a}
* ข. {opt_b}
* ค. {opt_c}
* ง. {opt_d}
* **Correct Answer**: {ans}
* **Explanation**: {exp}
"""

out += "\n---\n\n# Section B: True / False Questions\n"

# Section B
for q in tf_questions:
    num, topic, lo, diff, stmt, ans, exp = q
    out += f"""
#### ข้อ {num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Statement**: "{stmt}"
* **Answer**: {ans}
* **Explanation**: {exp}
"""

out += "\n---\n\n# Section C: Scenario-Based Questions\n"

# Section C
for q in sc_questions:
    num, topic, lo, diff, scen, q_text, ans, exp = q
    out += f"""
#### ข้อ {num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Scenario**: {scen}
* **Question**: {q_text}
* **Answer**: {ans}
* **Explanation**: {exp}
"""

out += "\n---\n\n# Section D: Short Answer Questions\n"

# Section D
for q in sa_questions:
    num, topic, lo, diff, prompt, exp_ans = q
    out += f"""
#### ข้อ {num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Question**: {prompt}
* **Expected Answer**: {exp_ans}
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(out)

with open(alt_file_path, "w", encoding="utf-8") as f:
    f.write(out)

print(f"Successfully generated pure English Grammar Grade 6 quiz files at {file_path} and {alt_file_path}!")
