#!/usr/bin/env python3
import os

md_file = 'Knowledge_Assessment_ประวัติศาสตร์_GR6.md'

content = []

# Header
content.append("""# Knowledge Assessment Quiz: History Grade 6 (ประวัติศาสตร์ ป.6 - MidFinal)

╔══════════════════════════════════════════════════════════════════════╗
║  QUIZ DATA — SciMaster Gr.6 Platform (History / ประวัติศาสตร์)        ║
╚══════════════════════════════════════════════════════════════════════╝

---

## Document Summary (สรุปเนื้อหาเอกสารและหลักสูตรประวัติศาสตร์ ป.6)

เอกสารฉบับนี้รวบรวมเนื้อหาและโจทย์ประเมินผลการเรียนรู้กลุ่มสาระการเรียนรู้สังคมศึกษา ศาสนา และวัฒนธรรม (สาระประวัติศาสตร์และศาสนา) ระดับชั้นประถมศึกษาปีที่ 6 ครอบคลุมสาระสำคัญ 3 หน่วยการเรียนรู้หลัก ได้แก่:

### 1. หน่วยการเรียนรู้ที่ 1: พระพุทธศาสนาและประวัติศาสดา (Buddhism, Buddha's Life & Jataka Stories)
* **ความสำคัญของพระพุทธศาสนา**: พระพุทธศาสนาในฐานะเอกลักษณ์ของชาติไทย รากฐานและมรดกทางวัฒนธรรม สถาบันหลักศูนย์รวมจิตใจ และหลักในการพัฒนาชาติ
* **พุทธประวัติ**: เหตุการณ์ปลงอายุสังขาร ณ ปาวาลเจดีย์, ปัจฉิมสาวก (พระสุภัททะ), ปรินิพพาน ณ สาลวโนทยาน เมืองกุสินารา, การถวายพระเพลิง, การแจกพระบรมสารีริกธาตุโดยโทณพราหมณ์, และสังเวชนียสถาน 4 แห่ง
* **ชาดกและศาสนิกชนตัวอย่าง**: ทีฆีติโกสลชาดก (การไม่จองเวรเป็นคุณธรรมสูงสุด), สัพพทาฐิชาดก (การไม่ลุ่มหลงในอำนาจ), พระสาสนโสภณ (เอื้อน ชินทัตโต) และอาจารย์เสถียร พงศทะสิทธิ์

### 2. หน่วยการเรียนรู้ที่ 2: วิธีการทางประวัติศาสตร์และหลักฐานทางประวัติศาสตร์ (Historical Method & Evidence)
* **ขั้นตอนของวิธีการทางประวัติศาสตร์ 5 ขั้น**: 1. กำหนดหัวข้อ 2. รวบรวมหลักฐาน 3. ประเมินคุณค่าหลักฐาน (วิพากษ์ภายนอก/ภายใน) 4. ตีความและวิเคราะห์ข้อมูล 5. เรียบเรียงและนำเสนอ
* **ประเภทของหลักฐานทางประวัติศาสตร์**: หลักฐานชั้นต้น (ปฐมภูมิ: ศิลาจารึก, พงศาวดาร, โบราณวัตถุ) vs หลักฐานชั้นรอง (ทุติยภูมิ: ตำราเรียน, งานวิจัยประวัติศาสตร์)

### 3. หน่วยการเรียนรู้ที่ 3: ประเทศเพื่อนบ้านและภูมิภาคเอเชียตะวันออกเฉียงใต้ (Thailand's Neighbors & Regional History)
* **พัฒนาการของประเทศเพื่อนบ้าน**: เมียนมา (พม่า), ลาว (อาณาจักรล้านช้าง), กัมพูชา (อาณาจักรขอม), มาเลเซีย, เวียดนาม
* **ระบบการเมืองและการปกครอง**: การปกครองระบอบประชาธิปไตยอันมีพระมหากษัตริย์ทรงเป็นประมุข (ไทย กัมพูชา มาเลเซีย), ระบอบประธานาธิบดี (เมียนมา สิงคโปร์ อินโดนีเซีย ฟิลิปปินส์), และระบอบสังคมนิยมคอมมิวนิสต์ (ลาว เวียดนาม)
* **ความร่วมมือในภูมิภาค**: ประวัติความเป็นมา ความสำคัญ และบทบาทของสมาคมประชาชาติแห่งเอเชียตะวันออกเฉียงใต้ (ASEAN)

---

## Learning Objectives Mapping (แผนผังจุดประสงค์การเรียนรู้)

* **LO-HIS1**: Knowledge & Understanding of Buddhist history, Buddha's life events, Jataka teachings, and exemplary Buddhists.
* **LO-HIS2**: Application of the 5-step Historical Method and classification of primary/secondary historical evidence.
* **LO-HIS3**: Analysis of geographical, historical, economic, and political development of Thailand's neighboring countries.
* **LO-HIS4**: Evaluation & Synthesis of regional ASEAN cooperation, cultural diversity, and constitutional governance systems.

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
""")

