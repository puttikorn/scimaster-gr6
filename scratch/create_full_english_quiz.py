import os

file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_English_Gr6.md"
alt_file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_English_Languages_Gr6.md"

header = """# Knowledge Assessment Quiz: English Language Grade 6 (Midterm & Final Assessment)

---

## Document Summary (English Language Grade 6 Curriculum & Assessment Summary)

This assessment document compiles learning content and evaluation questions for English Language Grade 6, covering 6 core units:

### 1. Unit 1: Grammar & Sentence Structures
* **Tenses**: Present Simple, Present Continuous, Past Simple, Future Simple (will / be going to), and Present Perfect
* **Parts of Speech**: Nouns (Countable/Uncountable), Pronouns (Subject/Object/Possessive/Reflexive), Adjectives & Adverbs, Comparatives & Superlatives
* **Prepositions & Quantifiers**: Prepositions of time and place (in, on, at, under, behind, next to), Quantifiers (some, any, much, many, a few, a little)

### 2. Unit 2: Vocabulary for Daily Life, Jobs & Health
* **Daily Routines & Hobbies**: Free time activities, sports, daily schedules
* **Occupations & Workplaces**: Jobs, professions, workplaces (doctor, firefighter, pilot, chef, engineer)
* **Health & Illnesses**: Symptoms, diseases, health advice (headache, fever, stomachache, sore throat, should/shouldn't)

### 3. Unit 3: Places, Directions, Weather & Environment
* **Asking for & Giving Directions**: Turn left, turn right, go straight ahead, opposite, next to, between
* **Weather & Environment**: Weather conditions, seasons, natural disasters, environmental conservation

### 4. Unit 4: Food, Drinks, Cooking & Shopping
* **Food & Tastes**: Ingredients, taste descriptors (sweet, sour, salty, spicy, bitter), cooking verbs
* **Shopping & Prices**: Asking prices (How much is/are...?), money currency, sizes, shopping dialogues

### 5. Unit 5: Everyday Communication, Expressions & Public Signs
* **Classroom & Social Expressions**: Greetings, offering help, asking permission, apologizing, giving advice
* **Public Signs & Notices**: Traffic signs, safety warnings, public notices (No Swimming, Quiet Please, Danger)

### 6. Unit 6: Reading Comprehension & Western Culture
* **Western Holidays & Traditions**: Christmas, Halloween, Thanksgiving, Easter, Valentine's Day
* **Reading Passages**: Short passages, main idea identification, detail retrieval, context clues

---

## Learning Objectives Mapping

* **LO-ENG1**: Knowledge and understanding of vocabulary, grammar rules, and public signs (Remember / Understand)
* **LO-ENG2**: Application of Tenses, prepositions, quantifiers, and sentence structures (Apply)
* **LO-ENG3**: Analysis of reading passages, sentence structures, and comparative forms (Analyze)
* **LO-ENG4**: Communication in realistic scenarios, giving advice, social etiquette, and Western culture (Evaluate / Create / Culture)

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
    # 1-15: Grammar
    (1, "Grammar (Tenses)", "LO-ENG1", "Easy",
     "She ________ to school by bus every morning.",
     "go", "goes", "went", "going", "ข",
     "The subject 'She' is singular third-person, so the verb in Present Simple Tense takes -s -> goes."),

    (2, "Grammar (Tenses)", "LO-ENG1", "Easy",
     "Look! The children ________ football in the playground right now.",
     "play", "played", "are playing", "will play", "ค",
     "The phrase 'right now' indicates an action in progress at the moment of speaking -> Present Continuous (are playing)."),

    (3, "Grammar (Tenses)", "LO-ENG2", "Medium",
     "Yesterday, Tom ________ a new bicycle at the mall.",
     "buy", "buys", "bought", "has bought", "ค",
     "The word 'Yesterday' indicates past time in Past Simple Tense -> bought."),

    (4, "Grammar (Tenses)", "LO-ENG2", "Medium",
     "They ________ to Japan next month. They have already booked the tickets.",
     "visit", "visited", "are going to visit", "have visited", "ค",
     "Prior arrangement/plan with booked tickets uses 'be going to' for future -> are going to visit."),

    (5, "Grammar (Pronouns)", "LO-ENG1", "Easy",
     "This is Mary's book. It belongs to ________.",
     "she", "her", "hers", "herself", "ข",
     "After the preposition 'to', we use the Object Pronoun 'her'."),

    (6, "Grammar (Prepositions)", "LO-ENG1", "Easy",
     "My birthday is ________ July 15th.",
     "in", "on", "at", "by", "ข",
     "We use 'on' for specific calendar dates (July 15th)."),

    (7, "Grammar (Prepositions)", "LO-ENG1", "Easy",
     "We usually have lunch ________ 12:30 p.m.",
     "in", "on", "at", "for", "ค",
     "We use 'at' for specific clock times (12:30 p.m.)."),

    (8, "Grammar (Quantifiers)", "LO-ENG2", "Medium",
     "There isn't ________ milk left in the refrigerator.",
     "some", "any", "many", "few", "ข",
     "We use 'any' in negative sentences with uncountable nouns (milk)."),

    (9, "Grammar (Quantifiers)", "LO-ENG2", "Medium",
     "How ________ students are there in your classroom?",
     "much", "many", "long", "often", "ข",
     "We use 'How many' for plural countable nouns (students)."),

    (10, "Grammar (Comparatives)", "LO-ENG2", "Medium",
     "An elephant is ________ than a tiger.",
     "big", "bigger", "biggest", "more big", "ข",
     "Comparative degree of single-syllable adjective 'big' with CVC pattern doubles last consonant -> bigger."),

    (11, "Grammar (Superlatives)", "LO-ENG2", "Medium",
     "Mount Everest is the ________ mountain in the world.",
     "high", "higher", "highest", "most high", "ค",
     "Superlative degree with 'the' for 'high' is highest."),

    (12, "Grammar (Modal Verbs)", "LO-ENG2", "Easy",
     "You ________ stop when the traffic light turns red.",
     "must", "may", "can", "might", "ก",
     "Expressing mandatory rule or legal obligation uses 'must'."),

    (13, "Grammar (Modal Verbs)", "LO-ENG2", "Medium",
     "If you have a toothache, you ________ see a dentist.",
     "should", "would", "may", "could", "ก",
     "Giving medical advice uses 'should' (should see a dentist)."),

    (14, "Grammar (Conjunctions)", "LO-ENG2", "Medium",
     "He was tired, ________ he continued working to finish the project.",
     "so", "because", "but", "or", "ค",
     "Connecting contrasting ideas (tired vs continued working) uses 'but'."),

    (15, "Grammar (Conditionals)", "LO-ENG3", "Hard",
     "If it ________ tomorrow, we will stay at home and watch movies.",
     "rain", "rains", "rained", "will rain", "ข",
     "First Conditional structure: If + Present Simple (rains), Will + V.1."),

    # 16-30: Vocabulary
    (16, "Vocabulary (Jobs)", "LO-ENG1", "Easy",
     "A person who puts out fires and saves people is a ________.",
     "policeman", "firefighter", "pilot", "dentist", "ข",
     "A firefighter puts out fires and rescues people."),

    (17, "Vocabulary (Jobs)", "LO-ENG1", "Easy",
     "A ________ flies airplanes and travels around the world.",
     "driver", "engineer", "pilot", "chef", "ค",
     "A pilot flies airplanes."),

    (18, "Vocabulary (Jobs)", "LO-ENG1", "Easy",
     "My uncle works in a restaurant kitchen. He prepares delicious food. He is a ________.",
     "chef", "waiter", "farmer", "doctor", "ก",
     "A chef cooks food in a kitchen."),

    (19, "Vocabulary (Health)", "LO-ENG1", "Easy",
     "Sam ate too much ice cream. Now he has a ________.",
     "headache", "stomachache", "sore throat", "fever", "ข",
     "Eating too much ice cream causes a stomachache."),

    (20, "Vocabulary (Health)", "LO-ENG1", "Easy",
     "When you have a high body temperature, you have a ________.",
     "fever", "cough", "toothache", "cut", "ก",
     "High body temperature is a fever."),

    (21, "Vocabulary (Places)", "LO-ENG1", "Easy",
     "Where do you go to send letters and parcels?",
     "Hospital", "Post office", "Bank", "Police station", "ข",
     "Letters and parcels are handled at the post office."),

    (22, "Vocabulary (Places)", "LO-ENG1", "Easy",
     "A place where you can borrow and read books for free is a ________.",
     "bookstore", "library", "museum", "school", "ข",
     "A library offers free book reading and borrowing."),

    (23, "Vocabulary (Tastes)", "LO-ENG1", "Easy",
     "Lemons taste ________, while sugar tastes sweet.",
     "salty", "sour", "spicy", "bitter", "ข",
     "Lemons taste sour."),

    (24, "Vocabulary (Animals)", "LO-ENG1", "Easy",
     "Which animal is known as the 'Ship of the Desert'?",
     "Elephant", "Camel", "Horse", "Lion", "ข",
     "The camel is known as the Ship of the Desert."),

    (25, "Vocabulary (Weather)", "LO-ENG1", "Easy",
     "It is ________ today. Don't forget to take an umbrella with you!",
     "sunny", "rainy", "windy", "snowy", "ข",
     "Taking an umbrella indicates rainy weather."),

    (26, "Vocabulary (Directions)", "LO-ENG1", "Easy",
     "Go ________ ahead and turn left at the traffic lights.",
     "straight", "right", "back", "around", "ก",
     "'Go straight ahead' means moving forward in a line."),

    (27, "Vocabulary (Time)", "LO-ENG1", "Easy",
     "A period of ten years is called a ________.",
     "century", "decade", "millennium", "fortnight", "ข",
     "A 10-year period is a decade."),

    (28, "Vocabulary (School Supplies)", "LO-ENG1", "Easy",
     "We use a ________ to measure length and draw straight lines.",
     "ruler", "scissors", "eraser", "stapler", "ก",
     "A ruler is used for drawing lines and measuring length."),

    (29, "Vocabulary (Housework)", "LO-ENG1", "Easy",
     "After dinner, I always help my mother wash the ________.",
     "clothes", "dishes", "floor", "car", "ข",
     "Washing tableware after meals is 'wash the dishes'."),

    (30, "Vocabulary (Vehicles)", "LO-ENG1", "Easy",
     "A large vehicle that carries many passengers on fixed city routes is a ________.",
     "taxi", "bus", "bicycle", "helicopter", "ข",
     "A bus carries many passengers along city routes."),

    # 31-45: Reading, Signs, Everyday Dialogues
    (31, "Public Signs", "LO-ENG1", "Easy",
     "You see a sign 'NO SWIMMING' at the beach. What does it mean?",
     "You can swim here safely.", "You must not swim here.", "You should buy a swimsuit.", "Swimming is recommended.", "ข",
     "'NO SWIMMING' means swimming is prohibited."),

    (32, "Public Signs", "LO-ENG1", "Easy",
     "A sign showing 'QUIET PLEASE' in a library asks people to ________.",
     "speak loudly", "stop talking and make no noise", "play music", "eat snacks", "ข",
     "'QUIET PLEASE' requests silence."),

    (33, "Public Signs", "LO-ENG1", "Easy",
     "A sign with 'DON'T FEED THE ANIMALS' at the zoo warns visitors ________.",
     "to give food to animals", "not to give food to animals", "to pet animals", "to clean animal cages", "ข",
     "'DON'T FEED THE ANIMALS' forbids feeding animals."),

    (34, "Social Expressions", "LO-ENG4", "Easy",
     "A: Thank you very much for your help.\nB: ________.",
     "You're welcome", "I'm sorry", "Yes, please", "Never mind", "ก",
     "Standard polite response to 'Thank you' is 'You're welcome'."),

    (35, "Social Expressions", "LO-ENG4", "Easy",
     "A: I'm really sorry for breaking your ruler.\nB: ________. It's okay.",
     "That's terrible", "Don't worry about it", "Congratulations", "Excuse me", "ข",
     "Standard response to an apology is 'Don't worry about it'."),

    (36, "Social Expressions", "LO-ENG4", "Medium",
     "A: Can I borrow your pencil, please?\nB: Sure, ________.",
     "here you are", "no way", "I don't know", "thank you", "ก",
     "Handing something over upon request uses 'Sure, here you are.'"),

    (37, "Social Expressions", "LO-ENG4", "Medium",
     "A: What would you like to order, sir?\nB: ________, please.",
     "I'm ten years old", "I'd like a fried rice and an iced tea", "I go to school by bus", "It's five o'clock", "ข",
     "Ordering food uses 'I'd like...'"),

    (38, "Social Expressions", "LO-ENG4", "Medium",
     "A: Excuse me, how can I get to the train station?\nB: ________.",
     "It costs ten dollars", "Go straight for two blocks, it's on your left", "Yes, I like trains", "I am going to Bangkok", "ข",
     "Giving direction response: 'Go straight for two blocks, it's on your left.'"),

    (39, "Social Expressions", "LO-ENG4", "Medium",
     "A: How much is this blue T-shirt?\nB: ________.",
     "It's size medium", "It's 250 Baht", "It's made of cotton", "It's very nice", "ข",
     "Answering price question 'How much is...' requires price amount 'It's 250 Baht'."),

    (40, "Social Expressions", "LO-ENG4", "Medium",
     "A: What is the weather like today in London?\nB: ________.",
     "It's Monday", "It's cold and rainy", "I like London", "It's 5:00 p.m.", "ข",
     "Answering weather question uses weather description 'It's cold and rainy'."),

    # 41-60: Reading Passages & Grammar Analysis
    (41, "Reading Comprehension", "LO-ENG3", "Medium",
     "Read the passage: 'Penguins are birds that cannot fly, but they are great swimmers. They live in cold places like Antarctica and eat fish.' What do penguins eat?",
     "Plants", "Fish", "Insects", "Birds", "ข",
     "According to the text: '...and eat fish.'"),

    (42, "Reading Comprehension", "LO-ENG3", "Medium",
     "From the penguin passage, where do penguins live?",
     "In warm tropical forests", "In hot deserts", "In cold places like Antarctica", "In deep rivers", "ค",
     "According to the text: 'They live in cold places like Antarctica.'"),

    (43, "Reading Comprehension", "LO-ENG3", "Medium",
     "Read the note: 'Dear Students, The school library will be closed this Friday for maintenance. Please return all borrowed books by Thursday. Thank you.' Why is the library closed on Friday?",
     "For holiday", "For maintenance", "For sports day", "For exams", "ข",
     "According to the text: 'closed this Friday for maintenance'"),

    (44, "Reading Comprehension", "LO-ENG3", "Medium",
     "When must students return their borrowed books according to the note?",
     "By Wednesday", "By Thursday", "By Friday", "By Monday next week", "ข",
     "According to the text: 'Please return all borrowed books by Thursday'"),

    (45, "Western Culture", "LO-ENG4", "Easy",
     "On Halloween (October 31st), children wear costumes and go door-to-door saying '________!'.",
     "Merry Christmas", "Trick or Treat", "Happy New Year", "Happy Thanksgiving", "ข",
     "Halloween tradition phrase is 'Trick or Treat!'"),

    (46, "Western Culture", "LO-ENG4", "Easy",
     "What food is traditionally eaten during Thanksgiving dinner in the USA?",
     "Pizza", "Roast turkey", "Sushi", "Hamburgers", "ข",
     "Traditional Thanksgiving dish is roast turkey."),

    (47, "Western Culture", "LO-ENG4", "Easy",
     "Who brings presents to children on Christmas Eve according to Western legend?",
     "Santa Claus", "Easter Bunny", "Tooth Fairy", "Cupid", "ก",
     "Santa Claus brings presents on Christmas Eve."),

    (48, "Grammar (Passive Voice)", "LO-ENG3", "Hard",
     "The Harry Potter books ________ by J.K. Rowling.",
     "wrote", "were written", "write", "are writing", "ข",
     "Passive Voice in past tense: object + were written."),

    (49, "Grammar (Question Tags)", "LO-ENG3", "Hard",
     "She is a doctor, ________?",
     "isn't she", "is she", "doesn't she", "does she", "ก",
     "Affirmative main statement requires negative question tag -> isn't she?"),

    (50, "Grammar (Question Tags)", "LO-ENG3", "Hard",
     "You didn't go to school yesterday, ________?",
     "did you", "didn't you", "do you", "don't you", "ก",
     "Negative main statement requires positive question tag -> did you?"),

    (51, "Grammar (Relative Pronouns)", "LO-ENG3", "Hard",
     "The man ________ lives next door is a famous artist.",
     "who", "which", "where", "whose", "ก",
     "Relative pronoun referring to a person as subject is 'who'."),

    (52, "Grammar (Relative Pronouns)", "LO-ENG3", "Hard",
     "This is the house ________ I was born.",
     "who", "where", "which", "when", "ข",
     "Relative pronoun referring to a place is 'where'."),

    (53, "Grammar (Adverbs of Frequency)", "LO-ENG2", "Medium",
     "Peter ________ arrives late for class because he gets up very early.",
     "always", "never", "often", "usually", "ข",
     "Getting up early implies he 'never' arrives late."),

    (54, "Grammar (Subject-Verb Agreement)", "LO-ENG3", "Hard",
     "Neither John nor his friends ________ coming to the party tonight.",
     "is", "are", "was", "be", "ข",
     "With 'Neither A nor B', verb agrees with the closer subject 'his friends' (plural) -> are."),

    (55, "Grammar (Subject-Verb Agreement)", "LO-ENG3", "Hard",
     "Every student in the classroom ________ a uniform.",
     "wear", "wears", "wearing", "have worn", "ข",
     "'Every + singular noun' takes a singular verb -> wears."),

    (56, "Vocabulary (Emotions)", "LO-ENG1", "Easy",
     "She was very ________ when she won first prize in the singing contest.",
     "sad", "excited", "bored", "angry", "ข",
     "Winning first prize makes a person excited."),

    (57, "Vocabulary (Environment)", "LO-ENG2", "Medium",
     "To protect our Earth, we should ________ plastic bags and recycle paper.",
     "waste", "reduce", "increase", "destroy", "ข",
     "Environmental conservation advocates reducing plastic bag usage."),

    (58, "Vocabulary (Phrasal Verbs)", "LO-ENG2", "Medium",
     "Don't put off until tomorrow what you can do today. What does 'put off' mean?",
     "Postpone / Delay", "Finish quickly", "Start immediately", "Forget", "ก",
     "Phrasal verb 'put off' means postpone or delay."),

    (59, "Vocabulary (Calendar)", "LO-ENG1", "Easy",
     "Which month comes right after August?",
     "July", "September", "October", "November", "ข",
     "September immediately follows August."),

    (60, "Communication Expressions", "LO-ENG4", "Easy",
     "What do you say to someone who is going to take an exam?",
     "Good luck!", "Happy Birthday!", "Get well soon!", "Bon appetit!", "ก",
     "Encouragement phrase for test takers is 'Good luck!'")
]

tf_questions = [
    # 61-90 True/False
    (61, "Grammar (Tenses)", "LO-ENG1", "Easy",
     "In English, the Present Continuous Tense is formed using 'Subject + is/am/are + V.-ing'.",
     "True", "Correct. Present Continuous formula is Subject + is/am/are + V.-ing."),

    (62, "Grammar (Plural Nouns)", "LO-ENG1", "Easy",
     "The plural form of the word 'child' is 'childs'.",
     "False", "Incorrect. The plural form of child is 'children'."),

    (63, "Grammar (Uncountable Nouns)", "LO-ENG1", "Easy",
     "The word 'water' is an uncountable noun, so we cannot say 'two waters'.",
     "True", "Correct. Water is uncountable and requires containers like 'two glasses of water'."),

    (64, "Grammar (Prepositions)", "LO-ENG1", "Easy",
     "We use the preposition 'at' before days of the week, such as 'at Monday'.",
     "False", "Incorrect. Days of the week take preposition 'on' (on Monday)."),

    (65, "Grammar (Comparatives)", "LO-ENG2", "Medium",
     "The comparative form of 'good' is 'gooder'.",
     "False", "Incorrect. The irregular comparative form of good is 'better'."),

    (66, "Grammar (Superlatives)", "LO-ENG2", "Medium",
     "The superlative form of 'beautiful' is 'the most beautiful'.",
     "True", "Correct. Three-syllable adjectives use 'the most beautiful' in superlative."),

    (67, "Vocabulary (Health)", "LO-ENG1", "Easy",
     "A 'dentist' is a doctor who takes care of people's teeth.",
     "True", "Correct. A dentist specializes in dental healthcare."),

    (68, "Vocabulary (Jobs)", "LO-ENG1", "Easy",
     "An 'architect' is a person whose job is to design buildings.",
     "True", "Correct. An architect plans and designs building structures."),

    (69, "Vocabulary (Places)", "LO-ENG1", "Easy",
     "An 'aquarium' is a building where historical objects are kept and displayed.",
     "False", "Incorrect. Historical objects are displayed in a museum; aquariums display aquatic life."),

    (70, "Vocabulary (Weather)", "LO-ENG1", "Easy",
     "When the weather forecast says 'foggy', it means the sky is clear and very sunny.",
     "False", "Incorrect. 'Foggy' means thick fog obscuring visibility, not clear and sunny."),

    (71, "Grammar (Pronouns)", "LO-ENG1", "Easy",
     "The possessive adjective for 'they' is 'their' when used before a noun (e.g., their house).",
     "True", "Correct. 'Their' is the possessive adjective preceding nouns."),

    (72, "Grammar (Modals)", "LO-ENG2", "Medium",
     "The modal verb 'mustn't' means 'do not have to' (you can choose whether to do it or not).",
     "False", "Incorrect. 'Mustn't' means strict prohibition, while 'don't have to' means lack of necessity."),

    (73, "Vocabulary (Time)", "LO-ENG1", "Easy",
     "The expression 'quarter past eight' means 8:15.",
     "True", "Correct. A quarter (15 minutes) past eight equals 8:15."),

    (74, "Vocabulary (Time)", "LO-ENG1", "Easy",
     "The expression 'half past ten' means 10:45.",
     "False", "Incorrect. 'Half past ten' means 10:30. 10:45 is 'quarter to eleven'."),

    (75, "Grammar (Irregular Verbs)", "LO-ENG2", "Medium",
     "The past simple form of the verb 'go' is 'went'.",
     "True", "Correct. Past simple V.2 of 'go' is 'went'."),

    (76, "Grammar (Irregular Verbs)", "LO-ENG2", "Medium",
     "The past simple form of the verb 'teach' is 'teached'.",
     "False", "Incorrect. Irregular past simple V.2 of 'teach' is 'taught'."),

    (77, "Public Signs", "LO-ENG1", "Easy",
     "A sign 'FRAGILE' on a package means the item inside breaks easily and should be handled with care.",
     "True", "Correct. 'FRAGILE' indicates delicate, breakable contents."),

    (78, "Social Expressions", "LO-ENG4", "Easy",
     "When someone says 'Bless you!' after you sneeze, it is a polite social custom in English culture.",
     "True", "Correct. 'Bless you!' is standard social etiquette after someone sneezes."),

    (79, "Quantifiers & Nouns", "LO-ENG2", "Medium",
     "We use 'a loaf of' to count bread, e.g., 'a loaf of bread'.",
     "True", "Correct. 'A loaf of' is the quantifier unit for bread."),

    (80, "Quantifiers & Nouns", "LO-ENG2", "Medium",
     "We use 'a bar of' to count water, e.g., 'a bar of water'.",
     "False", "Incorrect. 'A bar of' is used for soap or chocolate; water uses 'a bottle of' or 'a glass of'."),

    (81, "Western Culture", "LO-ENG4", "Easy",
     "Christmas Day is celebrated annually on December 25th.",
     "True", "Correct. Christmas Day falls on December 25th."),

    (82, "Western Culture", "LO-ENG4", "Easy",
     "On Easter Sunday, children traditionally search for hidden painted eggs.",
     "True", "Correct. Hunting Easter eggs is a traditional Easter activity."),

    (83, "Grammar (Articles)", "LO-ENG1", "Easy",
     "We use the article 'a' before words starting with a vowel sound, such as 'a apple'.",
     "False", "Incorrect. Words starting with vowel sounds require article 'an' (an apple)."),

    (84, "Grammar (Articles)", "LO-ENG1", "Easy",
     "We use 'an' before 'hour' because the letter 'h' is silent and it starts with a vowel sound.",
     "True", "Correct. 'Hour' has a silent 'h' and starts with vowel sound /aʊər/, taking article 'an'."),

    (85, "Vocabulary (Sports)", "LO-ENG1", "Easy",
     "We use the verb 'play' with sports ending in -ing, like 'play swimming' and 'play running'.",
     "False", "Incorrect. Sports ending in -ing take verb 'go' (go swimming, go running)."),

    (86, "Vocabulary (Sports)", "LO-ENG1", "Easy",
     "We use the verb 'do' with martial arts and individual exercises like 'do gymnastics' and 'do karate'.",
     "True", "Correct. Martial arts and individual non-team exercises take verb 'do'."),

    (87, "Grammar (Question Words)", "LO-ENG1", "Easy",
     "The question word 'Whose' is used to ask about ownership/possession.",
     "True", "Correct. 'Whose' inquires about possession (Whose pen is this?)."),

    (88, "Vocabulary (Directions)", "LO-ENG1", "Easy",
     "The opposite of 'North' is 'West'.",
     "False", "Incorrect. The opposite of North is South; West is opposite East."),

    (89, "Vocabulary (Clothing)", "LO-ENG1", "Easy",
     "The word 'gloves' is typically used in plural form because they come in pairs for both hands.",
     "True", "Correct. 'Gloves' is plural as it comes in a two-hand pair."),

    (90, "Vocabulary (Semantics)", "LO-ENG3", "Medium",
     "A 'synonym' is a word that has the opposite meaning of another word.",
     "False", "Incorrect. A synonym has the SAME meaning. Words with OPPOSITE meanings are antonyms.")
]

sc_questions = [
    # 91-105 Scenario
    (91, "Restaurant Ordering Scenario", "LO-ENG4", "Hard",
     "John is at a restaurant. He wants to order a cheeseburger, french fries, and a bottle of mineral water. How should he politely place his order to the waiter?",
     "Question: How should John politely state his order to the waiter?",
     "John says: 'Hello! I would like to order a cheeseburger, french fries, and a bottle of mineral water, please.'",
     "Explanation: Polite food ordering utilizes 'I would like to order...' (or 'I'd like...') ending with 'please'."),

    (92, "Asking Directions Scenario", "LO-ENG4", "Hard",
     "A tourist is lost in the city and wants to find the nearest police station. He approaches a local citizen politely. What should the tourist say?",
     "Question: What polite phrase should the tourist use to ask for directions?",
     "Tourist says: 'Excuse me, could you please tell me how to get to the nearest police station?'",
     "Explanation: Polite direction inquiry starts with 'Excuse me, could you please tell me how to get to...?'"),

    (93, "Medical Consultation Scenario", "LO-ENG4", "Hard",
     "Sarah feels unwell. She has a high fever and a severe cough. The doctor asks her about her symptoms. How should Sarah describe her illness?",
     "Question: How should Sarah describe her symptoms to the doctor?",
     "Sarah says: 'Doctor, I don't feel well. I have a high fever and a bad cough.'",
     "Explanation: Symptom descriptions use 'I have a + (symptom)' structure."),

    (94, "Clothing Store Scenario", "LO-ENG4", "Hard",
     "Ben is trying on a jacket at a clothing store. He likes it, but it is too small for him. He wants to ask the shop assistant for a larger size. What should Ben say?",
     "Question: How should Ben ask for a different size from the sales clerk?",
     "Ben says: 'This jacket is a bit too small for me. Do you have a larger size, please?'",
     "Explanation: Stating the issue (too small) followed by request 'Do you have a larger size, please?'."),

    (95, "Weekend Activity Invitation Scenario", "LO-ENG4", "Hard",
     "Anna wants to invite her classmate Mark to go to the cinema to watch an animated movie this Saturday afternoon. How should Anna phrase her invitation?",
     "Question: How should Anna formulate her invitation to Mark?",
     "Anna says: 'Hi Mark! Would you like to go to the cinema to watch an animated movie with me this Saturday afternoon?'",
     "Explanation: Polite activity invitations use 'Would you like to + V.1 ... with me?'"),

    (96, "Classroom Borrowing Scenario", "LO-ENG4", "Hard",
     "David forgot his pencil case at home. He needs an eraser for his art class. He asks his desk mate Lisa. Write their borrowing dialogue.",
     "Question: Write a complete borrowing dialogue between David and Lisa.",
     "David: 'Lisa, I forgot my pencil case today. May I borrow your eraser, please?' Lisa: 'Sure, David! Here you are.' David: 'Thank you so much!' Lisa: 'You're welcome!'",
     "Explanation: Polite borrowing uses 'May I borrow...?' Handing over uses 'Sure, here you are.'"),

    (97, "Weather Forecast Advice Scenario", "LO-ENG3", "Hard",
     "Tom and his family planned a beach trip tomorrow. Tom checks the weather forecast news. The reporter says it will be stormy with heavy rain. What advice should Tom give his family?",
     "Question: What advice should Tom give to his family based on the weather report?",
     "Tom says: 'The weather forecast says it will be stormy tomorrow. We shouldn't go to the beach. We should stay home instead.'",
     "Explanation: Giving advice uses modal verbs 'shouldn't go' and 'should stay home'."),

    (98, "Spill Apology Scenario", "LO-ENG4", "Hard",
     "Ken accidentally knocked over a glass of water onto Jenny's notebook. Ken immediately apologizes and offers to help clean it up. Write their conversation.",
     "Question: Write the apology, offer of help, and forgiving response dialogue.",
     "Ken: 'Oh, I'm so sorry, Jenny! I accidentally spilled water on your notebook. Let me help you wipe it dry.' Jenny: 'That's alright, Ken. Accidents happen. Thank you for your help.'",
     "Explanation: Apologizing uses 'I'm so sorry...', offering help uses 'Let me help...', forgiving uses 'That's alright.'"),

    (99, "Schedule Inquiry Scenario", "LO-ENG4", "Hard",
     "Peter wants to know what time the English class starts today and where it takes place. He asks his teacher Miss Green. Write their short dialogue.",
     "Question: Write the dialogue inquiring about class time and room location.",
     "Peter: 'Excuse me, Miss Green. What time does our English class start today, and where is it?' Miss Green: 'It starts at 10:15 a.m. in Room 302.' Peter: 'Thank you, teacher.'",
     "Explanation: Asking start time uses 'What time does... start?' and location uses 'Where is it?'"),

    (100, "Self-Introduction Scenario", "LO-ENG4", "Hard",
     "The teacher introduces a new student named Kenji from Japan to the class. Kenji introduces himself briefly (name, age, country, hobby). What does Kenji say?",
     "Question: Write Kenji's self-introduction speech to his new classmates.",
     "Kenji says: 'Hello everyone! My name is Kenji. I am 12 years old. I come from Japan. My hobby is playing football. Nice to meet you all!'",
     "Explanation: Standard self-introduction covers name, age, origin country, hobby, and polite greeting."),

    (101, "Movie Ticket Purchasing Scenario", "LO-ENG4", "Hard",
     "Emma goes to the cinema. She wants to buy 2 adult tickets for the 5:00 p.m. show of 'Spider-Man'. How does she speak with the ticket cashier?",
     "Question: Write Emma's dialogue with the ticket cashier.",
     "Emma says: 'Hello, I'd like two tickets for Spider-Man at 5:00 p.m., please.' Cashier: 'That will be 300 Baht, please.' Emma: 'Here is the money. Thank you!'",
     "Explanation: Ticket purchasing specifies number of tickets, movie title, showtime, and payment."),

    (102, "Health Advice Scenario", "LO-ENG4", "Hard",
     "Mike tells his friend May that he has a severe toothache and cannot eat food properly. What advice should May give to Mike?",
     "Question: What healthcare advice should May give to Mike?",
     "May says: 'You shouldn't eat sweet candies, and you should go to see a dentist right away.'",
     "Explanation: Healthcare advice includes negative suggestion (shouldn't eat candies) and positive recommendation (should see a dentist)."),

    (103, "Movie Opinion Expressing Scenario", "LO-ENG3", "Hard",
     "Two friends just finished watching an action movie. Tim thought it was exciting, but Bob thought it was boring. Write their short opinion dialogue.",
     "Question: Write a short dialogue where two friends express differing movie opinions.",
     "Tim: 'I thought the movie was really exciting! What did you think?' Bob: 'Well, to be honest, I found it a bit boring because the story was too long.'",
     "Explanation: Inquiring opinion uses 'What did you think?' and stating opinion uses 'I thought...' / 'I found it...'"),

    (104, "Christmas Celebration Narrative Scenario", "LO-ENG4", "Hard",
     "On Christmas Day, Jack's family decorates the Christmas tree, exchanges gifts, and wishes each other well. Write a short paragraph describing Jack's Christmas.",
     "Question: Write a short narrative paragraph describing Jack's Christmas activities.",
     "Jack's Christmas: 'On Christmas Day, my family decorates the green Christmas tree with colorful lights and stars. We give gifts to each other and say Merry Christmas!'",
     "Explanation: Narrative covers tree decoration, gift exchange, and festive greetings."),

    (105, "Polite Decline Scenario", "LO-ENG4", "Hard",
     "Paul invites Amy to play computer games at his house this afternoon, but Amy has to study for her English test tomorrow. How does Amy politely decline?",
     "Question: How should Amy politely decline Paul's invitation with a valid reason?",
     "Amy says: 'Thank you for the invitation, Paul, but I'm afraid I can't. I have to study for my English exam tomorrow. Maybe next time!'",
     "Explanation: Polite refusal thanks the inviter, uses 'I'm afraid I can't', states the reason, and offers 'Maybe next time!'")
]

sa_questions = [
    # 106-115 Short Answer
    (106, "Plural Noun Formation Rules", "LO-ENG1", "Medium",
     "Explain the rules for changing singular nouns into plural nouns for: 1) cat -> cats, 2) bus -> buses, 3) baby -> babies, 4) man -> men. Provide explanations for each case.",
     "1) Regular nouns: Add -s (cat -> cats)\\n2) Nouns ending in -s, -ss, -sh, -ch, -x: Add -es (bus -> buses)\\n3) Nouns ending in consonant + y: Change y to i and add -es (baby -> babies)\\n4) Irregular nouns: Change the internal vowel (man -> men)"),

    (107, "Comparative & Superlative Degree Rules", "LO-ENG2", "Medium",
     "Complete the comparison table for the adjectives: 1) tall, 2) big, 3) expensive, 4) good. Write their Comparative and Superlative forms with explanations.",
     "1) tall -> taller -> the tallest (Short adjective: add -er / -est)\\n2) big -> bigger -> the biggest (CVC pattern: double final consonant)\\n3) expensive -> more expensive -> the most expensive (Long adjective: use more / most)\\n4) good -> better -> the best (Irregular adjective)"),

    (108, "Present Simple vs Present Continuous Tense", "LO-ENG2", "Medium",
     "Explain the difference in usage between Present Simple Tense and Present Continuous Tense with 1 example sentence for each.",
     "1. Present Simple Tense: Used for daily routines, habits, and general truths.\\nExample: He plays football every Sunday.\\n2. Present Continuous Tense: Used for actions happening right now at the moment of speaking.\\nExample: He is playing football right now."),

    (109, "Prepositions of Time Rules (in, on, at)", "LO-ENG2", "Medium",
     "Explain when to use the prepositions of time 'in', 'on', and 'at' with 1 example phrase for each.",
     "1. 'at': Used for specific clock times and parts of night (e.g., at 7:00 a.m., at night)\\n2. 'on': Used for specific days and calendar dates (e.g., on Monday, on December 25th)\\n3. 'in': Used for months, years, seasons, and parts of the day (e.g., in July, in 2026, in the morning)"),

    (110, "Sentence Analysis & Parts of Speech", "LO-ENG3", "Hard",
     "Analyze the sentence: 'The smart student quickly solved the difficult math problem.' Identify the Subject, Verb, Adjectives, and Adverb.",
     "Analysis:\\n- Subject: The smart student\\n- Verb: solved\\n- Adjectives: smart (modifies student), difficult (modifies math problem)\\n- Adverb: quickly (modifies verb solved)\\n- Object: the difficult math problem"),

    (111, "Quantifiers Usage (some vs any)", "LO-ENG2", "Medium",
     "Explain the main rules for using 'some' and 'any' in sentences with 2 example sentences.",
     "Rules:\\n1. 'some': Used in affirmative positive sentences and polite offers/requests.\\nExample: There are some apples on the table. / Would you like some tea?\\n2. 'any': Used in negative sentences and questions.\\nExample: There isn't any milk in the fridge. / Do you have any questions?"),

    (112, "Halloween Culture & Traditions", "LO-ENG4", "Medium",
     "Describe the origin and key traditions of Halloween (date, costumes, activities, symbols) in 3-4 sentences in English.",
     "Halloween is celebrated annually on October 31st in Western countries. Children dress up in fancy costumes such as ghosts, witches, or superheroes. They go door-to-door saying 'Trick or Treat!' to collect candies. People also carve pumpkins into jack-o'-lanterns with candle lights inside."),

    (113, "Modal Verbs Differentiation (should vs must)", "LO-ENG2", "Medium",
     "Explain the difference between 'should' and 'must' when giving instructions or advice, with 1 example for each.",
     "1. 'should': Used for giving suggestions or mild advice (what is good to do).\\nExample: You should drink more water when you have a cold.\\n2. 'must': Used for strong obligation, necessity, or strict laws/rules.\\nExample: You must wear a helmet when riding a motorbike."),

    (114, "Restaurant Lunch Ordering Dialogue", "LO-ENG4", "Hard",
     "Write a short dialogue (4 lines) between a Customer and a Waiter ordering lunch at a restaurant in English.",
     "Waiter: Good afternoon! Are you ready to order?\\nCustomer: Yes, please. I'd like a chicken salad and a cup of green tea.\\nWaiter: Would you like any dessert?\\nCustomer: No, thank you. That will be all for now."),

    (115, "Friendly Email Composition", "LO-ENG4", "Hard",
     "Write a short friendly email (4-5 lines) inviting your friend to your birthday party this weekend in English.",
     "Hi Sam,\\nHow are you? I am writing to invite you to my 12th birthday party this Saturday at 4:00 p.m. at my home. We will play games, eat delicious birthday cake, and listen to music. I hope you can come!\\nBest wishes,\\nTom")
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

print(f"Successfully generated pure English quiz files for {file_path} and {alt_file_path}!")
