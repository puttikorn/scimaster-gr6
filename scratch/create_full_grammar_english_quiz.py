import os

def generate_grammar_quiz_from_pdf():
    # 60 MCQ Questions based on Grammar Gr6-MidFinal.pdf
    mcq_questions = [
        # 1-12: Past Continuous & Past Simple vs. Past Continuous (Pages 1-4)
        ("Past Continuous Form", "Form correct past continuous affirmative sentences.", "Easy",
         "Which sentence correctly uses the past continuous tense?",
         ["She reading a newspaper yesterday.", "She was reading a newspaper yesterday at 3 PM.", "She readed a newspaper yesterday.", "She is reading a newspaper yesterday."], "B",
         "The past continuous structure is subject + was/were + verb-ing (e.g., 'She was reading...')."),

        ("Past Continuous Questions", "Form past continuous yes/no questions.", "Easy",
         "What is the correct past continuous question form for 'you / study / in the library'?",
         ["Did you study in the library?", "Were you studying in the library?", "Was you studying in the library?", "Are you studying in the library yesterday?"], "B",
         "Yes/No questions in past continuous start with Was/Were + Subject + Verb-ing ('Were you studying...?')."),

        ("Past Continuous Negative", "Form past continuous negative sentences.", "Easy",
         "Choose the correct negative past continuous sentence for 'They / practice / the piano'.",
         ["They didn't practice the piano.", "They wasn't practicing the piano.", "They weren't practicing the piano.", "They not practicing the piano."], "C",
         "Plural subject 'They' uses 'weren't' (were not) + verb-ing."),

        ("Past Simple vs Past Continuous", "Distinguish specific time continuous vs completed action.", "Medium",
         "Complete the sentence: 'Sam watched a movie yesterday afternoon, but at 2:30 yesterday afternoon, he ________ a movie.'",
         ["watched", "was watching", "is watching", "will watch"], "B",
         "The past continuous ('was watching') describes an action in progress at a specific time in the past (2:30 PM)."),

        ("When Clause Pattern", "Apply 'when' with past simple in past continuous contexts.", "Medium",
         "Choose the correct verb form: 'I was taking a nap when the doorbell ________.'",
         ["rang", "was ringing", "rings", "is ringing"], "A",
         "A clause introduced by 'when' usually takes the past simple tense ('rang') to show an interrupting action."),

        ("While Clause Pattern", "Apply 'while' with past continuous.", "Medium",
         "Complete the sentence: 'It started to rain while we ________ our bikes.'",
         ["rode", "were riding", "are riding", "ride"], "B",
         "A clause introduced by 'while' takes the past continuous tense ('were riding') to show an ongoing background action."),

        ("When vs While Usage", "Select between 'when' and 'while' conjunctions.", "Medium",
         "Choose the correct conjunction: 'The teacher came in ________ the students were singing.'",
         ["while", "when", "until", "before"], "A",
         "'While' introduces the ongoing action clause in the past continuous ('the students were singing')."),

        ("Past Continuous Interruptions", "Analyze past continuous interrupted by past simple.", "Medium",
         "Complete the sentence: 'Amy ________ a picture when the teacher came in.'",
         ["drew", "was drawing", "is drawing", "draws"], "B",
         "The ongoing activity ('was drawing') was interrupted by the teacher's entry ('came in')."),

        ("Past Continuous Interruption Context", "Identify correct past continuous form in reading context.", "Medium",
         "In the story: 'While Mom and Dad were building a tent, a park ranger ________ on horseback.'",
         ["was coming", "came", "comes", "is coming"], "B",
         "The background action is past continuous ('were building'), and the completed interruption uses past simple ('came')."),

        ("Past Continuous Interruption Context", "Identify background action in camping story.", "Medium",
         "Complete: 'While we ________ in the tent at night, the ranger came back to check on us.'",
         ["slept", "were sleeping", "are sleeping", "sleep"], "B",
         "'While' requires the past continuous tense ('were sleeping') for the background activity."),

        ("Past Simple vs Past Continuous Choice", "Select correct verb pair for past action.", "Hard",
         "Which sentence correctly combines past simple and past continuous?",
         ["Sam was breaking a plate while he did the dishes.", "Sam broke a plate while he was doing the dishes.", "Sam broke a plate while he is doing dishes.", "Sam breaks a plate when he was doing dishes."], "B",
         "'Broke' (past simple interrupting event) occurs during 'was doing' (past continuous ongoing process)."),

        ("Past Continuous Subject-Verb Agreement", "Choose correct auxiliary was/were.", "Easy",
         "Complete: 'Ken and Sally ________ talking to each other when the teacher came in.'",
         ["was", "were", "are", "have"], "B",
         "Compound subject 'Ken and Sally' requires plural auxiliary 'were'."),

        # 13-24: Future Tenses (Will, Be Going To, Be + -ing) (Pages 5-8)
        ("Future with Will", "Form simple future affirmative with 'will'.", "Easy",
         "Which sentence correctly uses 'will' for a future event?",
         ["My dad will buy a new car soon.", "My dad will buying a new car soon.", "My dad will bought a new car soon.", "My dad is will buy a new car soon."], "A",
         "Future with 'will' uses will + base verb ('will buy')."),

        ("Future Negative with Will", "Form negative future with 'won't'.", "Easy",
         "Choose the correct negative future form: 'Jenny ________ watch a movie tonight.'",
         ["won't", "don't", "isn't", "wasn't"], "A",
         "The negative of 'will' is 'won't' (will not) + base verb."),

        ("Future Question with Will", "Form future questions with 'will'.", "Easy",
         "Choose the correct question: '________ travel to Europe next summer?'",
         ["Will you", "Do you", "Are you", "Were you"], "A",
         "Future questions with 'will' invert subject and modal: Will + Subject + Base Verb."),

        ("Future with Be Going To", "Form affirmative 'be going to' for planned actions.", "Easy",
         "Complete the sentence: 'I ________ open the window.'",
         ["am going to", "is going to", "are going to", "going to"], "A",
         "First-person singular 'I' pairs with 'am going to' + base verb."),

        ("Be Going To Negative", "Form negative 'be going to' sentences.", "Medium",
         "Choose the correct negative sentence: 'I ________ home this weekend.'",
         ["am not going to be", "am going to not be", "not am going to be", "don't going to be"], "A",
         "Negative form: Subject + am/is/are + not + going to + base verb."),

        ("Be Going To Question", "Form 'be going to' questions.", "Medium",
         "Complete the question: '________ John going to help us with this project?'",
         ["Is", "Are", "Will", "Does"], "A",
         "Third-person singular 'John' takes 'Is' at the start of 'be going to' questions."),

        ("Present Continuous as Future", "Identify Present Continuous used for fixed future plans.", "Medium",
         "In the sentence 'Mark is running in a race tomorrow', what does the present continuous tense express?",
         ["An action happening right now", "A definite plan or arrangement for the future", "A past habit", "A general truth"], "B",
         "The present continuous + future time word ('tomorrow') expresses a definite planned future arrangement."),

        ("Present Continuous for Future", "Select correct verb form for future arrangement.", "Medium",
         "Complete: 'They ________ a birthday party this afternoon.'",
         ["are having", "were having", "had", "have had"], "A",
         "'are having' (present continuous) is used with 'this afternoon' for a planned future event."),

        ("Future Tense Comparison", "Select between will and be going to for spontaneous vs planned.", "Hard",
         "Sam and I can't ski. We ________ to ski this winter.",
         ["will learn", "learned", "were learning", "are learned"], "A",
         "'will learn' expresses a decision/intention regarding future learning."),

        ("Future Context Analysis", "Analyze Ben's weekend plan dialogue.", "Medium",
         "In Ben's dialogue: 'My uncle ________ to visit us this weekend. He ________ me how to water-ski.'",
         ["is coming / will teach", "came / taught", "was coming / teaches", "comes / was teaching"], "A",
         "'is coming' (planned arrival) and 'will teach' (future action/promise)."),

        ("Future Question Formation", "Form future question in dialogue.", "Medium",
         "Choose the correct question: '________ you come to my house next weekend?'",
         ["Will", "Are", "Did", "Were"], "A",
         "'Will you come...?' invites someone to a future event."),

        ("Future Expression Choice", "Select appropriate future expression.", "Medium",
         "Complete: 'I'm not hungry now. I ________ eat lunch later.'",
         ["will", "was", "did", "have"], "A",
         "'will' expresses a future decision."),

        # 25-36: Present Perfect Tense & Irregular Past Participles (Pages 9-12)
        ("Present Perfect Form", "Form present perfect affirmative with regular/irregular verbs.", "Easy",
         "Which sentence is correctly written in the present perfect tense?",
         ["She has waited for you since three o'clock.", "She is waiting for you since three o'clock.", "She waited for you since three o'clock.", "She has wait for you since three o'clock."], "A",
         "Present perfect form: has/have + past participle (V3) + since/for."),

        ("Present Perfect Negative", "Form present perfect negative sentences.", "Easy",
         "Complete: 'He ________ me this week.'",
         ["hasn't called", "haven't called", "didn't called", "doesn't call"], "A",
         "Third-person singular 'He' uses 'hasn't' (has not) + V3 ('called')."),

        ("Present Perfect Time Words (For vs Since)", "Distinguish 'for' (duration) vs 'since' (starting point).", "Medium",
         "Choose the correct preposition: 'They have studied math ________ two hours.'",
         ["for", "since", "during", "ago"], "A",
         "'for' is used with a period of time/duration ('two hours'); 'since' is used with a specific starting point."),

        ("Present Perfect Time Words (Since)", "Apply 'since' for starting point.", "Medium",
         "Complete: 'She has watched TV ________ dinner.'",
         ["since", "for", "in", "by"], "A",
         "'since' indicates the starting point of an action continuing to the present."),

        ("Present Perfect Question Form", "Form yes/no questions in present perfect.", "Easy",
         "What is the correct present perfect question form for 'They have saved a lot of money'?",
         ["Have they saved a lot of money?", "Did they save a lot of money?", "Are they saving a lot of money?", "Do they save a lot of money?"], "A",
         "Yes/No questions invert auxiliary and subject: Have/Has + Subject + V3...?"),

        ("Irregular Past Participles", "Identify V3 form of 'do'.", "Easy",
         "What is the past participle (V3) form of the verb 'do'?",
         ["done", "did", "doing", "does"], "A",
         "The verb 'do' has principal parts: do - did - done (V3 = done)."),

        ("Irregular Past Participles", "Identify V3 form of 'eat'.", "Easy",
         "Complete: 'We have ________ Thai food before.'",
         ["eaten", "ate", "eating", "eats"], "A",
         "The past participle of 'eat' is 'eaten'."),

        ("Present Perfect Experience", "Express past experience with 'ever' and 'never'.", "Medium",
         "Choose the correct sentence expressing experience:",
         ["Have you ever caught a fish?", "Did you ever caught a fish?", "Were you ever catch a fish?", "Have you ever catch a fish?"], "A",
         "Present perfect question for life experience: Have/Has + subject + ever + V3...?"),

        ("Present Perfect Usage", "Identify action continuing from past to present.", "Medium",
         "In 'Tom is my friend. I have known him for three years', what does the present perfect show?",
         ["An action that started in the past and continues into the present", "An action that ended yesterday", "A future prediction", "A past habit"], "A",
         "Present perfect with 'for/since' describes a state that started in the past and continues into the present."),

        ("Irregular V3 in Context", "Select correct V3 form of 'be'.", "Medium",
         "Complete: 'This winter has been cold. The old tree has ________ here for 100 years.'",
         ["been", "was", "were", "being"], "A",
         "The past participle of 'be' is 'been'."),

        ("Present Perfect with 'Already' / 'Yet'", "Apply 'yet' in present perfect negative.", "Medium",
         "Complete: 'Mike hasn't read the book ________.'",
         ["yet", "already", "since", "ever"], "A",
         "'yet' is used in present perfect negative sentences and questions, usually placed at the end."),

        ("Present Perfect Context Dialogue", "Analyze amusement park Drop Tower dialogue.", "Hard",
         "In the Drop Tower dialogue: 'Have you ________ on the Drop Tower before?' - 'No, I haven't. Have you ________ your safety belt yet?'",
         ["ridden / put on", "rode / putted on", "ride / put on", "riding / putting on"], "A",
         "V3 of 'ride' is 'ridden'; V3 of 'put' is 'put'. Both use present perfect in context."),

        # 37-48: Modal Verbs 1 (May, Might, Could, Would) (Pages 13-16)
        ("Modal Verbs: May for Possibility", "Identify 'may' for possibility.", "Easy",
         "Complete: 'Amy is not in the classroom. She ________ be in the library.'",
         ["may", "mustn't", "shall", "wouldn't"], "A",
         "'may' expresses possibility (something that is likely to happen)."),

        ("Modal Verbs: Might for Possibility", "Identify 'might' for possibility.", "Easy",
         "Complete: 'Take an umbrella with you. It ________ rain this afternoon.'",
         ["might", "must", "shall", "would"], "A",
         "'might' expresses future possibility."),

        ("Modal Verbs: May not / Might not", "Form negative possibility with may/might not.", "Medium",
         "Complete: 'John has a bad cold. He ________ go to school tomorrow.'",
         ["may not", "must", "should", "will"], "A",
         "'may not' indicates negative possibility (likely won't happen)."),

        ("Polite Request: May I...?", "Use 'May I' for polite permission requests.", "Easy",
         "Which question politely asks for permission to use a phone?",
         ["May I use your phone?", "Will I use your phone?", "Must I use your phone?", "Should I use your phone?"], "A",
         "'May I...?' is used to ask for permission politely."),

        ("Polite Request: Could I...?", "Use 'Could I' for polite permission requests.", "Easy",
         "Choose the polite request for water:",
         ["Could I have some water?", "Must I have some water?", "Shall I have some water?", "Will I have some water?"], "A",
         "'Could I...?' asks for permission or requests something politely."),

        ("Polite Request: Would you...?", "Use 'Would you' for polite action requests.", "Medium",
         "Which question politely asks someone to close the door?",
         ["Would you close the door, please?", "May you close the door, please?", "Must you close the door, please?", "Shall you close the door, please?"], "A",
         "'Would you...?' or 'Could you...?' asks someone else to perform an action politely."),

        ("Polite Request Answers", "Identify appropriate responses to polite requests.", "Medium",
         "What is a polite positive response to 'Could I borrow your pen, please?'",
         ["Of course. / Certainly.", "No, you don't.", "Yes, I will.", "I am not."], "A",
         "Polite responses to 'May I / Could I' include 'Of course', 'Certainly', or 'Sure'."),

        ("Modal Selection in Context", "Select modal for messy room situation.", "Medium",
         "In context: 'Your room is a mess. ________ clean your room?'",
         ["Could you", "May I", "Might you", "Shall I"], "A",
         "'Could you...?' is used to ask someone to clean their room."),

        ("Modal Selection in Context", "Select modal for asking teacher's permission.", "Medium",
         "To ask your teacher for permission to go out, you should say: '________ go to the restroom, please?'",
         ["May I", "Would you", "Must you", "Shall you"], "A",
         "'May I...?' is the formal, polite way to ask a teacher for permission."),

        ("Modal Word Order", "Arrange scrambled modal polite request.", "Medium",
         "Unscramble: 'please / phone / Would / the / you / answer / ?'",
         ["Would you answer the phone, please?", "Would please you answer the phone?", "Answer you would the phone, please?", "You would answer the phone, please?"], "A",
         "Correct order: Modal (Would) + Subject (you) + Verb (answer) + Object (the phone) + please?"),

        ("Modal Comparison: May I vs Would You", "Distinguish 'May I' vs 'Would you'.", "Hard",
         "What is the functional difference between 'May I open the window?' and 'Would you open the window?'",
         ["'May I' asks permission for speaker; 'Would you' asks listener to act", "'May I' asks listener to act; 'Would you' asks speaker permission", "Both ask for speaker permission", "Both ask listener to act"], "A",
         "'May I' = permission for speaker; 'Would you' = request for listener to act."),

        ("Modal Context Dialogue", "Select modal for turning on lights in dark room.", "Medium",
         "Dialogue: 'It's dark in here. ________ turn on the lights?' - 'Certainly.'",
         ["Could you", "May I", "Might you", "Shall I"], "A",
         "'Could you...?' asks another person to turn on the lights."),

        # 49-60: Modal Verbs 2 (Can, Could, Will, Would, Shall, Should, Must, Have To) (Pages 17-20)
        ("Modal: Ability Past vs Present", "Contrast past ability 'could' vs present ability 'can'.", "Medium",
         "Complete: 'I ________ inline skate last year, but I CAN now.'",
         ["couldn't", "can't", "mustn't", "shouldn't"], "A",
         "'couldn't' expresses past inability ('last year'), contrasted with present ability ('can now')."),

        ("Modal: Obligation with Must", "Identify 'must' for strong rule/obligation.", "Easy",
         "Complete: 'All passengers ________ wear seat belts.'",
         ["must", "may", "might", "could"], "A",
         "'must' expresses strong rule or mandatory obligation."),

        ("Modal: Prohibition with Mustn't", "Identify 'mustn't' for prohibition.", "Easy",
         "Complete: 'You ________ cross the street at a red crossing light.'",
         ["mustn't", "don't have to", "might not", "shall not"], "A",
         "'mustn't' expresses strict prohibition (forbidden action)."),

        ("Modal: Advice with Should", "Identify 'should' for advice.", "Easy",
         "Complete: 'Tom has a fever. He ________ see a doctor and rest.'",
         ["should", "mustn't", "shall", "would"], "A",
         "'should' is used to give advice or recommendations."),

        ("Modal: Lack of Obligation with Don't Have To", "Distinguish 'don't have to' from 'mustn't'.", "Hard",
         "Complete: 'Tomorrow is a holiday. I ________ get up early!'",
         ["don't have to", "mustn't", "shouldn't", "can't"], "A",
         "'don't have to' means lack of necessity/obligation (you can sleep in if you want), unlike 'mustn't' which means forbidden."),

        ("Modal: Past Obligation with Had To", "Identify past obligation 'had to'.", "Medium",
         "Complete: 'It was raining hard yesterday. They ________ stop the baseball game.'",
         ["had to", "must", "have to", "shall"], "A",
         "The past tense of obligation ('must' / 'have to') is 'had to'."),

        ("Modal: Suggestions with Shall We...?", "Use 'Shall we' for making suggestions.", "Medium",
         "Which modal is used to make a polite suggestion to a group: '________ we go to the park this afternoon?'",
         ["Shall", "Must", "Will", "Would"], "A",
         "'Shall we...?' is used to make suggestions to a group."),

        ("Modal Selection in Responsibility Context", "Identify 'has to' for personal duty.", "Medium",
         "Complete: 'Tom ________ feed his dog after breakfast. It's his responsibility.'",
         ["has to", "mustn't", "shall", "would"], "A",
         "'has to' expresses external responsibility or duty."),

        ("Modal Comparison: Mustn't vs Don't Have To", "Contrast prohibition vs lack of obligation.", "Hard",
         "What is the difference between 'You MUSTN'T talk to strangers' and 'You DON'T HAVE TO go shopping today'?",
         ["'Mustn't' means forbidden; 'Don't have to' means optional", "'Mustn't' means optional; 'Don't have to' means forbidden", "Both mean forbidden", "Both mean optional"], "A",
         "'Mustn't' = prohibition/forbidden; 'Don't have to' = optional/not necessary."),

        ("Modal Context Dialogue: Study vs Fun", "Select modals in weekend study dialogue.", "Hard",
         "Dialogue: 'We have a test next week. I ________ study. - Come on, you SHOULD have some fun. ________ we go to the park?'",
         ["have to / Shall", "mustn't / Would", "don't have to / Will", "could / May"], "A",
         "'have to study' (obligation) and 'Shall we go...?' (suggestion)."),

        ("Modal: Refusal with Won't", "Identify 'won't' for refusal.", "Medium",
         "Complete: 'Mr. Lewis is leaving our school. He ________ teach us next year.'",
         ["won't", "can", "must", "shall"], "A",
         "'won't' expresses future negative fact/refusal."),

        ("Grammar Unit Summary", "Summarize core Grade 6 grammar topics.", "Medium",
         "Which set of topics represents the core Grade 6 Grammar curriculum in the textbook?",
         ["Past Continuous, Future (Will/Going to), Present Perfect, and Modals", "Past Simple only", "Alphabet spelling only", "Passive Voice only"], "A",
         "The textbook units cover Past Continuous, Future Tenses, Present Perfect, and Modal Verbs 1 & 2.")
    ]

    # 30 True/False Questions based on Grammar Gr6-MidFinal.pdf
    tf_questions = [
        # 61-90 True/False
        ("Past Continuous Structure", "Recall past continuous formula.", "Easy",
         "The past continuous tense is formed using was/were + verb-ing.", "True",
         "Past continuous formula: Subject + was/were + V-ing."),

        ("Past Continuous Specific Time", "Recall past continuous time usage.", "Easy",
         "The past continuous talks about an action that was in progress at a specific time in the past.", "True",
         "Past continuous specifies ongoing action at a specific past moment."),

        ("When Clause Rule", "Recall 'when' clause tense rule.", "Medium",
         "A clause introduced by 'when' is often in the past simple tense (e.g., 'when the doorbell rang').", "True",
         "'when' clauses typically take Past Simple to show interrupting events."),

        ("While Clause Rule", "Recall 'while' clause tense rule.", "Medium",
         "A clause introduced by 'while' is often in the past simple tense.", "False",
         "'while' clauses take the PAST CONTINUOUS tense (e.g., 'while I was walking home')."),

        ("Past Continuous Agreement", "Recall subject-verb agreement for was/were.", "Easy",
         "We use 'was' with I, he, she, it, and 'were' with we, you, they.", "True",
         "Singular subjects take 'was'; plural/you take 'were'."),

        ("Future with Will", "Recall 'will' usage.", "Easy",
         "The future tense with 'will' is used to make predictions or state future facts.", "True",
         "'will' + base verb indicates future actions or predictions."),

        ("Future Negative 'Won't'", "Recall 'won't' contraction.", "Easy",
         "The negative form of 'will' is 'will not', which contracts to 'won't'.", "True",
         "'will not' contracts to 'won't'."),

        ("Be Going To Intention", "Recall 'be going to' usage.", "Easy",
         "'Be going to' is used to express future plans and intentions.", "True",
         "'be going to' expresses pre-planned intentions."),

        ("Present Continuous as Future", "Recall present continuous for future.", "Medium",
         "The present continuous tense can never be used to talk about future plans.", "False",
         "Present continuous + future time word expresses fixed future arrangements (e.g., 'Mark is running tomorrow')."),

        ("Present Perfect Link", "Recall present perfect core function.", "Easy",
         "The present perfect tense expresses a link between the past and the present.", "True",
         "Present perfect connects past actions/experiences to the present moment."),

        ("Present Perfect Formula", "Recall present perfect formula.", "Easy",
         "The present perfect tense is formed with subject + have/has + past participle (V3).", "True",
         "Present perfect structure: Subject + have/has + V3."),

        ("Regular Past Participles", "Recall regular V3 forms.", "Easy",
         "The past participle of regular verbs is the same as their simple past form (ending in -ed).", "True",
         "Regular verbs share identical V2 and V3 forms ending in '-ed'."),

        ("Time Word 'For'", "Recall 'for' usage in present perfect.", "Medium",
         "In present perfect, 'for' is used to state a specific starting point in time (e.g., for 3 o'clock).", "False",
         "'for' states a DURATION of time (for 2 hours); 'since' states a starting point (since 3 o'clock)."),

        ("Time Word 'Since'", "Recall 'since' usage in present perfect.", "Medium",
         "In present perfect, 'since' is used to state the starting point of an action (e.g., since yesterday).", "True",
         "'since' marks the specific beginning point of an ongoing state."),

        ("Irregular V3 of Be", "Recall V3 of 'be'.", "Easy",
         "The past participle (V3) of the verb 'be' is 'been'.", "True",
         "be - was/were - been."),

        ("Irregular V3 of Catch", "Recall V3 of 'catch'.", "Easy",
         "The past participle (V3) of 'catch' is 'catched'.", "False",
         "The past participle of 'catch' is 'caught' (catch - caught - caught)."),

        ("Irregular V3 of Eat", "Recall V3 of 'eat'.", "Easy",
         "The past participle (V3) of 'eat' is 'eaten'.", "True",
         "eat - ate - eaten."),

        ("Modal 'May' and 'Might'", "Recall may/might possibility function.", "Easy",
         "Modal verbs 'may' and 'might' express possibility in the present or future.", "True",
         "'may' and 'might' show that something is likely to happen."),

        ("Polite Request 'May I'", "Recall 'May I' function.", "Easy",
         "'May I borrow your pen?' is a polite question asking for permission.", "True",
         "'May I...?' asks for permission politely."),

        ("Polite Request 'Could I'", "Recall 'Could I' function.", "Easy",
         "'Could I...?' can be used to ask for permission politely.", "True",
         "'Could I...?' is a polite permission request."),

        ("Action Request 'Would You'", "Recall 'Would you' vs 'May I'.", "Medium",
         "'Would you close the door?' is asking for permission for yourself to close the door.", "False",
         "'Would you...?' is asking ANOTHER PERSON to perform an action."),

        ("Past Ability 'Could'", "Recall 'could' for past ability.", "Medium",
         "'Could' can be used as the past tense of 'can' to express past ability.", "True",
         "'could' expresses past ability (e.g., 'I couldn't skate last year, but I can now')."),

        ("Prohibition 'Mustn't'", "Recall 'mustn't' definition.", "Easy",
         "'You mustn't smoke here' means you are not allowed to smoke here.", "True",
         "'mustn't' expresses strict prohibition."),

        ("Lack of Obligation 'Don't have to'", "Recall 'don't have to' meaning.", "Medium",
         "'You don't have to get up early' means it is forbidden to get up early.", "False",
         "'don't have to' means it is NOT NECESSARY (lack of obligation), not forbidden."),

        ("Obligation 'Must'", "Recall 'must' function.", "Easy",
         "'Must' expresses strong obligation or necessity.", "True",
         "'must' indicates compulsory rules or obligations."),

        ("Past Obligation 'Had to'", "Recall past obligation form.", "Medium",
         "The past tense of 'must' and 'have to' for past obligation is 'had to'.", "True",
         "'had to' is the past form of 'must'/'have to' (e.g., 'They had to stop the game')."),

        ("Advice 'Should'", "Recall 'should' function.", "Easy",
         "'Should' is used to give advice or recommendations.", "True",
         "'should' suggests what is good or sensible to do."),

        ("Suggestions 'Shall We'", "Recall 'shall we' function.", "Medium",
         "'Shall we go to the park?' is used to make a suggestion to a group.", "True",
         "'Shall we...?' proposes a group activity."),

        ("Refusal 'Won't'", "Recall 'won't' refusal function.", "Medium",
         "'He won't teach us next year' expresses a future negative fact or refusal.", "True",
         "'won't' indicates future negative status."),

        ("Grade 6 Grammar Scope", "Recall unit scope.", "Easy",
         "Mastering Past Continuous, Future, Present Perfect, and Modals enables students to communicate complex past, present, and future ideas accurately.", "True",
         "This represents the primary learning objective of the Grade 6 Grammar curriculum.")
    ]

    # 15 Scenario-Based Questions based on Grammar Gr6-MidFinal.pdf
    scenario_questions = [
        # 91-105 Scenario-Based Questions (2 pts each)
        ("Classroom Interruption Scenario (Page 3 Exercise 1)", "Analyze past continuous interruption in classroom.", "Hard",
         "When Teacher Brown walked into the classroom at 9:00 AM, the students were engaged in various activities: Amy was drawing a picture, John and Mike were playing board games, Mia was listening to music, Tom was eating an apple, and Ken and Sally were talking.",
         "Write 3 complete sentences combining Past Continuous and Past Simple using 'when' to describe what Amy, Tom, and Ken & Sally were doing when the teacher entered.",
         "1. Amy was drawing a picture when the teacher came in. 2. Tom was eating an apple when the teacher came in. 3. Ken and Sally were talking to each other when the teacher came in.",
         "Past continuous describes ongoing actions ('was drawing', 'was eating', 'were talking') interrupted by past simple ('when the teacher came in')."),

        ("Redwood Forest Camping Story Scenario (Page 4 Exercise Choose & Write)", "Analyze past continuous and simple past in narrative.", "Hard",
         "Read the campsite incident: 'While Mom and Dad WERE BUILDING a tent, a park ranger CAME on horseback. She told us that bears WERE SEARCHING for food near our campsite. While we WERE SLEEPING in the tent at night, the ranger CAME back to check on us.'",
         "Identify the 3 instances of 'while' + past continuous and explain why past continuous was chosen over past simple in each instance.",
         "1. 'While Mom and Dad were building...' 2. 'bears were searching...' 3. 'While we were sleeping...'. Past continuous is used with 'while' to represent ongoing background duration during which another event occurred.",
         "'while' introduces background duration; past simple marks specific interrupting events."),

        ("Ben's Weekend Plans Dialogue Scenario (Page 8 Exercise Choose & Write)", "Analyze future tense choices in dialogue.", "Hard",
         "In a dialogue between Ben and Mark about weekend plans: Ben says his uncle IS COMING to visit and WILL TEACH him to water-ski. Mark says he IS STAYING at home and WILL PLAY with his dog Max. Ben asks: 'WILL YOU COME to my house next weekend?' Mark replies: 'Yes, I WILL.'",
         "Analyze the future tense forms used ('be going to/present continuous' vs 'will') and explain why each form was selected.",
         "'is coming' / 'is staying' represent fixed planned arrangements (present continuous as future). 'will teach' / 'will play' / 'will come' / 'will' represent future promises, offers, or decisions.",
         "Present continuous = fixed arrangements; 'will' = decisions/offers/promises."),

        ("Drop Tower Amusement Park Scenario (Page 12 Exercise Choose & Write)", "Analyze present perfect in experience dialogue.", "Hard",
         "At an amusement park, Mia asks Alex: 'HAVE YOU RIDDEN on the Drop Tower before?' Alex answers: 'No, I HAVEN'T. This is my first time.' Later, right before the ride starts, Mia asks: 'HAVE YOU PUT ON your safety belt yet?' Alex replies: 'Yes, I HAVE.'",
         "Explain why the Present Perfect tense is used in both questions instead of Past Simple, and identify the past participles (V3) used.",
         "Present Perfect is used because the questions ask about life experience up to the present ('before') and completed readiness ('yet') at an unspecified time. V3 of 'ride' is 'ridden'; V3 of 'put' is 'put'.",
         "Experience ('before') and completion status ('yet') require Present Perfect (Have + V3)."),

        ("Polite Requests in Classroom Scenario (Page 16 Exercise Choose & Write)", "Analyze modal requests between friends and siblings.", "Hard",
         "In a study session, Peter asks his sister: 'COULD YOU HELP me with my homework? It's too difficult. COULD YOU TURN ON the lights? It's dark in here. MAY I BORROW a pencil and eraser?' His sister agrees, but when he asks: 'COULD I USE your computer?', she refuses: 'Of course not!'",
         "Categorize Peter's 4 requests into 'Action Requests to Listener' (Could you...?) vs 'Permission Requests for Speaker' (May I / Could I...?). Explain why his sister refused the last one.",
         "Action Requests to Listener: 'Could you help me...', 'Could you turn on...'. Permission Requests for Speaker: 'May I borrow...', 'Could I use...'. Computer request was refused due to personal privacy.",
         "'Could you' asks another person to act; 'May I / Could I' asks permission for oneself."),

        ("Weekend Study vs Fun Scenario (Page 20 Exercise Choose & Write)", "Analyze modal verbs in decision-making dialogue.", "Hard",
         "Two students discuss their weekend: Student A says: 'We have a test next week. I HAVE TO STUDY.' Student B replies: 'You SHOULD have some fun. SHALL WE GO to the park? We CAN RIDE our bikes.' Student A notes: 'It MAY RAIN.' Student B asks: 'WOULD YOU COME to my house to study?'",
         "Identify the 6 modal expressions used in this dialogue and state the function of each (obligation, advice, suggestion, ability, possibility, request).",
         "1. 'have to' (obligation). 2. 'should' (advice). 3. 'shall we' (suggestion). 4. 'can' (ability). 5. 'may' (possibility). 6. 'would you' (polite request/invitation).",
         "Shows practical usage of modal functions in everyday dialogue."),

        ("When vs While Sentence Transformation Scenario", "Transform past simple/continuous sentences.", "Hard",
         "Given the sentence pair: (A) 'I was doing my homework when you called.' (B) 'You called while I was doing my homework.'",
         "Explain how the position of 'when' and 'while' changes the clause structure between Past Simple and Past Continuous.",
         "'when' precedes the short, interrupting Past Simple clause ('when you called'). 'while' precedes the long, background Past Continuous clause ('while I was doing my homework').",
         "'when' + Past Simple vs 'while' + Past Continuous."),

        ("For vs Since Time Transformation Scenario", "Transform present perfect time expressions.", "Hard",
         "Situation: A student is rephrasing time expressions in present perfect sentences.",
         "Transform the sentence 'She has lived in Bangkok since 2021' (current year is 2026) using 'for' instead of 'since'.",
         "Transformed sentence: 'She has lived in Bangkok for 5 years.'",
         "Explanation: 'since' takes starting point (2021); 'for' takes calculated duration (5 years)."),

        ("Mustn't vs Don't Have To Rules Scenario", "Apply prohibition vs non-obligation rules.", "Hard",
         "A school handbook states: 'Rule 1: Students MUSTN'T use mobile phones during exams. Rule 2: Students DON'T HAVE TO wear uniforms on sports day.'",
         "Explain the exact difference in student behavior required by Rule 1 versus Rule 2.",
         "Rule 1 (Mustn't) is a strict prohibition (using phones is forbidden/punishable). Rule 2 (Don't have to) means lack of obligation (wearing uniform is optional, students may choose).",
         "Mustn't = forbidden; Don't have to = optional/no obligation."),

        ("Irregular Past Participle Error Correction Scenario", "Identify and correct V3 errors in student paragraph.", "Hard",
         "A student writes: 'I have catched three fish today. My brother has ate all the snacks, and we have went to the lake twice.'",
         "Identify the 3 incorrect irregular verb forms and provide their correct past participles (V3).",
         "1. 'catched' -> 'caught'. 2. 'ate' -> 'eaten'. 3. 'went' -> 'gone' (or 'been'). Corrected: 'have caught', 'has eaten', 'have gone/been'.",
         "Irregular V3 forms: catch -> caught, eat -> eaten, go -> gone/been."),

        ("Present Continuous vs Present Perfect Distinction", "Contrast ongoing action vs experience.", "Hard",
         "Situation: Comparing sentence pairs: (A) 'I am eating Thai food.' (B) 'I have eaten Thai food before.'",
         "Explain the difference in meaning and time frame between Sentence A and Sentence B.",
         "Sentence A (Present Continuous) describes an action happening right now. Sentence B (Present Perfect) describes a past life experience.",
         "Present Continuous = action now; Present Perfect = life experience up to now."),

        ("Modal Ability Transformation Scenario", "Express past inability vs present ability.", "Hard",
         "Situation: You are contrasting your skills between last year and this year.",
         "Write a 2-clause sentence about yourself comparing an activity you COULDN'T do last year with what you CAN do now.",
         "Example: 'I couldn't swim last year, but I can swim now.'",
         "Explanation: 'couldn't' shows past inability; 'can' shows present ability."),

        ("Polite Request Differentiation Scenario", "Formulate requests for borrowing vs action.", "Hard",
         "You want to ask your friend (A) for permission to borrow his bicycle, and (B) to help you carry a box.",
         "Write the two precise polite questions using 'May I' / 'Could I' for (A) and 'Would you' / 'Could you' for (B).",
         "(A) 'May I (or Could I) borrow your bicycle?' (B) 'Would you (or Could you) help me carry this box?'",
         "Permission for self = May I / Could I; Action by listener = Would you / Could you."),

        ("Future Prediction vs Intention Scenario", "Contrast 'will' and 'be going to'.", "Hard",
         "Compare: (A) 'Look at those dark clouds! It is going to rain.' (B) 'I think it will rain tomorrow.'",
         "Explain why 'is going to' is used in (A) while 'will' is used in (B).",
         "In (A), 'is going to' is used because there is immediate present evidence (dark clouds). In (B), 'will' is used for a general future prediction/opinion.",
         "Immediate visual evidence = be going to; Personal opinion/prediction = will."),

        ("Past Continuous Specific Time Scenario", "Analyze past continuous timeline.", "Hard",
         "At 6:00 PM yesterday, Mom started cooking. She finished at 7:00 PM. At 6:35 PM, the family was at the dinner table.",
         "Describe what the family was doing at 6:35 PM yesterday using the past continuous tense and explain why.",
         "The family was eating dinner at 6:35 PM yesterday. Explanation: At 6:35 PM, the action of eating dinner was in progress in the middle of the 6:00-7:00 timeframe.",
         "Specific mid-action past moment requires Past Continuous.")
    ]

    # 10 Short Answer Questions based on Grammar Gr6-MidFinal.pdf
    short_answer_questions = [
        # 106-115 Short Answer Questions (3 pts each)
        ("Past Simple vs Past Continuous Summary", "Explain the difference between Past Simple and Past Continuous.", "Hard",
         "Explain the main difference in usage between the Past Simple tense and the Past Continuous tense, providing one example sentence for each.",
         "Past Simple describes actions that began and ended at a completed time in the past (e.g., 'Sam watched a movie yesterday'). Past Continuous describes actions that were in progress at a specific time or during another event in the past (e.g., 'Sam was watching a movie at 2:30 PM').",
         "Clear contrast between completed past action and ongoing past action with valid examples."),

        ("When vs While Rules", "Formulate the rules for using 'when' and 'while'.", "Hard",
         "State the rules for using 'when' and 'while' in sentences combining Past Simple and Past Continuous, with an example for each.",
         "Rule 1: 'when' is followed by a Past Simple clause showing a short interrupting event (e.g., 'I was sleeping when the phone rang'). Rule 2: 'while' is followed by a Past Continuous clause showing an ongoing background duration (e.g., 'The phone rang while I was sleeping').",
         "Accurate rules for 'when' (+ Past Simple) and 'while' (+ Past Continuous) with examples."),

        ("Three Future Tenses Comparison", "Compare Will, Be Going To, and Present Continuous as Future.", "Hard",
         "Explain the different future usages of (1) Will, (2) Be Going To, and (3) Present Continuous (Be + -ing), giving one example for each.",
         "1. Will: Spontaneous decisions or general predictions (e.g., 'I will help you'). 2. Be Going To: Pre-planned intentions or evidence-based events (e.g., 'I am going to open the window'). 3. Present Continuous: Fixed, scheduled future arrangements with time expressions (e.g., 'Mark is running in a race tomorrow').",
         "Full explanation of all 3 future forms with correct example sentences."),

        ("Present Perfect Core Usage", "Explain the two main usages of Present Perfect.", "Hard",
         "Describe the two main usages of the Present Perfect tense (link to present with for/since, and life experience with ever/never) with examples.",
         "Usage 1: Action/state starting in the past continuing to the present (e.g., 'I have lived here for 5 years'). Usage 2: Life experience at an unspecified past time (e.g., 'Have you ever eaten Thai food?').",
         "Explains past-to-present continuity and life experience usages with clear examples."),

        ("For vs Since Rule", "Formulate the rule for 'for' versus 'since'.", "Hard",
         "State the rule for using 'for' versus 'since' in the Present Perfect tense, and give two examples.",
         "Rule: Use 'for' with a duration or period of time (e.g., for two hours, for 5 years). Use 'since' with a specific starting point in time (e.g., since 8:00 AM, since 2021).",
         "Distinguishes duration ('for') vs starting point ('since') with valid examples."),

        ("Polite Request Modals Comparison", "Compare 'May I', 'Could I', and 'Would you'.", "Hard",
         "Explain the difference between 'May I / Could I...?' and 'Would you / Could you...?' when making polite requests, giving an example of each.",
         "1. 'May I...?' / 'Could I...?' asks for PERMISSION for the speaker to do something (e.g., 'May I borrow your pen?'). 2. 'Would you...?' / 'Could you...?' asks another person (the listener) to PERFORM AN ACTION (e.g., 'Would you close the door, please?').",
         "Clear distinction between requesting speaker permission vs requesting listener action."),

        ("Mustn't vs Don't Have To Contrast", "Contrast prohibition vs lack of obligation.", "Hard",
         "Explain the critical difference in meaning between 'mustn't' and 'don't have to / doesn't have to', providing an example for each.",
         "1. 'mustn't' expresses prohibition (it is forbidden / not allowed, e.g., 'You mustn't smoke here'). 2. 'don't have to' expresses lack of obligation/necessity (it is optional, e.g., 'You don't have to get up early on Sunday').",
         "Accurate contrast between prohibition ('mustn't') and optional non-necessity ('don't have to')."),

        ("Modal Verbs for Possibility", "Explain 'may' and 'might' for possibility.", "Hard",
         "Explain how 'may' and 'might' are used to express possibility, and write one affirmative and one negative sentence as examples.",
         "Usage: 'may' and 'might' show that something is likely or possible in the present or future. Affirmative example: 'It might rain this afternoon.' Negative example: 'He may not come to the party.'",
         "Defines possibility function with clear affirmative and negative example sentences."),

        ("Modal Verbs for Obligation & Advice", "Compare 'must', 'have to', and 'should'.", "Hard",
         "Compare the meanings and strength of 'must', 'have to', and 'should' when talking about responsibilities and actions.",
         "1. 'must': Strong personal obligation or strict rule (e.g., 'Passengers must wear seat belts'). 2. 'have to': External duty or requirement (e.g., 'Tom has to feed his dog'). 3. 'should': Mild recommendation or advice (e.g., 'Tom should see a doctor').",
         "Explains strong obligation ('must'), external requirement ('have to'), and mild advice ('should')."),

        ("Irregular Past Participle Patterns", "List 5 irregular verbs with their V2 and V3 forms.", "Hard",
         "List 5 irregular verbs from the Grade 6 unit with their Simple Past (V2) and Past Participle (V3) forms (e.g., do - did - done).",
         "1. be - was/were - been. 2. catch - caught - caught. 3. do - did - done. 4. eat - ate - eaten. 5. ride - rode - ridden (or know - knew - known / see - saw - seen).",
         "5 complete irregular verb triads (V1 - V2 - V3) correctly matched.")
    ]

    # Assemble Markdown text
    lines = []
    lines.append("# แบบทดสอบประเมินผลความรู้ English Grammar Assessment Grade 6 In English language")
    lines.append("")
    lines.append("> **คำชี้แจง**: แบบทดสอบนี้ใช้สำหรับประเมินผลสัมฤทธิ์ทางการเรียนรู้ English Grammar Grade 6 (Past Continuous, Future Tenses, Present Perfect, and Modal Verbs 1 & 2) อ้างอิงตามเนื้อหาแบบเรียน Grammar Gr6-MidFinal.pdf ครอบคลุม 4 ส่วน จำนวนรวม 115 ข้อ คะแนนเต็ม 150 คะแนน")
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

    for filepath in ["Knowledge_Assessment_Grammar_Gr6.md", "Knowledge_Assessment_Grammar__Gr6.md"]:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Generated {filepath} successfully from Grammar PDF OCR content!")

if __name__ == "__main__":
    generate_grammar_quiz_from_pdf()