# MCQ Data (1 to 60)
mcq_data = [
    # 1-20: Buddhism, Buddha's Life, Jataka & Exemplary Buddhists
    (1, "Importance of Buddhism", "LO-HIS1", "Easy",
     "Why is Buddhism considered an identity of the Thai nation?",
     "Because all citizens are legally forced to become Buddhist monks",
     "Because Buddhist moral principles have shaped Thai cultural values, politeness, and hospitality",
     "Because Buddhism originated inside the borders of ancient Thailand",
     "Because Thai law prohibits all other religions from operating in the country",
     "ข", "Buddhism has deeply influenced Thai social manners, friendliness ('Land of Smiles'), and cultural ethics over centuries."),

    (2, "Buddhism as Cultural Heritage", "LO-HIS1", "Easy",
     "Which architectural site represents Thai Buddhist cultural heritage?",
     "Eiffel Tower", "Wat Phra Kaew (Grand Palace Temple)", "Parthenon", "Colosseum",
     "ข", "Wat Phra Kaew and traditional Thai temples represent the pinnacle of Thai Buddhist art, architecture, and cultural heritage."),

    (3, "Buddha's Life - Relinquishing Life", "LO-HIS1", "Medium",
     "Where did the Buddha perform the 'Relinquishing of Life Duration' (ปลงอายุสังขาร) three months before Parinibbana?",
     "Lumbini Grove", "Pavala Cetiya in Vesali", "Sanath Deer Park in Sarnath", "Bodh Gaya under the Bodhi tree",
     "ข", "The Buddha performed the relinquishing of his life duration at Pavala Cetiya in Vesali, announcing he would attain Parinibbana in three months."),

    (4, "Buddha's Life - Last Disciple", "LO-HIS1", "Medium",
     "Who was the last direct disciple (ปัจฉิมสาวก) ordained by the Buddha right before his Parinibbana?",
     "Subhadda", "Ananda", "Sariputta", "Moggallana",
     "ก", "Subhadda the wandering ascetic requested to hear the Buddha's teaching at Kusinara and became his final ordained disciple (ปัจฉิมสาวก)."),

    (5, "Buddha's Life - Parinibbana", "LO-HIS1", "Easy",
     "In which town did the Buddha attain Parinibbana under the dual Sala trees?",
     "Rajagaha", "Kusinara (Kushinagar)", "Kapilavastu", "Varanasi",
     "ข", "The Buddha attained Parinibbana in the Upavattana Sala Grove of the Mallian royal family at Kusinara."),

    (6, "Buddha's Life - Holy Relics", "LO-HIS1", "Medium",
     "Which Brahmin mediated and distributed the Buddha's holy relics (พระบรมสารีริกธาตุ) among eight royal kingdoms after cremation?",
     "Asita Devala", "Kondanna Brahmin", "Dona Brahmin (โทณพราหมณ์)", "Anuruddha",
     "ค", "Dona Brahmin stepped in to prevent war and fairly distributed the sacred relics into eight equal portions for eight royal stupas."),

    (7, "Holy Pilgrimage Sites", "LO-HIS1", "Medium",
     "Which holy site (สังเวชนียสถาน) represents the place where the Buddha attained Enlightenment (ตรัสรู้)?",
     "Lumbini (Nepal)", "Bodh Gaya (India)", "Sarnath (India)", "Kusinara (India)",
     "ข", "Bodh Gaya is the sacred place where Prince Siddhattha attained Supreme Enlightenment under the Bodhi tree."),

    (8, "Holy Pilgrimage Sites", "LO-HIS1", "Easy",
     "Where is Lumbini Grove, the birthplace (ประสูติ) of Prince Siddhattha, located today?",
     "Modern Nepal", "Modern Sri Lanka", "Modern Myanmar", "Modern Thailand",
     "ก", "Lumbini Grove, the birthplace of the Buddha, is located in modern Nepal."),

    (9, "Dhiti Kosala Jataka", "LO-HIS1", "Medium",
     "What is the central moral lesson of the Dhiti Kosala Jataka (ทีฆีติโกสลชาดก)?",
     "Hatred is never ended by hatred, but only by non-hatred and forgiveness",
     "Physical strength is the only key to winning military victories",
     "Wealth and gold can buy eternal happiness",
     "Deception is acceptable if it accomplishes political goals",
     "ก", "Prince Dhighavu remembered his father King Dhighiti's dying words: 'Hatred ceases not by hatred, but by love and non-forgiveness.'"),

    (10, "Sabbadathi Jataka", "LO-HIS1", "Medium",
     "What moral warning does the Sabbadathi Jataka (สัพพทาฐิชาดก) provide to society?",
     "Power intoxicates the foolish and leads to downfall through excessive greed and pride",
     "Animals should never live together in forests",
     "Jackals are superior rulers compared to lions",
     "Kings must conquer all neighboring countries by force",
     "ก", "The jackal who gained magical power over all beasts became intoxicated with pride, leading to his own ruin and destruction."),

    (11, "Exemplary Buddhists", "LO-HIS1", "Medium",
     "Phra Sasana Sophon (Euan Chintatto) is remembered for which key contribution to Thai Buddhism?",
     "Translating scripture and promoting education and moral development among Thai youth",
     "Building military fortifications during the Ayutthaya period",
     "Establishing Thailand's first paper currency printing press",
     "Leading commercial banking development in Asia",
     "ก", "Phra Sasana Sophon was a highly respected Thai Buddhist monk who dedicated his life to education, scripture study, and youth ethics."),

    (12, "Exemplary Buddhists", "LO-HIS1", "Medium",
     "Acharn Sathien Phongphatthanasit contributed to Thai society primarily as a:",
     "Dedicated Buddhist scholar who explained Dhamma principles clearly for public moral application",
     "Famous international military commander",
     "Royal court painter in the Rattanakosin era",
     "Pioneer of modern rubber plantations in southern Thailand",
     "ก", "Acharn Sathien was a prominent Buddhist lay scholar who explained Buddhist philosophy and ethics to the general public."),

    (13, "Holy Pilgrimage Sites", "LO-HIS1", "Easy",
     "Where did the Buddha deliver his First Sermon (Dhammacakkappavattana Sutta) to the Five Ascetics?",
     "Lumbini Grove", "Sarnath Deer Park (Isipatana)", "Kusinara Sala Grove", "Pavala Cetiya",
     "ข", "The First Sermon was preached at the Deer Park in Isipatana near Sarnath (Varanasi)."),

    (14, "Buddha's Life - Cremation", "LO-HIS1", "Medium",
     "The royal cremation ceremony of the Buddha's body took place at which monument in Kusinara?",
     "Makutabandhana Cetiya (มกุฏพันธนเจดีย์)", "Sanchi Stupa", "Anuradhapura Stupa", "Shwedagon Pagoda",
     "ก", "The Mallian kings performed the cremation at the Makutabandhana Cetiya in Kusinara."),

    (15, "Three Jewels of Buddhism", "LO-HIS1", "Easy",
     "With the ordination of Kondanna after the First Sermon, which fundamental event occurred?",
     "The complete Three Jewels (Buddha, Dhamma, Sangha) were fully established for the first time",
     "The Buddha returned to his palace in Kapilavastu permanently",
     "The first Buddhist council was held immediately",
     "The Tripitaka was printed into paper books",
     "ก", "Kondanna's ordination created the first Buddhist monk, completing the Triple Gem (พระรัตนตรัย: พระพุทธ, พระธรรม, พระสงฆ์)."),

    (16, "Moral Lessons of Jataka", "LO-HIS1", "Medium",
     "In the Dhiti Kosala Jataka, why did Prince Dhighavu put away his sword instead of executing King Brahmadatta?",
     "Because he remembered his father's teaching on overcoming vengeance with forgiveness",
     "Because he lost his balance and dropped his weapon",
     "Because royal guards ambushed him from behind",
     "Because King Brahmadatta paid him a large monetary bribe",
     "ก", "Prince Dhighavu chose forgiveness over revenge, ending the endless cycle of blood feuds."),

    (17, "Buddhism and Thai Culture", "LO-HIS1", "Easy",
     "Which traditional Thai festival is directly connected to Buddhist merit-making and rain conservation traditions?",
     "Songkran and Loy Krathong", "Vassa (Khao Phansa / Entering Rains Retreat)", "Christmas", "New Year's Eve Countdown",
     "ข", "Khao Phansa (Entering Rains Retreat) and Ok Phansa are traditional Buddhist merit-making observances in Thailand."),

    (18, "Dhamma Practice in Daily Life", "LO-HIS1", "Easy",
     "What is the basic moral foundation (ศีล 5) for layman Buddhists to maintain peaceful co-existence?",
     "5 Moral Precepts (refraining from killing, stealing, sexual misconduct, lying, and intoxicants)",
     "5 Corporate Tax Regulations", "5 Military Strategy Laws", "5 Foreign Language Grammar Rules",
     "ก", "The 5 Moral Precepts (ศีล 5) guide everyday ethical conduct for lay Buddhists."),

    (19, "Importance of Buddhism", "LO-HIS1", "Medium",
     "How do Buddhist temples (วัด) historically serve as community centers in Thai society?",
     "As centers for education, moral instruction, community gatherings, and social welfare",
     "As private stock trading exchanges for merchants",
     "As heavy industrial manufacturing factories",
     "As tax collection headquarters for foreign embassies",
     "ก", "Historically, Thai temples served as schools, hospitals, cultural centers, and spiritual sanctuaries for local communities."),

    (20, "Buddhist Heritage - Literature", "LO-HIS1", "Medium",
     "Which classical Thai literary work written by King Li Thai of Sukhothai describes Buddhist cosmology and moral ethics?",
     "Tribhumikatha (Traibhumikatha / ไตรภูมิพระร่วง)", "Inao", "Khun Chang Khun Phaen", "Ramakien",
     "ก", "Traibhumikatha (ไตรภูมิพระร่วง) was authored by King Li Thai to instruct subjects on karma, virtues, and Buddhist cosmology."),

    # 21-40: Historical Method & Primary vs Secondary Sources
    (21, "Historical Method Steps", "LO-HIS2", "Easy",
     "What is the very FIRST step in the 5-step Historical Method (วิธีการทางประวัติศาสตร์)?",
     "Synthesizing the final research report",
     "Formulating the research topic or question (กำหนดหัวข้อที่จะศึกษา)",
     "Gathering historical artifacts",
     "Critiquing the honesty of historical witnesses",
     "ข", "Step 1 of the Historical Method is defining a clear topic, research question, or historical boundary to study."),

    (22, "Historical Method Steps", "LO-HIS2", "Easy",
     "What is the second step in the Historical Method after choosing a topic?",
     "Gathering historical evidence and sources (รวบรวมหลักฐาน)",
     "Publishing a textbook immediately",
     "Evaluating internal bias of sources",
     "Writing conclusions without reading documents",
     "ก", "Step 2 involves searching for and collecting relevant primary and secondary historical evidence."),

    (23, "Historical Method Steps - Criticism", "LO-HIS2", "Medium",
     "What is the primary purpose of Step 3: Source Criticism (การประเมินคุณค่าหลักฐาน / วิพากษ์หลักฐาน)?",
     "To verify the authenticity, reliability, age, and accuracy of historical evidence",
     "To translate all documents into English",
     "To burn original historical palm-leaf manuscripts",
     "To count the number of pages in historical books",
     "ก", "Source criticism (external and internal criticism) checks whether an evidence item is genuine and accurate."),

    (24, "Historical Criticism - External", "LO-HIS2", "Medium",
     "Checking whether a stone inscription is made of genuine ancient stone and whether its ink/carving style matches the historical era is an example of:",
     "External Criticism (การวิพากษ์ภายนอก)",
     "Internal Criticism (การวิพากษ์ภายใน)",
     "Synthesizing the final paper",
     "Choosing a research topic",
     "ก", "External criticism evaluates the physical authenticity, material, age, and external origin of the evidence."),

    (25, "Historical Criticism - Internal", "LO-HIS2", "Medium",
     "Analyzing whether an author of a royal chronicle had personal bias or exaggerated troop numbers is known as:",
     "External Criticism", "Internal Criticism (การวิพากษ์ภายใน)", "Collecting physical artifacts", "Topic selection",
     "ข", "Internal criticism assesses the credibility, truthfulness, motives, and reliability of the text/author's content."),

    (26, "Historical Method Steps - Final Step", "LO-HIS2", "Easy",
     "What is the FIFTH and final step of the Historical Method?",
     "Synthesizing, organizing, and presenting historical findings (เรียบเรียงและนำเสนอ)",
     "Formulating a new unverified hypothesis",
     "Discarding all collected research data",
     "Gathering more primary stone tablets",
     "ก", "Step 5 is synthesizing the analyzed historical facts into a coherent narrative report or presentation."),

    (27, "Types of Historical Evidence", "LO-HIS2", "Easy",
     "What is a 'Primary Source' (หลักฐานชั้นต้น / ปฐมภูมิ) in historical research?",
     "Evidence created during the actual historical time period by direct eye-witnesses or contemporaries",
     "A textbook written by a modern high school teacher in 2025",
     "A movie dramatization created by a contemporary film studio",
     "An encyclopedia summary published on a modern blog",
     "ก", "Primary sources are direct contemporary records, artifacts, or eye-witness accounts produced during the period being studied."),

    (28, "Primary Source Examples", "LO-HIS2", "Easy",
     "Which of the following is considered a Primary Historical Source for Sukhothai history?",
     "King Ramkhamhaeng Inscription Stone No. 1 (ศิลาจารึกพ่อขุนรามคำแหง)",
     "A modern Grade 6 social studies textbook",
     "A historical fiction novel written in 2010",
     "A cartoon animation about ancient kings",
     "ก", "King Ramkhamhaeng's Stone Inscription No. 1 is an authentic primary source carved during the Sukhothai period."),

    (29, "Types of Historical Evidence", "LO-HIS2", "Easy",
     "What is a 'Secondary Source' (หลักฐานชั้นรอง / ทุติยภูมิ)?",
     "Accounts, books, or analyses written after the event by researchers who did not witness the event directly",
     "Original royal letters written during the Ayutthaya war",
     "Ancient pottery dug up from Ban Chiang archaeological site",
     "Inscribed palm-leaf manuscripts from the 14th century",
     "ก", "Secondary sources synthesize, analyze, or interpret primary sources long after the historical event occurred."),

    (30, "Secondary Source Examples", "LO-HIS2", "Medium",
     "Which item is classified as a Secondary Source?",
     "A historical analysis book written by a modern university professor analyzing Ayutthaya trade records",
     "An original treaty signed by King Chulalongkorn and France in 1893",
     "An ancient bronze bell excavated from an old temple foundation",
     "Coins minted during the reign of King Rama IV",
     "ก", "Modern academic books analyzing past events are secondary sources derived from studying original primary data."),

    (31, "Historical Artifacts", "LO-HIS2", "Easy",
     "Ancient bronze drums, pottery jars, and stone axes excavated from archaeological sites are examples of:",
     "Non-written primary archaeological artifacts (หลักฐานชั้นต้นไม่เป็นลายลักษณ์อักษร)",
     "Secondary written textbooks",
     "Deceptive modern propaganda materials",
     "Digital online databases",
     "ก", "Unwritten physical items like pottery and bronze tools created in ancient times are primary non-written artifacts."),

    (32, "Chronicles (พงศาวดาร)", "LO-HIS2", "Medium",
     "Royal Chronicles (พระราชพงศาวดาร) primarily record historical events related to:",
     "Monarchs, royal court decrees, state wars, and political dynasties",
     "Daily market prices of vegetables in rural villages",
     "Folk stories and fairy tales of mythical creatures",
     "Modern weather forecasts in foreign countries",
     "ก", "Chronicles (พงศาวดาร) are historical records focusing on royal deeds, military campaigns, and state governance."),

    (33, "Historical Evidence Evaluation", "LO-HIS2", "Medium",
     "Why should historians compare multiple primary sources before writing a historical account?",
     "Because a single witness account may contain personal bias, errors, or incomplete perspectives",
     "Because law requires using at least 50 documents per sentence",
     "Because ancient historians were not allowed to write the truth",
     "Because primary sources are always completely false",
     "ก", "Cross-referencing multiple sources helps eliminate individual bias and reconstruct a balanced historical reality."),

    (34, "Written vs Non-Written Evidence", "LO-HIS2", "Easy",
     "Which historical item is classified as 'Written Evidence' (หลักฐานที่เป็นลายลักษณ์อักษร)?",
     "Royal decrees recorded on palm leaves (ใบลาน)",
     "Ancient terracotta roof tiles",
     "Stone spearheads from the Paleolithic era",
     "Gold ornaments excavated from ancient crypts",
     "ก", "Palm-leaf manuscripts, inscriptions, letters, and archives containing written script are written evidence."),

    (35, "Historical Interpretation", "LO-HIS2", "Medium",
     "What does Step 4: Data Interpretation (การตีความข้อมูล) require a historian to do?",
     "Analyze the underlying meaning of verified facts objectively without personal prejudice",
     "Invent fictional stories to fill gaps in historical records",
     "Change original historical dates to fit modern calendars",
     "Select only facts that support a predetermined political opinion",
     "ก", "Data interpretation involves analyzing proven historical facts with academic objectivity to understand cause-and-effect relationships."),

    (36, "Historical Bias", "LO-HIS2", "Medium",
     "When reading a war report written by a victorious general, a historian should be cautious of:",
     "Exaggeration of enemy casualties and minimization of own army losses due to bias",
     "The color of the paper used in modern printing presses",
     "The price of the book in retail bookstores",
     "The font size of the English translation",
     "ก", "War accounts by victors frequently contain self-serving bias, requiring careful internal criticism by historians."),

    (37, "Ban Chiang Archaeological Site", "LO-HIS2", "Easy",
     "Ban Chiang in Udon Thani is world-famous for providing primary archaeological evidence of:",
     "Prehistoric painted pottery and early bronze metallurgy in Southeast Asia",
     "Ayutthaya period royal palaces",
     "Rattanakosin period steam locomotives",
     "Sukhothai stone inscriptions",
     "ก", "Ban Chiang is a UNESCO World Heritage site known for prehistoric bronze age technology and painted pottery."),

    (38, "Historical Facts vs Opinions", "LO-HIS2", "Medium",
     "Which statement represents a historical 'Fact' rather than an opinion?",
     "King Ramkhamhaeng established the Thai alphabet inscription in 1826 B.E. (1283 C.E.)",
     "Sukhothai was the most fun kingdom in human history",
     "Ancient soldiers were much braver than modern people",
     "Ayutthaya architecture is prettier than European castles",
     "ก", "Verifiable dates and documented historical events represent facts, whereas subjective claims are opinions."),

    (39, "Local History Evidence", "LO-HIS2", "Medium",
     "If a student wants to study the history of their home village, what local primary source would be most valuable?",
     "Oral interviews with elderly village founders and old local temple records",
     "A national world geography atlas published in London",
     "A futuristic sci-fi novel about space exploration",
     "A modern fashion magazine",
     "ก", "Local oral histories from village elders, old family photos, and local temple registers provide direct primary evidence."),

    (40, "Importance of Historical Method", "LO-HIS2", "Medium",
     "Why is applying the Historical Method essential for historical study?",
     "It ensures historical conclusions are grounded in reliable, verified evidence rather than rumors or myths",
     "It guarantees that historical research can be completed in under 5 minutes",
     "It allows researchers to rewrite history without needing evidence",
     "It eliminates the need to read old documents",
     "ก", "The Historical Method provides a rigorous scientific framework to discover truth and prevent unverified myths from being accepted as history."),

    # 41-60: Thailand's Neighbors & Regional Cooperation (ASEAN)
    (41, "Thailand's Neighbors - Myanmar", "LO-HIS3", "Easy",
     "What is the official capital city of Myanmar (เมียนมา) today?",
     "Yangon (Rangoon)", "Naypyidaw (เนปยีดอ)", "Mandalay", "Bagan",
     "ข", "Naypyidaw replaced Yangon as the official administrative capital of Myanmar in 2005."),

    (42, "Thailand's Neighbors - Laos", "LO-HIS3", "Easy",
     "Which historical kingdom is recognized as the ancient historical predecessor of modern Laos?",
     "Lan Xang Kingdom (อาณาจักรล้านช้าง)", "Khmer Empire", "Majapahit Empire", "Srivijaya Kingdom",
     "ก", "The Lan Xang Kingdom (Kingdom of a Million Elephants) founded by King Fa Ngum is the historical ancestor of modern Laos."),

    (43, "Thailand's Neighbors - Laos Capital", "LO-HIS3", "Easy",
     "What is the capital city of the Lao People's Democratic Republic (สปป. ลาว)?",
     "Vientiane (เวียงจันทน์)", "Luang Prabang", "Pakse", "Savannakhet",
     "ก", "Vientiane is the capital and largest city of Laos."),

    (44, "Thailand's Neighbors - Cambodia", "LO-HIS3", "Easy",
     "Which world-famous ancient stone temple monument complex is located in Cambodia?",
     "Angkor Wat (ปราสาทนครวัด)", "Borobudur", "Shwedagon Pagoda", "Bagan Stupas",
     "ก", "Angkor Wat in Siem Reap, Cambodia, is one of the largest and most famous religious monuments in the world."),

    (45, "Thailand's Neighbors - Malaysia Religion", "LO-HIS3", "Easy",
     "What is the official state religion of Malaysia?",
     "Buddhism", "Islam", "Christianity", "Hinduism",
     "ข", "Islam is the official constitutional religion of Malaysia."),

    (46, "Thailand's Neighbors - Malaysia Capital", "LO-HIS3", "Easy",
     "What is the federal capital city of Malaysia?",
     "Kuala Lumpur", "George Town", "Johor Bahru", "Malacca",
     "ก", "Kuala Lumpur is the federal capital and main commercial hub of Malaysia."),

    (47, "Government Systems - Constitutional Monarchy", "LO-HIS3", "Medium",
     "Which group of Southeast Asian countries share a Constitutional Monarchy system where a King is Head of State under constitution?",
     "Thailand, Cambodia, and Malaysia", "Vietnam, Laos, and Myanmar", "Singapore, Philippines, and Indonesia", "Brunei, Vietnam, and Laos",
     "ก", "Thailand, Cambodia, and Malaysia operating under constitutional monarchy systems (Malaysia uses a rotational monarchy system among hereditary rulers)."),

    (48, "Government Systems - Republic", "LO-HIS3", "Medium",
     "Which neighboring Southeast Asian country is governed as a Republic with an elected President as Head of State?",
     "Myanmar and Indonesia", "Thailand", "Cambodia", "Brunei Darussalam",
     "ก", "Myanmar, Indonesia, Singapore, and the Philippines operate as Republics with Presidents as Heads of State."),

    (49, "Government Systems - Socialist State", "LO-HIS3", "Medium",
     "What form of government system is practiced in Laos and Vietnam?",
     "Socialist / Communist Republic (ระบอบสังคมนิยมคอมมิวนิสต์)",
     "Absolute Monarchy", "Federal Constitutional Republic with King", "Parliamentary Oligarchy",
     "ก", "Both Laos and Vietnam are single-party Socialist/Communist Republics."),

    (50, "Thailand's Bordering Countries", "LO-HIS3", "Easy",
     "Thailand shares land borders with four neighboring countries. Which of the following does NOT share a land border with Thailand?",
     "Vietnam", "Myanmar", "Laos", "Malaysia",
     "ก", "Vietnam does not share a direct physical land border with Thailand (separated by Laos and Cambodia)."),

    (51, "ASEAN Founding Year", "LO-HIS4", "Easy",
     "In which year was the Association of Southeast Asian Nations (ASEAN / สมาคมอาเซียน) founded by the Bangkok Declaration?",
     "1967 (พ.ศ. 2510)", "1945", "1999", "2015",
     "ก", "ASEAN was officially established on August 8, 1967, with the signing of the Bangkok Declaration in Thailand."),

    (52, "ASEAN Founding Members", "LO-HIS4", "Medium",
     "How many original founding member nations signed the Bangkok Declaration establishing ASEAN in 1967?",
     "5 nations (Thailand, Malaysia, Indonesia, Philippines, Singapore)",
     "10 nations", "3 nations", "12 nations",
     "ก", "The 5 founding nations were Thailand, Malaysia, Indonesia, Philippines, and Singapore."),

    (53, "ASEAN Member Count", "LO-HIS4", "Easy",
     "How many full member countries comprise ASEAN today?",
     "10 countries", "5 countries", "15 countries", "20 countries",
     "ก", "ASEAN consists of 10 member nations across Southeast Asia."),

    (54, "ASEAN Motto", "LO-HIS4", "Easy",
     "What is the official motto of ASEAN?",
     "One Vision, One Identity, One Community",
     "Peace, Wealth, Power",
     "Global Unity and Trade Supremacy",
     "Freedom, Equality, Brotherhood",
     "ก", "'One Vision, One Identity, One Community' is the official ASEAN motto."),

    (55, "ASEAN Emblem", "LO-HIS4", "Medium",
     "What does the central symbol of 10 yellow paddy stalks (รวงข้าวสีทอง 10 รวง) on the ASEAN flag represent?",
     "The 10 member nations bound together in friendship and solidarity",
     "The 10 main rivers of Southeast Asia",
     "The 10 major crops exported to Europe",
     "The 10 founding kings of ancient Asian empires",
     "ก", "The 10 golden rice stalks represent the 10 Southeast Asian nations bound together in solidarity."),

    (56, "ASEAN Community Pillars", "LO-HIS4", "Medium",
     "The ASEAN Community consists of three core pillars. Which of the following is NOT one of the three pillars?",
     "ASEAN Space Exploration Community",
     "ASEAN Political-Security Community (APSC)",
     "ASEAN Economic Community (AEC)",
     "ASEAN Socio-Cultural Community (ASCC)",
     "ก", "The 3 ASEAN pillars are Political-Security (APSC), Economic (AEC), and Socio-Cultural (ASCC)."),

    (57, "Economic Development - Singapore", "LO-HIS3", "Medium",
     "Why is Singapore recognized as an economic leader in Southeast Asia despite its small land size?",
     "It developed an advanced financial hub, strategic global port, and high-tech service economy",
     "It possesses the largest oil reserves in the world",
     "It relies exclusively on agricultural rice exports",
     "It has no foreign trade connections",
     "ก", "Singapore leveraged strategic location, human capital, financial infrastructure, and shipping logistics to achieve high economic status."),

    (58, "Cultural Diversity in ASEAN", "LO-HIS4", "Medium",
     "Why is Southeast Asia recognized as one of the most culturally diverse regions in the world?",
     "Due to centuries of trade, migration, and coexistence of major religions (Buddhism, Islam, Christianity, Hinduism)",
     "Because all countries speak the exact same dialect",
     "Because foreign visitors are banned from entering",
     "Because no historical events occurred before 1900",
     "ก", "Crossroad maritime geography brought diverse religious traditions, languages, and ethnic heritage across Southeast Asia."),

    (59, "Benefits of ASEAN Economic Community (AEC)", "LO-HIS4", "Medium",
     "How does the ASEAN Economic Community (AEC) benefit member countries?",
     "By promoting free flow of goods, services, investment, skilled labor, and regional economic integration",
     "By imposing high tariffs on all goods traded between neighboring member states",
     "By forcing all citizens to use a single currency printed in Europe",
     "By prohibiting regional tourism between member states",
     "ก", "AEC facilitates regional trade, investment flow, reduced tariffs, and economic collaboration across the 10 member states."),

    (60, "Thailand's Role in ASEAN", "LO-HIS4", "Medium",
     "What key historical role did Thailand play in the creation of ASEAN?",
     "Thailand hosted the signing of the founding Bangkok Declaration in 1967 and acted as a key regional mediator",
     "Thailand opposed the formation of any regional association",
     "Thailand joined ASEAN as the 10th member in 1999",
     "Thailand demanded to relocate ASEAN headquarters to North America",
     "ก", "Thailand hosted the 1967 founding meeting in Bangkok, under Foreign Minister Thanat Khoman, establishing ASEAN.")
]

