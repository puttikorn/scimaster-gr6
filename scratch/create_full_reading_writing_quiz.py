#!/usr/bin/env python3
import sys
import os

md_content = """# Knowledge Assessment Quiz: Reading with Writing Grade 6 (Reading with Writing Gr.6 - MidFinal)

> **Assessment Information**
> - **Subject**: Reading with Writing (ระบบทดสอบวัดผลการเรียนรู้ทักษะการอ่านและการเขียน ภาษาอังกฤษ ป.6)
> - **Grade Level**: Grade 6 (Primary 6)
> - **Source Material**: Reading with Writing GR6-MidFinal.pdf (28 Pages)
> - **Total Questions**: 115 Questions
> - **Total Points**: 150 Points
> - **Passing Criteria**: 80% (120 / 150 Points)

---

## Document Summary (สรุปเนื้อหาเอกสารและหลักสูตร Reading with Writing ป.6)

เอกสารฉบับนี้รวบรวมเนื้อหาและโจทย์ประเมินผลการเรียนรู้ทักษะการอ่านและการเขียนภาษาอังกฤษ (Reading & Writing) ระดับชั้นประถมศึกษาปีที่ 6 ครอบคลุมสาระสำคัญ 2 หน่วยการเรียนรู้หลัก ได้แก่:

### 1. Unit 5: Navigation, Visuals & Information Literacy
* **Identify and Analyze Setting**: การระบุและวิเคราะห์ฉาก (สถานที่และเวลา) ในเรื่องเล่า ("Lost and Found") ผลกระทบของฉากต่ออารมณ์ ตัวละคร และโครงเรื่อง
* **Use Visuals**: การใช้ภาพประกอบ แผนที่ เข็มทิศ และแผนภูมิเพื่อเสริมความเข้าใจในการอ่าน ("The World of Orienteering", ประภาคาร Lighthouses)
* **Bar Graphs & Global Languages**: การอ่านและตีความแผนภูมิแท่งเพื่อวิเคราะห์ข้อมูลเชิงสถิติ (ภาษาเป็นทางการใน 196 ประเทศ, ภาษามือ Sign Languages)
* **Process Essay Writing**: การเขียนเรียงความอธิบายขั้นตอนกระบวนการ (Process Essay) โดยใช้คำเชื่อมบอกลำดับเวลา (Sequence words: First, Next, Then, After that, Finally)

### 2. Unit 6: Predictions, Language Dynamics & Writing Reviews
* **Make Predictions**: การทำนายเหตุการณ์ล่วงหน้าโดยใช้คำใบ้จากเรื่อง (Clues) และความรู้เดิม ("The Mystery Pencil")
* **Living and Dead Languages**: การแยกแยะภาษาที่มีชีวิต (Living Languages เช่น ภาษาจีนกลาง Mandarin) และภาษาที่ตายแล้ว (Dead Languages เช่น ภาษาละติน Latin)
* **Linguistic Concepts**: คำศัพท์ทางภาษาศาสตร์ ได้แก่ Bilingualism (การพูดได้สองภาษา), Accent (สำเนียง), Native Speaker (เจ้าของภาษา)
* **Writing a Review**: การเขียนรีวิวหนังสือหรือเรื่องสั้น (Book/Story Review) การจัดโครงสร้างบทนำ เนื้อหา ข้อดี-ข้อเสีย การยกตัวอย่าง (for example, for instance) และการสรุปข้อเสนอแนะ

---

## Learning Objectives Mapping (แผนผังจุดประสงค์การเรียนรู้)

* **LO-RW1**: Identify and analyze the setting (time, place, atmosphere) in narrative texts.
* **LO-RW2**: Interpret and use reading visuals (maps, diagrams, charts, compasses) to extract explicit and implicit information.
* **LO-RW3**: Read and analyze statistical information presented in bar graphs (e.g., global languages, speaker counts).
* **LO-RW4**: Make logical predictions about text outcomes based on context clues and background knowledge.
* **LO-RW5**: Understand and differentiate linguistic concepts (living vs. dead languages, bilingualism, native speakers).
* **LO-RW6**: Apply process essay structure and transition words to explain chronological procedures clearly.
* **LO-RW7**: Write well-structured book/story reviews with clear summaries, evaluations, examples, and recommendations.

---

## สรุปคะแนนรวม

| ส่วน | จำนวนข้อ | คะแนน/ข้อ | คะแนนรวม |
|------|----------|-----------|----------|
| A: ปรนัย (MCQ) | 60 | 1 | 60 |
| B: ถูก/ผิด (TF) | 30 | 1 | 30 |
| C: สถานการณ์ (Scenario) | 15 | 2 | 30 |
| D: อัตนัย (ShortAnswer) | 10 | 3 | 30 |
| **รวม** | **115** | — | **150** |
| **เกณฑ์ผ่าน (80%)** | — | — | **120** |

---

# Section A: Multiple Choice Questions (ปรนัย 4 ตัวเลือก)

"""

