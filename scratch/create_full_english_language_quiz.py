import os
import shutil

def generate_english_language_quiz():
    # 60 MCQ Questions based on Enlish Languages Gr6-MidFinal.pdf
    mcq_questions = [
        # Unit 1: Comparative Adjectives (City vs. Countryside) (1-12)
        ("Comparative Adjectives Form", "Identify correct comparative form for short adjectives.", "Easy",
         "What is the comparative form of the adjective 'simple'?",
         ["more simple", "simpler", "simplest", "simplier"], "B",
         "Short adjectives or those ending in -e take '-r' or '-er' to form comparatives: 'simple' becomes 'simpler'."),

        ("Comparative Adjectives Form", "Identify correct comparative form for long adjectives.", "Easy",
         "Which is the correct comparative form of 'peaceful'?",
         ["peacefuler", "more peaceful", "most peaceful", "peacefully"], "B",
         "Adjectives with two or more syllables (like 'peaceful') use 'more' before the adjective: 'more peaceful'."),

        ("Comparative Adjectives Form", "Identify correct comparative form of 'modern'.", "Easy",
         "Complete the comparative pair: 'modern' -> ________.",
         ["moderner", "more modern", "most modern", "modernest"], "B",
         "The adjective 'modern' forms its comparative by adding 'more': 'more modern'."),

        ("Comparative Adjectives Form", "Identify correct comparative form of 'traditional'.", "Easy",
         "What is the comparative form of 'traditional'?",
         ["traditionaler", "more traditional", "most traditional", "traditionalest"], "B",
         "Long adjectives like 'traditional' use 'more' for comparison: 'more traditional'."),

        ("City vs Countryside Comparison", "Compare lifestyle characteristics of city and countryside.", "Easy",
         "Complete the sentence: 'Life in the city is ________ than in the countryside.'",
         ["more traditional", "simpler", "more modern", "more quiet"], "C",
         "According to the textbook dialogue, life in the city is 'more modern' than in the countryside."),

        ("City vs Countryside Comparison", "Identify comparative sentence structure.", "Easy",
         "Complete the sentence: 'Life in the countryside is ________ than in the city.'",
         ["simpler", "more modern", "more populated", "busier"], "A",
         "The textbook states: 'Life in the countryside is simpler than in the city.'"),

        ("Comparative Sentence Structure", "Use 'than' in comparative sentences.", "Easy",
         "Which word is used to connect two items being compared in a comparative sentence?",
         ["then", "than", "that", "from"], "B",
         "The conjunction 'than' is used after comparative adjectives (e.g., 'more modern than...')."),

        ("Comparative Adjectives - Interest", "Identify correct comparative of 'interesting'.", "Easy",
         "Sue thinks life in the city is ________ than life in the countryside.",
         ["interesting", "interestinger", "more interesting", "most interesting"], "C",
         "The comparative form of 'interesting' is 'more interesting'."),

        ("City vs Countryside Context", "Analyze traditional vs modern life.", "Medium",
         "Complete the conversation: A: 'Life in the countryside is more traditional than in the city.' B: 'Yes, but life in the city is ________.'",
         ["simpler", "more interesting", "harder", "peacefuler"], "B",
         "From the textbook dialogue on Page 2: 'Yes, but life in the city is more interesting.'"),

        ("Comparative Adjectives - Hard", "Identify comparative form of 'hard'.", "Easy",
         "What is the comparative form of 'hard'?",
         ["harder", "more hard", "hardest", "hardly"], "A",
         "One-syllable adjectives take '-er': 'hard' becomes 'harder'."),

        ("Comparative Practice Dialogue", "Complete comparative exchanges.", "Medium",
         "Complete: 'Life in the countryside is ________ (peaceful) than in the city.'",
         ["peacefuler", "more peaceful", "most peaceful", "peacefully"], "B",
         "'Peaceful' takes 'more peaceful' in comparative sentences."),

        ("Comparative Sentence Error Identification", "Recognize correct comparative syntax.", "Medium",
         "Which sentence is grammatically CORRECT?",
         ["Life in the city is more simpler than in the countryside.", "Life in the city is simpler than in the countryside.", "Life in the city is simplest than in the countryside.", "Life in the city is more simple than in the countryside."], "B",
         "'Simpler' is already a comparative form and should not be combined with 'more'."),

        # Unit 2: Superlative Adjectives & World Facts (13-24)
        ("Superlative Form - Fastest", "Identify superlative form of 'fast'.", "Easy",
         "What is the superlative form of the adjective 'fast'?",
         ["faster", "the fastest", "most fast", "fastly"], "B",
         "Short adjectives add '-est' with the definite article 'the': 'the fastest'."),

        ("Superlative World Fact - Land Animal", "Recall world record facts from text.", "Easy",
         "Which animal is the fastest land animal in the world according to the text?",
         ["The lion", "The cheetah", "The monkey", "The elephant"], "B",
         "Page 3 quiz question: 'The cheetah is the fastest land animal in the world.'"),

        ("Superlative Form - Deepest", "Identify superlative form of 'deep'.", "Easy",
         "The Congo River is over 200 metres deep. It is the ________ river in the world.",
         ["deeper", "deepest", "more deep", "most deepest"], "B",
         "The superlative form of 'deep' is 'deepest'."),

        ("Superlative World Fact - Deepest River", "Identify world fact about Congo River.", "Medium",
         "What is the deepest river in the world mentioned in the textbook?",
         ["The Amazon River", "The Nile River", "The Congo River", "The Mekong River"], "C",
         "Page 4 text: 'The Congo River... It's over 200 metres deep.'"),

        ("Superlative Form - Most Populated", "Identify superlative of multi-syllable adjective 'populated'.", "Medium",
         "What is the superlative form of 'populated'?",
         ["the populatedest", "the most populated", "the populateder", "more populated"], "B",
         "Multi-syllable adjectives use 'the most': 'the most populated'."),

        ("Superlative World Fact - UK City Population", "Identify London's population fact.", "Medium",
         "What is the most populated city in the UK with around 9 million people?",
         ["Manchester", "London", "Edinburgh", "Liverpool"], "B",
         "Page 4 text: 'What's the most populated city in the UK? It's London. It has around 9 million people.'"),

        ("Superlative World Fact - Largest Bird", "Recall facts about the ostrich.", "Easy",
         "Which bird is the largest bird in the world, weighing up to 160 kg?",
         ["The eagle", "The ostrich", "The penguin", "The flamingo"], "B",
         "Page 4 text: 'What's the largest bird? It's the ostrich. It weighs up to 160kg.'"),

        ("Superlative World Fact - Fastest Sea Animal", "Recall facts about the sailfish.", "Medium",
         "Which sea animal can swim at 110 kilometres per hour?",
         ["The dolphin", "The sailfish", "The blue whale", "The shark"], "B",
         "Page 4 text: 'What's the fastest sea animal? It's the sailfish. It can swim at 110 kilometres per hour.'"),

        ("Superlative Form - Largest", "Form superlative of 'large'.", "Easy",
         "What is the superlative form of 'large'?",
         ["larger", "the largest", "the most large", "the largestest"], "B",
         "Adjectives ending in -e add '-st' with 'the': 'the largest'."),

        ("Superlative Form - Noisiest", "Form superlative of adjectives ending in -y.", "Medium",
         "What is the superlative form of 'noisy'?",
         ["noisier", "the noisiest", "the most noisy", "noisiest"], "B",
         "Adjectives ending in -y change -y to -i and add '-est': 'the noisiest'."),

        ("Superlative Question Pattern", "Construct superlative wh- questions.", "Medium",
         "Choose the correct question format to ask about world records:",
         ["What's the most populated island in the world?", "What's populated island in the world?", "Which is more populated island in the world?", "What's populatedest island in the world?"], "A",
         "Superlative questions use: 'What's the + superlative adjective + noun...?'"),

        ("Superlative World Fact - World Lake Location", "Recall largest lake fact.", "Medium",
         "According to the class quiz on Page 3, where is the largest lake in the world located?",
         ["In Russia", "In Japan", "In Australia", "In Egypt"], "A",
         "Page 3 listening quiz: 'The largest lake in the world is in Russia.'"),

        # Unit 3: Holiday Packing & Question Tags (25-36)
        ("Holiday Essentials Vocabulary", "Identify travel vocabulary items.", "Easy",
         "Which document is essential when traveling to another country by plane?",
         ["first aid kit", "passport", "bug spray", "bumbag"], "B",
         "A passport is the official document required for international travel."),

        ("Holiday Essentials Vocabulary", "Identify travel health items.", "Easy",
         "What do you take on holiday to protect your skin from insect bites?",
         ["sunscreen", "bug spray", "purse", "passport"], "B",
         "Bug spray protects skin against insect bites while outdoors."),

        ("Holiday Essentials Vocabulary", "Identify emergency travel equipment.", "Easy",
         "What contains bandages and basic medical supplies for minor injuries during a trip?",
         ["bumbag", "first aid kit", "suitcase", "passport"], "B",
         "A first aid kit contains bandages and basic medical supplies."),

        ("Frequency Adverbs with Holiday Packing", "Apply adverbs of frequency.", "Easy",
         "Complete: 'I ________ take my passport on holiday because I cannot travel without it.'",
         ["never", "sometimes", "always", "seldom"], "C",
         "An essential item like a passport is 'always' packed for travel."),

        ("Frequency Adverbs Practice", "Distinguish frequency adverbs.", "Easy",
         "Which adverb of frequency means 'at no time' or 'not ever'?",
         ["always", "sometimes", "never", "usually"], "C",
         "'Never' means at no time or not ever."),

        ("Question Tag Basics - Affirmative Statement", "Form negative question tags for affirmative statements.", "Medium",
         "Complete the question tag: 'You packed your passport, ________?'",
         ["did you", "didn't you", "don't you", "haven't you"], "B",
         "An affirmative past simple statement takes a negative past tag: 'didn't you?'"),

        ("Question Tag Practice - Response", "Select correct positive answer to question tag.", "Medium",
         "A: 'You packed your purse, didn't you?' B: '________, I packed it in my bag.'",
         ["No, I didn't", "Yes, I did", "Yes, I am", "No, I don't"], "B",
         "Confirming an action in response to a tag question uses 'Yes, I did.'"),

        ("Question Tag Practice - Negative Response", "Select correct negative answer to question tag.", "Medium",
         "A: 'You packed your medicine, didn't you?' B: '________, I forgot it on the table.'",
         ["Yes, I did", "No, I didn't", "No, I don't", "Yes, I have"], "B",
         "Denying an action in response to a tag question uses 'No, I didn't.'"),

        ("Question Tag Structure Rule", "Understand statement-tag polarity rule.", "Medium",
         "What is the basic rule for forming question tags?",
         ["Positive statement -> Positive tag", "Positive statement -> Negative tag", "Negative statement -> Negative tag", "Tag tense is independent of statement tense"], "B",
         "A positive statement requires a negative tag (and vice versa)."),

        ("Holiday Vocabulary - Bumbag", "Identify small waist bag vocabulary.", "Easy",
         "A small pouch or bag worn around the waist or hips during travel is called a:",
         ["backpack", "bumbag", "suitcase", "duffel bag"], "B",
         "In British English, a small waist pouch is called a 'bumbag'."),

        ("Question Tag - Bug Spray", "Form tag question for packing bug spray.", "Medium",
         "Complete: 'You packed your bug spray, ________?'",
         ["did you", "didn't you", "aren't you", "haven't you"], "B",
         "Past simple positive verb 'packed' takes the negative tag 'didn't you?'."),

        ("Holiday Airport Dialogue", "Analyze story details from Page 5 listening.", "Medium",
         "In Nick's family story on Page 5, why did Mum and Dad need to go back home from the airport?",
         ["They forgot the money.", "Dad forgot his passport.", "They lost their bags.", "They missed the plane."], "B",
         "Page 5 answer key: 'Dad forgot his passport.'"),

        # Unit 4: Landscape Vocabulary & Reading Comprehension (37-48)
        ("Landscape Vocabulary - Valley", "Identify geographical landforms.", "Easy",
         "A low area of land between hills or mountains, often with a river running through it, is a:",
         ["desert", "valley", "ocean", "cave"], "B",
         "A valley is a low land area situated between hills or mountains."),

        ("Landscape Vocabulary - Cave", "Identify underground hollow features.", "Easy",
         "A large natural hole in the side of a cliff or hill, or under the ground, is called a:",
         ["cave", "waterfall", "reef", "valley"], "A",
         "A cave is a natural underground chamber or hole in a hill/cliff."),

        ("Landscape Vocabulary - Rainforest", "Identify dense tropical forest.", "Easy",
         "A thick tropical forest that receives high amounts of rainfall is called a:",
         ["desert", "rainforest", "valley", "glacier"], "B",
         "A rainforest is a dense forest in a tropical area with heavy rainfall."),

        ("Landscape Vocabulary - Desert", "Identify dry arid landform.", "Easy",
         "A large, dry, sandy area of land with very little rainfall is a:",
         ["rainforest", "desert", "valley", "waterfall"], "B",
         "A desert is a dry region with minimal rainfall."),

        ("Reading Comprehension - Daisy's Letter", "Identify main topic of Daisy's letter to grandparents.", "Medium",
         "In Daisy's letter on Page 8, what is she writing to her grandparents about?",
         ["Her school exam results", "Her upcoming holiday plans and places to visit", "Her new pet dog", "Her trip to the market"], "B",
         "Daisy writes to her grandparents about her upcoming holiday and deciding what places to visit."),

        ("Reading Comprehension - Daisy's Hiking Choice", "Identify specific details from reading passage.", "Medium",
         "Where does Daisy want to go hiking during her holiday?",
         ["In the desert", "In the large valley with a rainforest", "In the city center", "On top of Mount Everest"], "B",
         "Letter excerpt: 'There's a large valley with a rainforest at the bottom. I want to go hiking there...'"),

        ("Reading Comprehension - Daisy's Beach Activity", "Identify planned activities near hotel.", "Medium",
         "What does Daisy want to do at the beach near the hotel?",
         ["Go skiing", "Take a photo inside a big cave", "Build a wooden house", "Visit a farm"], "B",
         "Letter excerpt: 'There's a beach with some caves on it... I want to take a photo inside one.'"),

        ("Reading Comprehension - Daisy's Opinion on Desert", "Analyze character opinions in text.", "Medium",
         "Why does Daisy NOT want to visit the desert?",
         ["It is too cold.", "It is far away and she thinks it will be boring.", "She lost her map.", "Her parents forbid it."], "B",
         "Letter excerpt: '...it's far away, and I don't want to go. I think it'll be boring.'"),

        ("Modal Verbs for Possibility - Could", "Apply 'could' for holiday activity suggestions.", "Medium",
         "Complete: 'When we are at the beach, we ________ go kayaking in the ocean.'",
         ["must", "could", "shouldn't", "can't"], "B",
         "'Could' expresses possibility or suggestions for holiday activities."),

        ("Geography Activity Pairings", "Match outdoor activities with appropriate geographical features.", "Medium",
         "Which activity is best matched with a river or ocean?",
         ["climbing a volcano", "kayaking", "hiking up a mountain", "exploring a dry cave"], "B",
         "Kayaking is a water activity conducted on rivers or oceans."),

        ("Reading True/False Verification", "Verify passage statement.", "Medium",
         "True or False: Daisy wants to stay near the hotel instead of traveling far to the desert.",
         ["True", "False", "Not Mentioned", "Both True and False"], "A",
         "Daisy explicitly writes: 'I think we should stay near the hotel instead.'"),

        ("Landscape Feature - Reef", "Identify marine coral structure.", "Easy",
         "A line of rocks or coral underwater near the surface of the ocean is a:",
         ["reef", "valley", "volcano", "desert"], "A",
         "A coral reef is an underwater marine ecosystem formed by coral colonies."),

        # Unit 5: Natural Wonders of the World (49-60)
        ("Natural Wonder - Northern Lights", "Identify alternative name for Northern Lights.", "Easy",
         "What is another official scientific name for the Northern Lights?",
         ["Aurora Australis", "Aurora Borealis", "Grand Canyon", "Victoria Falls"], "B",
         "Page 9 text: 'Another name for this wonder is the Aurora Borealis.'"),

        ("Northern Lights Colors", "Recall natural phenomenon facts.", "Medium",
         "What is the most common normal color of the Northern Lights?",
         ["red", "pink", "green", "blue"], "C",
         "Page 9 text: 'The lights are usually green, but you might see pink, red or white.'"),

        ("Northern Lights Locations", "Identify countries where Northern Lights are best viewed.", "Medium",
         "Which of the following countries is one of the best places to see the Northern Lights?",
         ["Thailand", "Norway", "Egypt", "Brazil"], "B",
         "Page 9 text: 'The best places to see them are Iceland, Norway and Sweden.'"),

        ("Natural Wonder - Grand Canyon", "Identify location of Grand Canyon.", "Easy",
         "Where is the Grand Canyon located?",
         ["In the desert in Arizona, USA", "In Australia", "In Zambia, Africa", "In Mexico"], "A",
         "Page 9 text: 'This amazing natural wonder is in the desert in Arizona, USA.'"),

        ("Grand Canyon Dimensions", "Recall geographical dimensions from text.", "Medium",
         "How long is the Grand Canyon according to the textbook?",
         ["100 km", "446 km", "2,300 km", "8,849 m"], "B",
         "Page 9 text: 'It's 446km long, and in one place, it's 29km wide.'"),

        ("Natural Wonder - Mount Everest", "Identify highest mountain facts.", "Easy",
         "How high is Mount Everest, the highest mountain in the world?",
         ["2,800 m", "4,400 m", "8,849 m", "10,000 m"], "C",
         "Page 9 text: 'This mountain in Asia is 8,849m high...'"),

        ("Mount Everest Explorers", "Identify historical mountaineering facts.", "Medium",
         "Who were the first two people to reach the summit of Mount Everest in 1953?",
         ["Edmund Hillary and Tenzing Norgay", "Neil Armstrong and Buzz Aldrin", "Christopher Columbus and Marco Polo", "Frank and Nick"], "A",
         "Page 9 text: 'The first people to climb it were Edmund Hillary and Tenzing Norgay in 1953.'"),

        ("Natural Wonder - Parícutin Volcano", "Identify facts about Parícutin Volcano.", "Medium",
         "What makes Parícutin Volcano in Mexico unique among world volcanoes?",
         ["It is the highest mountain in the world.", "It is the youngest volcano in the world, growing in a farmer's field in 1943.", "It is located under the ocean.", "It is covered in ice."], "B",
         "Page 10 text: 'Before 1943, this was just a farmer's field... It's the youngest volcano in the world.'"),

        ("Natural Wonder - Victoria Falls", "Identify river location of Victoria Falls.", "Medium",
         "On which river in Africa is Victoria Falls located?",
         ["The Amazon River", "The Congo River", "The Zambezi River", "The Nile River"], "C",
         "Page 10 text: 'This large waterfall is on the Zambezi River in Africa.'"),

        ("Victoria Falls Border Countries", "Identify geographic border countries.", "Medium",
         "Victoria Falls is located on the border between which two African countries?",
         ["Egypt and Sudan", "Zambia and Zimbabwe", "Kenya and Tanzania", "South Africa and Namibia"], "B",
         "Page 10 text: '...is in two different countries - Zambia and Zimbabwe.'"),

        ("Natural Wonder - Great Barrier Reef", "Recall biological facts of Great Barrier Reef.", "Medium",
         "How many types of coral are found in Australia's Great Barrier Reef?",
         ["100 types", "400 types", "1,500 types", "4,000 types"], "B",
         "Page 10 text: '...famous for its 400 types of coral and 1,500 types of fish.'"),

        ("Great Barrier Reef Threat", "Identify environmental conservation threat.", "Medium",
         "Why is the coral in the Great Barrier Reef starting to die?",
         ["Because the ocean water is getting too cold", "Because the ocean is getting warmer", "Because there are too many fish", "Because tourists take all the coral"], "B",
         "Page 10 text: 'Sadly, as the ocean gets warmer, the coral is starting to die.'")
    ]

    # 30 True/False Questions
    tf_questions = [
        ("Comparative Adjective Formation", "Verify comparative rules for long adjectives.", "Easy",
         "Adjectives with three or more syllables (like 'traditional') form their comparative by adding '-er' at the end.", "False",
         "Long adjectives with two or more syllables use 'more' before the adjective (e.g. 'more traditional'), not '-er'."),

        ("City vs Countryside Comparative", "Verify textbook comparative statement.", "Easy",
         "According to the textbook dialogue, life in the countryside is simpler than in the city.", "True",
         "Page 2 text: 'Life in the countryside is simpler than in the city.'"),

        ("Modern Comparison", "Verify comparative statement about city life.", "Easy",
         "Life in the city is considered more modern than life in the countryside.", "True",
         "Page 2 text: 'Life in the city is more modern than in the countryside.'"),

        ("Cheetah Speed Record", "Verify animal speed record.", "Easy",
         "The cheetah is the fastest land animal in the world.", "True",
         "Page 3 quiz question: 'The cheetah is the fastest land animal in the world.'"),

        ("Congo River Depth", "Verify world river facts.", "Medium",
         "The Congo River is over 200 metres deep, making it the deepest river in the world.", "True",
         "Page 4 text confirms the Congo River is over 200 metres deep."),

        ("Sailfish Swimming Speed", "Verify marine animal speed record.", "Medium",
         "The sailfish can swim at speeds of up to 110 kilometres per hour.", "True",
         "Page 4 text: 'It can swim at 110 kilometres per hour.'"),

        ("Ostrich Weight Fact", "Verify bird weight records.", "Easy",
         "The ostrich is the largest bird in the world and can weigh up to 160 kg.", "True",
         "Page 4 text: 'What's the largest bird? It's the ostrich. It weighs up to 160kg.'"),

        ("Question Tag Polarity", "Verify grammar rule for tag questions.", "Medium",
         "An affirmative statement like 'You packed your passport' takes a negative question tag 'didn't you?'.", "True",
         "Positive statements take negative tags in English grammar."),

        ("Question Tag Response", "Verify short answer response to tag questions.", "Easy",
         "If someone asks 'You packed your purse, didn't you?' and you DID pack it, you should answer 'No, I didn't'.", "False",
         "To confirm that you packed it, you must answer 'Yes, I did.'"),

        ("Bumbag Definition", "Verify travel clothing vocabulary.", "Easy",
         "A bumbag is a type of heavy winter coat worn when hiking in cold mountains.", "False",
         "A bumbag is a small pouch or bag worn around the waist or hips during travel."),

        ("Frequency Adverb Position", "Verify placement of frequency adverbs.", "Medium",
         "In the sentence 'I always take my passport on holiday', the frequency adverb 'always' comes before the main verb.", "True",
         "Adverbs of frequency (always, sometimes, never) generally precede main action verbs."),

        ("Daisy's Letter Recipient", "Verify reading text details.", "Easy",
         "Daisy wrote her letter on Page 8 to her teacher, Ms Clark.", "False",
         "Daisy wrote her letter to her Grandma and Grandpa ('Dear Grandma and Grandpa')."),

        ("Daisy's Hiking Plan", "Verify reading text details.", "Medium",
         "Daisy wants to go hiking in a large valley with a rainforest at the bottom.", "True",
         "Page 8 text: 'There's a large valley with a rainforest at the bottom. I want to go hiking there...'"),

        ("Daisy's Desert Preference", "Verify character preference in reading text.", "Easy",
         "Daisy is very excited to visit the desert because she loves hot weather.", "False",
         "Daisy does NOT want to visit the desert because it's far away and she thinks it will be boring."),

        ("Northern Lights Color Range", "Verify natural phenomenon facts.", "Medium",
         "The Northern Lights are ONLY ever green and cannot appear in any other color.", "False",
         "Page 9 text: 'The lights are usually green, but you might see pink, red or white. Sometimes they're even blue!'"),

        ("Northern Lights Location", "Verify geographic viewing locations.", "Medium",
         "Iceland, Norway, and Sweden are among the best places in the world to view the Northern Lights.", "True",
         "Page 9 text explicitly lists Iceland, Norway, and Sweden as prime viewing locations."),

        ("Grand Canyon Age", "Verify geological age facts.", "Medium",
         "The Grand Canyon in Arizona, USA, is more than 6 million years old.", "True",
         "Page 9 text: 'It's more than 6 million years old.'"),

        ("Mount Everest Location", "Verify mountain geography.", "Easy",
         "Mount Everest is located in South America.", "False",
         "Mount Everest is located in Asia (in the Himalayas on the border of Nepal and China)."),

        ("Mount Everest First Ascent Year", "Verify historical mountaineering date.", "Medium",
         "The first successful climb to the summit of Mount Everest took place in 1953.", "True",
         "Page 9 text: 'The first people to climb it were Edmund Hillary and Tenzing Norgay in 1953.'"),

        ("Parícutin Volcano Origin", "Verify volcano formation history.", "Medium",
         "Parícutin Volcano was a 2,800m tall mountain for thousands of years before 1943.", "False",
         "Before 1943, Parícutin was just a flat farmer's field in Mexico before the volcano erupted and grew over 9 years."),

        ("Parícutin Volcano Age Classification", "Verify volcano classification.", "Easy",
         "Parícutin Volcano in Mexico is known as the youngest volcano in the world.", "True",
         "Page 10 text: '...and it's the youngest volcano in the world.'"),

        ("Victoria Falls River", "Verify waterfall geography.", "Medium",
         "Victoria Falls is located on the Amazon River.", "False",
         "Victoria Falls is located on the Zambezi River in Africa."),

        ("Victoria Falls Activities", "Verify tourist activities.", "Easy",
         "Tourists visiting Victoria Falls can participate in outdoor activities such as kayaking and rafting.", "True",
         "Page 10 text lists rafting, kayaking, horse riding and more."),

        ("Great Barrier Reef Location", "Verify reef marine geography.", "Easy",
         "The Great Barrier Reef is situated in the sea around Australia.", "True",
         "Page 10 text: 'In the sea around Australia, this natural wonder is famous...'"),

        ("Great Barrier Reef Coral Diversity", "Verify coral species count.", "Medium",
         "The Great Barrier Reef is home to about 400 different types of coral.", "True",
         "Page 10 text confirms 400 types of coral and 1,500 types of fish."),

        ("Great Barrier Reef Climate Impact", "Verify environmental conservation status.", "Medium",
         "Warming ocean temperatures are causing coral in the Great Barrier Reef to die.", "True",
         "Page 10 text: 'Sadly, as the ocean gets warmer, the coral is starting to die.'"),

        ("Amazon Rainforest Tree Count", "Verify Amazon facts.", "Hard",
         "There are more than 400 billion trees in the Amazon rainforest.", "True",
         "Page 10 listening exercise confirms there are over 400 billion trees in the Amazon."),

        ("Superlative Adjective Rule for Short Words", "Verify short adjective superlative spelling.", "Easy",
         "Short adjectives ending in a single consonant (like 'big') double the final consonant before adding '-est' ('the biggest').", "True",
         "Short CVC (consonant-vowel-consonant) adjectives double the final consonant (e.g. big -> biggest)."),

        ("Comparative Modifier 'Much'", "Verify usage of comparative modifiers.", "Medium",
         "The word 'much' can be added before a comparative adjective to emphasize a large difference (e.g. 'much faster').", "True",
         "'Much' is commonly used to intensify comparative adjectives (e.g., 'much faster', 'much more modern')."),

        ("Travel Packing Bug Spray Function", "Verify practical travel safety.", "Easy",
         "Bug spray is used to keep insects away when going outdoors or sleeping near rainforests.", "True",
         "Bug spray is an essential repellent used to protect travelers from insect bites.")
    ]

    # 15 Scenario-Based Questions
    sc_questions = [
        ("Comparing City and Countryside Living", "Analyze comparative lifestyle advantages and construct comparative sentences.", "Hard",
         "Ben lives in a busy apartment in downtown Bangkok, while his cousin Mark lives on a peaceful farm in Chiang Mai. Ben claims that city life is more modern and interesting, but Mark argues that countryside life is simpler and more peaceful.",
         "Write two complete comparative sentences comparing life in the city with life in the countryside using adjectives from the unit ('modern', 'simpler', 'peaceful', 'interesting').",
         "Sample Answer: (1) 'Life in the city is more modern and interesting than life in the countryside.' (2) 'Life in the countryside is simpler and more peaceful than life in the city.'",
         "Sentence 1 compares city life using 'more modern/interesting than'. Sentence 2 compares countryside life using 'simpler/more peaceful than'."),

        ("World Superlatives Travel Quiz", "Identify superlative world facts and construct superlative questions.", "Hard",
         "During an English class quiz competition, team A must answer questions about natural world records: the fastest land animal, the deepest river, and the largest bird.",
         "Identify the three correct answers and write the complete superlative question used to ask about the deepest river.",
         "Answers: (1) Fastest land animal: The cheetah. (2) Deepest river: The Congo River. (3) Largest bird: The ostrich. Question format: 'What's the deepest river in the world?'",
         "Cheetah (fastest land animal), Congo River (deepest river >200m), Ostrich (largest bird up to 160kg). Question uses 'What's the deepest river in the world?'"),

        ("Airport Packing Check with Question Tags", "Formulate tag questions and appropriate answers in a travel scenario.", "Hard",
         "Sarah and her parents are packing their bags at the airport before boarding a flight to London. Sarah's mother wants to double-check that Sarah packed her passport, her medicine, and her bumbag.",
         "Create three complete tag questions Sarah's mother would ask (e.g., 'You packed your...'), and write Sarah's affirmative response for packing her passport.",
         "Mother's questions: (1) 'You packed your passport, didn't you?' (2) 'You packed your medicine, didn't you?' (3) 'You packed your bumbag, didn't you?' Sarah's affirmative response: 'Yes, I did. It is in my bag.'",
         "Tag questions follow: positive statement + 'didn't you?'. Affirmative confirmation response is 'Yes, I did.'"),

        ("Planning a Nature Holiday - Reading Passage Analysis", "Extract travel choices and reasons from Daisy's letter.", "Hard",
         "Daisy is writing a letter to her grandparents about her upcoming holiday options. She considers visiting a large valley with a rainforest, a beach with sea caves near the hotel, and a distant desert.",
         "Explain (a) which two places Daisy wants to visit and why, and (b) why she refuses to visit the desert.",
         "Answer: (a) Daisy wants to visit the rainforest valley to go hiking, and the beach caves near the hotel to take photos and go kayaking. (b) She refuses to visit the desert because it is far away from the hotel and she thinks it will be boring.",
         "From Page 8 text: Wants rainforest (hiking) and beach caves (photos/kayaking). Rejects desert (far away, boring)."),

        ("Exploring the Northern Lights", "Analyze scientific and geographic facts about the Aurora Borealis.", "Hard",
         "A travel magazine features an article about the Northern Lights (Aurora Borealis). A student named Tom wants to plan a winter trip to see them in Europe.",
         "State (a) three European countries where Tom can best view the Northern Lights, (b) the most common color he will see, and (c) two other possible colors he might spot.",
         "Answer: (a) Tom can view them in Iceland, Norway, and Sweden. (b) The most common color is green. (c) Other possible colors include pink, red, white, or blue.",
         "Page 9 text: Countries = Iceland, Norway, Sweden. Common color = green. Other colors = pink, red, white, blue."),

        ("Mount Everest Expedition Study", "Evaluate historical facts and physical statistics of Mount Everest.", "Hard",
         "In a geography presentation, Alex presents slides about Mount Everest, highlighting its height, geographical continent, and mountaineering history.",
         "List (a) the exact height of Mount Everest in meters, (b) the names of the first two climbers to reach the summit, and (c) the year of their historic climb.",
         "Answer: (a) Mount Everest is 8,849 meters high. (b) The first two climbers were Sir Edmund Hillary and Tenzing Norgay. (c) They reached the summit in 1953.",
         "Page 9 text: Height = 8,849m. Climbers = Edmund Hillary and Tenzing Norgay. Year = 1953."),

        ("Comparing Natural Geological Wonders - Grand Canyon vs Parícutin Volcano", "Compare age, location, and formation of two natural wonders.", "Hard",
         "Two students are comparing natural wonders: Emma is researching the Grand Canyon in the USA, while Carlos is researching Parícutin Volcano in Mexico.",
         "Compare the age and formation of these two wonders based on the textbook readings.",
         "Answer: The Grand Canyon is an ancient geological wonder over 6 million years old located in Arizona, USA. In contrast, Parícutin Volcano in Mexico is the youngest volcano in the world, which suddenly erupted in a farmer's field in 1943 and grew over nine years.",
         "Grand Canyon = >6 million years old (ancient canyon). Parícutin = youngest volcano (erupted in 1943 in farmer's field)."),

        ("Marine Conservation at the Great Barrier Reef", "Analyze marine ecosystem statistics and environmental threats.", "Hard",
         "A marine biology documentary discusses Australia's Great Barrier Reef, highlighting its immense length, rich biodiversity, and current environmental threats.",
         "Detail (a) the approximate length of the reef, (b) how many types of coral and fish live there, and (c) the main environmental threat causing coral death.",
         "Answer: (a) The Great Barrier Reef is about 2,300 km long. (b) It houses 400 types of coral and 1,500 types of fish. (c) The main threat is ocean warming, which causes the coral to die.",
         "Page 10 text: Length = 2,300 km. Coral types = 400. Fish types = 1,500. Threat = warming ocean temperatures."),

        ("African River Wildlife and Waterfall Exploration", "Examine geographical and recreational facts about Victoria Falls.", "Hard",
         "A safari tour package offers visits to Victoria Falls in Africa. Travelers want to know about the waterfall's location and outdoor recreational activities available.",
         "State (a) the river on which Victoria Falls is located, (b) the two border countries it spans, and (c) two water activities tourists can do there.",
         "Answer: (a) Victoria Falls is located on the Zambezi River. (b) It lies between Zambia and Zimbabwe. (c) Water activities include rafting and kayaking.",
         "Page 10 text: River = Zambezi River. Countries = Zambia and Zimbabwe. Activities = rafting, kayaking, horse riding."),

        ("Amazon Rainforest Ecological Importance", "Analyze rainforest biodiversity and transportation.", "Hard",
         "Frank gives a presentation about the Amazon Rainforest. He shares key facts about its tree population, river system, and travel methods through the dense forest.",
         "State (a) how many trees are estimated to grow in the Amazon, and (b) why the Amazon River is important for traveling through the rainforest.",
         "Answer: (a) There are more than 400 billion trees in the Amazon rainforest. (b) The Amazon River is an essential waterway route for navigating and traveling through the dense, thick forest.",
         "Page 10 text: Tree count = >400 billion trees. River = key transportation route through the dense forest."),

        ("Packing Frequency and Travel Preparedness", "Formulate sentences combining frequency adverbs and travel items.", "Hard",
         "Jenny is preparing a travel packing guide for Grade 6 students going on a school trip to a tropical island. She emphasizes packing essential items based on frequency (always, sometimes, never).",
         "Write three complete sentences using 'always', 'sometimes', and 'never' with travel items (passport, first aid kit, heavy winter coat).",
         "Sample Sentences: (1) 'I always take my passport when traveling abroad.' (2) 'I sometimes take a first aid kit on outdoor hiking trips.' (3) 'I never take a heavy winter coat to a tropical beach.'",
         "Sentences correctly use frequency adverbs (always, sometimes, never) placed before main action verbs with appropriate travel gear."),

        ("Superlative Marine Animal Speed Contest", "Calculate speed and compare marine animal characteristics.", "Hard",
         "In an ocean science quiz, students compare the swimming speed of the sailfish with other sea creatures. The sailfish is recognized as the fastest sea animal.",
         "State (a) the top swimming speed of the sailfish in km/h, and (b) construct the full superlative sentence describing the sailfish's speed record.",
         "Answer: (a) The sailfish can swim at 110 kilometres per hour. (b) 'The sailfish is the fastest sea animal in the world.'",
         "Page 4 text: Sailfish speed = 110 km/h. Superlative sentence: 'The sailfish is the fastest sea animal in the world.'"),

        ("Comparative Adjective Transformation Challenge", "Transform base adjectives into comparative forms within sentences.", "Hard",
         "A teacher writes four base adjectives on the board: 'hard', 'simple', 'modern', and 'traditional'. She asks students to rewrite them in comparative sentences comparing two items.",
         "Provide the comparative forms of all four adjectives and write one complete sentence comparing 'city life' with 'countryside life' using 'more traditional'.",
         "Answer: Comparative forms: hard -> harder; simple -> simpler; modern -> more modern; traditional -> more traditional. Sentence: 'Life in the countryside is more traditional than life in the city.'",
         "Correct comparative transformations. Sentence correctly uses 'more traditional than'."),

        ("Question Tag Dialogue Repair", "Correct grammar errors in tag question exchanges.", "Hard",
         "A student wrote the following dialogue: A: 'You packed your bug spray, didn't you?' B: 'No, I did.' A: 'You didn't forget your purse, did you?' B: 'Yes, I forgot.'",
         "Identify the grammatical contradiction in student B's first response and write the two correct short answer options (positive confirmation vs negative denial) for 'You packed your bug spray, didn't you?'.",
         "Answer: Student B's response 'No, I did' is contradictory because 'No' must pair with 'didn't'. The correct positive confirmation is 'Yes, I did.' The correct negative denial is 'No, I didn't.'",
         "Grammar rule: Affirmative short answer = 'Yes, I did.' Negative short answer = 'No, I didn't.' Combining 'No' with 'I did' is ungrammatical."),

        ("Travel Destination Preference Analysis", "Synthesize landscape vocabulary and travel recommendations.", "Hard",
         "Two friends, Alice and Nick, are looking at a travel brochure featuring a huge cave with a waterfall, a peaceful river surrounded by trees, and a mountain peak.",
         "Write a short dialogue (4 lines) between Alice and Nick where Alice suggests kayaking on the river and Nick expresses his desire to visit the cave.",
         "Sample Dialogue:\nAlice: 'Look! There's a peaceful river. We could go kayaking there.'\nNick: 'Oh, cool! I want to go there.'\nAlice: 'Is there anywhere else you want to go?'\nNick: 'I want to visit the huge cave with the waterfall.'",
         "Dialogue incorporates landscape vocabulary (river, cave, waterfall), modal 'could' for suggestion, and expressions of desire ('want to go').")
    ]

    # 10 Short Answer Questions
    sa_questions = [
        ("Comparative Adjectives Formation Rules", "Explain grammatical rules for forming comparative adjectives.", "Hard",
         "Explain the rules for forming comparative adjectives in English. Contrast short one-syllable adjectives (e.g. 'hard') with long multi-syllable adjectives (e.g. 'traditional'). Give two examples for each category.",
         "(1) Short one-syllable adjectives form comparatives by adding '-er' (or '-r' if ending in -e) to the end of the base adjective (e.g., hard -> harder, simple -> simpler). (2) Long adjectives with two or more syllables form comparatives by adding the word 'more' before the base adjective (e.g., traditional -> more traditional, peaceful -> more peaceful). (3) The word 'than' is used after the comparative form when comparing two items."),

        ("Superlative Adjectives Formation Rules", "Explain grammatical rules for forming superlative adjectives.", "Hard",
         "Explain how superlative adjectives are formed in English. Contrast short adjectives (e.g. 'fast') with long adjectives (e.g. 'populated'). Describe the role of the definite article 'the'.",
         "(1) Superlative adjectives describe the highest degree of a quality among three or more items and are always preceded by the definite article 'the'. (2) Short adjectives add '-est' (or '-st' if ending in -e) to the end (e.g., fast -> the fastest, large -> the largest). If ending in consonant-vowel-consonant, the final letter doubles (e.g., big -> the biggest). (3) Long adjectives use 'the most' before the base form (e.g., populated -> the most populated, interesting -> the most interesting)."),

        ("Question Tags Rules and Functions", "Explain structure, polarity, and responses of question tags.", "Hard",
         "Explain how question tags (tag questions) are constructed in the past simple tense. Describe the rule of polarity between the main statement and the tag, and state how to answer them.",
         "(1) Question tags are short questions added to the end of a statement to check information or seek agreement. (2) Polarity Rule: An affirmative statement takes a negative tag (e.g., 'You packed your passport, didn't you?'), while a negative statement takes a positive tag (e.g., 'You didn't forget your purse, did you?'). (3) In the past simple tense with action verbs, the auxiliary verb 'did/didn't' + subject pronoun is used. (4) Answering: Confirming an affirmative action requires 'Yes, I did', while denying requires 'No, I didn't'."),

        ("Frequency Adverbs in Daily Routines and Travel", "Explain usage and sentence placement of frequency adverbs.", "Medium",
         "Define the function of adverbs of frequency ('always', 'sometimes', 'never') and explain their correct position in a sentence relative to main action verbs versus the verb 'to be'. Provide one example for each.",
         "(1) Adverbs of frequency express how often an action occurs ('always' = 100%, 'sometimes' = ~50%, 'never' = 0%). (2) Sentence Position: Frequency adverbs are placed BEFORE main action verbs (e.g., 'I always pack my passport') but AFTER the verb 'to be' (e.g., 'Life in the city is always busy'). (3) Examples: 'I always take my passport on holiday.' 'I sometimes go kayaking.' 'I never travel without bug spray.'"),

        ("Daisy's Holiday Letter Comprehension", "Summarize character choices and travel reasoning from reading text.", "Hard",
         "Based on Daisy's letter on Page 8, summarize Daisy's holiday plans. List the activities she wants to do, where she wants to do them, and explain why she rejects visiting the desert.",
         "(1) Daisy wants to visit a large valley with a rainforest at the bottom to go hiking. (2) She wants to visit a beach near the hotel to take photos inside large sea caves, as well as go swimming or kayaking in the ocean. (3) She rejects visiting the desert because it is located far away from their hotel and she feels the trip would be boring, preferring to stay near the hotel instead."),

        ("Northern Lights Phenomenon Analysis", "Explain the nature, location, and visual characteristics of Northern Lights.", "Hard",
         "Describe the Northern Lights (Aurora Borealis) based on the unit 5 textbook reading. Mention what they are, where in the world they are best viewed, and what colors can be observed.",
         "(1) The Northern Lights, scientifically named Aurora Borealis, are a spectacular natural light phenomenon visible in the night sky in northern countries. (2) The best places to view them are northern Scandinavian and Arctic countries such as Iceland, Norway, and Sweden. (3) While the light displays are most commonly green, observers can also see pink, red, white, or occasionally blue lights depending on atmospheric conditions."),

        ("Grand Canyon Geological Features", "Detail the location, age, and physical dimensions of the Grand Canyon.", "Medium",
         "Summarize the key facts about the Grand Canyon from Page 9. Detail its geographical location, geological age, length, width, and depth.",
         "(1) Location: The Grand Canyon is a massive natural wonder situated in the desert region of Arizona, USA. (2) Geological Age: It is an ancient geological formation over 6 million years old. (3) Physical Dimensions: It stretches 446 kilometers in length, reaches up to 29 kilometers wide at its broadest point, and drops to a depth of over 1,800 meters from top to bottom."),

        ("Mount Everest Historic Mountaineering Accomplishment", "Explain the geography and historic 1953 expedition of Mount Everest.", "Hard",
         "Discuss Mount Everest based on the text on Page 9. Mention its location, elevation record, the historic 1953 expedition, and how many people have climbed it since.",
         "(1) Mount Everest is located in Asia in the Himalayan mountain range and holds the world record as the highest mountain on Earth at an elevation of 8,849 meters. (2) Historic Expedition: It was first successfully summited in 1953 by mountaineers Sir Edmund Hillary (from New Zealand) and Tenzing Norgay (a Sherpa climber). (3) Modern Significance: Since that historic 1953 climb, more than 6,000 people have successfully climbed to the summit."),

        ("Parícutin Volcano Formation and Uniqueness", "Explain the unique origin and rapid growth of Parícutin Volcano.", "Hard",
         "Explain why Parícutin Volcano in Mexico is considered a unique geological wonder. Describe its origin before 1943, its growth duration, height, and current tourist activity.",
         "(1) Parícutin Volcano in Mexico is unique because it is recognized as the youngest volcano in the world. (2) Origin & Growth: Before 1943, the site was simply a flat farmer's cornfield. A volcanic vent opened in 1943 and the volcano actively erupted and grew over a period of nine years, reaching a height of 2,800 meters. (3) Tourist Activity: Today, visitors can trek and climb the volcano, which takes approximately 6 to 7 hours."),

        ("Great Barrier Reef Biodiversity and Climate Threat", "Analyze the ecological importance and environmental threat facing the Great Barrier Reef.", "Hard",
         "Describe Australia's Great Barrier Reef based on Page 10. Discuss its size, biological diversity of coral and marine life, why it is popular for diving, and the major climate threat affecting it.",
         "(1) Size & Location: Located in the sea off the coast of Australia, the Great Barrier Reef stretches approximately 2,300 kilometers in length. (2) Biodiversity: It is world-famous for its rich marine biodiversity, housing over 400 types of coral and 1,500 species of fish. (3) Tourist Popularity: It is extremely popular for scuba diving due to the vibrant, beautiful colors of the coral reefs. (4) Climate Threat: As global climate change causes ocean waters to warm, the coral is bleaching and dying, prompting international conservation efforts to save the reef.")
    ]

    # Generate Markdown Content
    md = []
    md.append("# English Language Assessment Grade 6 (English Gr.6 - MidFinal)")
    md.append("")
    md.append("> **Assessment Information**")
    md.append("> - **Subject**: English Language (ระบบทดสอบวัดผลการเรียนรู้ภาษาอังกฤษ ป.6)")
    md.append("> - **Grade Level**: Grade 6 (Primary 6)")
    md.append("> - **Source Material**: Enlish Languages Gr6-MidFinal.pdf (10 Pages)")
    md.append("> - **Total Questions**: 115 Questions")
    md.append("> - **Total Points**: 150 Points")
    md.append("> - **Passing Criteria**: 80% (120 / 150 Points)")
    md.append("")
    md.append("---")
    md.append("")

    # Section A
    md.append("# Section A: Multiple Choice Questions (ปรนัย)")
    md.append("")
    md.append("<!--")
    md.append("RULES Section A:")
    md.append("- ข้อ 1–60 (60 ข้อ, 1 คะแนน/ข้อ)")
    md.append("- ทุกข้อมี 4 ตัวเลือก: ก, ข, ค, ง")
    md.append("-->")
    md.append("")

    opt_letters = ["ก", "ข", "ค", "ง"]
    letter_map = {"A": "ก", "B": "ข", "C": "ค", "D": "ง"}

    for idx, (topic, lo, diff, prompt, options, ans_let, exp) in enumerate(mcq_questions, 1):
        md.append(f"#### ข้อ {idx}")
        md.append(f"* **Topic**: {topic}")
        md.append(f"* **Learning Objective**: {lo}")
        md.append(f"* **Difficulty**: {diff}")
        md.append(f"* **Prompt**: {prompt}")
        for opt_idx, opt_text in enumerate(options):
            md.append(f"* {opt_letters[opt_idx]}. {opt_text}")
        correct_thai_let = letter_map.get(ans_let, ans_let)
        md.append(f"* **Correct Answer**: {correct_thai_let}")
        md.append(f"* **Explanation**: {exp}")
        md.append("")

    md.append("---")
    md.append("")

    # Section B
    md.append("# Section B: True / False Questions (ถูก-ผิด)")
    md.append("")
    md.append("<!--")
    md.append("RULES Section B:")
    md.append("- ข้อ 61–90 (30 ข้อ, 1 คะแนน/ข้อ)")
    md.append("- คำตอบ: True หรือ False")
    md.append("-->")
    md.append("")

    for idx, (topic, lo, diff, stmt, ans_tf, exp) in enumerate(tf_questions, 61):
        md.append(f"#### ข้อ {idx}")
        md.append(f"* **Topic**: {topic}")
        md.append(f"* **Learning Objective**: {lo}")
        md.append(f"* **Difficulty**: {diff}")
        md.append(f'* **Statement**: "{stmt}"')
        md.append(f"* **Correct Answer**: {ans_tf}")
        md.append(f"* **Explanation**: {exp}")
        md.append("")

    md.append("---")
    md.append("")

    # Section C
    md.append("# Section C: Scenario-Based Questions (สถานการณ์จำลอง)")
    md.append("")
    md.append("<!--")
    md.append("RULES Section C:")
    md.append("- ข้อ 91–105 (15 ข้อ, 2 คะแนน/ข้อ)")
    md.append("-->")
    md.append("")

    for idx, (topic, lo, diff, scen, q, ans, exp) in enumerate(sc_questions, 91):
        md.append(f"#### ข้อ {idx}")
        md.append(f"* **Topic**: {topic}")
        md.append(f"* **Learning Objective**: {lo}")
        md.append(f"* **Difficulty**: {diff}")
        md.append(f"* **Scenario**: {scen}")
        md.append(f"* **Question**: {q}")
        md.append(f"* **Answer**: {ans}")
        md.append(f"* **Explanation**: {exp}")
        md.append("")

    md.append("---")
    md.append("")

    # Section D
    md.append("# Section D: Short Answer Questions (อัตนัย / อธิบายความรู้)")
    md.append("")
    md.append("<!--")
    md.append("RULES Section D:")
    md.append("- ข้อ 106–115 (10 ข้อ, 3 คะแนน/ข้อ)")
    md.append("-->")
    md.append("")

    for idx, (topic, lo, diff, prompt, exp_ans) in enumerate(sa_questions, 106):
        md.append(f"#### ข้อ {idx}")
        md.append(f"* **Topic**: {topic}")
        md.append(f"* **Learning Objective**: {lo}")
        md.append(f"* **Difficulty**: {diff}")
        md.append(f"* **Prompt**: {prompt}")
        md.append(f"* **Expected Answer**: {exp_ans}")
        md.append("")

    md.append("---")
    md.append("")

    # Answer Key Table
    md.append("# Answer Key")
    md.append("")
    md.append("### Section A: Multiple Choice Answers")
    md.append("| Question | Answer | Question | Answer | Question | Answer | Question | Answer |")
    md.append("| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |")

    for row in range(15):
        q1, a1 = row + 1, letter_map.get(mcq_questions[row][5], mcq_questions[row][5])
        q2, a2 = row + 16, letter_map.get(mcq_questions[row+15][5], mcq_questions[row+15][5])
        q3, a3 = row + 31, letter_map.get(mcq_questions[row+30][5], mcq_questions[row+30][5])
        q4, a4 = row + 46, letter_map.get(mcq_questions[row+45][5], mcq_questions[row+45][5])
        md.append(f"| ข้อ {q1} | {a1} | ข้อ {q2} | {a2} | ข้อ {q3} | {a3} | ข้อ {q4} | {a4} |")

    md.append("")
    md.append("### Section B: True / False Answers")
    md.append("| Question | Answer | Question | Answer | Question | Answer |")
    md.append("| :---: | :---: | :---: | :---: | :---: | :---: |")
    for row in range(10):
        q1, a1 = row + 61, tf_questions[row][4]
        q2, a2 = row + 71, tf_questions[row+10][4]
        q3, a3 = row + 81, tf_questions[row+20][4]
        md.append(f"| ข้อ {q1} | {a1} | ข้อ {q2} | {a2} | ข้อ {q3} | {a3} |")

    output_path1 = "Knowledge_Assessment_English_Languages_Gr6.md"
    output_path2 = "Knowledge_Assessment_English_Gr6.md"
    
    content = "\n".join(md)
    with open(output_path1, "w", encoding="utf-8") as f:
        f.write(content)
    with open(output_path2, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully generated {output_path1} and {output_path2} with 115 questions!")

if __name__ == "__main__":
    generate_english_language_quiz()