for item in mcq_data:
    q_num, topic, lo, diff, prompt, opt_a, opt_b, opt_c, opt_d, ans, exp = item
    content.append(f"""#### ข้อ {q_num}
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
""")

content.append("""
# Section B: True / False Questions (ถูก / ผิด 30 ข้อ)

<!--
RULES Section B:
- ข้อ 61–90 (30 ข้อ, 1 คะแนน/ข้อ)
- **Correct Answer**: True | False
-->
""")

# TF Data (61 to 90)
tf_data = [
    (61, "Buddhism & Thai Culture", "LO-HIS1", "Easy",
     "Buddhism is recognized as a fundamental pillar of Thai national identity and cultural heritage.",
     "True", "Buddhism deeply permeates Thai architecture, literature, social etiquette, and national traditions."),

    (62, "Buddha's Life - Relinquishing Life", "LO-HIS1", "Medium",
     "The Buddha announced his intention to attain Parinibbana in three months while staying at Pavala Cetiya in Vesali.",
     "True", "This event is known as the Relinquishing of Life Duration (ปลงอายุสังขาร) at Pavala Cetiya."),

    (63, "Buddha's Life - Last Disciple", "LO-HIS1", "Easy",
     "Subhadda was the first monk ordained by the Buddha at Sarnath Deer Park.",
     "False", "Kondanna was the first monk ordained at Sarnath. Subhadda was the last disciple (ปัจฉิมสาวก) ordained at Kusinara."),

    (64, "Buddha's Relics", "LO-HIS1", "Medium",
     "Dona Brahmin divided the Buddha's holy relics into eight equal portions to prevent armed conflict among regional kings.",
     "True", "Dona Brahmin mediated peacefully and distributed the relics into eight equal shares for stupa construction."),

    (65, "Jataka Stories", "LO-HIS1", "Medium",
     "The main moral lesson of the Dhiti Kosala Jataka is that vengeance and violence should be pursued until all enemies are destroyed.",
     "False", "The core lesson of Dhiti Kosala Jataka is that hatred is overcome by non-hatred and forgiveness, not by revenge."),

    (66, "Sabbadathi Jataka", "LO-HIS1", "Medium",
     "In the Sabbadathi Jataka, the jackal's downfall was caused by his excessive arrogance and intoxication with magical power.",
     "True", "The jackal became prideful and drunk with power, causing his own destruction."),

    (67, "Exemplary Buddhists", "LO-HIS1", "Easy",
     "Phra Sasana Sophon (Euan Chintatto) dedicated his life to promoting Buddhist scripture study and youth moral education.",
     "True", "He was a distinguished Thai monk who advanced religious education and moral development."),

    (68, "Holy Pilgrimage Sites", "LO-HIS1", "Easy",
     "The place where the Buddha attained Parinibbana is located at Sarnath Deer Park.",
     "False", "Parinibbana occurred at Kusinara. Sarnath is the site of the First Sermon (ตรัสรู้ at Bodh Gaya, ประสูติ at Lumbini)."),

    (69, "Historical Method Steps", "LO-HIS2", "Easy",
     "The first step of the 5-step Historical Method is writing the final research report.",
     "False", "The first step is formulating the research topic (กำหนดหัวข้อ). Writing the final report is step 5."),

    (70, "Historical Method - Evidence Collection", "LO-HIS2", "Easy",
     "Gathering primary documents, inscriptions, and artifacts takes place in Step 2 of the Historical Method.",
     "True", "Step 2 is evidence collection (การรวบรวมหลักฐาน)."),

    (71, "Historical Criticism", "LO-HIS2", "Medium",
     "External Criticism evaluates whether a historical document or artifact is physically authentic and genuine.",
     "True", "External criticism examines physical materials, age, writing style, and physical authenticity."),

    (72, "Historical Criticism", "LO-HIS2", "Medium",
     "Internal Criticism focuses on checking the physical stone material of an ancient inscription.",
     "False", "Checking physical stone material is External Criticism. Internal criticism analyzes the author's credibility, content accuracy, and personal bias."),

    (73, "Primary Historical Sources", "LO-HIS2", "Easy",
     "A modern school textbook written in 2025 is classified as a Primary Source for ancient Sukhothai history.",
     "False", "Modern textbooks analyzing past eras are Secondary Sources. Primary sources were created during the historical era itself."),

    (74, "Primary Source Examples", "LO-HIS2", "Easy",
     "King Ramkhamhaeng's Stone Inscription No. 1 is a primary historical source for Sukhothai historical research.",
     "True", "It is an original contemporary inscription produced during the Sukhothai kingdom."),

    (75, "Secondary Sources", "LO-HIS2", "Medium",
     "Secondary sources are historical accounts compiled and analyzed after the event by researchers who did not witness the event directly.",
     "True", "Secondary sources interpret and synthesize primary data long after the event occurred."),

    (76, "Historical Artifacts", "LO-HIS2", "Easy",
     "Ban Chiang painted pottery and bronze tools excavated from ancient burial mounds are unwritten primary artifacts.",
     "True", "Prehistoric physical objects made in ancient times are primary non-written archaeological artifacts."),

    (77, "Chronicles (พงศาวดาร)", "LO-HIS2", "Medium",
     "Royal Chronicles focus primarily on recording ordinary village recipes and international sports events.",
     "False", "Royal Chronicles (พงศาวดาร) record royal monarchies, state wars, political decrees, and dynastic affairs."),

    (78, "Historical Objectivity", "LO-HIS2", "Medium",
     "Historians should rely on a single historical document without cross-checking other sources to ensure speed.",
     "False", "Historians must cross-reference multiple independent sources to detect bias and uncover objective historical truth."),

    (79, "Thailand's Neighbors - Myanmar Capital", "LO-HIS3", "Easy",
     "Naypyidaw is the current official capital city of Myanmar.",
     "True", "Naypyidaw became the official administrative capital of Myanmar in 2005."),

    (80, "Thailand's Neighbors - Laos History", "LO-HIS3", "Easy",
     "The ancient Lan Xang Kingdom is recognized as the historical predecessor of modern Laos.",
     "True", "Lan Xang (Kingdom of a Million Elephants) formed the historical foundations of Laos."),

    (81, "Thailand's Neighbors - Cambodia", "LO-HIS3", "Easy",
     "Angkor Wat is a famous ancient stone temple complex located in Myanmar.",
     "False", "Angkor Wat is located in Siem Reap, Cambodia."),

    (82, "Thailand's Neighbors - Malaysia Religion", "LO-HIS3", "Easy",
     "Islam is the official state religion of Malaysia.",
     "True", "Islam holds official constitutional status as the state religion of Malaysia."),

    (83, "Government Systems", "LO-HIS3", "Medium",
     "Thailand, Cambodia, and Malaysia all operate under Constitutional Monarchy systems with Kings as Heads of State.",
     "True", "All three nations have constitutional monarchies, though Malaysia utilizes a rotational monarchy system among royal sultans."),

    (84, "Government Systems - Republic", "LO-HIS3", "Medium",
     "Singapore and the Philippines operate as Constitutional Monarchies with hereditary kings.",
     "False", "Both Singapore and the Philippines are Republics with elected Presidents as Heads of State."),

    (85, "Government Systems - Socialist State", "LO-HIS3", "Medium",
     "Laos and Vietnam are single-party Socialist / Communist Republics.",
     "True", "Both Laos (สปป. ลาว) and Vietnam (สาธารณรัฐสังคมนิยมเวียดนาม) are socialist republics."),

    (86, "Geography of Thailand's Neighbors", "LO-HIS3", "Easy",
     "Thailand shares a direct physical land border with Vietnam.",
     "False", "Thailand does not share a direct land border with Vietnam. Vietnam is separated from Thailand by Laos and Cambodia."),

    (87, "ASEAN Founding", "LO-HIS4", "Easy",
     "ASEAN was founded in Bangkok, Thailand, in 1967 by the Bangkok Declaration.",
     "True", "The Bangkok Declaration was signed on August 8, 1967, at Saranrom Palace in Bangkok."),

    (88, "ASEAN Member Count", "LO-HIS4", "Easy",
     "There are currently 10 member countries in ASEAN.",
     "True", "ASEAN comprises 10 Southeast Asian member states."),

    (89, "ASEAN Emblem", "LO-HIS4", "Medium",
     "The 10 golden paddy stalks on the ASEAN flag represent the 10 major European trading partners.",
     "False", "The 10 golden paddy stalks represent the 10 Southeast Asian member countries bound in solidarity."),

    (90, "ASEAN Community Pillars", "LO-HIS4", "Medium",
     "The ASEAN Economic Community (AEC) aims to create a single market and production base for free flow of goods and services.",
     "True", "The AEC pillar promotes regional market integration, trade expansion, and free movement of skilled labor.")
]