# Generating 60 MCQs
mcqs = [
    # 1-10: Setting Analysis ("Lost and Found")
    ("Identify and Analyze Setting", "LO-RW1", "Easy",
     "What is the definition of the 'setting' of a story?",
     "The main message or moral of the story",
     "Where and when a story takes place",
     "The conflict between the main characters",
     "The list of vocabulary words in a book",
     "ข", "Setting refers to the location (where) and time period/environment (when) in which a story occurs."),

    ("Identify and Analyze Setting", "LO-RW1", "Easy",
     "How can the setting affect a story?",
     "It only changes the title of the book.",
     "It influences the characters' actions, mood, and plot events.",
     "It has no impact on what characters do.",
     "It replaces the need for any dialogue.",
     "ข", "Setting sets the atmosphere and directly shapes character decisions and plot events."),

    ("Identify and Analyze Setting", "LO-RW1", "Easy",
     "In the story 'Lost and Found', what were Jaya and her family doing?",
     "Riding bicycles in the city",
     "Hiking in their favorite park on a foggy morning",
     "Sailing a boat near a lighthouse",
     "Visiting a museum on a sunny afternoon",
     "ข", "Jaya, Manoj, and their Mom went hiking on a foggy morning to reach a hill with a crooked tree."),

    ("Identify and Analyze Setting", "LO-RW1", "Medium",
     "What was the family's destination for their picnic in 'Lost and Found'?",
     "A lighthouse near town",
     "A hill with a tall, crooked tree on top",
     "An old wooden bench on the left side of the main trail",
     "A crowded restaurant in the city center",
     "ข", "Their goal was a hill topped with a distinctive tall, crooked tree where they liked to picnic."),

    ("Identify and Analyze Setting", "LO-RW1", "Medium",
     "How did Jaya and her family realize they were on the wrong trail?",
     "They saw a giant lighthouse right in front of them.",
     "They noticed a long bench on the left side of the trail and checked the time.",
     "A park ranger stopped them and gave them new directions.",
     "They reached the ocean and could not walk any further.",
     "ข", "Seeing the bench and noting it was almost noon made them realize they should have already reached their destination."),

    ("Identify and Analyze Setting", "LO-RW1", "Medium",
     "What weather condition created difficulty during the family's hike?",
     "Heavy snowfall and icy wind",
     "Thick fog that blocked their view of landmarks",
     "A sudden thunderous rainstorm",
     "Extreme desert heat and lack of water",
     "ข", "The foggy morning obscured landmarks until they climbed high enough above the fog."),

    ("Identify and Analyze Setting", "LO-RW1", "Medium",
     "What landmark did Mom use to orient their position relative to south?",
     "The crooked tree",
     "The lighthouse near town",
     "The wooden bench",
     "A giant waterfall",
     "ข", "Mom identified the lighthouse near town to know which direction was south."),

    ("Identify and Analyze Setting", "LO-RW1", "Hard",
     "Why did Jaya describe the destination hill as looking like 'an island in a sea of clouds'?",
     "The hill was completely surrounded by real ocean water.",
     "The top of the hill stood above the thick fog layer surrounding it.",
     "They were looking at a painting inside a museum.",
     "The hill had a large lake floating on top of it.",
     "ข", "Standing above the fog line made the hilltop look like an island rising out of white clouds."),

    ("Identify and Analyze Setting", "LO-RW1", "Medium",
     "Which question best helps a reader analyze the setting of a story?",
     "How many pages long is this chapter?",
     "How does the environment shape the choices characters make?",
     "What is the author's middle name?",
     "Which font size is used for the text?",
     "ข", "Asking how the setting influences character choices helps readers understand its literary significance."),

    ("Identify and Analyze Setting", "LO-RW1", "Easy",
     "If a story takes place during a dark, stormy night in a dense forest, what mood is created?",
     "Cheerful and relaxing",
     "Mysterious and tense",
     "Boring and silly",
     "Bright and celebratory",
     "ข", "Darkness, storms, and dense forests naturally evoke tension and mystery."),

    # 11-20: Visuals in Reading ("The World of Orienteering" & Lighthouses)
    ("Use Visuals", "LO-RW2", "Easy",
     "What are 'visuals' in a reading text?",
     "Pictures, diagrams, maps, and charts that provide extra information",
     "The hard cover and binding of a physical book",
     "The printed letters and font colors of the text",
     "Audio recordings attached to a digital textbook",
     "ก", "Visuals include photos, diagrams, maps, and graphs that visually support and extend reading content."),

    ("Use Visuals", "LO-RW2", "Easy",
     "Why do authors include visuals alongside text?",
     "To make the pages heavier",
     "To provide information and context not fully described in text alone",
     "To confuse readers who don't like pictures",
     "To replace all written words in a book",
     "ข", "Visuals enhance comprehension by adding visual context and details not stated in text."),

    ("Use Visuals", "LO-RW2", "Medium",
     "What is 'orienteering' as described in Unit 5?",
     "A indoor board game played with dice",
     "An outdoor sport where racers use a map and compass to find controls",
     "A swimming race held in an Olympic pool",
     "A cooking contest using natural outdoor herbs",
     "ข", "Orienteering is a outdoor navigation race requiring map reading and compass skills."),

    ("Use Visuals", "LO-RW2", "Medium",
     "In orienteering, what are 'controls'?",
     "Buttons on a stopwatch used to record lap times",
     "Checkpoints marked on maps and marked in nature with special flags",
     "Rules enforced by race judges along the trail",
     "Obstacles like mud and fallen trees placed by organizers",
     "ข", "Controls are target checkpoints that competitors must locate using map coordinates."),

    ("Use Visuals", "LO-RW2", "Easy",
     "What two essential tools must racers carry during an orienteering event?",
     "A camera and a smartphone",
     "A map and a compass",
     "A flashlight and a shovel",
     "A tent and a sleeping bag",
     "ข", "Orienteers rely strictly on a detailed map and a magnetic compass to navigate."),

    ("Use Visuals", "LO-RW2", "Medium",
     "What color scheme is typically used for control flags in orienteering?",
     "Black and white",
     "Orange and white",
     "Green and blue",
     "Yellow and purple",
     "ข", "Orienteering control flags feature a distinctive square divided diagonally into orange and white."),

    ("Use Visuals", "LO-RW2", "Medium",
     "According to the text on Lighthouses, where are lighthouses built?",
     "In the middle of dense mountain forests",
     "On coastal shores and rocky cliffs near water",
     "In urban town squares far from the ocean",
     "On top of tall city skyscrapers",
     "ข", "Lighthouses are positioned along sea coasts and dangerous shorelines to warn vessels."),

    ("Use Visuals", "LO-RW2", "Medium",
     "What key equipment does a lighthouse have to guide ships during heavy fog?",
     "A giant searchlight and a loud fog horn",
     "A radar tower and radio speakers",
     "A fireworks launcher and smoke signals",
     "A flashing mirror and tolling church bells",
     "ก", "Lighthouses feature powerful lamps (lights) and acoustic fog horns to warn nearby ships."),

    ("Use Visuals", "LO-RW2", "Easy",
     "What primary warning signal does a lighthouse give to ships?",
     "It invites ships to dock at the rocky shore.",
     "It warns ships where land is so they avoid crashing into rocks.",
     "It tells ships that bad weather is ending soon.",
     "It signals that fresh drinking water is available.",
     "ข", "The light and horn warn sailors of dangerous coastline obstacles and shallow waters."),

    ("Use Visuals", "LO-RW2", "Hard",
     "How does combining text with a map diagram help an orienteering racer?",
     "It lets them calculate exact walking elevation and terrain features visually.",
     "It replaces the need to practice running.",
     "It translates English directions into other languages automatically.",
     "It provides exact weather forecasts for the entire week.",
     "ก", "Visual map diagrams reveal spatial relationships, contours, and landmarks instantly."),

    # 21-30: Bar Graphs & Global Languages
    ("Bar Graphs & Global Languages", "LO-RW3", "Easy",
     "What is a 'bar graph' used for in reading informational texts?",
     "To display a timeline of historic fictional events",
     "To compare quantities or numbers across categories using rectangular bars",
     "To show photographs of famous authors",
     "To list definitions of vocabulary words in alphabetical order",
     "ข", "Bar graphs visually compare data across discrete categories using bar lengths."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Medium",
     "According to Unit 5, how many countries in the world were surveyed regarding official languages?",
     "50 countries",
     "196 countries",
     "500 countries",
     "1,000 countries",
     "ข", "The bar graph study evaluated official language policies across 196 countries."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Medium",
     "Which language is used as an official language in the highest number of countries?",
     "Spanish",
     "English",
     "French",
     "Mandarin",
     "ข", "English holds official status in more countries globally than any other single language."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Medium",
     "What is an 'official language' of a country?",
     "A secret language known only by government officials",
     "A language legally recognized and used for law, government, and education",
     "Any slang words spoken by teenagers in a nation",
     "A language that has no written alphabet",
     "ข", "An official language is designated by law for government, legislation, and public education."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Easy",
     "What special form of communication is used by people who are deaf or hard of hearing?",
     "Whistle signals",
     "Sign languages",
     "Morse code",
     "Braille printing",
     "ข", "Sign languages are visual-gestural languages used by deaf and hard-of-hearing communities."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Medium",
     "Are sign languages identical across all countries worldwide?",
     "Yes, there is only one universal sign language everywhere.",
     "No, different countries have distinct sign languages (e.g., ASL, BSL).",
     "Yes, all sign languages use English spelling rules.",
     "No, sign languages are only used in hospitals.",
     "ข", "Sign languages vary by country and region, such as American Sign Language (ASL) and British Sign Language (BSL)."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Hard",
     "If a country has 'no official language', what does this mean?",
     "Nobody in that country is allowed to speak.",
     "The government has not legally designated one single language above all others.",
     "The country has banned foreign books.",
     "Only sign language is spoken there.",
     "ข", "It means no single language is legally codified as the sole official national language."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Medium",
     "How does a bar graph help a reader understand statistical data faster than paragraph text?",
     "It presents numerical comparisons in a clear visual format.",
     "It replaces all facts with imaginary stories.",
     "It uses smaller font sizes to save paper.",
     "It translates all numbers into roman numerals.",
     "ก", "Visual comparison of bar lengths allows readers to digest relative values immediately."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Easy",
     "Which country brought the Spanish language to Mexico centuries ago?",
     "England",
     "Spain",
     "France",
     "Italy",
     "ข", "Colonizers and settlers from Spain introduced Spanish to Mexico."),

    ("Bar Graphs & Global Languages", "LO-RW3", "Medium",
     "Why do many people in the United States speak English?",
     "English originated natively in North America.",
     "Settlers from England brought the English language to North America.",
     "The United States passed a law banning all other languages.",
     "English was created by American scientists in 1900.",
     "ข", "English was brought to North America by English settlers and historical migration."),

    # 31-40: Making Predictions ("The Mystery Pencil" & Language Dynamics)
    ("Make Predictions", "LO-RW4", "Easy",
     "What is a 'prediction' in reading comprehension?",
     "A exact summary of what happened in chapter one",
     "A sensible guess about what will happen next based on clues and knowledge",
     "A list of grammatical errors found in a passage",
     "The author's biography on the back cover",
     "ข", "A prediction is an educated anticipation of future plot events using textual clues."),

    ("Make Predictions", "LO-RW4", "Medium",
     "What clues should a reader use to make accurate predictions?",
     "Only the total page count of the book",
     "Story clues, character actions/dialogue, and personal background knowledge",
     "Random guesses without looking at the text",
     "The color of the book cover illustration",
     "ข", "Good predictions blend textual evidence (clues, behavior) with real-world knowledge."),

    ("Make Predictions", "LO-RW4", "Medium",
     "In 'The Mystery Pencil', why did Rosa ask Erico so many rapid questions?",
     "She was angry at him for breaking her desk.",
     "She was curious and excited to learn about her new classmate.",
     "She was testing him for a school examination.",
     "She didn't know how to speak English properly.",
     "ข", "Rosa was enthusiastic, curious, and talkative upon meeting Erico."),

    ("Make Predictions", "LO-RW4", "Medium",
     "What does the term 'bilingual' mean?",
     "Speaking only one language fluently",
     "Able to speak two languages fluently",
     "Able to write without making spelling mistakes",
     "Learning a language using computer software",
     "ข", "Bilingual refers to fluency in two distinct languages."),

    ("Make Predictions", "LO-RW4", "Easy",
     "What is a 'living language'?",
     "A language that is used by people in daily life and continues to evolve",
     "A language that can speak by itself on television",
     "A language that was invented last year by children",
     "A language that has no written dictionary",
     "ก", "A living language has active native speakers and evolves through daily usage."),

    ("Make Predictions", "LO-RW4", "Easy",
     "What is a 'dead language'?",
     "A language spoken only during nighttime",
     "A language no longer spoken in daily life by any native community",
     "A language that uses numbers instead of letters",
     "A language that exists only in songs",
     "ข", "A dead language (such as Latin) is no longer spoken as a primary native tongue in daily communication."),

    ("Make Predictions", "LO-RW4", "Medium",
     "Which language has the largest number of native speakers in the world?",
     "English",
     "Mandarin Chinese",
     "Spanish",
     "Hindi",
     "ข", "Mandarin Chinese has the highest total number of native speakers globally (~995M)."),

    ("Make Predictions", "LO-RW4", "Medium",
     "Latin is considered an example of a:",
     "Living language spoken in modern supermarkets",
     "Dead language still studied in literature and science but not spoken natively",
     "Newly created digital programming language",
     "Sign language used in South America",
     "ข", "Latin is a classical dead language studied in academic contexts but lacking native speakers."),

    ("Make Predictions", "LO-RW4", "Hard",
     "If only 50 elderly people speak a rare regional language today, what can you predict about its future?",
     "It will become the official language of the United Nations.",
     "It is at high risk of disappearing and becoming a dead language.",
     "Millions of students will start speaking it next year.",
     "It will replace English on the internet.",
     "ข", "With very few elderly speakers remaining, a language faces imminent endangerment and extinction."),

    ("Make Predictions", "LO-RW4", "Medium",
     "What does 'accent' mean when discussing language?",
     "The volume at which someone shouts",
     "A distinctive way of pronouncing words associated with a region or nation",
     "The length of sentences in a written story",
     "The speed at which a person reads out loud",
     "ข", "An accent is a regional or cultural pattern of pronunciation."),

    # 41-50: Process Essay Writing
    ("Process Essay Writing", "LO-RW6", "Easy",
     "What is the main goal of a 'process essay'?",
     "To convince readers to buy a specific product",
     "To explain step-by-step how to do or make something in chronological order",
     "To write a fictional fairy tale about dragons",
     "To describe a personal vacation with emotional poems",
     "ข", "A process essay provides sequential instructions explaining how a task or operation is completed."),

    ("Process Essay Writing", "LO-RW6", "Easy",
     "Which set of transition words is essential for organizing a process essay?",
     "Because, Since, Although, However",
     "First, Next, Then, After that, Finally",
     "Beautiful, Quickly, Red, Heavy",
     "Yesterday, Someday, Never, Always",
     "ข", "Chronological sequence markers (First, Next, Then, Finally) guide step-by-step process writing."),

    ("Process Essay Writing", "LO-RW6", "Medium",
     "Which transition word is most appropriate for starting the very first step of a process?",
     "Finally",
     "First",
     "Meanwhile",
     "In conclusion",
     "ข", "'First' or 'To begin with' introduces the initial step of a procedure."),

    ("Process Essay Writing", "LO-RW6", "Medium",
     "Which transition word signals the final step in a process essay?",
     "First",
     "Secondly",
     "Finally",
     "For example",
     "ค", "'Finally' or 'Lastly' designates the ultimate concluding step of a process."),

    ("Process Essay Writing", "LO-RW6", "Medium",
     "Why are imperative action verbs (e.g., 'Fold', 'Cut', 'Mix') useful in process essays?",
     "They make sentences longer and harder to read.",
     "They give clear, direct instructions to the reader.",
     "They describe feelings and emotions.",
     "They introduce past history facts.",
     "ข", "Action verbs direct the reader precisely on what action to perform at each step."),

    ("Process Essay Writing", "LO-RW6", "Hard",
     "If a process essay skips a step or presents steps out of order, what happens?",
     "The essay becomes more poetic and interesting.",
     "The reader will get confused and fail to achieve the correct result.",
     "The essay automatically wins a writing prize.",
     "The topic changes to a book review.",
     "ข", "Strict chronological sequence is crucial for instructional clarity in process writing."),

    ("Process Essay Writing", "LO-RW6", "Medium",
     "In a process essay explaining 'How to Read a Map', what should be explained first?",
     "How to store the map in your backpack after hiking",
     "How to orient the map with a compass and locate your starting point",
     "What snack to eat when you finish hiking",
     "How to draw a map from memory",
     "ข", "Orienting the map and identifying your starting location is the essential initial step."),

    ("Process Essay Writing", "LO-RW6", "Easy",
     "What type of organizational structure does a process essay follow?",
     "Spatial order",
     "Chronological (time) order",
     "Compare and contrast order",
     "Random order",
     "ข", "Process writing adheres strictly to chronological time sequence."),

    ("Process Essay Writing", "LO-RW6", "Medium",
     "Which sentence uses a sequence transition correctly?",
     "First, stir the soup, and finally wash the vegetables before chopping.",
     "First, wash the vegetables. Next, chop them into small pieces. Finally, add them to the pot.",
     "Finally, turn on the stove. First, serve the hot soup to guests.",
     "Then, wash the pot before you buy vegetables at the market first.",
     "ข", "The steps follow logical sequence: First (wash) -> Next (chop) -> Finally (cook/add)."),

    ("Process Essay Writing", "LO-RW6", "Medium",
     "What should the introduction of a process essay include?",
     "A detailed list of all mistakes you made last year",
     "The purpose of the process and what the reader will accomplish",
     "A secret code that readers must solve",
     "A review of a movie you watched recently",
     "ข", "The intro states the objective of the process and why it is useful or important."),

    # 51-60: Book/Story Review Writing
    ("Book/Story Review Writing", "LO-RW7", "Easy",
     "What is a 'book review'?",
     "A exact copy of all chapters in a book",
     "A written evaluation expressing an opinion, summary, and recommendation about a book",
     "A list of grammatical spelling rules for authors",
     "A legal contract between a printer and a publisher",
     "ข", "A review analyzes, summarizes, evaluates, and recommends a literary work."),

    ("Book/Story Review Writing", "LO-RW7", "Easy",
     "What are the main structural parts of a standard book review?",
     "Headline, Advertisements, Coupon",
     "Introduction (Summary), Body (Likes/Dislikes), Conclusion (Recommendation)",
     "Chapter 1, Chapter 2, Index",
     "Vocabulary list, Grammar notes, Quiz",
     "ข", "Reviews follow Intro/Summary -> Body evaluation -> Conclusion recommendation format."),

    ("Book/Story Review Writing", "LO-RW7", "Medium",
     "Which phrases are commonly used in a review body paragraph to introduce supporting examples?",
     "First of all, Secondly",
     "For example, For instance",
     "In spite of, Nevertheless",
     "Once upon a time, Long ago",
     "ข", "'For example' and 'For instance' introduce specific text evidence supporting opinions."),

    ("Book/Story Review Writing", "LO-RW7", "Medium",
     "What belongs in the summary section of a book review?",
     "A complete spoiler of the ending twist",
     "A brief overview of the main plot, characters, and setting without spoiling the ending",
     "A detailed list of the author's family background",
     "The price of the book at different bookstores",
     "ข", "Summaries provide basic plot/character context while preserving resolution surprises."),

    ("Book/Story Review Writing", "LO-RW7", "Medium",
     "Where in a review should the writer state their final recommendation and rating?",
     "In the very first sentence of the title",
     "In the body paragraph describing character names",
     "In the conclusion paragraph",
     "In a footnote at the bottom of page 10",
     "ค", "The conclusion summarizes final thoughts and delivers the final recommendation."),

    ("Book/Story Review Writing", "LO-RW7", "Medium",
     "Which statement expresses an opinion suitable for a book review?",
     "The book has 124 pages and 8 chapters.",
     "The author's description of the foggy setting makes the story incredibly exciting.",
     "The book was published in London in 2020.",
     "The main character is named Jaya.",
     "ข", "Evaluative opinions highlight strengths like vivid setting descriptions."),

    ("Book/Story Review Writing", "LO-RW7", "Hard",
     "Why should a reviewer include both likes and dislikes in a balanced review?",
     "To make the review look twice as long",
     "To give a fair, honest, and objective evaluation of the work",
     "Because the publisher requires equal word counts",
     "To confuse readers so they buy two books",
     "ข", "Addressing both strengths and minor drawbacks establishes credibility and fairness."),

    ("Book/Story Review Writing", "LO-RW7", "Medium",
     "Which phrase is used to introduce a recommendation in a review?",
     "I strongly recommend this book to readers who enjoy outdoor mysteries.",
     "First, open the front cover of the book.",
     "In line 4, the word bench is a noun.",
     "The bar graph shows 196 countries.",
     "ก", "Recommending target audiences is a key function of review conclusions."),

    ("Book/Story Review Writing", "LO-RW7", "Easy",
     "What should a reviewer avoid doing in a book review summary?",
     "Mentioning the main characters' names",
     "Giving away the entire secret ending (spoilers)",
     "Describing the main setting",
     "Mentioning the main genre of the book",
     "ข", "Revealing major plot climaxes or endings ruins the reading experience for potential readers."),

    ("Book/Story Review Writing", "LO-RW7", "Medium",
     "Which sentence demonstrates proper use of 'for instance' in a review?",
     "The plot is fast-paced. For instance, in chapter two the characters get trapped in a foggy cave.",
     "For instance, I read the book yesterday at school.",
     "I didn't like the book for instance it was too expensive.",
     "For instance, the author wrote a process essay.",
     "ก", "'For instance' correctly introduces a specific plot event demonstrating fast pacing.")
]

