import os

def generate_phonics_quiz_from_pdf():
    # 60 MCQ Questions based on Phonics Gr6-MidFinal.pdf (Affixes: Prefixes, Suffixes & Stress)
    mcq_questions = [
        # 1-10: Basic Affix Concepts & Prefix Meanings (from Pages 1-3)
        ("Affix Definitions", "Identify the three structural parts of a word.", "Easy",
         "Which part of the word 'uncomfortable' is the ROOT?",
         ["un-", "comfort", "-able", "-fort"], "B",
         "In 'uncomfortable', 'comfort' is the base root word, 'un-' is the prefix, and '-able' is the suffix."),

        ("Prefix Meanings", "Determine the meaning of the prefix 're-'.", "Easy",
         "What is the meaning of the prefix 're-' in words like 'renew' and 'restart'?",
         ["Before", "Again or back", "Not", "Under"], "B",
         "The prefix 're-' means 'again' or 'back' (e.g., renew = make new again)."),

        ("Prefix Meanings", "Determine the meaning of the prefix 'pre-'.", "Easy",
         "What does the prefix 'pre-' mean in words such as 'preview' and 'predict'?",
         ["Before", "After", "Against", "Many"], "A",
         "The prefix 'pre-' means 'before' (e.g., preview = view before publication)."),

        ("Prefix Meanings", "Identify the prefix meaning for 'mis-'.", "Medium",
         "What does the prefix 'mis-' signify in 'misbehave' or 'misunderstand'?",
         ["Under or low", "Wrongly or badly", "Half", "Across"], "B",
         "The prefix 'mis-' means 'wrong' or 'badly' (e.g., misbehave = behave badly)."),

        ("Prefix Meanings", "Identify the prefix meaning for 'de-'.", "Medium",
         "In the word 'deforestation', what does the prefix 'de-' mean?",
         ["Remove or reduce", "Twice", "Against", "One"], "A",
         "The prefix 'de-' means 'remove' or 'reduce' (e.g., deforestation = removal of forests)."),

        ("Prefix Meanings", "Identify the prefix meaning for 'tele-'.", "Easy",
         "What does the prefix 'tele-' mean in 'television' and 'telephone'?",
         ["Far or distant", "Eight", "Before", "Not"], "A",
         "The prefix 'tele-' comes from Greek meaning 'far' or 'distant'."),

        ("Prefix Meanings", "Identify the prefix meaning for 'bi-'.", "Easy",
         "What is the meaning of the prefix 'bi-' in 'biweekly' or 'bimonthly'?",
         ["Three times", "Twice (two times)", "Every month", "Under"], "B",
         "The prefix 'bi-' means 'two' or 'twice' (e.g., biweekly = published twice a week)."),

        ("Prefix Meanings", "Identify the prefix meaning for 'uni-'.", "Easy",
         "What does the prefix 'uni-' mean in 'uniform' and 'universe'?",
         ["One or same", "Against", "Middle", "Half"], "A",
         "The prefix 'uni-' means 'one' or 'same' (e.g., uniform = one form/same appearance)."),

        ("Prefix Meanings", "Identify the prefix meaning for 'oct-'.", "Easy",
         "What number does the prefix 'oct-' represent in words like 'octopus' and 'October'?",
         ["6", "8", "10", "12"], "B",
         "The prefix 'oct-' means 'eight' (e.g., octopus has 8 arms; October was the 8th month in Roman calendar)."),

        ("Prefix Meanings", "Identify the prefix meaning for 'sub-'.", "Medium",
         "What is the meaning of the prefix 'sub-' in 'subway' and 'submarine'?",
         ["Above or over", "Under or low", "Between", "Across"], "B",
         "The prefix 'sub-' means 'under' or 'low' (e.g., subway = underground train pathway)."),

        # 11-20: Advanced Prefixes & Opposite Prefixes (from Pages 4-5)
        ("Opposite Prefixes", "Identify prefixes that create opposite meanings.", "Medium",
         "Which prefix should be added to the word 'happy' to form its opposite?",
         ["dis-", "un-", "mis-", "in-"], "B",
         "The prefix 'un-' forms the opposite of 'happy' -> 'unhappy'."),

        ("Prefix Assimilation", "Identify the correct prefix for words starting with 'r'.", "Hard",
         "Which prefix is correctly paired with 'regular' to mean 'not regular'?",
         ["un-", "dis-", "ir-", "im-"], "C",
         "Words starting with 'r' take the assimilated prefix 'ir-' to form opposites (regular -> irregular)."),

        ("Prefix Assimilation", "Identify the correct prefix for words starting with 'l'.", "Hard",
         "Which prefix attaches to 'legal' to mean 'against the law / not legal'?",
         ["il-", "im-", "un-", "dis-"], "A",
         "Words starting with 'l' take the assimilated prefix 'il-' to form opposites (legal -> illegal)."),

        ("Prefix Assimilation", "Identify the correct prefix for words starting with 'p' or 'm'.", "Hard",
         "Which prefix is added to 'possible' to mean 'not possible'?",
         ["in-", "im-", "il-", "un-"], "B",
         "Words starting with 'p' or 'm' take the assimilated prefix 'im-' (possible -> impossible)."),

        ("Prefix Meanings", "Identify the meaning of 'multi-'.", "Medium",
         "What does the prefix 'multi-' mean in 'multicolored' and 'multilingual'?",
         ["Single", "Many (usually more than two)", "Half", "Under"], "B",
         "The prefix 'multi-' means 'many' (e.g., multilingual = speaking many languages)."),

        ("Prefix Meanings", "Identify the meaning of 'fore-'.", "Medium",
         "What does the prefix 'fore-' mean in 'forearm' and 'foreshadow'?",
         ["Before or front", "Against", "After", "Far"], "A",
         "The prefix 'fore-' means 'front' or 'before' (e.g., forearm = front part of the arm)."),

        ("Prefix Meanings", "Identify the meaning of 'semi-'.", "Medium",
         "What does the prefix 'semi-' mean in 'semifinal' and 'semiweekly'?",
         ["Full", "Half or partly", "Double", "Zero"], "B",
         "The prefix 'semi-' means 'half' or 'partly' (e.g., semifinal = half-final round)."),

        ("Prefix Meanings", "Identify the meaning of 'anti-'.", "Medium",
         "What does the prefix 'anti-' mean in 'anti-bacterial' and 'anti-gravity'?",
         ["Against or opposing", "Together", "Under", "Middle"], "A",
         "The prefix 'anti-' means 'against' or 'opposing' (e.g., antibacterial = acting against bacteria)."),

        ("Prefix Meanings", "Identify the meaning of 'inter-'.", "Medium",
         "What does the prefix 'inter-' mean in 'interact' and 'interstate'?",
         ["Between or among", "Inside", "Outside", "Without"], "A",
         "The prefix 'inter-' means 'between' or 'among' (e.g., interstate = between states)."),

        ("Prefix Selection in Context", "Select the correct prefixed word for a story context.", "Medium",
         "In the story 'Al and the party', Marie received gifts. Which word describes what Marie did to her gifts?",
         ["unchained", "unloaded", "unwrapped", "unpaid"], "C",
         "Marie 'unwrapped' her gifts at the party (removed the wrapping paper)."),

        # 21-30: Prefixed Vocabulary in Sentence Contexts (from Pages 6-7)
        ("Prefix Context Analysis", "Interpret 'biweekly' in news publishing.", "Medium",
         "If a newspaper is described as a 'biweekly', how often is it published?",
         ["Once a week", "Twice a week", "Three times a week", "Once a month"], "B",
         "A biweekly newspaper is published twice a week."),

        ("Prefix Context Analysis", "Analyze the term 'nasal decongestant'.", "Medium",
         "What is the function of a 'nasal decongestant' medicine?",
         ["It causes nasal congestion", "It helps reduce nasal congestion", "It makes your nose bigger", "It stops your heart"], "B",
         "The prefix 'de-' means reduce/remove, so a nasal decongestant reduces nasal congestion."),

        ("Prefix Context Analysis", "Interpret the word 'reusable'.", "Easy",
         "If a shopping bag is 'reusable', what should you do with it?",
         ["Throw it away immediately", "Keep it because it can be used again", "Recycle it into paper", "Burn it"], "B",
         "Reusable means it can be used again ('re-' = again)."),

        ("Prefix Context Analysis", "Interpret 'misread' and 'misunderstood'.", "Medium",
         "If someone 'misread' a notice and 'misunderstood' a message, what happened?",
         ["They read and understood it correctly", "They did not read it correctly and misunderstood it", "They did not read it at all", "They wrote the notice"], "B",
         "'mis-' means wrongly, so misread = read wrongly, misunderstood = understood wrongly."),

        ("Prefix Context Analysis", "Interpret the term 'preview'.", "Medium",
         "What does it mean when a publisher 'previews' an article before publishing?",
         ["They read the article after publication", "They read the article before publication", "They never read the article", "They delete the article"], "B",
         "'pre-' means before, so preview means to view or read before publication."),

        ("Prefix Context Analysis", "Contrast 'reforestation' vs 'deforestation'.", "Hard",
         "What is the key environmental difference between 'reforestation' and 'deforestation'?",
         ["Reforestation plants trees again; deforestation cuts down trees", "Both mean cutting down trees", "Both mean planting trees", "Reforestation reduces water"], "A",
         "'reforestation' ('re-' = again) means planting trees again; 'deforestation' ('de-' = remove) means cutting down forests."),

        ("Etymological Phonics", "Analyze October prefix historical anomaly.", "Hard",
         "Why is 'October' named with the prefix 'oct-' (meaning 8) when it is the 10th month of our modern calendar?",
         ["Because oct- means ten in Latin", "Because October used to be the eighth month in the ancient Roman calendar", "It is a spelling error", "Because octopus has 10 legs"], "B",
         "October was the 8th month in the original ancient Roman calendar before July and August were added."),

        ("Syllable Division & Prefixes", "Identify syllable boundary after prefixes.", "Medium",
         "Where is the primary syllable division in the word 'prehistoric'?",
         ["pre-his-tor-ic", "preh-is-tor-ic", "prehi-stor-ic", "p-rehistoric"], "A",
         "The prefix 'pre-' separates cleanly from the root, yielding pre-his-tor-ic (4 syllables)."),

        ("Syllable Stress in Prefixes", "Identify primary stress in prefixed verbs.", "Hard",
         "In words like 're-PLY', 're-PEAT', and 're-START', where is the primary stress located?",
         ["On the prefix 're-'", "On the root syllable following the prefix", "On the last letter", "Equally on both syllables"], "B",
         "In root-focused prefixed verbs, primary stress falls on the ROOT syllable (re-PLY, re-PEAT, re-START), while the prefix is unstressed."),

        ("Prefix Syllable Count", "Count syllables in multi-prefix words.", "Medium",
         "How many syllables are in the word 'uncomfortable'?",
         ["3", "4", "5", "6"], "C",
         "'un-com-fort-a-ble' consists of 5 syllables."),

        # 31-40: Suffix Definitions & Identification (from Pages 8-10)
        ("Suffix Definitions", "Define what a suffix is and its location.", "Easy",
         "What is a suffix?",
         ["A sound added to the beginning of a root word", "A sound added to the end of a root word", "The main part of a word", "A silent letter"], "B",
         "A suffix is an ending element attached to the end of a root word to modify its meaning or grammatical class."),

        ("Common Suffixes", "Identify the most common English suffixes.", "Easy",
         "According to phonics rules, which three are the most common suffixes in the English language?",
         ["-es, -ed, and -ing", "-tion, -sion, and -ness", "-able, -ful, and -less", "-anti, -pre, and -sub"], "A",
         "The three most frequent suffixes in English are '-es', '-ed', and '-ing'."),

        ("Suffix Meanings", "Identify the meaning of the suffix '-less'.", "Easy",
         "What does the suffix '-less' mean in words like 'lifeless', 'careless', and 'homeless'?",
         ["Full of", "Without or lacking", "Able to be", "State of being"], "B",
         "The suffix '-less' means 'without' (e.g., homeless = without a home)."),

        ("Suffix Meanings", "Identify the meaning of the suffix '-ful'.", "Easy",
         "What does the suffix '-ful' mean in 'successful', 'wonderful', and 'thoughtful'?",
         ["Without", "Full of or characterized by", "Capable of", "Small"], "B",
         "The suffix '-ful' means 'full of' (e.g., thoughtful = full of thought)."),

        ("Suffix Meanings", "Identify the meaning of the suffix '-able'.", "Medium",
         "What does the suffix '-able' mean in 'washable', 'payable', and 'acceptable'?",
         ["Capable of being or fit for", "Without", "Past time", "One who does"], "A",
         "The suffix '-able' means 'capable of being' (e.g., washable = able to be washed)."),

        ("Suffix Meanings", "Identify the function of the suffix '-ness'.", "Medium",
         "What grammatical change occurs when '-ness' is added to 'happy' (happiness)?",
         ["It changes an adjective into an abstract noun", "It turns a noun into a verb", "It makes the word past tense", "It creates an opposite"], "A",
         "Adding '-ness' converts adjectives into abstract nouns describing a state of being (happy -> happiness)."),

        ("Suffix Meanings", "Identify the function of '-ment'.", "Medium",
         "What function does '-ment' serve in words like 'amazement', 'development', and 'excitement'?",
         ["Forms nouns denoting an action, state, or result", "Forms past tense verbs", "Forms opposite adjectives", "Forms plural nouns"], "A",
         "The suffix '-ment' creates nouns expressing the result or state of an action."),

        ("Suffix Meanings", "Identify the function of '-en'.", "Medium",
         "What does the suffix '-en' do in 'darken', 'deepen', 'quicken', and 'straighten'?",
         ["Turns words into verbs meaning 'to make or become'", "Makes words plural", "Turns words into negative nouns", "Makes vowels long"], "A",
         "The suffix '-en' forms verbs meaning to cause to be or become (e.g., deepen = to make deep)."),

        ("Suffix Meanings", "Identify the suffix '-ity'.", "Hard",
         "What does the suffix '-ity' signify in 'purity', 'ability', and 'majority'?",
         ["State, quality, or condition of being", "Action happening now", "Without quality", "Before time"], "A",
         "The suffix '-ity' forms nouns expressing a state, quality, or degree."),

        ("Suffix Sound Patterns", "Identify '-tion' vs '-sion' sounds.", "Medium",
         "How is the suffix '-tion' pronounced in 'nation', 'tradition', and 'lotion'?",
         ["/tiːɒn/", "/ʃən/", "/ʒən/", "/tʃən/"], "B",
         "The suffix '-tion' is pronounced as /ʃən/ (or /ʃn̩/)."),

        # 41-50: Suffix Spelling Rules & Morphophonics (from Pages 8-11)
        ("Suffix Spelling Rules", "Identify y-to-i spelling rule.", "Medium",
         "When adding '-ness' to 'happy', what spelling change occurs?",
         ["The 'y' changes to 'i' -> happiness", "The 'y' is dropped -> happness", "No change -> happyness", "An 'e' is added -> happyeness"], "A",
         "Rule: When a root ends in a consonant + 'y', change 'y' to 'i' before adding a suffix (happy -> happiness)."),

        ("Suffix Spelling Rules", "Identify silent-e dropping rule.", "Medium",
         "What happens to the silent 'e' in 'imagine' when adding the suffix '-ary' (imaginary)?",
         ["The silent 'e' is kept", "The silent 'e' is dropped", "The 'e' turns into 'i'", "The consonant 'n' is doubled"], "B",
         "Rule: Drop silent 'e' at the end of a root word before adding a suffix starting with a vowel (-ary -> imaginary)."),

        ("Suffix Spelling Rules", "Identify silent-e dropping rule in '-ed'.", "Easy",
         "When adding '-ed' to the verb 'like', how is it correctly spelled?",
         ["likeed", "liked", "likded", "likid"], "B",
         "When root ends in silent 'e', simply add 'd' (like + ed = liked)."),

        ("Suffix Spelling Rules", "Identify y-to-i rule with '-ly'.", "Medium",
         "How is the word 'easily' formed from 'easy' and '-ly'?",
         ["easy + ly = easyly", "easy + ly = easily (y changes to i)", "easy + ly = easly", "easy + ly = ease-ly"], "B",
         "Root 'easy' ends in consonant + 'y'; change 'y' to 'i' before adding '-ly' -> easily."),

        ("Suffix Spelling Rules", "Identify consonant doubling rule.", "Hard",
         "Why is the consonant 'm' doubled when adding '-ing' to 'swim' (swimming)?",
         ["Because swim has a short vowel in a 1-syllable word ending in 1 consonant", "Because swim ends in a vowel", "Because ing requires two m's", "To make it a noun"], "A",
         "1-1-1 Rule: 1-syllable word, 1 short vowel, 1 final consonant -> double consonant before vowel suffix (-ing)."),

        ("Suffix Spelling Rules", "Identify doubling rule in 'muddy'.", "Medium",
         "How is the adjective 'muddy' formed from the noun 'mud'?",
         ["mud + y = mudy", "mud + y = muddy (double 'd')", "mud + y = mudyed", "mud + y = mudey"], "B",
         "1-1-1 Rule: 'mud' doubles final 'd' before vowel suffix '-y' -> muddy."),

        ("Suffix Spelling Rules", "Analyze travel + ing spelling variation.", "Hard",
         "In British/International English, how is 'travel' + '-ing' spelled?",
         ["traveled", "travelling (doubled 'l')", "traveling", "travelingness"], "B",
         "In standard international English phonics curriculum, 'travel' doubles the final 'l' -> travelling."),

        ("Suffix Word Formation", "Form new word with '-ful'.", "Easy",
         "What word is formed by combining 'care' + '-less'?",
         ["careful", "careless", "caring", "carely"], "B",
         "care + '-less' = careless (without care)."),

        ("Suffix Word Formation", "Form new word with '-ment'.", "Easy",
         "What word is formed by combining 'amaze' + '-ment'?",
         ["amazeful", "amazement", "amazing", "amazely"], "B",
         "amaze + '-ment' = amazement (dropping silent 'e' or combining directly)."),

        ("Suffix Word Formation", "Form new word with '-able'.", "Easy",
         "What word is formed by combining 'pay' + '-able'?",
         ["payable", "payless", "payful", "payed"], "A",
         "pay + '-able' = payable (able to be paid)."),

        # 51-60: Syllable Stress Patterns with Affixes (from Pages 1-11)
        ("Affix Stress Rules", "Identify stress placement on suffix '-tion'.", "Hard",
         "Where is the PRIMARY stress placed in words ending with '-tion' like 'tradition' and 'education'?",
         ["On the suffix '-tion'", "On the syllable immediately BEFORE '-tion'", "On the very first syllable", "On the last letter"], "B",
         "Stress Rule: Words ending in '-tion' or '-sion' always place primary stress on the syllable immediately preceding the suffix (tra-DI-tion, ed-u-CA-tion)."),

        ("Affix Stress Rules", "Identify stress placement with '-ity'.", "Hard",
         "Where is primary stress located in words ending with '-ity' such as 'majority' and 'ability'?",
         ["On the suffix '-ity'", "On the syllable directly before '-ity'", "On the first syllable", "No stress"], "B",
         "Stress Rule: Words ending in '-ity' have primary stress on the syllable right before '-ity' (ma-JOR-i-ty, a-BIL-i-ty)."),

        ("Affix Stress Rules", "Identify neutral suffixes.", "Hard",
         "Suffixes like '-less', '-ful', '-ness', and '-ly' are called 'neutral suffixes'. What does this mean?",
         ["They change the primary stress of the root word", "They DO NOT change the primary stress of the root word", "They make all vowels short", "They remove all accents"], "B",
         "Neutral suffixes (like '-ful' or '-ness') do not shift the primary stress of the base root word (CARE-less, HAP-pi-ness)."),

        ("Affix Stress Rules", "Identify stress in 'uncomfortable'.", "Hard",
         "Where is the primary stress in the word 'uncomfortable'?",
         ["UN-com-fort-a-ble", "un-COM-fort-a-ble", "un-com-FORT-a-ble", "un-com-fort-A-ble"], "B",
         "In 'uncomfortable', primary stress stays on the root syllable 'COM' (un-COM-fort-a-ble)."),

        ("Affix Stress Rules", "Identify stress in 'irregular'.", "Hard",
         "Which syllable receives primary stress in the word 'irregular'?",
         ["IR-reg-u-lar", "ir-REG-u-lar", "ir-reg-U-lar", "ir-reg-u-LAR"], "B",
         "Primary stress falls on the second syllable: ir-REG-u-lar."),

        ("Affix Stress Rules", "Identify stress in 'impossible'.", "Hard",
         "Which syllable is stressed in 'impossible'?",
         ["IM-pos-si-ble", "im-POS-si-ble", "im-pos-SI-ble", "im-pos-si-BLE"], "B",
         "Primary stress falls on 'POS': im-POS-si-ble."),

        ("Affix Stress Rules", "Identify stress in 'decongestant'.", "Hard",
         "Where is primary stress located in 'decongestant'?",
         ["DE-con-ges-tant", "de-con-GES-tant", "de-CON-ges-tant", "de-con-ges-TANT"], "B",
         "Primary stress falls on 'GES': de-con-GES-tant."),

        ("Affix Stress Rules", "Identify stress in 'reforestation'.", "Hard",
         "Which syllable receives the main primary stress in 'reforestation'?",
         ["re-for-es-TA-tion", "RE-for-es-ta-tion", "re-FOR-es-ta-tion", "re-for-es-ta-TION"], "A",
         "Before '-tion', stress falls on 'TA': re-for-es-TA-tion."),

        ("Affix Stress Rules", "Analyze unstressed prefix vowel quality.", "Hard",
         "In prefixed words like 'remember' and 'repeat', how is the vowel in the prefix 're-' pronounced?",
         ["As a long stressed /iː/", "As an unstressed short /rɪ/ or schwa /rə/", "As a silent letter", "As /rɛ/"], "B",
         "When the prefix is unstressed, the vowel reduces to short /rɪ/ or schwa /rə/ (re-MEMBER, re-PEAT)."),

        ("Morphophonic Summary", "Identify function of affix study in Phonics Grade 6.", "Medium",
         "According to the Grade 6 Phonics curriculum, why is learning syllable division and stress in affixes important?",
         ["To spell words backwards", "To make long, complex words easier and more correct to pronounce", "To eliminate suffixes", "To count letters"], "B",
         "Understanding syllable division and stress patterns makes multi-syllable prefixed/suffixed words easier and correct to pronounce.")
    ]

    # 30 True/False Questions based on Phonics Gr6-MidFinal.pdf
    tf_questions = [
        # 61-90 True/False
        ("Affix Structure", "Recall definition of root word.", "Easy",
         "The root of a word is the core base to which prefixes and suffixes are attached.", "True",
         "A root word is the fundamental base element containing the core meaning."),

        ("Prefix Position", "Recall prefix position.", "Easy",
         "A prefix is added to the END of a root word.", "False",
         "A prefix is added to the BEGINNING of a root word; a suffix is added to the end."),

        ("Word Length & Pronunciation", "Analyze affix impact on pronunciation.", "Medium",
         "Adding prefixes and suffixes makes a word longer, which can make it more difficult to pronounce without syllable division rules.", "True",
         "Affixes increase syllable count, requiring proper stress and syllable division techniques for clear pronunciation."),

        ("Prefix Meaning 're-'", "Recall 're-' meaning.", "Easy",
         "The prefix 're-' means 'before'.", "False",
         "'re-' means 'again' or 'back'. 'pre-' means 'before'."),

        ("Prefix Meaning 'pre-'", "Recall 'pre-' meaning.", "Easy",
         "The prefix 'pre-' means 'before', as in 'preview' and 'predict'.", "True",
         "'pre-' indicates prior time or action."),

        ("Prefix Meaning 'mis-'", "Recall 'mis-' meaning.", "Easy",
         "The prefix 'mis-' in 'misbehave' means 'wrongly' or 'badly'.", "True",
         "'mis-' indicates wrong or incorrect action."),

        ("Prefix Meaning 'de-'", "Recall 'de-' meaning.", "Medium",
         "The prefix 'de-' means 'to add or increase'.", "False",
         "'de-' means 'remove', 'reduce', or 'down' (e.g., decongest, deforestation)."),

        ("Prefix Meaning 'bi-'", "Recall 'bi-' meaning.", "Easy",
         "A 'biweekly' publication comes out twice a week.", "True",
         "'bi-' means two or twice."),

        ("Prefix Meaning 'tri-'", "Recall 'tri-' meaning.", "Easy",
         "The prefix 'tri-' means 'three', as in 'triangle' or 'tricycle'.", "True",
         "'tri-' denotes three."),

        ("Prefix Meaning 'sub-'", "Recall 'sub-' meaning.", "Easy",
         "The prefix 'sub-' means 'under' or 'below', as in 'submarine' and 'subway'.", "True",
         "'sub-' indicates an underground or subordinate position."),

        ("Prefix Assimilation 'im-'", "Recall 'im-' assimilation rule.", "Medium",
         "We use the prefix 'im-' before words starting with 'p' or 'm', such as 'impossible'.", "True",
         "'in-' assimilates to 'im-' before bilabial consonants /p/ and /m/."),

        ("Prefix Assimilation 'ir-'", "Recall 'ir-' assimilation rule.", "Medium",
         "The prefix 'ir-' is used before root words starting with the letter 'r', such as 'irregular'.", "True",
         "'in-' assimilates to 'ir-' before root words beginning with 'r'."),

        ("Prefix Assimilation 'il-'", "Recall 'il-' assimilation rule.", "Medium",
         "The prefix 'il-' attaches to root words beginning with 'l', such as 'illegal' and 'illogical'.", "True",
         "'in-' assimilates to 'il-' before root words beginning with 'l'."),

        ("Opposite Prefix 'un-'", "Recall 'un-' function.", "Easy",
         "Adding 'un-' to 'tidy' creates 'untidy', which means 'not tidy'.", "True",
         "'un-' is a primary negative prefix meaning 'not'."),

        ("Suffix Definition", "Recall suffix definition.", "Easy",
         "A suffix is added to the beginning of a word.", "False",
         "A suffix is added to the END of a root word."),

        ("Common Suffixes", "Identify top common suffixes.", "Easy",
         "The suffixes '-es', '-ed', and '-ing' are among the most common suffixes in English.", "True",
         "These three inflectional suffixes appear most frequently in English text."),

        ("Suffix '-less'", "Recall '-less' meaning.", "Easy",
         "The suffix '-less' means 'full of'.", "False",
         "'-less' means 'without' or 'lacking' (e.g., careless = without care)."),

        ("Suffix '-ful'", "Recall '-ful' meaning.", "Easy",
         "The word 'successful' means 'full of success'.", "True",
         "'-ful' means 'full of'."),

        ("Suffix '-able'", "Recall '-able' meaning.", "Medium",
         "The suffix '-able' means 'capable of being', as in 'washable'.", "True",
         "'-able' indicates ability or fitness to undergo an action."),

        ("Spelling Rule Y-to-I", "Recall y-to-i rule.", "Medium",
         "When adding '-ness' to 'happy', the spelling remains 'happyness'.", "False",
         "When root ends in consonant + 'y', change 'y' to 'i' -> 'happiness'."),

        ("Spelling Rule Silent E", "Recall silent-e dropping rule.", "Medium",
         "When adding a suffix starting with a vowel to a root ending in silent 'e', we usually drop the silent 'e'.", "True",
         "Silent 'e' is dropped before vowel suffixes (e.g., write + er = writer)."),

        ("Spelling Rule Doubling", "Recall 1-1-1 doubling rule.", "Medium",
         "In the word 'swimming', the final 'm' of 'swim' is doubled before adding '-ing'.", "True",
         "1-1-1 rule applies to 'swim' -> 'swimming'."),

        ("Suffix '-ment'", "Recall '-ment' word class.", "Medium",
         "Adding '-ment' to a verb creates a noun (e.g., excite -> excitement).", "True",
         "'-ment' forms nouns expressing action or state."),

        ("Suffix '-en'", "Recall '-en' verb formation.", "Medium",
         "Adding '-en' to 'dark' creates 'darken', which is a verb meaning 'to make dark'.", "True",
         "'-en' forms causative verbs from adjectives/nouns."),

        ("Suffix '-tion' Stress", "Recall '-tion' stress rule.", "Hard",
         "In words ending with '-tion', the primary stress falls on the '-tion' suffix itself.", "False",
         "Primary stress falls on the syllable BEFORE '-tion' (e.g., ed-u-CA-tion)."),

        ("Suffix '-ity' Stress", "Recall '-ity' stress rule.", "Hard",
         "In words ending with '-ity' (like 'purity'), primary stress falls on the syllable immediately preceding '-ity'.", "True",
         "'-ity' causes primary stress to land on the pre-suffix syllable (pu-RI-ty, ma-JOR-i-ty)."),

        ("Prefix Stress in Verbs", "Recall prefix stress in verbs.", "Hard",
         "In prefixed verbs like 'repeat' and 'restart', the prefix 're-' receives the strongest stress.", "False",
         "The root syllable receives the primary stress (re-PEAT, re-START)."),

        ("Prefix Meaning 'non-'", "Recall 'non-' meaning.", "Easy",
         "The prefix 'non-' means 'not', as in 'nonliving' and 'nonstop'.", "True",
         "'non-' means not or non-existent."),

        ("Prefix Meaning 'mid-'", "Recall 'mid-' meaning.", "Easy",
         "The prefix 'mid-' means 'middle', as in 'midday' and 'midnight'.", "True",
         "'mid-' indicates middle position or time."),

        ("Affix Curriculum Goal", "Recall Grade 6 Phonics goal.", "Easy",
         "Mastering prefixes, suffixes, and stress patterns helps students pronounce and spell long English words correctly.", "True",
         "This is the core objective of the Grade 6 Phonics curriculum module.")
    ]

    # 15 Scenario-Based Questions based on Phonics Gr6-MidFinal.pdf
    scenario_questions = [
        # 91-105 Scenario-Based Questions (2 pts each)
        ("Story Context: Al and the Party (Exercise 6)", "Analyze prefix usage in narrative context.", "Hard",
         "In a reading exercise about 'Al and the party', Al receives an invitation from Marie. He was UNSURE if he could go, DISLIKED ice cream and cake, and decided to DEPART early. At the party, Marie UNWRAPPED her gifts and was eager to UNTIE the bows.",
         "Identify the 5 prefixed words in this story excerpt, state their prefix, and explain the meaning of each word.",
         "1. UNSURE (un- = not sure). 2. DISLIKED (dis- = did not like). 3. DEPART (de- = leave/go away). 4. UNWRAPPED (un- = remove wrapping). 5. UNTIE (un- = loosen tie).",
         "All 5 words use prefixes ('un-', 'dis-', 'de-') to modify base roots in context."),

        ("Sentence Analysis: Newspaper Publishing (Exercise 7 Q1)", "Analyze 'biweekly' in publishing context.", "Hard",
         "Editor John says: 'This newspaper is a biweekly. We usually do not publish articles we don't preview.'",
         "Explain what 'biweekly' and 'preview' mean in John's statement, identifying their prefixes and root words.",
         "'biweekly' (bi- + weekly = published twice a week). 'preview' (pre- + view = read/view before publication).",
         "'bi-' means twice; 'pre-' means before."),

        ("Sentence Analysis: Medical Terminology (Exercise 7 Q2)", "Analyze 'nasal decongestant' phonetics and meaning.", "Hard",
         "Doctor Smith prescribes a 'nasal decongestant' to a patient suffering from a cold.",
         "Deconstruct the word 'decongestant' into its prefix, root, and suffix, and explain how the prefix 'de-' changes the patient's medical condition.",
         "Prefix: 'de-', Root: 'congest', Suffix: '-ant'. 'de-' means remove/reduce, so it relieves or reduces nasal congestion.",
         "'de-' indicates removal or reduction of congestion."),

        ("Environmental Article Analysis (Exercise 7 Q6-7)", "Compare 'reforestation' vs 'deforestation'.", "Hard",
         "An environmental report states: 'Reforestation will help to restore our environment, whereas deforestation will cause severe environmental depletion.'",
         "Deconstruct 'reforestation' and 'deforestation' by identifying their prefixes, roots, and suffixes. Explain how the prefixes create opposite environmental outcomes.",
         "'re-forest-ation' (re- = again; planting trees again restores environment). 'de-forest-ation' (de- = remove; cutting down trees causes depletion).",
         "'re-' means again (restoration); 'de-' means removal (destruction/depletion)."),

        ("Prefix Assimilation Rule Analysis", "Explain assimilation rules for 'in-'.", "Hard",
         "A teacher writes four words on the board: 'irresponsible', 'illegal', 'impossible', and 'inaccurate'.",
         "Explain why the negative prefix 'in-' changes its spelling to 'ir-', 'il-', and 'im-' across these four words.",
         "'ir-' before 'r' (irresponsible), 'il-' before 'l' (illegal), 'im-' before 'p/m' (impossible), and stays 'in-' before vowels/other consonants (inaccurate). This is prefix assimilation for smoother pronunciation.",
         "Assimilation matches the prefix consonant to the initial phonetic sound of the root."),

        ("Spelling Transformation: Y-to-I Rule", "Apply Y-to-I rule in sentence writing.", "Hard",
         "Student Sarah writes: 'She was happy because she easily opened the jar. Last year she happily let her brother do it.'",
         "Analyze how the root words 'easy' and 'happy' transformed when suffixes '-ly' were added, and state the spelling rule.",
         "'easy' + '-ly' = 'easily'; 'happy' + '-ly' = 'happily'. Rule: When root ends in consonant + 'y', change 'y' to 'i' before adding suffix.",
         "Consonant + 'y' converts to 'i' before suffix addition."),

        ("1-1-1 Doubling Rule in Context", "Analyze doubling rule in 'swimming' and 'muddy'.", "Hard",
         "Consider the sentence: 'He liked swimming, but the mud made the water too muddy to swim in.'",
         "Explain why 'swim' becomes 'swimming' and 'mud' becomes 'muddy' with double consonants, while 'like' becomes 'liked' without doubling.",
         "'swim' and 'mud' follow the 1-1-1 rule (1 syllable, 1 short vowel, 1 consonant) so final consonant doubles before vowel suffixes (-ing, -y). 'like' ends in silent 'e', so 'e' is dropped when adding '-ed'.",
         "1-1-1 doubling vs silent-e dropping rules."),

        ("Stress Shift Analysis: Suffix '-tion'", "Analyze primary stress shift with '-tion'.", "Hard",
         "Compare the pronunciation and stress placement of the root verb 'eduCATE' versus the suffixed noun 'eduCAtion'.",
         "Explain how adding the suffix '-tion' influences the primary stress position and syllable count of the word.",
         "'eduCATE' has 3 syllables with stress on 'CATE'. Adding '-tion' creates 'ed-u-CA-tion' (4 syllables) and shifts primary stress to the syllable 'CA' directly preceding '-tion'.",
         "'-tion' dictates primary stress placement on the penultimate (pre-suffix) syllable."),

        ("Stress Shift Analysis: Suffix '-ity'", "Analyze stress shift with '-ity'.", "Hard",
         "Compare the root adjective 'PURE' /pyʊər/ with the suffixed noun 'puRITy' /ˈpyʊərəti/ and 'MAjor' with 'maJORity'.",
         "Describe the change in primary stress location when '-ity' is added to 'pure' and 'major'.",
         "In 'pure' (1 syllable), stress is on 'pure'. In 'purity' (3 syllables), stress moves to 'RI' (pu-RI-ty). In 'majority', stress is on 'JOR' (ma-JOR-i-ty), right before '-ity'.",
         "'-ity' forces primary stress onto the syllable immediately preceding it."),

        ("Prefix Meaning & Stress: 'misbehave'", "Analyze prefix 'mis-' and stress in 'misbehave'.", "Hard",
         "A student reads: 'The child began to misbehave during the long ceremony.'",
         "Deconstruct 'misbehave' into prefix and root, state its meaning, and indicate which syllable receives primary stress.",
         "Prefix: 'mis-' (wrongly/badly). Root: 'behave'. Meaning: behave badly. Syllable division: mis-be-HAVE. Primary stress is on 'HAVE'.",
         "'mis-' means badly; primary stress remains on the root 'HAVE'."),

        ("Suffix Analysis: '-less' vs '-ful'", "Contrast opposite suffixes '-less' and '-ful'.", "Hard",
         "Compare the two words 'careless' and 'careful'.",
         "Deconstruct both words, explain how '-less' and '-ful' change the meaning of the root 'care', and identify their word class.",
         "Root: 'care'. 'careless' (-less = without care). 'careful' (-ful = full of care). Both words function as adjectives.",
         "'-less' (without) and '-ful' (full of) create antonymous adjectives from the same root."),

        ("Prefix Analysis: 'anti-' vs 'pro-'", "Analyze 'anti-' prefix in science context.", "Medium",
         "In a biology lesson, students learn about 'antibacterial' soap and 'antigravity' experiments.",
         "What does 'anti-' mean in these words, and how does it modify 'bacterial' and 'gravity'?",
         "'anti-' means against or opposing. 'antibacterial' = acting against bacteria; 'antigravity' = opposing gravity.",
         "'anti-' indicates opposition or protection against."),

        ("Historical Phonics Anomaly: October", "Explain Roman calendar prefix anomaly.", "Hard",
         "A Grade 6 student asks: 'If oct- means 8 like in octopus, why is October the 10th month?'",
         "Formulate a clear explanation based on the phonics unit notes regarding the Roman calendar.",
         "In the ancient Roman calendar, October was originally the 8th month. Later, January and February (or July/August) were inserted, moving October to the 10th position while retaining its original prefix name.",
         "Etymological retention of prefix 'oct-' from Roman calendar."),

        ("Morphophonics: Deconstruct 'uncomfortable'", "Deconstruct 5-syllable word into affixes and root.", "Hard",
         "Deconstruct the multi-syllable word 'uncomfortable' into all its structural parts.",
         "Identify the prefix, root word, suffix, total syllable count, and primary stressed syllable.",
         "Prefix: 'un-'. Root: 'comfort'. Suffix: '-able'. Syllable division: un-COM-fort-a-ble (5 syllables). Primary stress: 'COM'.",
         "Complete morphological and phonetic breakdown."),

        ("Suffix Analysis: '-en' Verbs", "Analyze verb formation with '-en'.", "Medium",
         "Consider the words: 'darken', 'deepen', 'quicken', 'straighten'.",
         "What root words do these come from, what suffix is used, and what is the resulting word class and meaning?",
         "Roots: 'dark', 'deep', 'quick', 'straight' (adjectives). Suffix: '-en'. Result: Verbs meaning 'to make or become' dark, deep, quick, or straight.",
         "'-en' converts adjectives into causative verbs.")
    ]

    # 10 Short Answer Questions based on Phonics Gr6-MidFinal.pdf
    short_answer_questions = [
        # 106-115 Short Answer Questions (3 pts each)
        ("Affix Structural Breakdown", "Define the 3 structural parts of a word.", "Hard",
         "Define the three structural parts of an English word (Root, Prefix, Suffix) and provide one example word showing all three parts.",
         "1. Root: The core base of the word (e.g., comfort). 2. Prefix: A beginning addition (e.g., un-). 3. Suffix: An ending addition (e.g., -able). Example: 'uncomfortable' (un + comfort + able).",
         "Clear definitions of root, prefix, suffix with valid full example."),

        ("Prefix Assimilation Rules", "Explain assimilation of negative prefix 'in-'.", "Hard",
         "Explain the rules for prefix assimilation of 'in-' into 'im-', 'il-', and 'ir-', providing one example word for each variation.",
         "1. 'im-' before root words starting with p or m (e.g., impossible, imperfect). 2. 'il-' before root words starting with l (e.g., illegal). 3. 'ir-' before root words starting with r (e.g., irregular). 4. 'in-' before other consonants/vowels (e.g., incorrect).",
         "Full explanation of all 3 assimilation rules with examples."),

        ("Stress Rule for '-tion' and '-sion'", "Formulate primary stress rule for '-tion'/'-sion'.", "Hard",
         "State the primary stress rule for words ending with the suffixes '-tion' or '-sion', and demonstrate with two examples marked for stress.",
         "Rule: Primary stress always falls on the syllable immediately preceding the '-tion' or '-sion' suffix. Examples: ed-u-CA-tion, di-VI-sion.",
         "Accurate rule formulation and two correctly stress-marked examples."),

        ("Stress Rule for '-ity'", "Formulate primary stress rule for '-ity'.", "Hard",
         "State the primary stress rule for words ending with '-ity' and give two examples showing syllable division and stress.",
         "Rule: Primary stress falls on the syllable directly before the '-ity' suffix. Examples: ma-JOR-i-ty, pu-RI-ty.",
         "Accurate rule formulation and two stress-marked examples."),

        ("Y-to-I Spelling Rule", "Explain Y-to-I spelling rule with affixes.", "Hard",
         "Explain the 'Y-to-I' spelling rule when adding suffixes to root words ending in 'y', and provide two examples.",
         "Rule: If a root word ends in a consonant + 'y', change the 'y' to 'i' before adding any suffix (except '-ing'). Examples: happy + ness = happiness; easy + ly = easily.",
         "Clear statement of consonant + y rule with 2 examples."),

        ("1-1-1 Consonant Doubling Rule", "Explain 1-1-1 doubling rule with affixes.", "Hard",
         "Explain the 1-1-1 doubling rule when adding a suffix starting with a vowel, and provide two examples.",
         "Rule: In a 1-syllable word ending in 1 short vowel and 1 consonant, double the final consonant before adding a suffix starting with a vowel. Examples: swim + ing = swimming; mud + y = muddy.",
         "Mentions 1 syllable, 1 short vowel, 1 consonant, and vowel suffix with 2 examples."),

        ("Silent-E Dropping Rule", "Explain silent-e dropping rule with affixes.", "Hard",
         "Explain when and why a final silent 'e' is dropped when attaching a suffix, and provide two examples.",
         "Rule: Drop the final silent 'e' when adding a suffix that begins with a vowel. Keep the silent 'e' if the suffix begins with a consonant. Examples: imagine + ary = imaginary (dropped); write + er = writer (dropped); care + ful = careful (kept).",
         "Full rule for vowel vs consonant suffixes with 2 examples."),

        ("Opposite Prefixes List", "List 5 negative prefixes meaning 'not'.", "Hard",
         "List 5 different prefixes that mean 'not' or 'opposite of', and give one example word for each.",
         "1. un- (unhappy). 2. dis- (disagree). 3. in-/im-/il-/ir- (impossible). 4. non- (nonstop). 5. mis- (misunderstand - wrong/bad).",
         "5 distinct negative prefixes with accurate example words."),

        ("Number Prefixes List", "List 4 number prefixes and their values.", "Hard",
         "List 4 numerical prefixes (such as uni-, bi-, tri-, oct-), state the number each represents, and give an example word for each.",
         "1. uni- = 1 (uniform). 2. bi- = 2 (biweekly). 3. tri- = 3 (triangle). 4. oct- = 8 (octopus).",
         "4 numerical prefixes with values and correct example words."),

        ("Syllable Division & Stress Objective", "Explain how affix study improves pronunciation.", "Hard",
         "Explain why studying syllable division and stressed/unstressed syllables is necessary when learning long prefixed and suffixed words.",
         "Adding prefixes and suffixes makes words longer and more complex. Syllable division and stress rules break words into manageable units and ensure correct, natural English pronunciation without slurring or misplacing accents.",
         "Clear summary of phonetic and pronunciation benefits of affix syllabification.")
    ]

    # Assemble Markdown text matching template structure
    lines = []
    lines.append("# แบบทดสอบประเมินผลความรู้ Phonics Grade 6 In English language")
    lines.append("")
    lines.append("> **คำชี้แจง**: แบบทดสอบนี้ใช้สำหรับประเมินผลสัมฤทธิ์ทางการเรียนรู้ Phonics Grade 6 (Affixes: Prefixes, Suffixes, Root Words & Stress Patterns) ครอบคลุม 4 ส่วน จำนวนรวม 115 ข้อ คะแนนเต็ม 150 คะแนน")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# Section A: Multiple Choice Questions (ข้อ 1 - 60)")
    lines.append("")

    opt_map = {"A": "ก", "B": "ข", "C": "ค", "D": "ง"}

    for idx, q in enumerate(mcq_questions, 1):
        topic, lo, diff, question, options, ans_letter, exp = q
        lines.append(f"#### ข้อ {idx}")
        lines.append(f"* **Topic**: {topic}")
        lines.append(f"* **Learning Objective**: {lo}")
        lines.append(f"* **Difficulty**: {diff}")
        lines.append(f"* **Question**: {question}")
        lines.append(f"* ก. {options[0]}")
        lines.append(f"* ข. {options[1]}")
        lines.append(f"* ค. {options[2]}")
        lines.append(f"* ง. {options[3]}")
        ans_th = opt_map[ans_letter]
        lines.append(f"* **Correct Answer**: {ans_th}")
        lines.append(f"* **Explanation**: {exp}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("# Section B: True / False Questions (ข้อ 61 - 90)")
    lines.append("")

    for idx, q in enumerate(tf_questions, 61):
        topic, lo, diff, stmt, ans_tf, exp = q
        lines.append(f"#### ข้อ {idx}")
        lines.append(f"* **Topic**: {topic}")
        lines.append(f"* **Learning Objective**: {lo}")
        lines.append(f"* **Difficulty**: {diff}")
        lines.append(f"* **Question**: \"{stmt}\"")
        lines.append(f"* **Answer**: {ans_tf}")
        lines.append(f"* **Explanation**: {exp}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("# Section C: Scenario-Based Questions (ข้อ 91 - 105)")
    lines.append("")

    for idx, q in enumerate(scenario_questions, 91):
        topic, lo, diff, scen, question, ans, exp = q
        lines.append(f"#### ข้อ {idx}")
        lines.append(f"* **Topic**: {topic}")
        lines.append(f"* **Learning Objective**: {lo}")
        lines.append(f"* **Difficulty**: {diff}")
        lines.append(f"* **Scenario**: {scen}")
        lines.append(f"* **Question**: {question}")
        lines.append(f"* **Answer**: {ans}")
        lines.append(f"* **Explanation**: {exp}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("# Section D: Short Answer Questions (ข้อ 106 - 115)")
    lines.append("")

    for idx, q in enumerate(short_answer_questions, 106):
        topic, lo, diff, question, exp_ans, exp = q
        lines.append(f"#### ข้อ {idx}")
        lines.append(f"* **Topic**: {topic}")
        lines.append(f"* **Learning Objective**: {lo}")
        lines.append(f"* **Difficulty**: {diff}")
        lines.append(f"* **Question**: {question}")
        lines.append(f"* **Expected Answer**: {exp_ans}")
        lines.append(f"* **Explanation**: {exp}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Answer Key & Explanations")
    lines.append("")
    lines.append("Complete Answer Key embedded in above sections.")

    filepath = "Knowledge_Assessment_Phonics_Gr6.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Generated {filepath} successfully from PDF OCR content!")

if __name__ == "__main__":
    generate_phonics_quiz_from_pdf()