for item in tf_data:
    q_num, topic, lo, diff, stmt, ans, exp = item
    content.append(f"""#### ข้อ {q_num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Statement**: {stmt}
* **Correct Answer**: {ans}
* **Explanation**: {exp}
""")

content.append("""
# Section C: Scenario-Based Questions (สถานการณ์จำลอง 15 ข้อ)

<!--
RULES Section C:
- ข้อ 91–105 (15 ข้อ, 2 คะแนน/ข้อ)
-->
""")

# Scenario Data (91 to 105)
scenario_data = [
    (91, "Applying Historical Method - Step 1 & 2", "LO-HIS2", "Hard",
     "Napa wants to study why her local riverside town in Ayutthaya experienced major flooding 200 years ago during the reign of King Rama III. She begins by visiting local old temples to look for palm-leaf manuscripts and interviewing temple abbots.",
     "Which steps of the 5-step Historical Method is Napa executing, and what should be her next step?",
     "Napa has completed Step 1 (Defining the research topic: flooding 200 years ago in Ayutthaya) and is currently executing Step 2 (Gathering primary evidence: searching palm-leaf records and conducting oral history interviews). Her immediate next step must be Step 3: Source Criticism (evaluating the authenticity, physical condition, author credibility, and factual accuracy of the gathered manuscripts and oral statements).",
     "The Historical Method requires systematic progression: Topic Definition -> Evidence Collection -> Source Criticism -> Interpretation -> Synthesis."),

    (92, "Source Criticism Application", "LO-HIS2", "Hard",
     "A researcher finds two historical documents describing a 17th-century battle: Document A (written by a court scribe of the winning king claiming 100,000 enemy casualties without friendly losses) and Document B (a merchant's logbook from a neutral foreign ship anchored in the bay reporting modest skirmishes).",
     "How should the researcher apply Internal Criticism to evaluate these conflicting accounts?",
     "The researcher should apply Internal Criticism to identify author bias. Document A contains obvious court propaganda bias (exaggerating enemy deaths and hiding own losses to flatter the king). Document B, written by an independent neutral observer with no political stake, is likely more objective regarding battle scale. The researcher must cross-reference both accounts with physical site evidence rather than taking Document A at face value.",
     "Internal criticism examines author motivation, political bias, and credibility to extract objective historical facts."),

    (93, "Primary vs. Secondary Source Evaluation", "LO-HIS2", "Hard",
     "Student Krai is writing a report on King Chulalongkorn's abolition of slavery in Thailand. He uses two sources: Source 1 (The original Royal Gazette decree published in 1905 C.E.) and Source 2 (A history website article published in 2024 by an unverified blogger).",
     "Categorize these sources into Primary vs Secondary and evaluate which provides greater historical authority.",
     "Source 1 (Royal Gazette 1905) is a Primary Source created directly during the historical event by the royal government, carrying authoritative legal and factual evidence. Source 2 (2024 blog article) is a Secondary Source of unverified quality. Krai must rely on Source 1 as his primary authority while double-checking Source 2 against peer-reviewed academic history books.",
     "Primary contemporary legal documents provide direct historical authority, whereas unverified internet blogs require strict verification."),

    (94, "Jataka Moral Application in Conflict Resolution", "LO-HIS1", "Hard",
     "Two students, Anan and Chai, get into a physical fight during football practice. Anan vows to ambush Chai after school with a stick to get revenge. Their teacher tells them the story of Prince Dhighavu from the Dhiti Kosala Jataka.",
     "How should Anan reflect upon the Dhiti Kosala Jataka to resolve this conflict peacefully?",
     "Anan should reflect on King Dhighiti's dying words: 'Hatred ceases not by hatred, but by forgiveness.' In the Jataka, Prince Dhighavu spared his enemy King Brahmadatta, ending generations of blood feuds and bringing peace. Anan should put away his weapon, apologize for his anger, and talk to Chai to resolve their misunderstanding through non-violence.",
     "The Dhiti Kosala Jataka teaches that breaking the cycle of revenge through forgiveness brings lasting peace."),

    (95, "Buddha's Life - Holy Relics Mediation", "LO-HIS1", "Hard",
     "After the Buddha's Parinibbana in Kusinara, seven powerful neighboring kings marched their armies to Kusinara, threatening full-scale war to claim the Buddha's sacred cremation relics. Dona Brahmin stepped forward with a golden vessel.",
     "Analyze Dona Brahmin's action and explain how his intervention preserved Buddhist peace.",
     "Dona Brahmin delivered a diplomatic sermon reminding the kings that the Buddha taught peace and non-violence, making it disgraceful to wage war over his sacred remains. He proposed dividing the relics into eight equal portions for each kingdom to build stupas. The kings agreed, avoiding a bloody war and spreading the relics across ancient India.",
     "Dona Brahmin's diplomatic intervention prevented military conflict and ensured widespread veneration of sacred relics."),

    (96, "Buddhism as National Identity & Heritage", "LO-HIS1", "Hard",
     "Foreign tourists visiting Bangkok notice that Thai people greet each other with a gentle 'Wai', show high respect to elders, donate food to morning monks, and build beautiful temple murals depicting historical stories.",
     "Explain how Buddhism forms the underlying foundation of these Thai cultural characteristics.",
     "Buddhism emphasizes moral values such as Metta (loving-kindness), Karuna (compassion), respect for elders, and generosity (Dana). Morning alms-giving reflects Buddhist merit-making, while temple murals and architecture preserve historical artistic craftsmanship. These Buddhist-inspired traits create Thailand's unique cultural identity ('Siam, Land of Smiles').",
     "Thai social etiquette, hospitality, art, and moral traditions are deeply rooted in centuries of Buddhist teachings."),

    (97, "Neighboring Country Analysis - Myanmar Transition", "LO-HIS3", "Hard",
     "A group of Thai traders wants to expand business into Myanmar. They analyze Myanmar's capital city, government structure, main economic resources, and cultural traditions.",
     "Summarize the key geographical, political, and economic facts about Myanmar for the traders.",
     "1. Capital: Naypyidaw (administrative capital; Yangon is the main commercial port). 2. Governance: Republic system with a President. 3. Economy & Resources: Rich in natural gas, teak timber, gems, and jade; growing trade with Thailand and China. 4. Culture: Predominantly Theravada Buddhist (e.g. Shwedagon Pagoda) with high respect for religious customs.",
     "Myanmar is a resource-rich neighboring republic with deep Buddhist heritage and strong trade links with Thailand."),

    (98, "Neighboring Country Analysis - Laos Development", "LO-HIS3", "Hard",
     "Thailand imports substantial hydroelectric electricity from Laos, which is known as the 'Battery of Southeast Asia'.",
     "Analyze the historical background, geography, government system, and economic development of Laos.",
     "1. History: Formerly the ancient Lan Xang Kingdom (ล้านช้าง). 2. Geography: Landlocked country with Mekong River flowing along Thai-Lao borders. 3. Government: Single-party Socialist / Communist Republic (สปป. ลาว) headed by a President. 4. Economy: Hydropower energy exports, mining, agricultural produce, and eco-tourism.",
     "Laos is a landlocked socialist republic with rich Lan Xang heritage and major hydropower trade with Thailand."),

    (99, "Neighboring Country Analysis - Malaysia Diversity", "LO-HIS3", "Hard",
     "Malaysia is a multicultural nation bordering southern Thailand. A Thai student notices that Malaysia has Malay, Chinese, and Indian populations living together under a federal constitutional monarchy.",
     "Describe the political, religious, and economic characteristics of Malaysia.",
     "1. Governance: Federal Constitutional Monarchy with a rotational Head of State (Yang di-Pertuan Agong) elected among hereditary state sultans. 2. Religion & Demographics: Islam is the official state religion; population includes Malays, Chinese, and Indians. 3. Economy: High economic stability, major exporter of palm oil, rubber, petroleum, and electronics.",
     "Malaysia is a stable, multi-ethnic constitutional monarchy with strong industrial, agricultural, and commercial sectors."),

    (100, "Government System Comparison - Regional ASEAN", "LO-HIS3", "Hard",
     "A political science student compares government systems across three ASEAN countries: Country X (King as Head of State under Constitution), Country Y (Elected President in a Republic), and Country Z (Socialist One-Party State).",
     "Match Thailand, Myanmar, and Vietnam to Countries X, Y, and Z, and justify your classification.",
     "1. Country X = Thailand: Constitutional Monarchy with King as Head of State under constitution. 2. Country Y = Myanmar: Republic system headed by a President. 3. Country Z = Vietnam: Socialist / Communist Republic governed by a single-party state.",
     "Southeast Asian nations utilize diverse governance models including Constitutional Monarchies, Republics, and Socialist States."),

    (101, "ASEAN Community Pillars Integration", "LO-HIS4", "Hard",
     "A Thai engineering student plans to work in Singapore after graduation under ASEAN professional mobility agreements, while a Thai fruit farmer exports durian to Malaysia tax-free under regional tariff reductions.",
     "Identify which ASEAN Community Pillar enables these activities and explain its economic goal.",
     "These activities are enabled by the ASEAN Economic Community (AEC) pillar. The AEC aims to establish a single market and production base across the 10 member states, facilitating zero-tariff regional trade in goods, investment flows, and mutual recognition agreements for skilled professionals.",
     "The AEC pillar promotes regional economic integration, market expansion, and mobility of goods, capital, and skilled labor."),

    (102, "ASEAN Founding & Geopolitical Role", "LO-HIS4", "Hard",
     "In 1967, five Southeast Asian foreign ministers gathered at Saranrom Palace in Bangkok during cold war tensions to sign the Bangkok Declaration.",
     "Why was ASEAN formed, who were the 5 original founding members, and what is its official motto?",
     "1. Purpose: Formed to promote regional peace, political stability, economic growth, and cultural cooperation. 2. 5 Founding Members: Thailand, Indonesia, Malaysia, Philippines, and Singapore. 3. Official Motto: 'One Vision, One Identity, One Community'.",
     "ASEAN was established in Bangkok in 1967 by 5 founding states to foster regional security, economic development, and unity."),

    (103, "Evaluating Historical Distortion & Myths", "LO-HIS2", "Hard",
     "A social media video claims that ancient Thai soldiers used laser weapons 1,000 years ago, citing a blurry self-made drawing as proof.",
     "How can a Grade 6 student apply the 5-step Historical Method to debunk this false claim?",
     "1. Topic: Investigate ancient Thai military technology. 2. Evidence: Gather authentic primary artifacts (ancient bronze swords, iron spears, stone inscriptions, contemporary foreign logs). 3. Source Criticism: Apply external/internal criticism to the video drawing—it lacks historical material proof, carbon dating, or primary record validation. 4. Interpretation & Synthesis: Conclude scientifically that laser claims are unhistorical internet hoaxes.",
     "Rigorous source evaluation under the Historical Method protects students against historical disinformation and hoaxes."),

    (104, "Buddha's Life - 4 Holy Pilgrimage Sites (สังเวชนียสถาน 4)", "LO-HIS1", "Hard",
     "A Thai Buddhist pilgrim travels to India and Nepal to visit the four major sacred sites commemorating key events in the Buddha's life.",
     "List the four holy pilgrimage locations (สังเวชนียสถาน 4) and match each to its corresponding life event.",
     "1. Lumbini (Nepal): Site of Prince Siddhattha's Birth (ประสูติ). 2. Bodh Gaya (India): Site of Supreme Enlightenment under the Bodhi tree (ตรัสรู้). 3. Sarnath Deer Park (India): Site of First Sermon / Dhamma Wheel (ปฐมเทศนา). 4. Kusinara (India): Site of Parinibbana under the dual Sala trees (ปรินิพพาน).",
     "The 4 holy pilgrimage sites represent the four principal monumental milestones in the life of the Buddha."),

    (105, "Cultural Preservation & Regional Unity", "LO-HIS4", "Hard",
     "A school organizes an 'ASEAN Cultural Day' where students showcase traditional national costumes, traditional foods (e.g. Nasi Lemak, Amok, Tom Yum), and shared historical ties.",
     "Why is understanding neighboring ASEAN history and cultural diversity important for Thai youth?",
     "Understanding neighboring histories fosters mutual respect, eliminates historic nationalistic prejudices, builds peaceful regional coexistence, and prepares youth to thrive actively within the ASEAN Socio-Cultural Community (ASCC).",
     "Cultural education builds regional harmony, empathy, and constructive cooperation among ASEAN member nations.")
]