# Write MCQs
for idx, item in enumerate(mcqs, start=1):
    topic, lo, diff, prompt, opt_a, opt_b, opt_c, opt_d, ans, exp = item
    md_content += f"""#### ข้อ {idx}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Prompt**: {prompt}
* ก. {opt_a}
* ข. {opt_b}
* ค. {opt_c}
* ง. {opt_d}
* **Correct Answer**: {ans}
* **Explanation**: {exp}

"""

md_content += """---

# Section B: True / False Questions (ถูก / ผิด)

<!--
RULES Section B:
- ข้อ 61–90 (30 ข้อ, 1 คะแนน/ข้อ)
- คำตอบ: True | False เท่านั้น
-->

"""

# Generating 30 True/False questions (61-90)
tf_questions = [
    # 61-68: Setting Analysis
    ("Setting Analysis", "LO-RW1", "Easy", "The setting of a story includes both the physical location and the time period.", "True", "Setting encompasses where and when story events take place."),
    ("Setting Analysis", "LO-RW1", "Easy", "In 'Lost and Found', Jaya's family planned to picnic near a lighthouse.", "False", "They planned to picnic on a hill with a tall, crooked tree on top, not near the lighthouse."),
    ("Setting Analysis", "LO-RW1", "Medium", "The thick fog in 'Lost and Found' made it difficult for the family to see landmarks from the main trail.", "True", "Fog obscured their view of surrounding hills and landmarks."),
    ("Setting Analysis", "LO-RW1", "Medium", "Mom used the lighthouse to determine which direction was North.", "False", "Mom used the lighthouse to determine which direction was South."),
    ("Setting Analysis", "LO-RW1", "Medium", "When Jaya and her family climbed above the fog line, the hilltop looked like an island in a sea of clouds.", "True", "The white fog below made the hilltop appear surrounded like an island."),
    ("Setting Analysis", "LO-RW1", "Easy", "Setting has no effect on character feelings or plot choices in narrative stories.", "False", "Setting heavily influences character emotions, challenges, and decisions."),
    ("Setting Analysis", "LO-RW1", "Medium", "A long wooden bench on the left side of the trail helped the family realize they were on the wrong path.", "True", "Passing the bench at nearly noon signaled they had hiked off their planned route."),

    # 69-75: Visuals & Orienteering
    ("Use Visuals", "LO-RW2", "Easy", "Visuals in reading texts include pictures, diagrams, maps, and bar graphs.", "True", "Visual elements encompass all non-textual graphical aids that support comprehension."),
    ("Use Visuals", "LO-RW2", "Medium", "Orienteering is an indoor sport where players use dice to move across a printed board.", "False", "Orienteering is an outdoor navigational sport using physical maps and compasses in nature."),
    ("Use Visuals", "LO-RW2", "Easy", "Racers in orienteering events use a map and compass to find control points.", "True", "Navigation rely strictly on map and compass skills."),
    ("Use Visuals", "LO-RW2", "Medium", "Control flags in orienteering are typically solid green and blue squares.", "False", "Control flags are split diagonally into orange and white."),
    ("Use Visuals", "LO-RW2", "Medium", "Lighthouses use bright lamps and loud fog horns to warn ships away from dangerous shores during fog.", "True", "Lighthouses combine powerful lights and acoustic signals to guide maritime traffic."),
    ("Use Visuals", "LO-RW2", "Easy", "Lighthouses are built in dense city centers to guide car traffic.", "False", "Lighthouses are built on coastal shorelines and cliffs to warn ships at sea."),

    # 76-82: Bar Graphs & Global Languages
    ("Bar Graphs & Global Languages", "LO-RW3", "Easy", "A bar graph uses rectangular bars to compare quantities across different categories.", "True", "Bar graphs visually display statistical comparisons using bar height/length."),
    ("Bar Graphs & Global Languages", "LO-RW3", "Medium", "English is an official language in more countries than French or Spanish.", "True", "Statistical bar graphs show English holds official status in the highest number of nations."),
    ("Bar Graphs & Global Languages", "LO-RW3", "Medium", "Sign language is identical and universal in every country across the globe.", "False", "Sign languages vary regionally (ASL, BSL, Auslan, etc.)."),
    ("Bar Graphs & Global Languages", "LO-RW3", "Easy", "An official language is a language legally designated by a government for public use.", "True", "Official languages are legally codified for laws, education, and government affairs."),
    ("Bar Graphs & Global Languages", "LO-RW3", "Medium", "If a country has no official language, citizens are not allowed to speak any language.", "False", "It simply means no single language is legally codified as the sole official national language."),
    ("Bar Graphs & Global Languages", "LO-RW3", "Medium", "Spanish was introduced to Mexico by settlers and colonizers from Spain.", "True", "Historical contact brought Spanish from Spain to Mexico."),
    ("Bar Graphs & Global Languages", "LO-RW3", "Easy", "Bar graphs make it harder to compare data than reading long text paragraphs.", "False", "Bar graphs provide visual clarity, making numerical comparison faster and easier."),

    # 83-87: Predictions & Language Dynamics
    ("Make Predictions", "LO-RW4", "Easy", "A prediction in reading is a logical guess about future events based on clues and knowledge.", "True", "Predictions combine text clues with personal background knowledge."),
    ("Make Predictions", "LO-RW4", "Medium", "Mandarin Chinese has the largest number of native speakers in the world.", "True", "Mandarin boasts the highest total of native speakers globally (~995M)."),
    ("Make Predictions", "LO-RW4", "Easy", "A 'dead language' is a language actively spoken every day by millions of children.", "False", "A dead language (like Latin) is no longer spoken in daily life by a native community."),
    ("Make Predictions", "LO-RW4", "Medium", "Bilingualism refers to the ability to speak two languages fluently.", "True", "Bilingual means fluent in two languages."),
    ("Make Predictions", "LO-RW4", "Hard", "If a language has only 20 elderly speakers left, we can predict it will quickly become a dead language.", "True", "Extinction risk is extremely high when native speakers diminish to a tiny elderly population."),

    # 88-90: Writing Skills
    ("Process Essay Writing", "LO-RW6", "Easy", "Process essays explain how to do or make something using step-by-step chronological order.", "True", "Process writing details sequential instructions clearly."),
    ("Process Essay Writing", "LO-RW6", "Medium", "Transition words like 'First', 'Next', 'Then', and 'Finally' are used in process essays to signal sequence.", "True", "Sequence transitions guide readers through chronological steps."),
    ("Book/Story Review Writing", "LO-RW7", "Medium", "A book review conclusion should always reveal the secret twist ending of the story.", "False", "Review conclusions should summarize recommendations without spoiling ending surprises.")
]

