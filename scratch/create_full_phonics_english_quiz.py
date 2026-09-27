import os

def generate_phonics_quiz():
    mcq_questions = [
        # 1-10: Vowels & Vowel Teams
        ("Short and Long Vowels", "Distinguish between short and long vowel sounds.", "Easy",
         "Which word contains a short 'i' sound?",
         ["Kite", "Stick", "Light", "Drive"], "B",
         "'Stick' has a short 'i' sound /ɪ/. 'Kite', 'light', and 'drive' have the long 'i' sound /aɪ/."),
        
        ("Vowel Teams", "Identify vowel team patterns in Grade 6 vocabulary.", "Medium",
         "Which word features the vowel team 'ea' pronounced as a short 'e' /ɛ/?",
         ["Beach", "Leader", "Heavy", "Stream"], "C",
         "In 'heavy', 'ea' represents the short 'e' sound /ɛ/, unlike 'beach', 'leader', and 'stream' where 'ea' is long /iː/."),

        ("Split Digraphs", "Recognize magic-e / split digraph long vowel structures.", "Easy",
         "In which word does the final silent 'e' change a short vowel into a long vowel?",
         ["Have", "Give", "Globe", "Come"], "C",
         "'Globe' uses silent 'e' to make 'o' long /oʊ/. Words like 'have' and 'give' are phonetic exceptions with short vowels."),

        ("R-Controlled Vowels", "Identify r-controlled vowel sounds (bossy r).", "Medium",
         "Which word contains an r-controlled vowel sound matching the sound in 'nurse'?",
         ["Garden", "Storm", "Thirst", "March"], "C",
         "'Thirst' contains 'ir' which makes the /ɜːr/ sound, the same r-controlled sound as 'ur' in 'nurse'."),

        ("Diphthongs", "Recognize diphthong vowel combinations /ɔɪ/ and /aʊ/.", "Medium",
         "Which of the following words contains a diphthong sound as heard in 'boy'?",
         ["Choice", "Coat", "Boat", "Chief"], "A",
         "'Choice' contains the diphthong 'oi' producing the /ɔɪ/ sound, identical to 'oy' in 'boy'."),

        ("Diphthongs", "Distinguish 'ou' and 'ow' diphthong sound patterns.", "Medium",
         "Which word contains the diphthong sound /aʊ/ as in 'shout'?",
         ["Window", "Crowd", "Yellow", "Shadow"], "B",
         "'Crowd' contains the diphthong /aʊ/, whereas 'window', 'yellow', and 'shadow' end in long /oʊ/."),

        ("Long Vowel Digraphs", "Analyze long 'o' graphemes.", "Easy",
         "Which word uses the 'oa' digraph to create the long 'o' sound?",
         ["Coast", "Cost", "Lost", "Frost"], "A",
         "'Coast' uses the 'oa' digraph for the long 'o' sound /oʊ/, while the others feature short 'o' /ɒ/."),

        ("Hard and Soft Vowels", "Understand how vowels affect hard and soft consonant sounds.", "Hard",
         "Why does the letter 'c' make a soft /s/ sound in the word 'circle'?",
         ["Because it comes at the beginning of the word", "Because it is followed by the vowel 'i'", "Because it is followed by an 'r'", "Because it is a two-syllable word"], "B",
         "The letter 'c' makes a soft /s/ sound when followed by 'e', 'i', or 'y'."),

        ("Long Vowel Patterns", "Identify long 'e' spelling patterns.", "Easy",
         "Which word represents a long 'e' sound using the 'ie' vowel pattern?",
         ["Friend", "Relief", "Pie", "Tie"], "B",
         "In 'relief', 'ie' makes the long 'e' sound /iː/. In 'friend' it is short /ɛ/, and in 'pie'/'tie' it makes long 'i'."),

        ("Schwa Sound", "Identify the unstressed schwa /ə/ sound.", "Hard",
         "Which underlined vowel sound represents an unstressed schwa sound /ə/?",
         ["b<u>a</u>nana (first vowel)", "c<u>a</u>t", "d<u>o</u>g", "m<u>u</u>g"], "A",
         "The first 'a' in 'banana' is in an unstressed syllable and is pronounced as a schwa /ə/."),

        # 11-20: Consonants, Blends & Digraphs
        ("Consonant Blends", "Identify initial triple consonant blends.", "Medium",
         "Which word begins with a triple consonant blend?",
         ["Black", "Sprint", "Clock", "Flight"], "B",
         "'Sprint' begins with the three-consonant blend 'spr-' /spr/."),

        ("Consonant Digraphs", "Distinguish voiced and voiceless 'th' digraphs.", "Hard",
         "Which word contains a VOICED 'th' sound /ð/?",
         ["Think", "Thumb", "Feather", "Thirty"], "C",
         "'Feather' contains the voiced 'th' sound /ð/. 'Think', 'thumb', and 'thirty' contain voiceless 'th' /θ/."),

        ("Consonant Digraphs", "Identify the 'ph' digraph sound.", "Easy",
         "What sound does the digraph 'ph' make in the word 'phantom'?",
         ["/p/", "/h/", "/f/", "/v/"], "C",
         "The digraph 'ph' represents the /f/ phoneme in English."),

        ("Silent Letters", "Identify silent consonant patterns (kn, wr, mb, gn).", "Medium",
         "Which word contains a silent 'w'?",
         ["Water", "Wrist", "Winter", "Winter"], "B",
         "In 'wrist', the initial 'w' before 'r' is silent."),

        ("Silent Letters", "Identify silent 'b' after 'm'.", "Easy",
         "In which of the following words is the letter 'b' silent?",
         ["Crumble", "Thumb", "Robber", "Subway"], "B",
         "The letter 'b' is silent when following 'm' at the end of a root word, as in 'thumb'."),

        ("Hard and Soft G", "Determine when 'g' makes a soft /dʒ/ sound.", "Medium",
         "Which word features a SOFT 'g' sound?",
         ["Giraffe", "Gorilla", "Garden", "Guitar"], "A",
         "'Giraffe' has a soft 'g' /dʒ/ sound because 'g' is followed by 'i'."),

        ("Trigraphs", "Recognize trigraph spelling patterns like '-tch' and '-dge'.", "Hard",
         "Why is the trigraph '-dge' used instead of 'g' in the word 'bridge'?",
         ["Because it follows a long vowel", "Because it follows a short vowel sound", "Because it is at the start of a word", "Because it is a compound word"], "B",
         "The trigraph '-dge' is used directly after a short vowel sound to represent /dʒ/."),

        ("Final Consonant Blends", "Identify final consonant blends.", "Easy",
         "Which word ends with the consonant blend '-st'?",
         ["Pass", "Forest", "Mess", "Less"], "B",
         "'Forest' ends with the blend '-st' where both /s/ and /t/ sounds are voiced in sequence."),

        ("Silent Letters", "Identify silent 't' in common words.", "Hard",
         "Which word contains a silent letter 't'?",
         ["Castle", "Plastic", "Active", "Travel"], "A",
         "In 'castle', the letter 't' is silent /kæsəl/."),

        ("Ch Digraph Variations", "Identify different sounds of the digraph 'ch'.", "Hard",
         "In which word is the digraph 'ch' pronounced as /k/?",
         ["Chair", "Chef", "Character", "Bench"], "C",
         "In 'character' (derived from Greek), 'ch' is pronounced as /k/. In 'chef' it is /ʃ/, and in 'chair' it is /tʃ/."),

        # 21-30: Syllabification & Syllable Types
        ("Syllables", "Count syllables in multi-syllable academic words.", "Medium",
         "How many syllables are in the word 'investigation'?",
         ["3", "4", "5", "6"], "C",
         "'in-ves-ti-ga-tion' consists of 5 distinct syllables."),

        ("Syllable Types", "Identify open vs closed syllables.", "Medium",
         "Which word begins with an OPEN syllable?",
         ["Magnet", "Robot", "Rabbit", "Doctor"], "B",
         "'Robot' splits as 'ro-bot'. The first syllable ends in a vowel, making it an open syllable with a long 'o'."),

        ("Syllable Types", "Identify Consonant-le (CLE) syllables.", "Easy",
         "Which word ends with a Consonant-le (CLE) syllable?",
         ["Bottle", "Hotel", "Model", "Tunnel"], "A",
         "'Bottle' ends with the Consonant-le syllable '-tle'. 'Hotel', 'model', and 'tunnel' end in '-el'."),

        ("Syllable Division", "Apply the VC/CV division pattern.", "Medium",
         "Where should the word 'napkin' be divided into syllables?",
         ["na-pkin", "nap-kin", "napk-in", "n-apkin"], "B",
         "According to the VC/CV rule (vowel-consonant/consonant-vowel), split between the two middle consonants: nap-kin."),

        ("Syllable Division", "Apply V/CV vs VC/V open and closed rules.", "Hard",
         "Why is the first syllable in 'silent' open, while the first syllable in 'silence' is open as well, but 'silver' is closed?",
         ["Because silver has two consonants (l-v) splitting the vowels", "Because silver ends in r", "Because silence has 3 syllables", "Because silent is an adjective"], "A",
         "'Silver' follows the VC/CV pattern (sil-ver) closing the first syllable, whereas 'silent' follows V/CV (si-lent) keeping the first syllable open."),

        ("Vowel Team Syllables", "Identify vowel team syllable types.", "Medium",
         "What type of syllable is the first syllable in 'rainbow'?",
         ["Closed syllable", "Vowel Team syllable", "Open syllable", "R-controlled syllable"], "B",
         "'rain' contains the vowel team 'ai', making it a Vowel Team syllable."),

        ("R-Controlled Syllables", "Identify R-controlled syllable structure.", "Easy",
         "Which word contains an R-controlled syllable?",
         ["Paper", "Tiger", "Table", "Music"], "B",
         "'Tiger' splits into ti-ger, where '-ger' is an R-controlled syllable."),

        ("Syllable Accent & Stress", "Determine primary stress in noun vs verb pairs.", "Hard",
         "Where is the primary stress placed in the NOUN 'present'?",
         ["On the first syllable (PRE-sent)", "On the second syllable (pre-SENT)", "Equally on both syllables", "On the last letter"], "A",
         "In two-syllable noun/verb homographs, the noun typically receives stress on the FIRST syllable (PRE-sent), while the verb is stressed on the SECOND (pre-SENT)."),

        ("Syllable Accent & Stress", "Identify stressed syllables in suffixes.", "Hard",
         "In words ending with '-tion' like 'education', where is the primary stress located?",
         ["On the suffix '-tion'", "On the syllable directly BEFORE '-tion'", "On the very first syllable", "On the root verb"], "B",
         "Words ending in '-tion' always have primary stress on the syllable immediately preceding '-tion' (ed-u-CA-tion)."),

        ("Compound Words", "Analyze syllabification in compound words.", "Easy",
         "How is the compound word 'sunflower' divided into syllables?",
         ["su-nflo-wer", "sun-flow-er", "sunf-low-er", "s-unflower"], "B",
         "Compound words divide between the compound components and syllable boundaries: sun-flow-er (3 syllables)."),

        # 31-40: Prefixes, Suffixes & Inflections
        ("Inflectional Endings", "Identify the pronunciation of past tense '-ed'.", "Medium",
         "In which word is the past-tense suffix '-ed' pronounced as an extra syllable /ɪd/?",
         ["Laughed", "Played", "Painted", "Washed"], "C",
         "When a verb base ends in /t/ or /d/ sound (like 'paint'), adding '-ed' creates an extra syllable pronounced /ɪd/ ('pain-ted')."),

        ("Inflectional Endings", "Identify the /t/ sound of '-ed'.", "Medium",
         "Which word's '-ed' ending is pronounced as /t/?",
         ["Jumped", "Cleaned", "Folded", "Rained"], "A",
         "Because 'jump' ends in the voiceless sound /p/, the '-ed' ending is pronounced as /t/ ('jumpt')."),

        ("Inflectional Endings", "Identify the /d/ sound of '-ed'.", "Medium",
         "Which word's '-ed' ending is pronounced as /d/?",
         ["Kicked", "Mended", "Smiled", "Stopped"], "C",
         "Because 'smile' ends in a voiced sound /l/, '-ed' is pronounced as /d/ ('smild')."),

        ("Plural Pronunciation", "Determine pronunciation of '-s' or '-es' endings.", "Hard",
         "In which word is the plural ending '-es' pronounced as /ɪz/?",
         ["Cats", "Dogs", "Buses", "Maps"], "C",
         "After sibilant sounds (/s/, /z/, /ʃ/, /tʃ/, /dʒ/), plural endings add a syllable pronounced /ɪz/ ('bus-es')."),

        ("Prefix Phonics", "Identify prefix sound change in 'un-'.", "Easy",
         "How does adding the prefix 'un-' alter the word 'happy'?",
         ["It changes the root vowel sound", "It adds an unstressed prefix syllable /ən/", "It makes the 'h' silent", "It changes happy into a noun"], "B",
         "Adding 'un-' adds the prefix syllable /ən/ to create 'unhappy' without changing the root pronunciation."),

        ("Suffix Phonics", "Recognize phonetic patterns of '-ous'.", "Medium",
         "What is the pronunciation of the suffix '-ous' in 'dangerous'?",
         ["/aʊs/", "/əs/", "/uːs/", "/ɒs/"], "B",
         "The suffix '-ous' is pronounced with a schwa sound /əs/ in words like 'dangerous' and 'famous'."),

        ("Suffix Phonics", "Distinguish '-tion' vs '-sion' sounds.", "Hard",
         "Which word features the voiced suffix sound /ʒən/ instead of /ʃən/?",
         ["Nation", "Action", "Vision", "Section"], "C",
         "In 'vision', '-sion' follows a vowel and makes the voiced sound /ʒən/, whereas '-tion' in 'nation' makes voiceless /ʃən/."),

        ("Prefix Assimilation", "Identify phonetic prefix assimilation (in-, im-, il-, ir-).", "Hard",
         "Why does the prefix 'in-' change to 'im-' before the word 'possible'?",
         ["Because 'p' is a bilabial sound that pairs naturally with 'm'", "Because 'in-' is grammatically illegal", "Because 'possible' starts with a vowel", "Because 'm' makes the vowel long"], "A",
         "Prefix assimilation aligns the nasal consonant /m/ with the bilabial consonant /p/ for ease of articulation."),

        ("Suffix Spelling Rules", "Dropping silent 'e' when adding vowel suffixes.", "Medium",
         "When adding '-ing' to 'make', why is the silent 'e' dropped?",
         ["Because two vowels cannot be next to each other", "To prevent creating a double vowel pattern while keeping the root clear", "Because 'ing' starts with a consonant", "Because make becomes a noun"], "B",
         "The silent 'e' is dropped before adding a suffix starting with a vowel (-ing) to form 'making'."),

        ("Suffix Spelling Rules", "Doubling final consonant rule.", "Medium",
         "Why is the final 'p' doubled in 'stopping'?",
         ["Because stop ends in a single short vowel + single consonant in a 1-syllable word", "Because stop has a long vowel", "Because p is silent", "Because ing requires two p's always"], "A",
         "1-1-1 rule: A 1-syllable word ending in 1 short vowel and 1 consonant doubles the final consonant before a vowel suffix."),

        # 41-50: Homophones, Homographs & Spelling Patterns
        ("Homophones", "Identify correct phonic homophone pairs.", "Easy",
         "Which pair of words are HOMOPHONES (sound the same but have different spellings and meanings)?",
         ["Read (present) / Read (past)", "Knight / Night", "Wind (breeze) / Wind (clock)", "Lead (metal) / Lead (guide)"], "B",
         "'Knight' /naɪt/ and 'Night' /naɪt/ sound identical, making them homophones."),

        ("Homographs", "Identify HOMOGRAPHS (same spelling, different pronunciation/meaning).", "Medium",
         "Which sentence uses 'lead' pronounced as /lɛd/ (the heavy metal)?",
         ["She will lead the team to victory.", "The pencil contains lead.", "Follow the leader.", "He leads the parade."], "B",
         "In 'the pencil contains lead', 'lead' is pronounced /lɛd/. As a verb meaning to guide, it is /liːd/."),

        ("Phonic Spelling Patterns", "Identify silent 'gh' patterns.", "Medium",
         "Which word contains the silent 'gh' in the vowel pattern '-ight'?",
         ["Ghost", "Flight", "Rough", "Lough"], "B",
         "'Flight' contains '-ight' where 'gh' is silent and 'i' is long /aɪ/."),

        ("Phonic Spelling Patterns", "Identify 'gh' pronounced as /f/.", "Medium",
         "In which of the following words is 'gh' pronounced as /f/?",
         ["Light", "Daughter", "Laughter", "Though"], "C",
         "In 'laughter' and 'enough', 'gh' is pronounced as the consonant sound /f/."),

        ("Phonic Spelling Patterns", "Analyze soft vs hard 'c' in words.", "Medium",
         "Which word contains BOTH a hard 'c' /k/ and a soft 'c' /s/?",
         ["Circus", "Cat", "City", "Cookie"], "A",
         "In 'circus', the first 'c' before 'i' is soft /s/, and the second 'c' before 'u' is hard /k/."),

        ("Phonic Spelling Patterns", "Analyze soft vs hard 'g' in words.", "Hard",
         "Which word contains BOTH a soft 'g' /dʒ/ and a hard 'g' /g/?",
         ["Garage", "Giant", "Game", "Geography"], "A",
         "In 'garage', the first 'g' before 'a' is hard /g/, and the second 'g' before 'e' is soft /ʒ/ or /dʒ/."),

        ("Grapheme-Phoneme Correspondence", "Identify multiple spellings for /ʃ/ sound.", "Hard",
         "Which word produces the /ʃ/ ('sh') sound using the spelling pattern 'ch'?",
         ["Chef", "Church", "Chorus", "Chain"], "A",
         "In 'chef' (borrowed from French), the letters 'ch' represent the /ʃ/ sound."),

        ("Grapheme-Phoneme Correspondence", "Identify spelling patterns for long /aɪ/.", "Medium",
         "Which word achieves the long 'i' sound /aɪ/ using the grapheme 'uy'?",
         ["Buy", "Guy", "Both A and B", "Neither A nor B"], "C",
         "Both 'buy' and 'guy' use the spelling pattern 'uy' to represent the long 'i' /aɪ/ sound."),

        ("Word Families", "Identify words belonging to the '-ought' phonics family.", "Medium",
         "Which word belongs to the same phonic family as 'thought' and 'bought'?",
         ["Through", "Caught", "Brought", "Drought"], "C",
         "'Brought' shares the '-ought' grapheme pattern pronounced as /ɔːt/."),

        ("Silent Letters", "Identify silent 'g' in '-gn' combinations.", "Easy",
         "In which word is the letter 'g' silent?",
         ["Design", "Dragon", "Glass", "Magnet"], "A",
         "In 'design', the letter 'g' preceding 'n' at the end of a syllable is silent."),

        # 51-60: Advanced Phonics & Pronunciation Rules
        ("Accent & Intonation", "Understand how stress changes word class.", "Hard",
         "How does pronunciation change between 'RE-cord' (noun) and 're-CORD' (verb)?",
         ["The vowel in the first syllable becomes a schwa in the verb form", "The consonant changes", "The second syllable becomes silent", "There is no change"], "A",
         "In 're-CORD' (verb), the first syllable shifts to an unstressed schwa /rɪ/ or /rə/, whereas in 'RE-cord' (noun), it is stressed /rɛ/."),

        ("Prefix Phonics", "Analyze prefix 'dis-' phonics.", "Easy",
         "What is the phonetic breakdown of the word 'disagree'?",
         ["dis-a-gree (3 syllables)", "di-sa-gree", "disag-ree", "d-isagree"], "A",
         "'dis-a-gree' has 3 syllables with prefix 'dis-', root 'a-', and base 'gree'."),

        ("Silent Letters", "Identify silent 'l' in word families.", "Medium",
         "In which word is the letter 'l' silent?",
         ["Calm", "Cold", "Film", "Fold"], "A",
         "In 'calm', 'half', and 'talk', the letter 'l' is silent."),

        ("Silent Letters", "Identify silent 'h' in 'wh' words.", "Easy",
         "Which word has a silent 'h' after 'w'?",
         ["Whisper", "Who", "Whose", "Whole"], "A",
         "In 'whisper', 'w' is voiced /w/ and 'h' is silent. In 'who', 'whose', and 'whole', 'w' is silent and 'h' is sounded /h/."),

        ("Contractions Phonics", "Analyze vowel omission in contractions.", "Easy",
         "What sound does the apostrophe replace in the contraction 'can't'?",
         ["The vowel sound /o/ in 'not'", "The letter 'a'", "The letter 'c'", "The letter 't'"], "A",
         "'Can't' contracts 'cannot', omitting the 'no' sound."),

        ("Vowel Length Rules", "Analyze open syllable vowel length.", "Medium",
         "Why is the vowel 'e' long in the word 'secret'?",
         ["Because it ends the first open syllable (se-cret)", "Because it has a silent e at the end", "Because c is soft", "Because it is a single-syllable word"], "A",
         "In 'se-cret', the first syllable is open ('se-'), causing the vowel 'e' to be long /iː/."),

        ("Consonant Doubling Phonics", "Phonetic function of double consonants.", "Hard",
         "What is the main phonetic role of double consonants in words like 'letter' and 'summer'?",
         ["They indicate that the preceding vowel is short", "They are both pronounced separately", "They make the word longer", "They change the accent to the end"], "A",
         "Double consonants act as a marker showing that the preceding vowel in the syllable is short."),

        ("R-Controlled Variations", "Identify 'air' sound graphemes.", "Medium",
         "Which word contains the /ɛər/ sound spelled with 'are'?",
         ["Share", "Are", "Car", "Far"], "A",
         "'Share' uses 'are' to make the /ɛər/ sound. 'Are' is an exception pronounced /ɑːr/."),

        ("Phoneme Segmentation", "Count total phonemes in a word.", "Hard",
         "How many phonemes (individual sounds) are in the word 'box'?",
         ["2", "3", "4", "5"], "C",
         "'Box' has 4 phonemes: /b/ /ɒ/ /k/ /s/. The letter 'x' represents two phonemes /k/ + /s/."),

        ("Phoneme Blending", "Identify word formed by phoneme blending.", "Medium",
         "Blending the phonemes /k/ /l/ /aɪ/ /m/ forms which word?",
         ["Claim", "Climb", "Climate", "Clamp"], "B",
         "Blending /k/ + /l/ + /aɪ/ + /m/ yields 'climb' (with silent 'b').")
    ]

    tf_questions = [
        # 61-90 True/False
        ("Vowel Digraphs", "Understand digraph concepts.", "Easy",
         "A vowel digraph consists of two vowels that come together to make one single vowel sound.", "True",
         "Vowel digraphs (like 'ai', 'oa', 'ee') feature two vowel letters representing one phoneme."),

        ("Consonant Blends", "Understand blend concepts.", "Easy",
         "In a consonant blend, each individual consonant sound can still be heard.", "True",
         "Unlike digraphs where two letters make one sound, in blends (like 'st' or 'bl') each sound is articulated."),

        ("Silent Letters", "Identify silent letters in 'wr-'.", "Easy",
         "The letter 'w' is silent in the word 'write'.", "True",
         "Initial 'w' followed by 'r' is always silent in English words like 'write' and 'wrong'."),

        ("Soft C Rules", "Recall soft C rules.", "Easy",
         "The letter 'c' always makes a hard /k/ sound when followed by the letter 'e'.", "False",
         "When 'c' is followed by 'e', 'i', or 'y', it makes a SOFT /s/ sound, as in 'cent' and 'city'."),

        ("Magic E Pattern", "Understand split digraph function.", "Easy",
         "The silent 'e' at the end of 'hop' turns it into 'hope' and changes the short vowel sound to a long vowel sound.", "True",
         "Silent 'e' signals that the preceding single vowel is long."),

        ("Syllable Definition", "Recall syllable definition.", "Easy",
         "Every English syllable must contain at least one vowel sound.", "True",
         "A syllable is a unit of pronunciation organized around a vowel sound peak."),

        ("Soft G Rules", "Recall soft G rules.", "Hard",
         "The letter 'g' in the word 'gate' is an example of a soft 'g' sound.", "False",
         "'Gate' contains a HARD 'g' /g/ sound because 'g' is followed by 'a'."),

        ("Diphthongs", "Understand diphthong concept.", "Medium",
         "A diphthong is a complex vowel sound where the voice glides from one vowel sound to another within the same syllable.", "True",
         "Diphthongs (like /ɔɪ/ in 'coin' or /aʊ/ in 'house') involve a phonetic glide between two vowel positions."),

        ("Voiced vs Voiceless TH", "Identify TH sound types.", "Medium",
         "The word 'math' contains a VOICED 'th' sound.", "False",
         "'Math' contains a VOICELESS 'th' /θ/ sound, produced without vocal cord vibration."),

        ("Past Tense -ed", "Recall -ed ending rules.", "Medium",
         "The past-tense ending '-ed' is pronounced as /t/ after voiceless consonant sounds like /p/, /k/, and /s/.", "True",
         "Voiceless root endings trigger the voiceless /t/ pronunciation for '-ed'."),

        ("Open Syllables", "Recall open syllable characteristics.", "Easy",
         "An open syllable ends in a consonant and usually has a short vowel sound.", "False",
         "An open syllable ends in a VOWEL and usually has a LONG vowel sound (e.g., 'me', 'go')."),

        ("Closed Syllables", "Recall closed syllable characteristics.", "Easy",
         "A closed syllable ends in a consonant and usually has a short vowel sound.", "True",
         "Closed syllables end in consonants, closing in the vowel and making it short (e.g., 'cat', 'bed')."),

        ("Trigraphs", "Recall trigraph definition.", "Medium",
         "A trigraph consists of three letters that represent a single sound, such as 'igh' in 'high'.", "True",
         "'igh' is a 3-letter grapheme (trigraph) representing the single vowel phoneme /aɪ/."),

        ("Homophones", "Recall homophone definition.", "Easy",
         "Homophones are words that are spelled the same but have different meanings and pronunciations.", "False",
         "Words with the same spelling but different pronunciations/meanings are HOMOGRAPHS. Homophones have the SAME SOUND but DIFFERENT spellings."),

        ("Schwa Sound", "Recall schwa sound characteristics.", "Hard",
         "The schwa sound /ə/ is the most common vowel sound in the English language and only occurs in UNSTRESSED syllables.", "True",
         "Schwa /ə/ occurs exclusively in unstressed syllables across English vocabulary."),

        ("Silent K Rule", "Recall silent K rule.", "Easy",
         "In the word 'knife', the letter 'k' is pronounced.", "False",
         "Initial 'k' before 'n' is silent in English."),

        ("R-Controlled Vowels", "Identify bossy R effect.", "Medium",
         "When a vowel is followed by 'r', the 'r' changes the vowel sound so it is neither strictly short nor long.", "True",
         "R-controlled vowels ('ar', 'er', 'ir', 'or', 'ur') create unique r-modified vowel phonemes."),

        ("Hard C Rules", "Recall hard C rules.", "Easy",
         "The letter 'c' in 'cat', 'cot', and 'cup' makes a hard /k/ sound.", "True",
         "'c' followed by 'a', 'o', or 'u' produces the hard /k/ sound."),

        ("Prefix Sound Changes", "Identify prefix phonics.", "Medium",
         "Adding the prefix 're-' to 'play' creates 'replay', which has two syllables.", "True",
         "'re-play' is a two-syllable word."),

        ("Silent L Pattern", "Identify silent L in 'walk'.", "Easy",
         "The letter 'l' is clearly pronounced in the word 'walk'.", "False",
         "In 'walk' and 'talk', the letter 'l' is silent /wɔːk/."),

        ("Suffix -tion", "Recall -tion pronunciation.", "Medium",
         "The suffix '-tion' is usually pronounced as /tiːɒn/.", "False",
         "'-tion' is pronounced as /ʃən/ or /ʃn̩/."),

        ("Compound Word Stress", "Recall compound word stress.", "Hard",
         "In most compound nouns like 'sunlight' and 'football', primary stress falls on the FIRST word.", "True",
         "Compound nouns typically receive primary stress on the first component (SUN-light, FOOT-ball)."),

        ("Double Consonants", "Recall double consonant sound rule.", "Medium",
         "In the word 'rabbit', both letters 'b' are pronounced separately as two distinct /b/ sounds.", "False",
         "Double consonants represent a single consonant sound; the second 'b' is not articulated twice."),

        ("Silent G Rule", "Identify silent G pattern.", "Medium",
         "The letter 'g' is silent in the word 'gnome'.", "True",
         "Initial 'g' before 'n' is silent, as in 'gnome' and 'gnat'."),

        ("Vowel Team 'oo'", "Recall 'oo' dual sounds.", "Medium",
         "The letter combination 'oo' makes the exact same sound in 'book' and 'boot'.", "False",
         "'Book' has short /ʊ/ sound, while 'boot' has long /uː/ sound."),

        ("Silent B Rule", "Identify silent B pattern.", "Easy",
         "The letter 'b' in 'climb' is silent.", "True",
         "Final 'b' following 'm' is silent in English words like 'climb', 'comb', and 'plumber'."),

        ("Voiceless TH", "Identify voiceless TH in 'thin'.", "Medium",
         "The word 'thin' begins with a voiced 'th' sound.", "False",
         "'Thin' begins with a VOICELESS 'th' sound /θ/."),

        ("Consonant-le Syllables", "Recall CLE syllable rule.", "Medium",
         "Consonant-le syllables always occur at the beginning of English words.", "False",
         "Consonant-le (CLE) syllables occur at the END of words (e.g., 'table', 'little')."),

        ("Phoneme Count in 'x'", "Recall 'x' phoneme breakdown.", "Hard",
         "The letter 'x' usually represents two consonant phonemes blended together (/k/ + /s/).", "True",
         "Letter 'x' (in 'fox' or 'six') represents two phonemes: /k/ + /s/."),

        ("Soft G Pattern", "Recall soft G with 'y'.", "Hard",
         "The letter 'g' makes a soft sound in the word 'gym'.", "True",
         "'g' followed by 'y' produces the soft /dʒ/ sound.")
    ]

    scenario_questions = [
        # 91-105 Scenario-Based Questions (2 pts each)
        ("Inflectional Endings (-ed)", "Categorize past-tense '-ed' pronunciations.", "Hard",
         "Teacher David gives his Grade 6 class three past-tense verb cards: 'wanted', 'helped', and 'called'. He asks students to sort them by their final '-ed' sound.",
         "Explain which category each word belongs to (/t/, /d/, or /ɪd/) and provide the phonetic reason for each.",
         "'wanted' belongs to /ɪd/ because the root ends in /t/. 'helped' belongs to /t/ because the root ends in voiceless /p/. 'called' belongs to /d/ because the root ends in voiced /l/.",
         "Roots ending in /t/ or /d/ take /ɪd/. Roots ending in voiceless consonants take /t/. Roots ending in voiced sounds take /d/."),

        ("Syllables & Stress", "Analyze stress shift in noun-verb pairs.", "Hard",
         "During a reading test, Maya reads the sentence: 'We need to record a new record for the school athletics team.' She pronounces both instances of 'record' identically.",
         "Identify Maya's error and explain how the syllable stress and vowel sound should differ between the two words.",
         "The first 'record' is a verb and should be stressed on the second syllable (re-CORD /rɪˈkɔːrd/). The second 'record' is a noun and should be stressed on the first syllable (RE-cord /ˈrɛkərd/).",
         "Two-syllable noun/verb homographs shift stress: Nouns are stressed on the 1st syllable; Verbs are stressed on the 2nd syllable."),

        ("Hard and Soft Consonants", "Analyze 'c' and 'g' pronunciation rules.", "Hard",
         "Leo is practicing reading new scientific terms. He comes across the word 'cyanide' and 'coagulate'. He wonders why the letter 'c' sounds like /s/ in the first word but like /k/ in the second.",
         "Explain the rule for soft 'c' versus hard 'c' that governs Leo's observation.",
         "'c' is soft /s/ in 'cyanide' because it is followed by 'y'. 'c' is hard /k/ in 'coagulate' because it is followed by 'o'.",
         "The letter 'c' turns soft (/s/) when followed by 'e', 'i', or 'y'. Otherwise, it remains hard (/k/)."),

        ("Silent Letter Identification", "Identify silent letters in medical/scientific terms.", "Hard",
         "In a science vocabulary list, students encounter the words 'pneumonia', 'psychology', and 'pterodactyl'.",
         "Identify the silent letter at the start of each word and explain the origin pattern of these spellings.",
         "The letter 'p' is silent in all three words (pneumonia, psychology, pterodactyl).",
         "Words derived from Greek beginning with 'pn-', 'ps-', or 'pt-' drop the initial /p/ sound in English pronunciation."),

        ("Homographs & Context", "Use context clues to determine homograph pronunciation.", "Hard",
         "Consider the sentence: 'The wind was too strong to wind up the sails on the boat.'",
         "Determine the correct pronunciation (phonetic sound) of 'wind' in both instances within this sentence.",
         "First 'wind' is a noun pronounced with short 'i' /wɪnd/. Second 'wind' is a verb pronounced with long 'i' /waɪnd/.",
         "Context determines homograph pronunciation: 'wind' /wɪnd/ (air current) vs 'wind' /waɪnd/ (to turn/twist)."),

        ("Syllable Division (VC/CV vs V/CV)", "Apply syllable division rules to new words.", "Hard",
         "An ESL student is trying to decode two unfamiliar words: 'signal' and 'silent'.",
         "Demonstrate how to divide both words into syllables and explain why the first vowel is short in 'signal' but long in 'silent'.",
         "'signal' splits as sig-nal (VC/CV), closing the first syllable so 'i' is short /ɪ/. 'silent' splits as si-lent (V/CV), leaving the first syllable open so 'i' is long /aɪ/.",
         "VC/CV pattern divides between consonants creating closed short-vowel syllables. V/CV pattern divides before the consonant creating open long-vowel syllables."),

        ("Vowel Digraphs vs Diphthongs", "Compare vowel team categories.", "Hard",
         "A student classifies 'boat' and 'boil' both as 'vowel digraphs'. Their teacher notes that 'boil' contains a diphthong while 'boat' contains a pure vowel digraph.",
         "Explain the phonetic difference between a pure vowel digraph and a diphthong using these examples.",
         "'boat' contains a pure vowel digraph ('oa') making one static long vowel sound /oʊ/. 'boil' contains a diphthong ('oi') where the voice glides from /ɔ/ to /ɪ/.",
         "Vowel digraphs yield a single steady vowel sound; diphthongs involve a active voice glide across two vowel sound positions."),

        ("R-Controlled Vowels", "Categorize r-controlled vowel spellings.", "Medium",
         "Grade 6 students are given the words 'fern', 'bird', and 'turn'. The teacher asks if these three words rhyme.",
         "Do these words rhyme? Explain the phonological rule regarding 'er', 'ir', and 'ur'.",
         "Yes, all three words rhyme. The spellings 'er', 'ir', and 'ur' frequently produce the exact same r-controlled vowel sound /ɜːr/.",
         "Despite different vowel spellings, 'er', 'ir', and 'ur' in stressed syllables share the /ɜːr/ phoneme."),

        ("Schwa Sound Analysis", "Identify schwa sounds in multi-syllable vocabulary.", "Hard",
         "In the word 'photography', students notice that the letter 'o' appears three times, but it is pronounced differently each time.",
         "Analyze the three 'o' sounds in 'pho-tog-ra-phy' and identify which one represents the schwa sound.",
         "1st 'o' (pho-) is schwa /fə/, 2nd 'o' (-tog-) is stressed short /ɒ/ (or /ɑː/), 3rd 'o' (-gra-phy) does not exist (the 'a' is schwa /rə/). The 1st 'o' is a schwa /ə/.",
         "Unstressed syllables in multi-syllable words reduce vowels to schwa /ə/."),

        ("Suffix Spelling Changes", "Apply consonant doubling rule (1-1-1 rule).", "Hard",
         "Compare adding '-ing' to 'hop' (hopping) versus adding '-ing' to 'hope' (hoping).",
         "Explain why 'hop' doubles the 'p' while 'hope' does not, and describe how this affects reader pronunciation.",
         "'hop' is a 1-1-1 word (1 syllable, 1 short vowel, 1 consonant), so 'p' is doubled to keep the vowel short in 'hopping'. 'hope' has a silent 'e' which is dropped to form 'hoping' with a long vowel.",
         "Doubling the consonant prevents the vowel from opening into a long sound."),

        ("Trigraphs vs Blends", "Distinguish trigraphs from consonant blends.", "Hard",
         "Analyze the words 'splash' and 'scratch' versus 'catch' and 'bridge'.",
         "Explain the difference between a initial 3-consonant blend ('spl-', 'scr-') and a final trigraph ('-tch', '-dge').",
         "'spl-' and 'scr-' are blends where 3 consonant sounds are heard together. '-tch' and '-dge' are trigraphs where 3 letters combine to form 1 single sound (/tʃ/ and /dʒ/).",
         "Blends maintain individual phonemes; trigraphs collapse three letters into one single phoneme."),

        ("Voiced vs Voiceless Consonant Pairs", "Identify cognate consonant pairs.", "Hard",
         "The consonant sounds /p/ and /b/, /t/ and /d/, /f/ and /v/ are called cognate pairs.", "Explain what makes these pairs related and how a speaker distinguishes between them.",
         "Each pair shares the exact same mouth position and articulation point. They are distinguished solely by voicing: one is voiceless (no vocal cord vibration) and one is voiced.",
         "Cognate pairs share place and manner of articulation, differing only in vocal cord vibration (voicing)."),

        ("Homophones in Context", "Differentiate homophone spellings by meaning.", "Medium",
         "A student writes: 'The knight rode his horse threw the dark night.'",
         "Identify the spelling error in this sentence, explain why it occurred phonetically, and state the correct word.",
         "The student wrote 'threw' (past tense of throw) instead of 'through' (preposition). Both are homophones pronounced /θruː/.",
         "Homophones share identical pronunciation /θruː/, causing spelling confusion if context is ignored."),

        ("Prefix Assimilation", "Analyze prefix sound changes (in- to im-).", "Hard",
         "Why does the prefix 'in-' become 'im-' in 'imperfect', but 'il-' in 'illegal' and 'ir-' in 'irresponsible'?",
         "Explain the linguistic reason behind these prefix spelling and sound changes.",
         "This is prefix assimilation. The final consonant of 'in-' adapts to match the starting sound of the root word for smoother pronunciation.",
         "Assimilation modifies prefix consonants to match the place of articulation of the base root sound."),

        ("Contractions & Pronunciation", "Analyze phonetics of irregular contractions.", "Medium",
         "Why is 'will not' contracted to 'won't' instead of 'willn't'?",
         "Explain the historical phonological reason why the vowel sound changes in this contraction.",
         "'Won't' derives from an older English verb form 'woll not'. When contracted, the vowel /oʊ/ was preserved in 'won't'.",
         "Historical sound changes from 'woll not' preserved the long /oʊ/ vowel sound in the modern contraction 'won't'.")
    ]

    short_answer_questions = [
        # 106-115 Short Answer Questions (3 pts each)
        ("Syllabification Rules", "Explain the 6 main English syllable types.", "Hard",
         "List and briefly describe 4 of the 6 major English syllable types (Closed, Open, Magic E, Vowel Team, R-Controlled, Consonant-le).",
         "1. Closed (ends in consonant, short vowel, e.g., cat). 2. Open (ends in vowel, long vowel, e.g., go). 3. V Magic E (ends in silent e, long vowel, e.g., bike). 4. Vowel Team (2 vowels make 1 sound, e.g., boat). 5. R-Controlled (vowel followed by r, e.g., car). 6. Consonant-le (ends in consonant+le, e.g., table).",
         "Full explanation of at least 4 syllable types with examples."),

        ("Past Tense '-ed' Rules", "State the 3 rules for pronouncing past-tense '-ed'.", "Hard",
         "Write down the three phonetic rules for pronouncing the past-tense suffix '-ed' (/t/, /d/, /ɪd/) with one example for each.",
         "1. Pronounced /ɪd/ after /t/ or /d/ sounds (e.g., wanted, needed). 2. Pronounced /t/ after voiceless consonant sounds (e.g., walked, stopped). 3. Pronounced /d/ after voiced sounds (e.g., played, cleaned).",
         "Correct formulation of all 3 rules with valid word examples."),

        ("Soft vs Hard C and G Rules", "Formulate soft C and G spelling rules.", "Hard",
         "State the general rule that determines whether the letters 'c' and 'g' are pronounced with a hard sound or a soft sound.",
         "The letters 'c' and 'g' make soft sounds (/s/ and /dʒ/) when followed by 'e', 'i', or 'y'. They make hard sounds (/k/ and /g/) when followed by 'a', 'o', 'u', or consonants.",
         "Clear statement of the e, i, y rule for soft c/g."),

        ("Voiced vs Voiceless TH", "Explain voiced vs voiceless TH with examples.", "Hard",
         "Explain the difference between a voiced 'th' and a voiceless 'th' sound, and provide two example words for each.",
         "Voiced 'th' /ð/ uses vocal cord vibration (e.g., 'this', 'mother'). Voiceless 'th' /θ/ uses only air stream without vocal cord vibration (e.g., 'think', 'bath').",
         "Accurate distinction between voiced /ð/ and voiceless /θ/ with 2 correct examples for each."),

        ("Schwa Sound Explanation", "Define the schwa sound and its role in English.", "Hard",
         "What is the schwa sound /ə/? Where does it occur in words, and why is it important for English pronunciation?",
         "Schwa /ə/ is a neutral, unstressed vowel sound (like 'uh'). It occurs in unstressed syllables of multi-syllable words (e.g., 'a' in 'about'). It is essential for natural speech rhythm.",
         "Comprehensive definition including unstressed syllable context and phonetic symbol /ə/."),

        ("Homophones vs Homographs", "Compare and contrast homophones and homographs.", "Hard",
         "Define 'homophones' and 'homographs', and provide one example pair for each.",
         "Homophones: Words with the SAME SOUND, different spellings/meanings (e.g., knight/night). Homographs: Words with the SAME SPELLING, different sounds/meanings (e.g., lead /liːd/ to guide vs lead /lɛd/ metal).",
         "Clear definitions of both terms with accurate example pairs showing sound/spelling contrasts."),

        ("The 1-1-1 Doubling Rule", "Explain the 1-1-1 consonant doubling rule.", "Hard",
         "Explain the '1-1-1 Rule' for doubling a final consonant when adding a suffix starting with a vowel.",
         "If a word has 1 syllable, 1 short vowel, and ends in 1 consonant (1-1-1), double the final consonant before adding a vowel suffix (e.g., run -> running, sit -> sitting).",
         "Explanation must mention 1 syllable, 1 short vowel, 1 consonant, and vowel suffix condition."),

        ("Diphthongs vs Vowel Teams", "Distinguish diphthongs from monophthongs.", "Hard",
         "What is a diphthong? Give two examples of diphthong letter combinations and the sounds they produce.",
         "A diphthong is a gliding vowel sound where the tongue moves from one vowel position to another within the same syllable. Examples: 'oi'/'oy' (/ɔɪ/ in coin/boy) and 'ou'/'ow' (/aʊ/ in house/cow).",
         "Definition must highlight gliding sound movement within one syllable and give 2 correct examples."),

        ("Silent Letters in English", "Explain why silent letters exist in English spelling.", "Hard",
         "Explain two reasons why English has so many silent letters (such as in 'knight', 'doubt', or 'castle').",
         "1. Historical sound changes: Letters were once pronounced in Old/Middle English (e.g., 'k' and 'gh' in 'knight'). 2. Etymological spellings: Scholars added silent letters to reflect Greek/Latin origins (e.g., 'b' in 'doubt' from Latin dubitandum).",
         "At least two valid linguistic/historical reasons explained clearly."),

        ("Primary Syllable Stress Rules", "Describe rules for primary stress placement.", "Hard",
         "Describe two general rules for predicting primary syllable stress in English words (e.g., two-syllable nouns vs verbs, or words ending in '-tion').",
         "Rule 1: In two-syllable words, NOUNS are usually stressed on the 1st syllable (PRES-ent), while VERBS are stressed on the 2nd (pre-SENT). Rule 2: Words ending in '-tion', '-sion', or '-ic' always have primary stress on the syllable immediately preceding the suffix (e.g., ed-u-CA-tion, gra-PHIC).",
         "Two accurate stress placement rules clearly stated with examples.")
    ]

    # Assemble Markdown text
    lines = []
    lines.append("# แบบทดสอบประเมินผลความรู้ Phonics Grade 6 In English language")
    lines.append("")
    lines.append("> **คำชี้แจง**: แบบทดสอบนี้ใช้สำหรับประเมินผลสัมฤทธิ์ทางการเรียนรู้ Phonics Grade 6 ครอบคลุม 4 ส่วน จำนวนรวม 115 ข้อ คะแนนเต็ม 150 คะแนน")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# Section A: Multiple Choice Questions (ข้อ 1 - 60)")
    lines.append("")

    opt_map = {"A": "ก", "B": "ข", "C": "ค", "D": "ง"}
    inv_opt_map = {"ก": "A", "ข": "B", "ค": "C", "ง": "D"}

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

    print(f"Generated {filepath} successfully!")

if __name__ == "__main__":
    generate_phonics_quiz()