for item in scenario_data:
    q_num, topic, lo, diff, scen, q, ans, exp = item
    content.append(f"""#### ข้อ {q_num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Scenario**: {scen}
* **Question**: {q}
* **Answer**: {ans}
* **Explanation**: {exp}
""")

content.append("""
# Section D: Short Answer Questions (อัตนัย / อธิบายความรู้ 10 ข้อ)

<!--
RULES Section D:
- ข้อ 106–115 (10 ข้อ, 3 คะแนน/ข้อ)
-->
""")

# Short Answer Data (106 to 115)
sa_data = [
    (106, "Importance of Buddhism in Thai History", "LO-HIS1", "Hard",
     "Explain three distinct ways Buddhism has served as a foundational pillar of Thai national identity and culture throughout history.",
     "1. Identity & Ethics: Buddhist moral principles (e.g. Metta, Karuna, Five Precepts) shaped Thai social manners, hospitality ('Land of Smiles'), and ethical standards. 2. Cultural & Artistic Heritage: Faith inspired national architecture (temples, stupas), fine arts (mural paintings, Buddha statues), and classical literature (Traibhumikatha). 3. Social & Educational Center: Historically, Buddhist temples (วัด) served as community education centers, healthcare hubs, and social gathering places."),

    (107, "Buddha's Life - Parinibbana Milestones", "LO-HIS1", "Hard",
     "Describe the sequence of major events surrounding the Buddha's Parinibbana from Relinquishing Life Duration to Relic Distribution.",
     "1. Relinquishing Life (ปลงอายุสังขาร): At Pavala Cetiya in Vesali, announcing Parinibbana in 3 months. 2. Last Disciple (ปัจฉิมสาวก): Ordaining Subhadda at Kusinara. 3. Parinibbana (ปรินิพพาน): Passing away between dual Sala trees at Kusinara. 4. Royal Cremation (ถวายพระเพลิง): At Makutabandhana Cetiya. 5. Relic Distribution (แจกพระบรมสารีริกธาตุ): Dona Brahmin mediated among eight royal kingdoms to distribute relics into eight stupas peacefully."),

    (108, "Moral Lessons of Jataka Stories", "LO-HIS1", "Hard",
     "Summarize the story and moral lesson of Dhiti Kosala Jataka (ทีฆีติโกสลชาดก) and explain its relevance to modern society.",
     "In Dhiti Kosala Jataka, King Dhighiti was executed by King Brahmadatta. Dhighiti's son, Prince Dhighavu, gained an opportunity to kill Brahmadatta in revenge but chose to spare his life, honoring his father's final words: 'Hatred is not ended by hatred, but by forgiveness.' Moved by this mercy, Brahmadatta restored Dhighavu's kingdom. The story teaches modern society that non-violence and forgiveness end destructive cycles of revenge."),

    (109, "Five Steps of the Historical Method", "LO-HIS2", "Hard",
     "List the 5 steps of the Historical Method (วิธีการทางประวัติศาสตร์) in correct chronological order and briefly explain the task performed in each step.",
     "1. Formulating the Topic (กำหนดหัวข้อ): Defining the research question or historical boundary. 2. Evidence Gathering (รวบรวมหลักฐาน): Collecting relevant primary and secondary sources. 3. Source Criticism (ประเมินคุณค่าหลักฐาน): Evaluating external authenticity and internal credibility. 4. Data Interpretation (ตีความและวิเคราะห์ข้อมูล): Analyzing verified facts objectively to determine cause-and-effect. 5. Synthesis & Presentation (เรียบเรียงและนำเสนอ): Structuring analyzed findings into a coherent historical report."),

    (110, "Primary vs. Secondary Historical Evidence", "LO-HIS2", "Hard",
     "Define Primary Sources and Secondary Sources in historical research, and provide two concrete examples of each type from Thai history.",
     "1. Primary Sources (หลักฐานชั้นต้น): Contemporary evidence created during the actual historical period by eye-witnesses or participants. Examples: King Ramkhamhaeng Stone Inscription No. 1, Ayutthaya Royal Chronicles (ใบลาน/จดหมายเหตุ), Ban Chiang bronze pottery. 2. Secondary Sources (หลักฐานชั้นรอง): Accounts, textbooks, or analyses written after the event by researchers analyzing primary data. Examples: Modern Grade 6 history textbooks, academic research journal articles written by modern historians."),

    (111, "External Criticism vs. Internal Criticism", "LO-HIS2", "Hard",
     "Explain the key differences between External Criticism and Internal Criticism in Step 3 of the Historical Method.",
     "External Criticism (วิพากษ์ภายนอก) evaluates the physical authenticity and material origin of historical evidence (e.g. testing stone age, ink chemistry, manuscript paper, handwriting style, to ensure it is not a modern physical forgery). Internal Criticism (วิพากษ์ภายใน) evaluates the content credibility and truthfulness of the written text itself (e.g. analyzing author motives, personal bias, exaggeration, or political propaganda to determine factual accuracy)."),

    (112, "Thailand's Neighboring Countries Overview", "LO-HIS3", "Hard",
     "Provide the official capital city, primary religion, and historical background for Thailand's neighboring countries: Myanmar, Laos, and Malaysia.",
     "1. Myanmar: Capital = Naypyidaw; Primary Religion = Theravada Buddhism; History = Rich empire history (Bagan, Konbaung), former British colony, resource-rich republic. 2. Laos: Capital = Vientiane; Primary Religion = Theravada Buddhism; History = Ancient Lan Xang Kingdom (ล้านช้าง), former French colony, landlocked socialist republic. 3. Malaysia: Capital = Kuala Lumpur; Official Religion = Islam; History = Maritime trading crossroads, former British colony, multicultural federal constitutional monarchy."),

    (113, "Regional Governance Systems Comparison", "LO-HIS3", "Hard",
     "Compare the three main types of government systems found in Southeast Asian nations, naming at least one country example for each system.",
     "1. Constitutional Monarchy: Head of State is a King operating under constitutional law. Examples: Thailand, Cambodia, Malaysia (rotational monarchy). 2. Republic: Head of State is an elected President. Examples: Myanmar, Singapore, Indonesia, Philippines. 3. Socialist / Communist Republic: Governed under single-party socialist leadership with a President. Examples: Laos (สปป. ลาว), Vietnam."),

    (114, "History and Founding of ASEAN", "LO-HIS4", "Hard",
     "Explain the founding background of ASEAN, listing its founding date, founding location, 5 original member states, and official motto.",
     "1. Founding Date & Location: August 8, 1967, established by the Bangkok Declaration signed at Saranrom Palace in Bangkok, Thailand. 2. 5 Original Member States: Thailand, Indonesia, Malaysia, Philippines, and Singapore. 3. Official Motto: 'One Vision, One Identity, One Community'. 4. Core Purpose: To promote regional peace, political stability, economic growth, and social-cultural integration."),

    (115, "Three Pillars of the ASEAN Community", "LO-HIS4", "Hard",
     "Name and describe the core objectives of the three community pillars comprising the integrated ASEAN Community.",
     "1. ASEAN Political-Security Community (APSC): Ensures regional peace, political stability, conflict resolution, and non-violence among member states. 2. ASEAN Economic Community (AEC): Creates a single market and production base with free flow of goods, services, investment, and skilled labor. 3. ASEAN Socio-Cultural Community (ASCC): Promotes human development, social welfare, environmental protection, and shared cultural identity among ASEAN peoples.")
]

for item in sa_data:
    q_num, topic, lo, diff, prompt, exp_ans = item
    content.append(f"""#### ข้อ {q_num}
* **Topic**: {topic}
* **Learning Objective**: {lo}
* **Difficulty**: {diff}
* **Prompt**: {prompt}
* **Expected Answer**: {exp_ans}
""")

# Write out full file
with open(md_file, 'w', encoding='utf-8') as f:
    f.write(''.join(content))

print(f"Successfully generated {md_file} with all 115 History questions!")