for idx, item in enumerate(tf_questions, start=61):
    topic, lo, diff, stmt, ans, exp = item
    md_content += f"""#### ข้อ {idx}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Statement**: "{stmt}"
* **Correct Answer**: {ans}
* **Explanation**: {exp}

"""

md_content += """---

# Section C: Scenario-Based Questions (สถานการณ์จำลอง)

<!--
RULES Section C:
- ข้อ 91–105 (15 ข้อ, 2 คะแนน/ข้อ)
- โจทย์แบบสร้างสถานการณ์ (Scenario)
-->

"""

# Generating 15 Scenario questions (91-105)
scenarios = [
    # 91
    ("Setting Analysis Scenario", "LO-RW1", "Hard",
     "Nop and his brother are reading a mystery story set in a deserted, creepy castle on a dark midnight during a thunderstorm. Nop predicts the characters will feel relaxed and go for a sunny picnic.",
     "Why is Nop's prediction illogical based on the setting?",
     "Nop ignored the setting details (dark midnight, creepy deserted castle, thunderstorm) which evoke fear and tension, not relaxed sunny picnics.",
     "The setting (dark midnight, storm, creepy castle) creates fear and danger. A logical prediction would be that characters feel scared, encounter mysteries, or seek shelter."),

    # 92
    ("Setting Analysis Scenario", "LO-RW1", "Hard",
     "In 'Lost and Found', Jaya's family realizes they cannot see the landmark crooked tree because heavy fog has rolled into the valley. Mom decides to hike up a smaller nearby hill.",
     "How does the setting directly influence Mom's decision?",
     "The fog obscured ground landmarks in the valley, forcing Mom to move to higher elevation above the fog layer to regain visibility.",
     "Because fog trapped in the valley blocked their view, climbing higher allowed them to get above the fog line and locate nearby landmarks."),

    # 93
    ("Orienteering Navigation Scenario", "LO-RW2", "Hard",
     "Suda is participating in her first outdoor orienteering race. She has a course map and a compass. At control point #3, she sees a dense pine forest on her left and a large boulder on her right.",
     "How should Suda use her visuals (map) and tools (compass) to reach control point #4?",
     "She should align her map with her compass needle pointing North, locate boulder and forest symbols on the map, and follow the directional bearing to #4.",
     "Suda must orient the map to magnetic North using her compass, match the boulder and forest landmarks to map symbols, and follow the map's vector toward control #4."),

    # 94
    ("Lighthouse Fog Warning Scenario", "LO-RW2", "Hard",
     "Captain Thorne is steering a cargo ship near a rocky coastline at night when sudden thick fog reduces visibility to zero. Suddenly, he hears a loud repeating horn and sees a sweeping beam of light.",
     "What visual/auditory landmark is Captain Thorne encountering, and what action should he take?",
     "He is encountering a lighthouse warning signal; he must alter his ship's course away from the shore to prevent crashing into rocks.",
     "The lighthouse horn and light warn of dangerous coastal rocks. Captain Thorne must steer away from the coast into deeper safe waters."),

    # 95
    ("Bar Graph Analysis Scenario", "LO-RW3", "Hard",
     "A student looks at a bar graph titled 'Official Languages of 196 Countries'. The bar for English reaches 59, French reaches 29, Arabic reaches 26, and Spanish reaches 21.",
     "What clear statistical conclusions can the student draw from this graph?",
     "English is the official language in the greatest number of countries (59), while French is second (29), followed by Arabic and Spanish.",
     "The bar graph visually shows English leads worldwide with 59 countries, nearly double that of French (29), Arabic (26), and Spanish (21)."),

    # 96
    ("Sign Language Communication Scenario", "LO-RW3", "Hard",
     "An international student from Japan who uses Japanese Sign Language (JSL) meets an American student who uses American Sign Language (ASL). They find that some hand signs are different.",
     "Why do JSL and ASL have different sign gestures despite both being sign languages?",
     "Because sign languages are independent, full languages developed within specific cultural regions, not a single universal code.",
     "Sign languages developed naturally within distinct national cultures, so JSL and ASL have unique vocabularies and grammar rules."),

    # 97
    ("Language Classification Scenario", "LO-RW5", "Hard",
     "Professor Miller explains that ancient Latin was spoken by Romans 2,000 years ago, but today no country uses Latin as its native daily spoken language. Meanwhile, Mandarin is spoken daily by nearly 1 billion people.",
     "How should a student classify Latin versus Mandarin based on these facts?",
     "Latin is classified as a dead language, whereas Mandarin is classified as a living language with the world's largest native speaker population.",
     "Latin is a dead language because it lacks native daily speakers; Mandarin is a living language actively spoken by daily communities."),

    # 98
    ("Bilingual Prediction Scenario", "LO-RW4", "Hard",
     "In a classroom story, Erico moved from Brazil to London. He speaks both Portuguese and English fluently. His classmate Rosa asks if he can help translate a letter from Lisbon.",
     "What prediction can you make about Erico's ability to help, and why?",
     "Erico will be able to translate it because Portuguese is the native language of both Brazil and Portugal, and he is bilingual.",
     "Because Erico is bilingual in Portuguese and English, and Portuguese is spoken in Portugal (Lisbon), he can easily translate the letter."),

    # 99
    ("Process Essay Order Scenario", "LO-RW6", "Hard",
     "Kanya is writing a process essay titled 'How to Pack a Hiking Backpack'. She writes: 'Finally, put heavy items at the bottom. First, adjust the shoulder straps. Next, close the zipper.'",
     "What is wrong with Kanya's process essay, and how should she revise it?",
     "Her chronological sequence is scrambled. She should start with 'First, put heavy items at the bottom...', followed by packing, closing zippers, and finally adjusting straps.",
     "The steps are out of logical order. She must place heavy gear at the bottom first, pack lighter gear next, zip up, and finally adjust shoulder straps."),

    # 100
    ("Process Essay Transition Scenario", "LO-RW6", "Hard",
     "A student wants to write a process essay explaining how to navigate using a compass. He has listed 4 steps: 1. Hold compass flat. 2. Turn housing until N aligns with needle. 3. Look at direction arrow. 4. Walk toward target.",
     "How can he connect these 4 steps into a clear instructional paragraph using transition words?",
     "By using sequence words: 'First, hold compass flat. Next, turn housing until N aligns with needle. Then, look at direction arrow. Finally, walk toward target.'",
     "Use transitions: First, hold the compass flat. Next, turn the dial until N matches the needle. Then, read your directional arrow. Finally, walk towards your target."),

    # 101
    ("Book Review Summary Scenario", "LO-RW7", "Hard",
     "In her draft book review of 'The Mystery Pencil', May writes 3 full pages summarizing every single event, including how the detective catches the thief on the final page.",
     "What critical mistake did May make in her review summary, and how should she fix it?",
     "She included major spoilers and gave away the ending. She should shorten the summary and leave the resolution secret.",
     "May included plot spoilers by revealing the ending. A good summary provides premise and conflict without revealing the climax or mystery resolution."),

    # 102
    ("Book Review Example Usage Scenario", "LO-RW7", "Hard",
     "Tom writes in his book review: 'I found the main character very funny.' He wants to add specific evidence from the story to support this opinion.",
     "How can Tom use the phrase 'for example' or 'for instance' to strengthen his review body paragraph?",
     "He should write: 'I found the main character very funny. For example, in chapter three he accidentally wore two different shoes to school and made everyone laugh.'",
     "Tom can state: 'The character is very funny. For instance, in chapter 3 he makes hilarious jokes while trying to pitch a tent in the fog.'"),

    # 103
    ("Book Review Conclusion Scenario", "LO-RW7", "Hard",
     "Ploy has written her summary and body paragraphs evaluating a mystery novel's plot and characters. She is now writing her final concluding paragraph.",
     "What key elements must Ploy include to complete her book review conclusion effectively?",
     "She must state her final overall opinion, deliver a clear recommendation (who should read it), and provide a star rating.",
     "The conclusion must summarize her overall impression, give a recommendation on who would enjoy the book, and state a final rating."),

    # 104
    ("Predicting Character Action Scenario", "LO-RW4", "Hard",
     "In a story, Manoj drops his map while hiking in a windy, foggy forest. He sees the wind blowing the map toward a steep cliff edge.",
     "Based on story context and safety knowledge, what should Manoj predict and do?",
     "Manoj should not chase the map dangerously close to the cliff edge; he should stay safe with his family and rely on visible landmarks or Mom's guidance.",
     "Manoj should prioritize safety over the lost map, stay back from the cliff, and work with his family to navigate using landmarks."),

    # 105
    ("Visual vs Text Analysis Scenario", "LO-RW2", "Hard",
     "An article about orienteering describes how racers run through forests. Next to the text is a diagram showing a map grid with contour lines, scale bar, and control legend.",
     "What specific information does the visual diagram provide that text paragraphs usually omit?",
     "The exact scale ratio (e.g., 1:10,000), contour line elevation intervals, and precise geometric control symbols.",
     "The diagram provides exact spatial measurements, elevation contours, scale ratios, and graphic map legends not easily detailed in prose text.")
]

