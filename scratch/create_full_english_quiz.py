import os

file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_English_Gr6.md"

header = """# Knowledge Assessment Quiz: ภาษาอังกฤษ ชั้นประถมศึกษาปีที่ 6 (ชุดข้อสอบประเมินผลกลางภาค/ปลายภาค)

---

## Document Summary (สรุปเนื้อหาเอกสารและหลักสูตรภาษาอังกฤษ ป.6)

เอกสารฉบับนี้รวบรวมเนื้อหาและโจทย์ประเมินผลการเรียนรู้กลุ่มสาระการเรียนรู้ภาษาต่างประเทศ (ภาษาอังกฤษ) ระดับชั้นประถมศึกษาปีที่ 6 ครอบคลุมสาระสำคัญ 6 หน่วยการเรียนรู้หลัก ได้แก่:

### 1. หน่วยการเรียนรู้ที่ 1: ไวยากรณ์และโครงสร้างประโยค (Grammar & Sentence Structures)
* **Tenses**: Present Simple, Present Continuous, Past Simple, Future Simple (will / be going to) และ Present Perfect
* **Parts of Speech**: คำนาม (Countable/Uncountable), คำสรรพนาม (Subject/Object/Possessive), คำคุณศัพท์และคำกริยาวิเศษณ์ การเปรียบเทียบขั้นกว่าและขั้นสุด (Comparatives & Superlatives)
* **Prepositions & Quantifiers**: คำบุพบทบอกเวลาและสถานที่ (in, on, at, under, behind, next to) และคำบอกปริมาณ (some, any, much, many, a few, a little)

### 2. หน่วยการเรียนรู้ที่ 2: คำศัพท์หมวดชีวิตประจำวัน อาชีพ และสุขภาพ (Daily Life, Jobs & Health)
* **กิจกรรมประจำวันและงานอดิเรก**: Daily routines, hobbies, free time activities
* **อาชีพและสถานที่ทำงาน**: Jobs, occupations, workplaces (doctor, firefighter, pilot, chef, engineer)
* **อาการเจ็บป่วยและสุขภาพ**: Health symptoms, illnesses, giving advice (headache, fever, stomachache, sore throat, should/shouldn't)

### 3. หน่วยการเรียนรู้ที่ 3: สถานที่ ทิศทาง และสภาพอากาศ (Places, Directions & Weather)
* **การถามทางและบอกทิศทาง**: Turn left, turn right, go straight ahead, opposite, next to, between
* **สภาพอากาศและสิ่งแวดล้อม**: Weather conditions, seasons, natural disasters, saving the environment

### 4. หน่วยการเรียนรู้ที่ 4: อาหาร เครื่องดื่ม และการซื้อขาย (Food, Drinks & Shopping)
* **อาหาร รสชาติ และการปรุง**: Food items, taste (sweet, sour, salty, spicy, bitter), cooking verbs
* **การซื้อของและราคา**: Asking prices (How much is/are...?), money, sizes, shopping dialogues

### 5. หน่วยการเรียนรู้ที่ 5: สำนวนการสื่อสารและป้ายสัญลักษณ์ (Expressions & Signs)
* **การสื่อสารในชีวิตประจำวัน**: Classroom expressions, greetings, offering help, asking permission, apologizing
* **ป้ายเตือนและสัญลักษณ์**: Traffic signs, safety signs, public notices (No Swimming, Quiet Please, Danger)

### 6. หน่วยการเรียนรู้ที่ 6: วัฒนธรรมเจ้าของภาษาและการอ่านจับใจความ (Culture & Reading Comprehension)
* **เทศกาลตะวันตก**: Christmas, Halloween, Thanksgiving, Easter, Valentine's Day
* **การอ่านบทความจับใจความ**: Short reading passages, identifying main ideas, details, and context clues

---

## Learning Objectives Mapping (แผนผังจุดประสงค์การเรียนรู้)

* **LO-ENG1**: ความรู้ความเข้าใจคำศัพท์ โครงสร้างไวยากรณ์ และป้ายสัญลักษณ์พื้นฐาน (Remember / Understand)
* **LO-ENG2**: การประยุกต์ใช้ Tenses คำบุพบท คำลักษณนาม และประโยคในภาษาอังกฤษ (Apply)
* **LO-ENG3**: การวิเคราะห์บทอ่าน โครงสร้างประโยคซับซ้อน และการเปรียบเทียบ (Analyze)
* **LO-ENG4**: การสื่อสารในสถานการณ์จำลอง การให้คำแนะนำ มารยาท และวัฒนธรรมตะวันตก (Evaluate / Create / Culture)

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

mcq_questions = [
    # 1-15: Grammar (Tenses, Pronouns, Prepositions)
    (1, "ไวยากรณ์ (Tenses)", "LO-ENG1", "Easy",
     "She ________ to school by bus every morning.",
     "go", "goes", "went", "going", "ข",
     "ประธาน She เป็นเอกพจน์ กริยาใน Present Simple Tense ต้องเติม s/es ดังนั้นจึงใช้ goes"),

    (2, "ไวยากรณ์ (Tenses)", "LO-ENG1", "Easy",
     "Look! The children ________ football in the playground right now.",
     "play", "played", "are playing", "will play", "ค",
     "คำว่า right now แสดงถึงเหตุการณ์ที่กำลังเกิดขึ้นในขณะนี้ จึงใช้ Present Continuous (are playing)"),

    (3, "ไวยากรณ์ (Tenses)", "LO-ENG2", "Medium",
     "Yesterday, Tom ________ a new bicycle at the mall.",
     "buy", "buys", "bought", "has bought", "ค",
     "คำว่า Yesterday แสดงถึงอดีตใน Past Simple Tense กริยาช่อง 2 ของ buy คือ bought"),

    (4, "ไวยากรณ์ (Tenses)", "LO-ENG2", "Medium",
     "They ________ to Japan next month. They have already booked the tickets.",
     "visit", "visited", "are going to visit", "have visited", "ค",
     "การวางแผนล่วงหน้าชัดเจน (booked tickets) ใช้ be going to (are going to visit) สำหรับอนาคต"),

    (5, "คำสรรพนาม (Pronouns)", "LO-ENG1", "Easy",
     "This is Mary's book. It belongs to ________.",
     "she", "her", "hers", "herself", "ข",
     "หลังคำบุพบท to ต้องใช้ Object Pronoun ของ Mary (she) คือ her"),

    (6, "คำบุพบท (Prepositions)", "LO-ENG1", "Easy",
     "My birthday is ________ July 15th.",
     "in", "on", "at", "by", "ข",
     "การระบุวันที่เฉพาะเจาะจง (July 15th) ต้องใช้คำบุพบท on"),

    (7, "คำบุพบท (Prepositions)", "LO-ENG1", "Easy",
     "We usually have lunch ________ 12:30 p.m.",
     "in", "on", "at", "for", "ค",
     "การระบุเวลาบนหน้าฬิกา (12:30 p.m.) ต้องใช้คำบุพบท at"),

    (8, "คำบอกปริมาณ (Quantifiers)", "LO-ENG2", "Medium",
     "There isn't ________ milk left in the refrigerator.",
     "some", "any", "many", "few", "ข",
     "ประโยคปฏิเสธ (isn't) และคำนามนับไม่ได้ (milk) ต้องใช้ any"),

    (9, "คำบอกปริมาณ (Quantifiers)", "LO-ENG2", "Medium",
     "How ________ students are there in your classroom?",
     "much", "many", "long", "often", "ข",
     "ถามจำนวนคำนามนับได้พหูพจน์ (students) ต้องใช้ How many"),

    (10, "การเปรียบเทียบ (Comparatives)", "LO-ENG2", "Medium",
     "An elephant is ________ than a tiger.",
     "big", "bigger", "biggest", "more big", "ข",
     "การเปรียบเทียบขั้นกว่า (มี than) สำหรับพยางค์เดียว ให้เบิ้ลพยัญชนะท้ายแล้วเติม -er -> bigger"),

    (11, "การเปรียบเทียบ (Superlatives)", "LO-ENG2", "Medium",
     "Mount Everest is the ________ mountain in the world.",
     "high", "higher", "highest", "most high", "ค",
     "การเปรียบเทียบขั้นสุด (มี the) ใช้ highest"),

    (12, "คำกริยานุเคราะห์ (Modal Verbs)", "LO-ENG2", "Easy",
     "You ________ stop when the traffic light turns red.",
     "must", "may", "can", "might", "ก",
     "การแสดงกฎข้อบังคับที่จำเป็นต้องปฏิบัติตาม ใช้คำกริยานุเคราะห์ must"),

    (13, "คำกริยานุเคราะห์ (Modal Verbs)", "LO-ENG2", "Medium",
     "If you have a toothache, you ________ see a dentist.",
     "should", "would", "may", "could", "ก",
     "การให้คำแนะนำ (giving advice) สำหรับผู้ป่วย ปวดฟัน ควรใช้ should (ควรจะ)"),

    (14, "คำเชื่อม (Conjunctions)", "LO-ENG2", "Medium",
     "He was tired, ________ he continued working to finish the project.",
     "so", "because", "but", "or", "ค",
     "ประโยคขัดแย้งกัน (เหนื่อย แต่ยังทำต่อ) ใช้คำเชื่อม but"),

    (15, "ประโยคเงื่อนไข (Conditionals)", "LO-ENG3", "Hard",
     "If it ________ tomorrow, we will stay at home and watch movies.",
     "rain", "rains", "rained", "will rain", "ข",
     "ประโยคเงื่อนไขแบบที่ 1 (First Conditional: If + Present Simple, Will + V.1) ใช้ rains"),

    # 16-30: Vocabulary (Jobs, Health, Hobbies, Places)
    (16, "คำศัพท์หมวดอาชีพ", "LO-ENG1", "Easy",
     "A person who puts out fires and saves people is a ________.",
     "policeman", "firefighter", "pilot", "dentist", "ข",
     "คนที่ดับเพลิงและช่วยชีวิตคนคือ firefighter (พนักงานดับเพลิง)"),

    (17, "คำศัพท์หมวดอาชีพ", "LO-ENG1", "Easy",
     "A ________ flies airplanes and travels around the world.",
     "driver", "engineer", "pilot", "chef", "ค",
     "คนที่ขับเครื่องบินคือ pilot (นักบิน)"),

    (18, "คำศัพท์หมวดอาชีพ", "LO-ENG1", "Easy",
     "My uncle works in a restaurant kitchen. He prepares delicious food. He is a ________.",
     "chef", "waiter", "farmer", "doctor", "ก",
     "คนที่ทำอาหารในครัวร้านอาหารคือ chef (พ่อครัว)"),

    (19, "คำศัพท์หมวดสุขภาพ", "LO-ENG1", "Easy",
     "Sam ate too much ice cream. Now he has a ________.",
     "headache", "stomachache", "sore throat", "fever", "ข",
     "กินไอศกรีมมากเกินไป จะปวดท้อง stomachache"),

    (20, "คำศัพท์หมวดสุขภาพ", "LO-ENG1", "Easy",
     "When you have a high body temperature, you have a ________.",
     "fever", "cough", "toothache", "cut", "ก",
     "เมื่อมีอุณหภูมิร่างกายสูง แสดงว่ามีไข้ fever"),

    (21, "คำศัพท์หมวดสถานที่", "LO-ENG1", "Easy",
     "Where do you go to send letters and parcels?",
     "Hospital", "Post office", "Bank", "Police station", "ข",
     "ส่งจดหมายและพัสดุ ต้องไปที่ Post office (ไปรษณีย์)"),

    (22, "คำศัพท์หมวดสถานที่", "LO-ENG1", "Easy",
     "A place where you can borrow and read books for free is a ________.",
     "bookstore", "library", "museum", "school", "ข",
     "สถานที่ยืมและอ่านหนังสือฟรีคือ library (ห้องสมุด)"),

    (23, "คำศัพท์หมวดรสชาติอาหาร", "LO-ENG1", "Easy",
     "Lemons taste ________, while sugar tastes sweet.",
     "salty", "sour", "spicy", "bitter", "ข",
     "มะนาวมีรสเปรี้ยว sour ส่วนน้ำตาลมีรสหวาน sweet"),

    (24, "คำศัพท์หมวดสัตว์", "LO-ENG1", "Easy",
     "Which animal is known as the 'Ship of the Desert'?",
     "Elephant", "Camel", "Horse", "Lion", "ข",
     "เรือแห่งทะเลทราย คือ อูฐ Camel"),

    (25, "คำศัพท์หมวดสภาพอากาศ", "LO-ENG1", "Easy",
     "It is ________ today. Don't forget to take an umbrella with you!",
     "sunny", "rainy", "windy", "snowy", "ข",
     "เตือนให้เอา ร่ม (umbrella) ไป แสดงว่าฝนตก rainy"),

    (26, "คำศัพท์หมวดทิศทาง", "LO-ENG1", "Easy",
     "Go ________ ahead and turn left at the traffic lights.",
     "straight", "right", "back", "around", "ก",
     "ตรงไป ใช้คำว่า Go straight ahead"),

    (27, "คำศัพท์หมวดเวลา", "LO-ENG1", "Easy",
     "A period of ten years is called a ________.",
     "century", "decade", "millennium", "fortnight", "ข",
     "ระยะเวลา 10 ปี เรียกว่า a decade (ทศวรรษ)"),

    (28, "คำศัพท์หมวดอุปกรณ์เรียน", "LO-ENG1", "Easy",
     "We use a ________ to measure length and draw straight lines.",
     "ruler", "scissors", "eraser", "stapler", "ก",
     "ใช้วัดความยาวและตีเส้นตรงคือ ruler (ไม้บรรทัด)"),

    (29, "คำศัพท์หมวดงานบ้าน", "LO-ENG1", "Easy",
     "After dinner, I always help my mother wash the ________.",
     "clothes", "dishes", "floor", "car", "ข",
     "หลังอาหารเย็น ช่วยล้างจาน wash the dishes"),

    (30, "คำศัพท์หมวดพาหนะ", "LO-CH1", "Easy",
     "A large vehicle that carries many passengers on fixed city routes is a ________.",
     "taxi", "bus", "bicycle", "helicopter", "ข",
     "รถขนาดใหญ่รับผู้โดยสารตามเส้นทางคือ bus (รถประจำทาง)"),

    # 31-45: Reading, Signs, Everyday Dialogue
    (31, "ป้ายสัญลักษณ์ (Signs)", "LO-ENG1", "Easy",
     "You see a sign 'NO SWIMMING' at the beach. What does it mean?",
     "You can swim here safely.", "You must not swim here.", "You should buy a swimsuit.", "Swimming is recommended.", "ข",
     "ป้าย NO SWIMMING หมายถึง ห้ามว่ายน้ำบริเวณนี้ (You must not swim here)"),

    (32, "ป้ายสัญลักษณ์ (Signs)", "LO-ENG1", "Easy",
     "A sign showing 'QUIET PLEASE' in a library asks people to ________.",
     "speak loudly", "stop talking and make no noise", "play music", "eat snacks", "ข",
     "ป้าย QUIET PLEASE ขอให้งดใช้เสียงและไม่ส่งเสียงดัง"),

    (33, "ป้ายสัญลักษณ์ (Signs)", "LO-ENG1", "Easy",
     "A sign with 'DON'T FEED THE ANIMALS' at the zoo warns visitors ________.",
     "to give food to animals", "not to give food to animals", "to pet animals", "to clean animal cages", "ข",
     "ป้าย DON'T FEED THE ANIMALS เตือนห้ามให้อาหารสัตว์"),

    (34, "สำนวนบทสนทนา (Dialogues)", "LO-ENG4", "Easy",
     "A: Thank you very much for your help.\nB: ________.",
     "You're welcome", "I'm sorry", "Yes, please", "Never mind", "ก",
     "เมื่อมีคนขอบคุณ Thank you ตอบกลับด้วย You're welcome (ด้วยความยินดี)"),

    (35, "สำนวนบทสนทนา (Dialogues)", "LO-ENG4", "Easy",
     "A: I'm really sorry for breaking your ruler.\nB: ________. It's okay.",
     "That's terrible", "Don't worry about it", "Congratulations", "Excuse me", "ข",
     "เมื่อมีคนขอโทษ I'm sorry ตอบให้อภัยด้วย Don't worry about it (ไม่ต้องกังวล/ไม่เป็นไร)"),

    (36, "สำนวนบทสนทนา (Dialogues)", "LO-ENG4", "Medium",
     "A: Can I borrow your pencil, please?\nB: Sure, ________.",
     "here you are", "no way", "I don't know", "thank you", "ก",
     "เมื่อส่งของให้ยืมตามคำขอ ตอบ Sure, here you are (นี่ครับ/ค่ะ)"),

    (37, "สำนวนบทสนทนา (Dialogues)", "LO-ENG4", "Medium",
     "A: What would you like to order, sir?\nB: ________, please.",
     "I'm ten years old", "I'd like a fried rice and a iced tea", "I go to school by bus", "It's five o'clock", "ข",
     "พนักงานถามรับออเดอร์อาหาร ตอบสั่งอาหาร I'd like a fried rice and a iced tea"),

    (38, "สำนวนบทสนทนา (Dialogues)", "LO-ENG4", "Medium",
     "A: Excuse me, how can I get to the train station?\nB: ________.",
     "It costs ten dollars", "Go straight for two blocks, it's on your left", "Yes, I like trains", "I am going to Bangkok", "ข",
     "ถามทางไปสถานีรถไฟ ตอบบอกทิศทาง Go straight for two blocks, it's on your left"),

    (39, "สำนวนบทสนทนา (Dialogues)", "LO-ENG4", "Medium",
     "A: How much is this blue T-shirt?\nB: ________.",
     "It's size medium", "It's 250 Baht", "It's made of cotton", "It's very nice", "ข",
     "ถามราคา How much is... ตอบระบุราคา It's 250 Baht"),

    (40, "สำนวนบทสนทนา (Dialogues)", "LO-ENG4", "Medium",
     "A: What is the weather like today in London?\nB: ________.",
     "It's Monday", "It's cold and rainy", "I like London", "It's 5:00 p.m.", "ข",
     "ถามสภาพอากาศ What is the weather like... ตอบ It's cold and rainy"),

    # 41-60: Reading Passages & Grammar Analysis
    (41, "การอ่านจับใจความ (Reading)", "LO-ENG3", "Medium",
     "Read the passage: 'Penguins are birds that cannot fly, but they are great swimmers. They live in cold places like Antarctica and eat fish.' What do penguins eat?",
     "Plants", "Fish", "Insects", "Birds", "ข",
     "จากข้อความ '...and eat fish.' อาหารของเพนกวินคือ ปลา (Fish)"),

    (42, "การอ่านจับใจความ (Reading)", "LO-ENG3", "Medium",
     "From the penguin passage, where do penguins live?",
     "In warm tropical forests", "In hot deserts", "In cold places like Antarctica", "In deep rivers", "ค",
     "จากข้อความ 'They live in cold places like Antarctica'"),

    (43, "การอ่านจับใจความ (Reading)", "LO-ENG3", "Medium",
     "Read the note: 'Dear Students, The school library will be closed this Friday for maintenance. Please return all borrowed books by Thursday. Thank you.' Why is the library closed on Friday?",
     "For holiday", "For maintenance", "For sports day", "For exams", "ข",
     "จากข้อความ 'closed this Friday for maintenance' ปิดเพื่อปรับปรุงซ่อมแซม"),

    (44, "การอ่านจับใจความ (Reading)", "LO-ENG3", "Medium",
     "When must students return their borrowed books according to the note?",
     "By Wednesday", "By Thursday", "By Friday", "By Monday next week", "ข",
     "จากข้อความ 'Please return all borrowed books by Thursday'"),

    (45, "วัฒนธรรมตะวันตก (Culture)", "LO-ENG4", "Easy",
     "On Halloween (October 31st), children wear costumes and go door-to-door saying '________!'.",
     "Merry Christmas", "Trick or Treat", "Happy New Year", "Happy Thanksgiving", "ข",
     "เด็กๆ ในวันฮาโลวีนจะพูดคำว่า Trick or Treat"),

    (46, "วัฒนธรรมตะวันตก (Culture)", "LO-ENG4", "Easy",
     "What food is traditionally eaten during Thanksgiving dinner in the USA?",
     "Pizza", "Roast turkey", "Sushi", "Hamburgers", "ข",
     "อาหารดั้งเดิมวันขอบคุณพระเจ้าคือ ไก่งวงอบ Roast turkey"),

    (47, "วัฒนธรรมตะวันตก (Culture)", "LO-ENG4", "Easy",
     "Who brings presents to children on Christmas Eve according to Western legend?",
     "Santa Claus", "Easter Bunny", "Tooth Fairy", "Cupid", "ก",
     "นำของขวัญมาให้ในคืนคริสต์มาสคือ ซานตาคลอส Santa Claus"),

    (48, "ไวยากรณ์ (Passive Voice Basics)", "LO-ENG3", "Hard",
     "The Harry Potter books ________ by J.K. Rowling.",
     "wrote", "were written", "write", "are writing", "ข",
     "ประธานเป็นสิ่งของถูกกระทำ (Passive Voice ในอดีต) ใช้ were written"),

    (49, "ไวยากรณ์ (Question Tags)", "LO-ENG3", "Hard",
     "She is a doctor, ________?",
     "isn't she", "is she", "doesn't she", "does she", "ก",
     "ประโยคหน้าเป็นบอกเล่า (is) Question tag ท้ายประโยคต้องเป็นปฏิเสธ (isn't she?)"),

    (50, "ไวยากรณ์ (Question Tags)", "LO-ENG3", "Hard",
     "You didn't go to school yesterday, ________?",
     "did you", "didn't you", "do you", "don't you", "ก",
     "ประโยคหน้าเป็นปฏิเสธ (didn't) Question tag ท้ายประโยคต้องเป็นบอกเล่า (did you?)"),

    (51, "ไวยากรณ์ (Relative Pronouns)", "LO-ENG3", "Hard",
     "The man ________ lives next door is a famous artist.",
     "who", "which", "where", "whose", "ก",
     "ขยายบุคคล (The man) ทำหน้าที่เป็นประธานของประโยคย่อย ใช้ Relative Pronoun: who"),

    (52, "ไวยากรณ์ (Relative Pronouns)", "LO-ENG3", "Hard",
     "This is the house ________ I was born.",
     "who", "where", "which", "when", "ข",
     "ขยายสถานที่ (the house) ใช้ Relative Pronoun: where"),

    (53, "ไวยากรณ์ (Adverbs of Frequency)", "LO-ENG2", "Medium",
     "Peter ________ arrives late for class because he gets up very early.",
     "always", "never", "often", "usually", "ข",
     "ตื่นเช้ามาก แสดงว่า ไม่เคย มาสาย ใช้ Adverb of frequency: never"),

    (54, "ไวยากรณ์ (Subject-Verb Agreement)", "LO-ENG3", "Hard",
     "Neither John nor his friends ________ coming to the party tonight.",
     "is", "are", "was", "be", "ข",
     "โครงสร้าง Neither A nor B กริยาจะผันตามประธานตัวหลัง (his friends - พหูพจน์) ใช้ are"),

    (55, "ไวยากรณ์ (Subject-Verb Agreement)", "LO-ENG3", "Hard",
     "Every student in the classroom ________ a uniform.",
     "wear", "wears", "wearing", "have worn", "ข",
     "Every + คำนามเอกพจน์ กริยาถือเป็นเอกพจน์ ใช้ wears"),

    (56, "คำศัพท์หมวดอารมณ์ความรู้สึก", "LO-ENG1", "Easy",
     "She was very ________ when she won the first prize in the singing contest.",
     "sad", "excited", "bored", "angry", "ข",
     "ชนะรางวัลที่ 1 จะรู้สึก ตื่นเต้น/ดีใจ excited"),

    (57, "คำศัพท์หมวดสิ่งแวดล้อม", "LO-ENG2", "Medium",
     "To protect our Earth, we should ________ plastic bags and recycle paper.",
     "waste", "reduce", "increase", "destroy", "ข",
     "เพื่อปกป้องโลก ควร ลด การใช้ถุงพลาสติก (reduce)"),

    (58, "คำศัพท์และกลุ่มคำ", "LO-ENG2", "Medium",
     "Don't put off until tomorrow what you can do today. What does 'put off' mean?",
     "Postpone / Delay", "Finish quickly", "Start immediately", "Forget", "ก",
     "กริยาวลี put off แปลว่า เลื่อนเวลาออกไป (postpone/delay)"),

    (59, "คำศัพท์หมวดเวลาและปฏิทิน", "LO-ENG1", "Easy",
     "Which month comes right after August?",
     "July", "September", "October", "November", "ข",
     "เดือนถัดจากสิงหาคม (August) คือ กันยายน (September)"),

    (60, "ภาษาอังกฤษในการสื่อสาร", "LO-ENG4", "Easy",
     "What do you say to someone who is going to take an exam?",
     "Good luck!", "Happy Birthday!", "Get well soon!", "Bon appetit!", "ก",
     "อวยพรคนกำลังจะสอบ พูดว่า Good luck! (โชคดีนะ)")
]

tf_questions = [
    # 61-90 True/False
    (61, "ไวยากรณ์ (Tenses)", "LO-ENG1", "Easy",
     "In English, the Present Continuous Tense is formed using 'Subject + verb to be + V.-ing'.",
     "True", "ถูกต้อง โครงสร้าง Present Continuous คือ Subject + is/am/are + V.-ing"),

    (62, "ไวยากรณ์ (Plural Nouns)", "LO-ENG1", "Easy",
     "The plural form of the word 'child' is 'childs'.",
     "False", "ผิด พหูพจน์ของ child คือ children ไม่ใช่ childs"),

    (63, "ไวยากรณ์ (Plural Nouns)", "LO-ENG1", "Easy",
     "The word 'water' is an uncountable noun, so we cannot say 'two waters'.",
     "True", "ถูกต้อง water เป็นคำนามนับไม่ได้ ต้องใช้ภาชนะบอกปริมาณ เช่น two glasses of water"),

    (64, "คำบุพบท (Prepositions)", "LO-ENG1", "Easy",
     "We use the preposition 'at' before days of the week, such as 'at Monday'.",
     "False", "ผิด วันในสัปดาห์ต้องใช้คำบุพบท on เช่น on Monday"),

    (65, "คำเปรียบเทียบ (Comparatives)", "LO-ENG2", "Medium",
     "The comparative form of 'good' is 'gooder'.",
     "False", "ผิด รูปขั้นกว่าของ good เป็นคำยกเว้น เปลี่ยนรูปเป็น better"),

    (66, "คำเปรียบเทียบ (Superlatives)", "LO-ENG2", "Medium",
     "The superlative form of 'beautiful' is 'most beautiful' or 'the most beautiful'.",
     "True", "ถูกต้อง คำคุณศัพท์ 3 พยางค์ ใช้ the most beautiful ในขั้นสุด"),

    (67, "คำศัพท์หมวดสุขภาพ", "LO-ENG1", "Easy",
     "A 'dentist' is a doctor who takes care of people's teeth.",
     "True", "ถูกต้อง dentist คือ หมอฟัน/ทันตแพทย์"),

    (68, "คำศัพท์หมวดอาชีพ", "LO-ENG1", "Easy",
     "An 'architect' is a person whose job is to design buildings.",
     "True", "ถูกต้อง architect คือ สถาปนิก ผู้ดูแลการออกแบบอาคาร"),

    (69, "คำศัพท์หมวดสถานที่", "LO-ENG1", "Easy",
     "An 'aquarium' is a building where historical objects are kept and displayed.",
     "False", "ผิด สถานที่เก็บวัตถุโบราณคือ museum (พิพิธภัณฑ์); ส่วน aquarium คือ สถานแสดงพันธุ์สัตว์น้ำ"),

    (70, "คำศัพท์หมวดสภาพอากาศ", "LO-ENG1", "Easy",
     "When the weather forecast says 'foggy', it means the sky is clear and very sunny.",
     "False", "ผิด foggy หมายถึง มีหมอกหนา ไม่ใช่แดดจัดฟ้าโปร่ง"),

    (71, "ไวยากรณ์ (Pronouns)", "LO-ENG1", "Easy",
     "The possessive pronoun for 'they' is 'their' when used before a noun (e.g., their house).",
     "True", "ถูกต้อง their เป็น possessive adjective ขยายคำนาม house"),

    (72, "ไวยากรณ์ (Modals)", "LO-ENG2", "Medium",
     "The modal verb 'mustn't' means 'do not have to' (you can choose whether to do it or not).",
     "False", "ผิด mustn't แปลว่า 'ต้องไม่/ห้ามทำ' (ข้อห้ามเด็ดขาด) ส่วน don't have to แปลว่า 'ไม่จำเป็นต้องทำ'"),

    (73, "คำศัพท์หมวดเวลา", "LO-ENG1", "Easy",
     "The expression 'quarter past eight' means 8:15.",
     "True", "ถูกต้อง quarter (15 นาที) past eight (ผ่าน 8 โมง) = 8:15"),

    (74, "คำศัพท์หมวดเวลา", "LO-ENG1", "Easy",
     "The expression 'half past ten' means 10:45.",
     "False", "ผิด half past ten หมายถึง 10:30 (10 โมงครึ่ง) ส่วน 10:45 คือ quarter to eleven"),

    (75, "ไวยากรณ์ (Past Tense Irregular Verbs)", "LO-ENG2", "Medium",
     "The past simple form of the verb 'go' is 'went'.",
     "True", "ถูกต้อง กริยาช่อง 2 ของ go คือ went"),

    (76, "ไวยากรณ์ (Past Tense Irregular Verbs)", "LO-ENG2", "Medium",
     "The past simple form of the verb 'teach' is 'teached'.",
     "False", "ผิด กริยาช่อง 2 ของ teach เป็นกริยาเปลี่ยนรูป คือ taught"),

    (77, "ป้ายสัญลักษณ์ (Signs)", "LO-ENG1", "Easy",
     "A sign 'FRAGILE' on a package means the item inside breaks easily and should be handled with care.",
     "True", "ถูกต้อง FRAGILE แปลว่า ระวังแตก/แตกหักง่าย"),

    (78, "สำนวนการสื่อสาร", "LO-ENG4", "Easy",
     "When someone says 'Bless you!' after you sneeze, it is a polite social custom in English culture.",
     "True", "ถูกต้อง หลังมีคนจาม คนตะวันตกมักพูด Bless you! เป็นมารยาทอวยพรสุขภาพ"),

    (79, "คำลักษณนามภาษาอังกฤษ", "LO-ENG2", "Medium",
     "We use 'a loaf of' to count bread, e.g., 'a loaf of bread'.",
     "True", "ถูกต้อง a loaf of bread คือ ขนมปัง 1 แถว/ปอนด์"),

    (80, "คำลักษณนามภาษาอังกฤษ", "LO-ENG2", "Medium",
     "We use 'a bar of' to count water, e.g., 'a bar of water'.",
     "False", "ผิด a bar of ใช้กับสบู่ ช็อกโกแลต (a bar of soap/chocolate) ส่วนน้ำใช้ a bottle/glass of water"),

    (81, "วัฒนธรรมตะวันตก", "LO-ENG4", "Easy",
     "Christmas Day is celebrated annually on December 25th.",
     "True", "ถูกต้อง วันคริสต์มาสตรงกับวันที่ 25 ธันวาคมของทุกปี"),

    (82, "วัฒนธรรมตะวันตก", "LO-ENG4", "Easy",
     "On Easter Sunday, children traditional search for hidden painted eggs.",
     "True", "ถูกต้อง ประเพณีเทศกาลอีสเตอร์มีกิจกรรมตามหาไข่อีสเตอร์ (Easter eggs)"),

    (83, "ไวยากรณ์ (Articles)", "LO-ENG1", "Easy",
     "We use the article 'a' before words starting with a vowel sound, such as 'a apple'.",
     "False", "ผิด คำขึ้นต้นด้วยเสียงสระ (apple) ต้องใช้ article 'an' -> an apple"),

    (84, "ไวยากรณ์ (Articles)", "LO-ENG1", "Easy",
     "We use 'an' before 'hour' because the letter 'h' is silent and it starts with a vowel sound.",
     "True", "ถูกต้อง hour ออกเสียงขึ้นต้นด้วยสระ /aʊər/ ไม่ออกเสียง h จึงใช้ an hour"),

    (85, "คำศัพท์หมวดกีฬา", "LO-ENG1", "Easy",
     "We use the verb 'play' with sports ending in -ing, like 'play swimming' and 'play running'.",
     "False", "ผิด กีฬาที่ลงท้ายด้วย -ing ต้องใช้กริยา go เช่น go swimming, go running"),

    (86, "คำศัพท์หมวดกีฬา", "LO-ENG1", "Easy",
     "We use the verb 'do' with martial arts and individual exercises like 'do gymnastics' and 'do karate'.",
     "True", "ถูกต้อง do ใช้กับศิลปะการป้องกันตัวและการออกกำลังกายเฉพาะบุคคล เช่น do karate, do gymnastics"),

    (87, "ไวยากรณ์ (Question Words)", "LO-ENG1", "Easy",
     "The question word 'Whose' is used to ask about ownership/possession.",
     "True", "ถูกต้อง Whose ใช้ถามถึงความเป็นเจ้าของ เช่น Whose pen is this?"),

    (88, "คำศัพท์หมวดทิศทาง", "LO-ENG1", "Easy",
     "The opposite of 'North' is 'West'.",
     "False", "ผิด ทิศตรงข้ามกับ North (เหนือ) คือ South (ใต้); ส่วน West (ตก) ตรงข้ามกับ East (ออก)"),

    (89, "คำศัพท์หมวดเครื่องแต่งกาย", "LO-ENG1", "Easy",
     "The word 'gloves' is always used in plural form because they come in a pair for both hands.",
     "True", "ถูกต้อง gloves (ถุงมือ) มักใช้รูปพหูพจน์เนื่องจากมี 2 ข้างคู่กัน"),

    (90, "การอ่านและจับใจความ", "LO-ENG3", "Medium",
     "A 'synonym' is a word that has the opposite meaning of another word.",
     "False", "ผิด synonym คือ คำที่มีความหมายเหมือนกัน ส่วนคำความหมายตรงข้ามกันเรียกว่า antonym")
]

sc_questions = [
    # 91-105 Scenario
    (91, "สถานการณ์การสั่งอาหารในร้านอาหาร", "LO-ENG4", "Hard",
     "John is at a restaurant. He wants to order a cheeseburger, french fries, and a bottle of mineral water. How should he politely place his order to the waiter?",
     "คำถาม: John ควรพูดประโยคสั่งอาหารกับพนักงานบริกรอย่างไรให้สุภาพ?",
     "John says: 'Hello! I would like to order a cheeseburger, french fries, and a bottle of mineral water, please.'",
     "คำอธิบาย: ใช้สำนวนสุภาพ 'I would like to...' (I'd like...) ตามด้วยรายการอาหารและลงท้ายด้วย 'please'"),

    (92, "สถานการณ์การถามทางไปสถานีตำรวจ", "LO-ENG4", "Hard",
     "A tourist is lost in the city and wants to find the nearest police station. He approaches a local citizen politely. What should the tourist say?",
     "คำถาม: นักท่องเที่ยวควรกล่าวทักทายและถามทางไปสถานีตำรวจอย่างไร?",
     "Tourist says: 'Excuse me, could you please tell me how to get to the nearest police station?'",
     "คำอธิบาย: การถามทางอย่างสุภาพขึ้นต้นด้วย 'Excuse me, could you please tell me...?'"),

    (93, "สถานการณ์การพบแพทย์เมื่อป่วย", "LO-ENG4", "Hard",
     "Sarah feels unwell. She has a high fever and a severe cough. The doctor asks her about her symptoms. How should Sarah describe her illness?",
     "คำถาม: Sarah ควรอธิบายอาการป่วยของเธอให้หมอฟังอย่างไร?",
     "Sarah says: 'Doctor, I don't feel well. I have a high fever and a bad cough.'",
     "คำอธิบาย: การบอกอาการป่วยใช้โครงสร้าง 'I have + (อาการป่วย)' เช่น I have a high fever and a bad cough."),

    (94, "สถานการณ์การซื้อเสื้อผ้าในร้านค้า", "LO-ENG4", "Hard",
     "Ben is trying on a jacket at a clothing store. He likes it, but it is too small for him. He wants to ask the shop assistant for a larger size. What should Ben say?",
     "คำถาม: Ben ควรพูดขอเปลี่ยนขนาดเสื้อกับพนักงานขายอย่างไร?",
     "Ben says: 'This jacket is a bit too small for me. Do you have a larger size, please?'",
     "คำอธิบาย: บอกปัญหา (too small) แล้วถามหาขนาดที่ใหญ่กว่า (Do you have a larger size / size L?)"),

    (95, "สถานการณ์การชวนเพื่อนทำกิจกรรมในวันหยุด", "LO-ENG4", "Hard",
     "Anna wants to invite her classmate Mark to go to the cinema to watch an animated movie this Saturday afternoon. How should Anna write her invitation message?",
     "คำถาม: Anna ควรเขียนประโยคเชิญชวน Mark ไปดูหนังอย่างไร?",
     "Anna says/writes: 'Hi Mark! Would you like to go to the cinema to watch an animated movie with me this Saturday afternoon?'",
     "คำอธิบาย: การเชิญชวนอย่างสุภาพใช้ 'Would you like to + V.1 ... with me?'"),

    (96, "สถานการณ์การยืมอุปกรณ์การเรียนในห้องเรียน", "LO-ENG4", "Hard",
     "David forgot his pencil case at home. He needs an eraser for his art class. He asks his desk mate Lisa. What is the dialogue between David and Lisa?",
     "คำถาม: จงเขียนบทสนทนาการขอยืมยางลบและการตอบรับให้ยืมระหว่าง David กับ Lisa",
     "David: 'Lisa, I forgot my pencil case today. May I borrow your eraser, please?' Lisa: 'Sure, David! Here you are.' David: 'Thank you so much!' Lisa: 'You're welcome!'",
     "คำอธิบาย: การขอยืมอย่างสุภาพใช้ 'May I borrow...?' ตอบรับส่งของใช้ 'Sure, here you are.'"),

    (97, "สถานการณ์การสอบถามสภาพอากาศการเดินทาง", "LO-ENG3", "Hard",
     "Tom and his family are planning a beach trip tomorrow. Tom checks the weather forecast news. The reporter says it will be stormy and heavy rain. What advice should Tom give to his family?",
     "คำถาม: Tom ควรให้คำแนะนำแก่ครอบครัวอย่างไรเมื่อสภาพอากาศไม่เอื้ออำนวย?",
     "Tom says: 'The weather forecast says it will be stormy tomorrow. We shouldn't go to the beach. We should stay home instead.'",
     "คำอธิบาย: ให้คำแนะนำตามสถานการณ์โดยใช้ shouldn't (ไม่ควรไป) และ should stay home (ควรอยู่บ้าน)"),

    (98, "สถานการณ์การกล่าวขอโทษทำน้ำหกใส่เพื่อน", "LO-ENG4", "Hard",
     "Ken accidentally knocked over a glass of water onto Jenny's notebook. Ken immediately apologizes and offers to help clean it up. What is the conversation?",
     "คำถาม: จงเขียนบทสนทนาการขอโทษ แสดงความช่วยเหลือ และการตอบรับให้อภัย",
     "Ken: 'Oh, I'm so sorry, Jenny! I accidentally spilled water on your notebook. Let me help you wipe it dry.' Jenny: 'That's alright, Ken. Accidents happen. Thank you for your help.'",
     "คำอธิบาย: ขอโทษสุภาพ 'I'm so sorry...' เสนอช่วยเหลือ 'Let me help you...' ตอบให้อภัย 'That's alright.'"),

    (99, "สถานการณ์การถามเวลาและการนัดหมาย", "LO-ENG4", "Hard",
     "Peter wants to know what time the English class starts today and where it takes place. He asks his teacher Miss Green. What is the dialogue?",
     "คำถาม: จงเขียนบทสนทนาการถามเวลาและสถานที่เรียนระหว่าง Peter กับ Miss Green",
     "Peter: 'Excuse me, Miss Green. What time does our English class start today, and where is it?' Miss Green: 'It starts at 10:15 a.m. in Room 302.' Peter: 'Thank you, teacher.'",
     "คำอธิบาย: ถามเวลา 'What time does... start?' ถามสถานที่ 'Where is it?'"),

    (100, "สถานการณ์การแนะนำเพื่อนใหม่ในโรงเรียน", "LO-ENG4", "Hard",
     "Teacher introduces a new student named Kenji from Japan to the class. Kenji introduces himself briefly (name, age, country, hobbies). What does Kenji say?",
     "คำถาม: Kenji ควรพูดแนะนำตัวเองหน้าชั้นเรียนเป็นภาษาอังกฤษอย่างไร?",
     "Kenji says: 'Hello everyone! My name is Kenji. I am 12 years old. I come from Japan. My hobby is playing football. Nice to meet you all!'",
     "คำอธิบาย: แนะนำชื่อ (My name is...) อายุ (I am... years old) ประเทศต้นทาง (I come from...) งานอดิเรก (My hobby is...)"),

    (101, "สถานการณ์การซื้อตั๋วภาพยนตร์", "LO-ENG4", "Hard",
     "Emma goes to the cinema. She wants to buy 2 adult tickets for the 5:00 p.m. show of 'Spider-Man'. How does she speak with the ticket cashier?",
     "คำถาม: Emma ควรพูดซื้อตั๋วภาพยนตร์กับพนักงานอย่างไร?",
     "Emma says: 'Hello, I'd like two tickets for Spider-Man at 5:00 p.m., please.' Cashier: 'That will be 300 Baht, please.' Emma: 'Here is the money. Thank you!'",
     "คำอธิบาย: ระบุจำนวนตั๋ว (two tickets) ชื่อเรื่อง (Spider-Man) รอบเวลา (at 5:00 p.m.)"),

    (102, "สถานการณ์การให้คำแนะนำสุขภาพเพื่อนป่วย", "LO-ENG4", "Hard",
     "Mike tells his friend May that he has a severe toothache and cannot eat food properly. What advice should May give to Mike?",
     "คำถาม: May ควรพูดให้คำแนะนำแก่ Mike เกี่ยวกับการดูแลฟันอย่างไร?",
     "May says: 'You shouldn't eat sweet candies, and you should go to see a dentist right away.'",
     "คำอธิบาย: ให้คำแนะนำเรื่องสิ่งที่ไม่ควรทำ (shouldn't eat candies) และสิ่งที่ควรทำ (should see a dentist)"),

    (103, "สถานการณ์การแสดงความคิดเห็นเกี่ยวกับภาพยนตร์", "LO-ENG3", "Hard",
     "Two friends just finished watching an action movie. Tim thought it was exciting, but Bob thought it was boring. Write their short dialogue expressing opinions.",
     "คำถาม: จงเขียนบทสนทนาแสดงความคิดเห็นที่แตกต่างกันเกี่ยวกับภาพยนตร์",
     "Tim: 'I thought the movie was really exciting! What did you think?' Bob: 'Well, to be honest, I found it a bit boring because the story was too long.'",
     "คำอธิบาย: ถามความคิดเห็น 'What did you think?' แสดงความรู้สึก 'I thought...' / 'I found it...'"),

    (104, "สถานการณ์การฉลองวันคริสต์มาสในครอบครัว", "LO-ENG4", "Hard",
     "On Christmas Day, Jack's family decorates the Christmas tree, exchanges gifts, and wishes each other well. Write a short paragraph describing Jack's Christmas.",
     "คำถาม: จงเขียนบรรยายกิจกรรมการเฉลิมฉลองวันคริสต์มาสของ Jack เป็นภาษาอังกฤษ",
     "Jack's Christmas: 'On Christmas Day, my family decorates the green Christmas tree with colorful lights and stars. We give gifts to each other and say Merry Christmas!'",
     "คำอธิบาย: บรรยายประเพณีคริสต์มาส (decorate Christmas tree, give gifts, say Merry Christmas)"),

    (105, "สถานการณ์การปฏิเสธคำชวนอย่างสุภาพ", "LO-ENG4", "Hard",
     "Paul invites Amy to play computer games at his house this afternoon, but Amy has to study for her English test tomorrow. How does Amy politely decline?",
     "คำถาม: Amy ควรพูดปฏิเสธคำชวนของ Paul อย่างสุภาพและบอกเหตุผลอย่างไร?",
     "Amy says: 'Thank you for the invitation, Paul, but I'm afraid I can't. I have to study for my English exam tomorrow. Maybe next time!'",
     "คำอธิบาย: ขอบคุณคำชวน ปฏิเสธสุภาพ 'I'm afraid I can't' บอกเหตุผล 'I have to study...' และลงท้าย 'Maybe next time!'")
]

sa_questions = [
    # 106-115 Short Answer
    (106, "การเปลี่ยนรูปคำนามพหูพจน์ (Plural Nouns)", "LO-ENG1", "Medium",
     "Explain the rules for changing singular nouns into plural nouns for: 1) cat -> cats, 2) bus -> buses, 3) baby -> babies, 4) man -> men. Provide explanations for each case.",
     "1) Regular nouns: Add -s (cat -> cats)\\n2) Nouns ending in -s, -ss, -sh, -ch, -x: Add -es (bus -> buses)\\n3) Nouns ending in consonant + y: Change y to i and add -es (baby -> babies)\\n4) Irregular nouns: Change the internal vowel (man -> men)"),

    (107, "การเปรียบเทียบขั้นกว่าและขั้นสุด (Comparatives & Superlatives)", "LO-ENG2", "Medium",
     "Complete the comparison table for the adjectives: 1) tall, 2) big, 3) expensive, 4) good. Write their Comparative and Superlative forms with explanation.",
     "1) tall -> taller -> the tallest (Short adjective: add -er / -est)\\n2) big -> bigger -> the biggest (Double last consonant for short vowel + single consonant)\\n3) expensive -> more expensive -> the most expensive (Long adjective: use more / most)\\n4) good -> better -> the best (Irregular adjective)"),

    (108, "ข้อแตกต่างระหว่าง Present Simple และ Present Continuous", "LO-ENG2", "Medium",
     "Explain the difference in usage between Present Simple Tense and Present Continuous Tense with 1 example sentence for each.",
     "1. Present Simple Tense: Used for daily routines, habits, and general facts.\\nExample: He plays football every Sunday.\\n2. Present Continuous Tense: Used for actions happening right now at the moment of speaking.\\nExample: He is playing football right now."),

    (109, "หลักการใช้ Prepositions of Time (in, on, at)", "LO-ENG2", "Medium",
     "Explain when to use the prepositions of time 'in', 'on', and 'at' with 1 example phrase for each.",
     "1. 'at': Used for specific clock times and midnight/noon (e.g., at 7:00 a.m., at night)\\n2. 'on': Used for specific days and dates (e.g., on Monday, on December 25th)\\n3. 'in': Used for months, years, seasons, and parts of the day (e.g., in July, in 2026, in the morning)"),

    (110, "วิเคราะห์ประโยคและชนิดของคำ (Parts of Speech)", "LO-ENG3", "Hard",
     "Analyze the sentence: 'The smart student quickly solved the difficult math problem.' Identify the Subject, Verb, Adjectives, and Adverb.",
     "Analysis:\\n- Subject: The smart student\\n- Verb: solved\\n- Adjectives: smart (modifies student), difficult (modifies math problem)\\n- Adverb: quickly (modifies verb solved)\\n- Object: the difficult math problem"),

    (111, "การใช้คำบอกปริมาณ (some vs any)", "LO-ENG2", "Medium",
     "Explain the main rules for using 'some' and 'any' in sentences with 2 example sentences.",
     "Rule:\\n1. 'some': Used in positive affirmative sentences and polite offers/requests.\\nExample: There are some apples on the table. / Would you like some tea?\\n2. 'any': Used in negative sentences and general questions.\\nExample: There isn't any milk in the fridge. / Do you have any questions?"),

    (112, "วัฒนธรรมและประเพณีวันฮาโลวีน (Halloween)", "LO-ENG4", "Medium",
     "Describe the origin and key traditions of Halloween (date, costumes, activities, symbols) in 3-4 sentences in English.",
     "Halloween is celebrated on October 31st every year in Western countries. Children wear fancy costumes such as ghosts, witches, or superheroes. They go door-to-door saying 'Trick or Treat!' to get candies. People also carve pumpkins into jack-o'-lanterns with candle lights inside."),

    (113, "การใช้ Modal Verbs (should vs must)", "LO-ENG2", "Medium",
     "Explain the difference between 'should' and 'must' when giving instructions or advice, with 1 example for each.",
     "1. 'should': Used for giving advice or suggestions (what is good to do).\\nExample: You should drink more water when you have a cold.\\n2. 'must': Used for strong obligation, necessity, or strict laws/rules.\\nExample: You must wear a helmet when riding a motorbike."),

    (114, "การแต่งบทสนทนาสั่งอาหารในร้านอาหาร", "LO-ENG4", "Hard",
     "Write a short dialogue (4 lines) between a Customer and a Waiter ordering lunch at a restaurant in English.",
     "Waiter: Good afternoon! Are you ready to order?\\nCustomer: Yes, please. I'd like a chicken salad and a cup of green tea.\\nWaiter: Would you like any dessert?\\nCustomer: No, thank you. That will be all for now."),

    (115, "การเขียนจดหมายหรืออีเมลสั้นๆ ถึงเพื่อน (Friendly Email)", "LO-ENG4", "Hard",
     "Write a short email (4-5 lines) inviting your friend to your birthday party this weekend in English.",
     "Hi Sam,\\nHow are you? I am writing to invite you to my 12th birthday party this Saturday at 4:00 p.m. at my home. We will play games, eat delicious birthday cake, and listen to music. I hope you can come!\\nBest wishes,\\nTom")
]

# Build Markdown content
out = header

# Section A
for q in mcq_questions:
    num, topic, lo, diff, prompt, opt_a, opt_b, opt_c, opt_d, ans, exp = q
    out += f"""