for idx, item in enumerate(scenarios, start=91):
    topic, lo, diff, scen, q, ans, exp = item
    md_content += f"""#### ข้อ {idx}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Scenario**: {scen}
* **Question**: {q}
* **Answer**: {ans}
* **Explanation**: {exp}

"""

md_content += """---

# Section D: Short Answer Questions (อัตนัย / อธิบายความรู้)

<!--
RULES Section D:
- ข้อ 106–115 (10 ข้อ, 3 คะแนน/ข้อ)
- โจทย์แบบอัตนัย เขียนอธิบายแนวคำตอบ
-->

"""

# Generating 10 Short Answer questions (106-115)
short_answers = [
    ("Analyze Story Setting", "LO-RW1", "Medium",
     "Explain how the foggy weather setting in 'Lost and Found' created both a problem and a resolution for Jaya and her family.",
     "Problem: The thick fog obscured valley landmarks, causing the family to take a wrong turn onto a smaller hill near a bench. Resolution: Climbing higher up the small hill took them above the fog line, allowing them to see the lighthouse (South) and spot their target hill with the crooked tree (Northeast)."),

    ("Importance of Reading Visuals", "LO-RW2", "Medium",
     "Why are visual aids like maps, diagrams, and compasses essential in informational texts such as 'The World of Orienteering'?",
     "Visual aids provide spatial relationships, geographic scale, and exact directional details that written words alone cannot convey quickly. In orienteering, maps and compasses allow readers to visualize how racers locate checkpoints and navigate terrain accurately."),

    ("Bar Graph Interpretation", "LO-RW3", "Medium",
     "Explain the main insights provided by a bar graph showing the official languages of 196 countries, and why some countries have multiple official languages.",
     "The bar graph highlights global language distribution, showing English as official in the highest number of nations (59), followed by French and Spanish. Countries may adopt multiple official languages due to diverse ethnic populations, colonial history, or cultural heritage."),

    ("Living vs. Dead Languages", "LO-RW5", "Medium",
     "Compare and contrast 'living languages' and 'dead languages'. Provide one example of each from your reading.",
     "Living languages (e.g., Mandarin Chinese) are actively spoken in daily life by native communities and continue to evolve. Dead languages (e.g., Latin) are no longer spoken as a primary native language in daily communication, though they may still be studied academically."),

    ("Predicting Text Outcomes", "LO-RW4", "Medium",
     "Describe the process of making a reading prediction. What two main sources of information must a reader combine to make an accurate prediction?",
     "To make an accurate prediction, a reader must combine: 1) Textual clues (character dialogue, actions, foreshadowing details) with 2) Personal background knowledge (real-world experience and logic) to anticipate reasonable plot outcomes."),

    ("Process Essay Structure", "LO-RW6", "Medium",
     "Outline the essential structural components and key transition words needed to write an effective process essay.",
     "A process essay requires: 1) An introduction stating the goal/purpose of the process, 2) Body paragraphs detailing steps in strict chronological order using sequence transition words (First, Next, Then, After that, Finally), and 3) A conclusion summarizing the final result or tip."),

    ("Writing a Balanced Book Review", "LO-RW7", "Medium",
     "Explain the main sections of a book review and why it is important to include both likes and minor dislikes in the body paragraph.",
     "A book review includes an Introduction (summary), Body (evaluation of strengths and weaknesses), and Conclusion (recommendation/rating). Including both likes and dislikes creates a fair, balanced, and credible evaluation that helps readers decide if the book suits them."),

    ("Role of Lighthouses in Maritime Safety", "LO-RW2", "Medium",
     "Based on the non-fiction reading passage, explain how lighthouses protect ships near rocky shorelines during severe fog.",
     "Lighthouses built on coastal shores operate high-powered lamps that shine beams far across the ocean and blast loud fog horns when fog rolls in. These visual and sound signals warn ship captains of shallow waters and rocky shorelines, preventing shipwrecks."),

    ("Using Example Transitions in Writing", "LO-RW7", "Medium",
     "Write two original sentences demonstrating how to use 'for example' and 'for instance' to support an opinion about a book's characters or setting.",
     "Example 1: 'The setting of the story is exceptionally scary; for example, the author describes a dark, howling wind blowing through the abandoned castle.' Example 2: 'The main character is very brave; for instance, she steps into the foggy forest alone to save her lost puppy.'"),

    ("Sign Language and Linguistic Diversity", "LO-RW3", "Medium",
     "Discuss the importance of sign languages in society and explain why sign language is considered a true language rather than just simple hand gestures.",
     "Sign languages (such as ASL) are vital visual-gestural languages that allow deaf and hard-of-hearing individuals to communicate fully. They are true languages because they possess complex grammar, syntax, extensive vocabulary, and regional variations, just like spoken languages.")
]

for idx, item in enumerate(short_answers, start=106):
    topic, lo, diff, q, exp_ans = item
    md_content += f"""#### ข้อ {idx}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Prompt**: {q}
* **Expected Answer**: {exp_ans}

"""

# Write to file
target_file = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_Reading_with_Writing_Gr6.md"
with open(target_file, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Successfully generated {target_file}")

# Also copy/write to Knowledge_Assessment_Reading with Writing_GR6.md
alt_file1 = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_Reading with Writing_GR6.md"
with open(alt_file1, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"Successfully generated {alt_file1}")

alt_file2 = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_Reading_with_Writing_GR6.md"
with open(alt_file2, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"Successfully generated {alt_file2}")