#### ข้อ {num}
* **หัวข้อ**: {topic}
* **จุดประสงค์การเรียนรู้**: {lo}
* **ระดับความยาก**: {diff}
* **โจทย์**: {prompt}
* ก. {opt_a}
* ข. {opt_b}
* ค. {opt_c}
* ง. {opt_d}
* **คำตอบที่ถูกต้อง**: {ans}
* **คำอธิบาย**: {exp}
"""

out += "\n---\n\n# Section B: True / False Questions (ถูก / ผิด)\n"

# Section B
for q in tf_questions:
    num, topic, lo, diff, stmt, ans, exp = q
    out += f"""
#### ข้อ {num}
* **หัวข้อ**: {topic}
* **จุดประสงค์การเรียนรู้**: {lo}
* **ระดับความยาก**: {diff}
* **ข้อความ**: "{stmt}"
* **คำตอบ**: {ans}
* **คำอธิบาย**: {exp}
"""

out += "\n---\n\n# Section C: Scenario-Based Questions (สถานการณ์จำลอง)\n"

# Section C
for q in sc_questions:
    num, topic, lo, diff, scen, q_text, ans, exp = q
    out += f"""
#### ข้อ {num}
* **หัวข้อ**: {topic}
* **จุดประสงค์การเรียนรู้**: {lo}
* **ระดับความยาก**: {diff}
* **สถานการณ์**: {scen}
* **คำถาม**: {q_text}
* **คำตอบ**: {ans}
* **คำอธิบาย**: {exp}
"""

out += "\n---\n\n# Section D: Short Answer Questions (อัตนัย / อธิบายความรู้)\n"

# Section D
for q in sa_questions:
    num, topic, lo, diff, prompt, exp_ans = q
    out += f"""
#### ข้อ {num}
* **หัวข้อ**: {topic}
* **จุดประสงค์การเรียนรู้**: {lo}
* **ระดับความยาก**: {diff}
* **โจทย์**: {prompt}
* **แนวคำตอบที่คาดหวัง**: {exp_ans}
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(out)

# Also write to alias filename if requested by user
alt_file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_English_Languages_Gr6.md"
with open(alt_file_path, "w", encoding="utf-8") as f:
    f.write(out)

print(f"Successfully generated {file_path} and {alt_file_path} with all 115 questions!")
