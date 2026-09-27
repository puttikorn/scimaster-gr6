import os

file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_Science_Gr6.md"
alt_file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_Science_En_Gr6.md"

header = """# Knowledge Assessment Quiz: Science Grade 6 (Midterm & Final Assessment)

---

## Document Summary (Science Grade 6 Curriculum & Assessment Summary)

This assessment document compiles comprehensive learning content and evaluation questions for Science Grade 6, covering 5 core units:

### 1. Unit 1: Human Body Systems, Nutrition & Growth
* **Human Digestive System**: Organs (mouth, esophagus, stomach, liver, pancreas, small intestine, large intestine) and digestive enzymes
* **Body Systems & Nutrition**: Circulatory, respiratory, and excretory systems; 5 essential nutrient groups (Carbohydrates, Proteins, Fats, Vitamins, Minerals, Water) and balanced diet calories

### 2. Unit 2: Ecosystems, Food Webs & Environment
* **Food Chains & Food Webs**: Producers (autotrophs), Primary/Secondary Consumers (heterotrophs), and Decomposers
* **Symbiotic Relationships**: Mutualism (+/+), Commensalism (+/0), Parasitism (+/-), and Predation (+/-)
* **Environmental Protection**: Deforestation, global warming, air/water pollution, and conservation strategies

### 3. Unit 3: States of Matter, Physical & Chemical Changes
* **States of Matter**: Properties of solids, liquids, and gases; particle arrangement and kinetic energy
* **Changes of Matter**: Physical changes (melting, freezing, evaporation, condensation, sublimation) vs Chemical changes (rusting, combustion, acid-base neutralization)
* **Separating Mixtures**: Filtration, evaporation to dryness, decantation, magnetic separation, and simple distillation

### 4. Unit 4: Forces, Sound, Light & Electric Circuits
* **Forces & Motion**: Gravitational force, frictional force, magnetic force, and buoyant force
* **Electric Circuits**: Simple electric circuits, series vs parallel connections, electrical conductors and insulators, electromagnets
* **Sound & Light**: Sound propagation through media, pitch, loudness, noise pollution, reflection and refraction of light

### 5. Unit 5: Earth Systems, Astronomy & Natural Disasters
* **Sun-Earth-Moon System**: Earth's rotation and revolution, phases of the Moon, solar and lunar eclipses
* **Rock Cycle & Earth Processes**: Igneous, sedimentary, and metamorphic rocks; weathering, soil erosion, and fossil formation
* **Natural Disasters**: Causes, effects, and safety measures for earthquakes, tsunamis, flash floods, and landslides

---

## Learning Objectives Mapping

* **LO-SCI1**: Basic scientific facts, definitions, organ functions, and state changes (Remember / Understand)
* **LO-SCI2**: Applying scientific principles, electric circuit assembly, mixture separation techniques (Apply)
* **LO-SCI3**: Analyzing food webs, chemical vs physical changes, and eclipse phenomena (Analyze)
* **LO-SCI4**: Environmental impact assessment, health advice, scientific experiment design, and disaster safety (Evaluate / Create)

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
    # 1-15: Human Body & Nutrition
    (1, "Human Body Systems", "LO-SCI1", "Easy",
     "Which organ in the human digestive system is primarily responsible for absorbing nutrients into the bloodstream?",
     "Stomach", "Small intestine", "Large intestine", "Esophagus", "ข",
     "The small intestine has villi that absorb digested nutrients into the blood."),

    (2, "Human Body Systems", "LO-SCI1", "Easy",
     "Where does the chemical digestion of carbohydrates begin in the human body?",
     "Mouth", "Stomach", "Small intestine", "Gallbladder", "ก",
     "Salivary amylase in the mouth starts digesting starches into simple sugars."),

    (3, "Nutrition", "LO-SCI1", "Easy",
     "Which nutrient group is the primary source of quick energy for human body activities?",
     "Proteins", "Carbohydrates", "Vitamins", "Minerals", "ข",
     "Carbohydrates (starches and sugars) provide main operational energy."),

    (4, "Human Body Systems", "LO-SCI1", "Easy",
     "Which organ produces bile to help digest and emulsify fats?",
     "Stomach", "Pancreas", "Liver", "Kidney", "ค",
     "The liver produces bile, which is stored in the gallbladder and released into the small intestine."),

    (5, "Human Body Systems", "LO-SCI1", "Easy",
     "What is the main function of the large intestine?",
     "Digest proteins", "Absorb water and mineral salts", "Produce digestive enzymes", "Pump blood", "ข",
     "The large intestine absorbs remaining water and salts from indigestible food residues."),

    (6, "Nutrition", "LO-SCI1", "Easy",
     "Lack of Vitamin C in the human diet causes which condition?",
     "Night blindness", "Scurvy (bleeding gums)", "Rickets", "Beriberi", "ข",
     "Vitamin C deficiency leads to scurvy."),

    (7, "Nutrition", "LO-SCI1", "Easy",
     "Which nutrient is essential for tissue repair, growth, and building muscle cells?",
     "Fat", "Protein", "Carbohydrate", "Vitamin D", "ข",
     "Protein supplies amino acids necessary for growth and tissue repair."),

    (8, "Human Body Systems", "LO-SCI2", "Medium",
     "Which blood vessels carry oxygenated blood away from the heart to body tissues?",
     "Veins", "Arteries", "Capillaries", "Vena cava", "ข",
     "Arteries carry oxygen-rich blood away from the heart to the body."),

    (9, "Human Body Systems", "LO-SCI2", "Medium",
     "During inhalation, what happens to the diaphragm muscle and ribcage?",
     "Diaphragm moves up, ribcage moves down", "Diaphragm moves down, ribcage moves up and out", "Both move down", "Both relax", "ข",
     "Inhalation contracts the diaphragm downward and lifts the ribcage upward and outward to expand chest volume."),

    (10, "Human Body Systems", "LO-SCI1", "Easy",
     "Which organ filters waste products like urea from the blood to produce urine?",
     "Heart", "Lungs", "Kidneys", "Liver", "ค",
     "Kidneys filter metabolic waste from blood to form urine."),

    # 11-25: Ecosystems & Environment
    (11, "Ecosystems", "LO-SCI1", "Easy",
     "Organisms that synthesize their own food using sunlight through photosynthesis are called ________.",
     "Producers", "Primary consumers", "Secondary consumers", "Decomposers", "ก",
     "Green plants and algae are producers (autotrophs)."),

    (12, "Ecosystems", "LO-SCI1", "Easy",
     "Fungi and bacteria that break down dead organic matter into soil nutrients are ________.",
     "Herbivores", "Carnivores", "Decomposers", "Omnivores", "ค",
     "Fungi and bacteria act as decomposers in an ecosystem."),

    (13, "Symbiosis", "LO-SCI2", "Medium",
     "The relationship between a shark and a remora fish (where remora feeds on scrap food without harming the shark) is an example of ________.",
     "Mutualism", "Commensalism", "Parasitism", "Predation", "ข",
     "Commensalism (+/0) benefits one species while the other is unharmed."),

    (14, "Symbiosis", "LO-SCI2", "Medium",
     "Lichens consist of an alga and a fungus living together where both benefit. This relationship is ________.",
     "Mutualism", "Commensalism", "Parasitism", "Competition", "ก",
     "Mutualism (+/+) benefits both organisms."),

    (15, "Ecosystems", "LO-SCI3", "Hard",
     "In a food chain: Grass -> Grasshopper -> Frog -> Snake. If frogs are eliminated due to disease, what will likely happen initially?",
     "Snake population increases", "Grasshopper population increases", "Grass population decreases", "Grasshopper population decreases", "ข",
     "Without frogs (predators), the grasshopper population will increase rapidly."),

    (16, "Environment", "LO-SCI2", "Medium",
     "Which gas is the primary greenhouse gas contributing to global warming from burning fossil fuels?",
     "Oxygen", "Nitrogen", "Carbon dioxide", "Helium", "ค",
     "Carbon dioxide (CO2) traps heat energy in the atmosphere."),

    (17, "Environment", "LO-SCI1", "Easy",
     "Which practice best demonstrates the 'Reduce' principle of environmental conservation?",
     "Making flower pots from old plastic bottles", "Turning off lights when leaving a room", "Selling scrap metal to recycling centers", "Buying new plastic bags", "ข",
     "Turning off lights reduces energy consumption at the source."),

    # 26-40: Matter, Changes & Separating Mixtures
    (18, "States of Matter", "LO-SCI1", "Easy",
     "Which state of matter has a definite volume but no definite shape, taking the shape of its container?",
     "Solid", "Liquid", "Gas", "Plasma", "ข",
     "Liquids have fixed volume but adopt the container's shape."),

    (19, "Changes of Matter", "LO-SCI1", "Easy",
     "The phase change from gas directly to liquid upon cooling is called ________.",
     "Evaporation", "Melting", "Condensation", "Sublimation", "ค",
     "Gas turning into liquid is condensation."),

    (20, "Changes of Matter", "LO-SCI1", "Easy",
     "The process of solid mothballs shrinking in size without turning into liquid is called ________.",
     "Freezing", "Sublimation", "Boiling", "Dissolving", "ข",
     "Solid changing directly into gas is sublimation."),

    (21, "Chemical Changes", "LO-SCI2", "Medium",
     "Which of the following is an example of a chemical change?",
     "Ice melting into water", "Cutting paper into small pieces", "Iron nail rusting in moist air", "Dissolving sugar in warm water", "ค",
     "Iron rusting creates a new chemical substance (iron oxide)."),

    (22, "Separating Mixtures", "LO-SCI2", "Medium",
     "Which separation method is best suited to separate insoluble sand from water?",
     "Evaporation to dryness", "Filtration", "Magnetic separation", "Distillation", "ข",
     "Filtration separates insoluble solids from liquids."),

    (23, "Separating Mixtures", "LO-SCI2", "Medium",
     "How can you recover pure salt from a saltwater solution?",
     "Filtration", "Decantation", "Evaporation to dryness", "Using a sieve", "ค",
     "Evaporating water leaves solid salt crystals behind."),

    (24, "Separating Mixtures", "LO-SCI2", "Medium",
     "Which technique separates iron filings from a mixture of iron and sulfur powder?",
     "Filtration", "Magnetic separation", "Distillation", "Chromatography", "ข",
     "A magnet attracts iron filings away from non-magnetic sulfur."),

    (25, "Solutions", "LO-SCI1", "Easy",
     "When sugar dissolves completely in water, what is the water called?",
     "Solute", "Solvent", "Solution", "Suspension", "ข",
     "Water is the dissolving medium, called the solvent."),

    # 41-50: Forces, Circuits, Sound & Light
    (26, "Forces", "LO-SCI1", "Easy",
     "Which force opposes the motion of two surfaces sliding past each other?",
     "Gravitational force", "Frictional force", "Magnetic force", "Electrostatic force", "ข",
     "Friction opposes relative sliding motion."),

    (27, "Forces", "LO-SCI2", "Medium",
     "An object weighs 60 N on Earth. If gravity on the Moon is 1/6 of Earth's gravity, how much will the object weigh on the Moon?",
     "0 N", "10 N", "60 N", "360 N", "ข",
     "Weight on Moon = 60 N / 6 = 10 N."),

    (28, "Electric Circuits", "LO-SCI1", "Easy",
     "Which material is a good electrical conductor?",
     "Plastic", "Rubber", "Copper wire", "Wood", "ค",
     "Copper is a metallic conductor of electricity."),

    (29, "Electric Circuits", "LO-SCI2", "Medium",
     "In a series circuit containing two light bulbs, what happens if one bulb burns out?",
     "The other bulb burns brighter", "The other bulb stays lit", "The other bulb goes out", "The circuit short circuits", "ค",
     "Series circuit path is broken, so all components turn off."),

    (30, "Electric Circuits", "LO-SCI2", "Medium",
     "In a parallel circuit with three light bulbs, what happens if one bulb burns out?",
     "All bulbs go out", "The remaining bulbs stay lit", "The battery explodes", "Voltage drops to zero", "ข",
     "Parallel circuits provide independent current paths for each bulb."),

    (31, "Sound", "LO-SCI1", "Easy",
     "Sound waves CANNOT travel through which medium?",
     "Air", "Water", "Steel beam", "Vacuum (outer space)", "ง",
     "Sound requires a physical medium to propagate; it cannot travel in a vacuum."),

    (32, "Sound", "LO-SCI2", "Medium",
     "The pitch of a sound (high or low pitch) depends primarily on the sound wave's ________.",
     "Amplitude", "Frequency", "Speed", "Color", "ข",
     "Frequency determines pitch (high frequency = high pitch)."),

    (33, "Light", "LO-SCI1", "Easy",
     "When light bounces off a smooth shiny surface like a mirror, this phenomenon is called ________.",
     "Refraction", "Reflection", "Absorption", "Diffraction", "ข",
     "Bouncing of light off a surface is reflection."),

    (34, "Light", "LO-SCI2", "Medium",
     "A pencil appearing bent when placed in a glass of water is caused by light ________.",
     "Reflection", "Refraction", "Dispersion", "Shadowing", "ข",
     "Refraction occurs when light changes speed traveling through different media (air and water)."),

    (35, "Forces & Floatation", "LO-SCI2", "Medium",
     "An object floats in water when the upward buoyant force acting on it is ________ its total weight.",
     "Less than", "Equal to", "Greater than zero but less than weight", "Zero", "ข",
     "For a floating object, Buoyant force equals object weight."),

    # 51-60: Earth, Astronomy & Disasters
    (36, "Astronomy", "LO-SCI1", "Easy",
     "Earth completes one full rotation on its axis in approximately ________.",
     "12 hours", "24 hours (1 day)", "30 days", "365 days (1 year)", "ข",
     "Earth's rotation takes 24 hours, causing day and night."),

    (37, "Astronomy", "LO-SCI1", "Easy",
     "Earth completes one full orbit (revolution) around the Sun in approximately ________.",
     "24 hours", "28 days", "365.25 days (1 year)", "10 years", "ค",
     "Revolution around the Sun takes 365.25 days."),

    (38, "Astronomy", "LO-SCI2", "Medium",
     "What alignment of the Sun, Earth, and Moon causes a Solar Eclipse?",
     "Sun - Earth - Moon", "Sun - Moon - Earth", "Earth - Sun - Moon", "Moon - Sun - Earth", "ข",
     "Solar Eclipse occurs when the Moon passes between the Sun and Earth (Sun - Moon - Earth)."),

    (39, "Astronomy", "LO-SCI2", "Medium",
     "During which Moon phase can a Lunar Eclipse occur?",
     "New Moon", "First Quarter", "Full Moon", "Crescent Moon", "ค",
     "Lunar Eclipse occurs only during Full Moon when Earth's shadow falls on the Moon."),

    (40, "Geology (Rocks)", "LO-SCI1", "Easy",
     "Rocks formed from the cooling and solidification of molten magma or lava are called ________.",
     "Sedimentary rocks", "Igneous rocks", "Metamorphic rocks", "Fossil rocks", "ข",
     "Cooling of magma/lava forms igneous rocks."),

    (41, "Geology (Rocks)", "LO-SCI1", "Easy",
     "Fossils of ancient plants and animals are most commonly found in which rock type?",
     "Igneous rocks", "Sedimentary rocks", "Metamorphic rocks", "Volcanic glass", "ข",
     "Layered sedimentary rocks preserve fossils."),

    (42, "Geology (Rocks)", "LO-SCI2", "Medium",
     "Marble is formed when limestone undergoes extreme heat and pressure inside the Earth. Marble is a(n) ________ rock.",
     "Igneous", "Sedimentary", "Metamorphic", "Extrusive", "ค",
     "Heat and pressure transform rocks into metamorphic rocks."),

    (43, "Natural Disasters", "LO-SCI1", "Easy",
     "A giant sea wave caused by a sudden underwater earthquake or volcanic eruption is a ________.",
     "Tornado", "Tsunami", "Hurricane", "Cyclone", "ข",
     "Underwater seismic activity triggers a tsunami."),

    (44, "Natural Disasters", "LO-SCI2", "Medium",
     "Which instrument is used to detect and record earthquake seismic waves?",
     "Barometer", "Seismograph", "Anemometer", "Thermometer", "ข",
     "Seismographs record earthquake ground vibrations."),

    (45, "Earth Systems", "LO-SCI2", "Medium",
     "The movement of water continuously between Earth's surface and the atmosphere is the ________.",
     "Rock cycle", "Water cycle", "Carbon cycle", "Nitrogen cycle", "ข",
     "Evaporation, condensation, and precipitation form the water cycle."),

    (46, "Nutrition", "LO-SCI2", "Medium",
     "Which vitamin is synthesized by human skin when exposed to morning sunlight?",
     "Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D", "ง",
     "Sunlight stimulates skin synthesis of Vitamin D."),

    (47, "Human Body Systems", "LO-SCI2", "Medium",
     "What is the function of red blood cells in the circulatory system?",
     "Fight bacterial infections", "Transport oxygen using hemoglobin", "Clot blood at wounds", "Digest food particles", "ข",
     "Red blood cells contain hemoglobin to transport oxygen."),

    (48, "Ecosystems", "LO-SCI2", "Medium",
     "Herbivores are organisms that eat ________.",
     "Only plants", "Only animals", "Both plants and animals", "Dead organisms", "ก",
     "Herbivores feed exclusively on plants."),

    (49, "States of Matter", "LO-SCI2", "Medium",
     "Why does ice float on water?",
     "Ice is denser than liquid water", "Ice is less dense than liquid water", "Ice has no mass", "Water repels ice", "ข",
     "Water expands when freezing, making ice less dense than liquid water."),

    (50, "Electric Circuits", "LO-SCI1", "Easy",
     "Which component opens or closes an electric circuit?",
     "Resistor", "Battery", "Switch", "Voltmeter", "ค",
     "A switch controls the opening and closing of a circuit."),

    (51, "Sound", "LO-SCI2", "Medium",
     "Noise pollution refers to sound levels exceeding ________ decibels (dB) that can cause hearing damage.",
     "40 dB", "60 dB", "85 dB", "120 dB", "ค",
     "Continuous exposure to sounds above 85 dB causes hearing impairment."),

    (52, "Forces", "LO-SCI2", "Medium",
     "How can friction be reduced between moving machine parts?",
     "Applying lubricants like oil or grease", "Roughening the contact surfaces", "Increasing object weight", "Using sandpaper", "ก",
     "Lubricants reduce surface friction between moving components."),

    (53, "Astronomy", "LO-SCI2", "Medium",
     "What causes the changing seasons on Earth?",
     "Distance between Earth and Sun changing", "Tilt of Earth's axis (23.5°) as it revolves around the Sun", "Moon's gravitational pull", "Sun's variable energy output", "ข",
     "Earth's 23.5° axial tilt during annual revolution causes seasonal variations."),

    (54, "Environment", "LO-SCI2", "Medium",
     "Acid rain is caused primarily by atmospheric emission of which gases?",
     "Sulfur dioxide and Nitrogen oxides", "Oxygen and Nitrogen", "Carbon monoxide and Argon", "Methane and Water vapor", "ก",
     "SO2 and NOx react with atmospheric water vapor to form acid rain."),

    (55, "Separating Mixtures", "LO-SCI2", "Medium",
     "Decantation is used to separate ________.",
     "Two miscible liquids", "Heavy insoluble solid settled at the bottom of a liquid", "Dissolved salt from water", "Two gases", "ข",
     "Decantation pours off liquid from settled dense insoluble solids."),

    (56, "Changes of Matter", "LO-SCI2", "Medium",
     "Which of the following processes absorbs heat energy (endothermic)?",
     "Water freezing into ice", "Water vapor condensing into rain", "Ice melting into water", "Steam condensing to liquid", "ค",
     "Melting requires heat energy input to break solid particle bonds."),

    (57, "Human Body Systems", "LO-SCI2", "Medium",
     "What is the main function of white blood cells?",
     "Carry carbon dioxide", "Defend the body against pathogens and infections", "Form blood clots", "Transport nutrients", "ข",
     "White blood cells produce antibodies and engulf pathogens."),

    (58, "Ecosystems", "LO-SCI2", "Medium",
     "Which organism represents a secondary consumer in a forest food chain?",
     "Oak tree", "Caterpillar eating leaves", "Bird eating caterpillars", "Fungus decomposing wood", "ค",
     "A bird eating a primary consumer (caterpillar) is a secondary consumer."),

    (59, "Natural Disasters", "LO-SCI2", "Medium",
     "During an earthquake, if you are indoors, what is the safest immediate action?",
     "Run outside using an elevator", "Stand near glass windows", "Drop, Cover, and Hold On under a sturdy table", "Panic and shout", "ค",
     "Taking shelter under sturdy furniture protects from falling debris."),

    (60, "Astronomy", "LO-SCI1", "Easy",
     "Which celestial body does NOT produce its own light and reflects sunlight?",
     "The Sun", "North Star (Polaris)", "The Moon", "Alpha Centauri", "ค",
     "The Moon is a non-luminous body reflecting sunlight.")
]

tf_questions = [
    # 61-90 True/False
    (61, "Human Body Systems", "LO-SCI1", "Easy",
     "Digestion of protein begins in the stomach with the action of pepsin and hydrochloric acid.",
     "True", "Correct. Gastric juice (pepsin + HCl) begins protein breakdown in the stomach."),

    (62, "Human Body Systems", "LO-SCI1", "Easy",
     "Vitamins and minerals provide zero calories of energy to the human body.",
     "True", "Correct. Vitamins and minerals regulate metabolic processes but supply no caloric energy."),

    (63, "Nutrition", "LO-SCI1", "Easy",
     "Fats yield more than twice as much energy per gram (9 kcal/g) compared to carbohydrates (4 kcal/g).",
     "True", "Correct. Fat provides 9 kcal/g, while carbohydrates and proteins provide 4 kcal/g."),

    (64, "Ecosystems", "LO-SCI1", "Easy",
     "Decomposers transfer energy directly back to the Sun.",
     "False", "Incorrect. Energy flows one-way from the Sun to organisms and leaves as heat; decomposers recycle nutrients, not solar energy."),

    (65, "Symbiosis", "LO-SCI2", "Medium",
     "A tick feeding on a dog's blood is an example of parasitism (+/-).",
     "True", "Correct. The parasite (tick) benefits (+), while the host (dog) is harmed (-)."),

    (66, "Changes of Matter", "LO-SCI1", "Easy",
     "Rusting of iron is a reversible physical change.",
     "False", "Incorrect. Rusting forms a new substance (iron oxide) and is an irreversible chemical change."),

    (67, "Changes of Matter", "LO-SCI1", "Easy",
     "Burning wood into ash and smoke is a chemical change.",
     "True", "Correct. Combustion forms new chemical substances (ash, CO2, water vapor)."),

    (68, "Separating Mixtures", "LO-SCI2", "Medium",
     "Filtration can be used to separate dissolved table salt from water.",
     "False", "Incorrect. Dissolved salt passes through filter paper; evaporation to dryness is required."),

    (69, "States of Matter", "LO-SCI1", "Easy",
     "Gas particles are tightly packed in fixed orderly positions.",
     "False", "Incorrect. Solids have tightly packed fixed particles; gas particles move freely with large spacing."),

    (70, "Forces", "LO-SCI1", "Easy",
     "Friction always acts in the direction OPPOSITE to an object's motion.",
     "True", "Correct. Friction opposes relative motion between contacting surfaces."),

    (71, "Forces", "LO-SCI2", "Medium",
     "Mass changes depending on the gravitational strength of the planet you are on.",
     "False", "Incorrect. Mass (amount of matter) remains constant; weight changes with gravity."),

    (72, "Electric Circuits", "LO-SCI1", "Easy",
     "Pure distilled water is an excellent conductor of electricity.",
     "False", "Incorrect. Pure water lacks free ions and is a poor conductor; dissolved salts enable conductivity."),

    (73, "Electric Circuits", "LO-SCI2", "Medium",
     "An electromagnet loses its magnetism when the electric current is turned off.",
     "True", "Correct. Electromagnets are temporary magnets dependent on electric current flow."),

    (74, "Sound", "LO-SCI1", "Easy",
     "Sound travels faster in solids than in liquids and gases.",
     "True", "Correct. Tightly packed particles in solids transmit sound vibrations faster than liquids or gases."),

    (75, "Sound", "LO-SCI2", "Medium",
     "Increasing the amplitude of a sound wave makes the pitch higher.",
     "False", "Incorrect. Amplitude determines loudness/volume, while frequency determines pitch."),

    (76, "Light", "LO-SCI1", "Easy",
     "Light travels in straight lines called rays.",
     "True", "Correct. Rectilinear propagation of light means light travels in straight lines."),

    (77, "Astronomy", "LO-SCI2", "Medium",
     "A Solar Eclipse occurs when Earth passes directly between the Sun and the Moon.",
     "False", "Incorrect. Earth between Sun and Moon causes a LUNAR Eclipse. Solar Eclipse occurs when the MOON passes between Sun and Earth."),

    (78, "Astronomy", "LO-SCI1", "Easy",
     "The Moon shines because it undergoes nuclear fusion like the Sun.",
     "False", "Incorrect. The Moon reflects light received from the Sun."),

    (79, "Geology", "LO-SCI1", "Easy",
     "Igneous rocks are formed from layers of accumulated sediment over millions of years.",
     "False", "Incorrect. Layered sediments form Sedimentary rocks. Igneous rocks form from cooling magma/lava."),

    (80, "Environment", "LO-SCI2", "Medium",
     "Deforestation increases atmospheric carbon dioxide because trees absorb CO2 during photosynthesis.",
     "True", "Correct. Fewer trees reduce CO2 absorption, raising global atmospheric CO2 levels."),

    (81, "Human Body Systems", "LO-SCI1", "Easy",
     "The alveoli in the lungs are the site of gas exchange between air and blood capillaries.",
     "True", "Correct. Oxygen diffuses into blood and CO2 diffuses out across alveolar walls."),

    (82, "Human Body Systems", "LO-SCI1", "Easy",
     "Platelets are blood components responsible for carrying oxygen.",
     "False", "Incorrect. Red blood cells carry oxygen; platelets facilitate blood clotting."),

    (83, "Nutrition", "LO-SCI1", "Easy",
     "Water is essential for temperature regulation, waste removal, and biochemical reactions in the body.",
     "True", "Correct. Water makes up ~60% of human body weight and regulates bodily functions."),

    (84, "Ecosystems", "LO-SCI1", "Easy",
     "A carnivore is an animal that eats only plants.",
     "False", "Incorrect. Carnivores eat meat/animals. Herbivores eat plants."),

    (85, "Forces", "LO-SCI1", "Easy",
     "Like magnetic poles (N-N or S-S) attract each other.",
     "False", "Incorrect. Like poles repel each other; opposite poles (N-S) attract."),

    (86, "Electric Circuits", "LO-SCI1", "Easy",
     "Fuses and circuit breakers protect electrical circuits from overheating due to excessive current.",
     "True", "Correct. Fuses melt to open the circuit during current overloads."),

    (87, "Changes of Matter", "LO-SCI2", "Medium",
     "Dissolving salt in water is a physical change because salt can be recovered by evaporating the water.",
     "True", "Correct. No new chemical substance is created, and the process is reversible."),

    (88, "Natural Disasters", "LO-SCI1", "Easy",
     "Tsunamis are giant wind-driven ocean waves caused by hurricanes.",
     "False", "Incorrect. Tsunamis are caused by undersea seismic activity (earthquakes/volcanoes), not wind."),

    (89, "Astronomy", "LO-SCI1", "Easy",
     "Day and night are caused by Earth's revolution around the Sun.",
     "False", "Incorrect. Day and night are caused by Earth's ROTATION on its axis."),

    (90, "Environment", "LO-SCI2", "Medium",
     "Recycling plastic reduces the volume of solid waste sent to landfills.",
     "True", "Correct. Recycling reprocesses materials into new products, reducing landfill waste.")
]

sc_questions = [
    # 91-105 Scenario
    (91, "Human Digestive System Scenario", "LO-SCI4", "Hard",
     "Tom ate a lunch consisting of grilled chicken (protein), steamed rice (carbohydrate), and buttered toast (fat). Trace the pathway of digestion for chicken (protein) through Tom's digestive tract, mentioning organs and digestive juices.",
     "Question: Describe the digestive path of protein (chicken) from entrance to absorption.",
     "1) Mouth: Mechanical breakdown by teeth, swallowed down esophagus.\\n2) Stomach: Gastric juice containing pepsin and hydrochloric acid begins chemical protein digestion.\\n3) Small Intestine: Pancreatic juice and intestinal enzymes complete protein breakdown into amino acids.\\n4) Absorption: Amino acids are absorbed into bloodstream through villi in small intestine.",
     "Explanation: Protein digestion begins in stomach (pepsin) and finishes in small intestine."),

    (92, "Food Web Analysis Scenario", "LO-SCI3", "Hard",
     "In a pond ecosystem food web: Phytoplankton -> Zooplankton -> Small Fish -> Osprey (bird). Farmers spray pesticides nearby, which wash into the pond. Pesticide concentration accumulates higher up the food chain (biomagnification). Which organism will have the highest pesticide concentration, and why?",
     "Question: Identify the organism with the highest pesticide toxicity and explain biomagnification.",
     "Organism: Osprey (top predator).\\nReason: Biomagnification causes non-biodegradable toxins to accumulate in progressively higher concentrations at higher trophic levels. As Osprey eats many small fish over its lifespan, it accumulates the maximum toxin concentration.",
     "Explanation: Biomagnification concentrates persistent toxins at top trophic levels."),

    (93, "Separating Mixture Scenario", "LO-SCI3", "Hard",
     "A student accidentally mixed iron filings, table salt, and coarse sand in a container. Design a step-by-step procedure using physical separation techniques to isolate all three components cleanly.",
     "Question: Outline the step-by-step separation process for iron, salt, and sand.",
     "Step 1: Use a magnet to attract and remove iron filings.\\nStep 2: Add water to remaining salt and sand mixture; stir until salt completely dissolves.\\nStep 3: Filter the mixture using filter paper to collect sand on paper.\\nStep 4: Heat the salt solution to evaporate water, leaving dry salt crystals.",
     "Explanation: Magnetic separation -> Dissolution -> Filtration -> Evaporation."),

    (94, "Electric Circuit Troubleshooting Scenario", "LO-SCI3", "Hard",
     "A student constructs a circuit with a battery, a switch, and two light bulbs connected in series. When the switch is closed, neither bulb lights up. List 3 possible reasons for this failure and how to test them.",
     "Question: Identify 3 possible circuit faults and diagnostic steps.",
     "Fault 1: Dead battery -> Test with a new battery or voltmeter.\\nFault 2: One bulb is burnt out -> Replace each bulb or inspect filaments.\\nFault 3: Loose wire connection or open switch -> Check and tighten all connection terminals.",
     "Explanation: Series circuits require a continuous unbroken path for current flow."),

    (95, "Eclipse Observation Scenario", "LO-SCI4", "Hard",
     "During a solar eclipse event, people are advised never to look directly at the Sun with naked eyes or regular sunglasses. Explain the astronomical cause of a solar eclipse and safe observation methods.",
     "Question: Explain the Solar Eclipse alignment and eye safety guidelines.",
     "Cause: Solar Eclipse occurs when Moon passes directly between Sun and Earth, casting Moon's shadow on Earth.\\nEye Safety: Direct solar viewing causes severe retinal burn from UV/IR radiation. Safe methods include ISO-certified solar eclipse glasses or pinhole projection.",
     "Explanation: Sun-Moon-Earth alignment; solar radiation damages retinal cells."),

    (96, "State Change & Heat Transfer Scenario", "LO-SCI3", "Hard",
     "A glass of iced water is placed on a table in a warm room. After 15 minutes, water droplets form on the outer surface of the glass. Explain where the water droplets came from and the heat process involved.",
     "Question: Explain the origin of outer glass water droplets and phase change.",
     "Origin: Water vapor present in ambient air.\\nProcess: Warm air water vapor contacts the cold glass surface, loses heat energy, and undergoes condensation into liquid water droplets.",
     "Explanation: Cooling air vapor below dew point causes condensation."),

    (97, "Friction & Safety Scenario", "LO-SCI4", "Hard",
     "Engineers design car tires with deep tread patterns. Explain how tread patterns affect frictional force on wet roads and why worn-out smooth tires are dangerous.",
     "Question: Explain tire tread function on wet roads and hazards of smooth tires.",
     "Tread Function: Deep grooves channel water away from tire contact area, maintaining rubber-road contact and high frictional grip.\\nWorn Tires: Smooth tires trap water underneath (hydroplaning), drastically reducing friction, causing skidding and brake failure.",
     "Explanation: Tire treads displace water to preserve frictional traction."),

    (98, "Sound Pitch & Frequency Scenario", "LO-SCI3", "Hard",
     "A student plucks two guitar strings: String A (thick and loose) and String B (thin and tight). Which string will produce a higher pitch sound? Explain the relationship between string tension/thickness, vibration frequency, and pitch.",
     "Question: Compare pitch between String A and B and explain acoustic frequency.",
     "Higher Pitch: String B (thin and tight).\\nExplanation: Thinner and tighter strings vibrate faster (higher frequency). Higher frequency vibrations produce higher pitch sound waves.",
     "Explanation: High string tension/thinness -> Higher frequency -> Higher pitch."),

    (99, "Photosynthesis & Plant Biology Scenario", "LO-SCI3", "Hard",
     "A green plant is placed in a sealed glass jar with sunlight, water, and carbon dioxide. Write the word equation for photosynthesis and explain how plants support oxygen supply for animals.",
     "Question: Write the photosynthesis word equation and explain gas exchange balance.",
     "Equation: Carbon dioxide + Water + Sunlight (Chlorophyll) -> Glucose + Oxygen.\\nAnimal Support: Plants release oxygen as a byproduct of photosynthesis, which animals inhale for cellular respiration.",
     "Explanation: CO2 + H2O + Light -> C6H12O6 + O2."),

    (100, "Balanced Diet & Caloric Need Scenario", "LO-SCI4", "Hard",
     "An 11-year-old active student needs approximately 1,800 kcal per day. Compare his diet requirements with an adult office worker who sits all day, and recommend a balanced meal plan.",
     "Question: Compare nutritional needs between active child and sedentary worker.",
     "Child Needs: Higher proportion of carbohydrates for energy and proteins for active growth/repair.\\nSedentary Worker Needs: Fewer total calories to prevent weight gain; higher fiber/vitamins.\\nChild Meal Plan: Brown rice (carbs), grilled chicken/egg (protein), milk (calcium), fresh fruits/vegetables.",
     "Explanation: Caloric and protein intake must match activity level and growth stage."),

    (101, "Light Refraction & Lenses Scenario", "LO-SCI3", "Hard",
     "A swimming pool appears shallower than its actual depth when viewed from above. Explain the optical phenomenon responsible for this illusion with a ray path description.",
     "Question: Explain why pool water appears shallower using optical refraction.",
     "Phenomenon: Light Refraction.\\nExplanation: Light reflected from pool bottom travels from water (denser) to air (less dense), speeding up and bending away from normal line before entering viewer's eye. The brain traces rays straight back, making pool bottom appear higher.",
     "Explanation: Refraction bending light away from normal at water-air boundary."),

    (102, "Earthquake & Tsunami Safety Scenario", "LO-SCI4", "Hard",
     "A coastal town experiences a strong 7.2 magnitude earthquake. Minutes later, sea water recedes rapidly from the beach. What natural disaster is imminent, and what immediate evacuation steps should residents take?",
     "Question: Identify the disaster warning signal and safety evacuation plan.",
     "Imminent Disaster: Tsunami.\\nEvacuation Steps: Immediately run to high ground or inland at least 2-3 km away; do not stay at beach to watch receding water; seek shelter in sturdy concrete buildings above 3rd floor.",
     "Explanation: Sudden coastal water recession is a natural warning sign of tsunami."),

    (103, "Rock Cycle & Geology Scenario", "LO-SCI3", "Hard",
     "Explain how a volcanic igneous rock (like basalt) can eventually transform into a metamorphic rock (like slate/schist) through geological processes.",
     "Question: Trace the geological transformation path from igneous to metamorphic rock.",
     "Step 1: Weathering & Erosion break basalt into small rock sediments.\\nStep 2: Transport & Deposition layer sediments in lakes/oceans.\\nStep 3: Compaction & Cementation form Sedimentary rock over millions of years.\\nStep 4: Tectonic Heat & Pressure deep underground transform sedimentary rock into Metamorphic rock.",
     "Explanation: Igneous -> Weathering/Sedimentation -> Sedimentary -> Heat/Pressure -> Metamorphic."),

    (104, "Global Warming & Carbon Footprint Scenario", "LO-SCI4", "Hard",
     "Explain how excessive burning of fossil fuels in power plants and vehicles leads to enhanced greenhouse effect and climate change, and suggest 3 personal actions to reduce carbon footprint.",
     "Question: Describe greenhouse mechanism and 3 personal carbon reduction actions.",
     "Mechanism: Burning fossil fuels releases CO2 gas. CO2 traps infrared heat radiated from Earth, preventing heat escape into space, causing global temperature rise.\\n3 Actions: 1) Use public transport or bicycle instead of private cars. 2) Save electricity by turning off unused appliances. 3) Plant trees to absorb CO2.",
     "Explanation: CO2 heat trapping -> Climate change; actions reduce energy/fuel usage."),

    (105, "Buoyancy & Ship Design Scenario", "LO-SCI3", "Hard",
     "A solid iron block sinks immediately in water, but a huge cargo ship made of iron floats easily on ocean waters. Explain Archimedes' principle and why the ship floats.",
     "Question: Explain why an iron ship floats while a solid iron block sinks.",
     "Explanation: A solid iron block is denser than water. However, a ship is hollowed out containing large air spaces. This increases the total volume, reducing the overall average density of the ship to less than water. The hollow ship displaces a large weight of water equal to its own total weight, generating sufficient buoyant force to float.",
     "Explanation: Hollow shape increases displaced volume, reducing average density below water.")
]

sa_questions = [
    # 106-115 Short Answer
    (106, "Human Digestive System Organs & Functions", "LO-SCI1", "Medium",
     "List the 5 major organs of the human digestive tract in sequence from food entry to waste exit, and state the main digestion function of the stomach and small intestine.",
     "Sequence: Mouth -> Esophagus -> Stomach -> Small Intestine -> Large Intestine.\\n- Stomach Function: Secretes gastric juice (HCl + pepsin) to digest proteins and kill bacteria.\\n- Small Intestine Function: Completes digestion of carbs, proteins, and fats, and absorbs nutrients into blood."),

    (107, "Food Chain & Trophic Energy Flow", "LO-SCI2", "Medium",
     "Construct a 4-step terrestrial food chain using: Hawk, Grass, Snake, Grasshopper. Identify the Producer, Primary Consumer, Secondary Consumer, and Tertiary Consumer.",
     "Food Chain: Grass -> Grasshopper -> Snake -> Hawk.\\n- Producer: Grass\\n- Primary Consumer: Grasshopper (herbivore)\\n- Secondary Consumer: Snake (carnivore)\\n- Tertiary Consumer: Hawk (top predator)"),

    (108, "Physical vs Chemical Changes Comparison", "LO-SCI2", "Medium",
     "Compare Physical Changes and Chemical Changes using 3 criteria: 1) Formation of new substances, 2) Reversibility, 3) Give 1 practical example for each.",
     "1) New Substances: Physical change = No new substance; Chemical change = New substance formed.\\n2) Reversibility: Physical change = Usually reversible; Chemical change = Usually irreversible.\\n3) Examples: Physical = Ice melting into water; Chemical = Iron nail rusting."),

    (109, "Separating 3-Component Mixture", "LO-SCI3", "Hard",
     "Explain how to separate a mixture of Salt, Water, and Sand to obtain pure dry sand and dry salt crystals.",
     "Step 1: Filter the saltwater and sand mixture through filter paper to collect sand on paper; wash and dry sand.\\nStep 2: Collect the clear saltwater filtrate.\\nStep 3: Heat the filtrate in an evaporating dish until all water evaporates, leaving solid dry salt crystals."),

    (110, "Series vs Parallel Circuits Comparison", "LO-SCI2", "Medium",
     "Compare Series Circuits and Parallel Circuits regarding: 1) Current pathway count, 2) Effect when one bulb burns out, 3) Common household application.",
     "1) Current Paths: Series = 1 single path; Parallel = Multiple independent paths.\\n2) Bulb Burnout Effect: Series = All bulbs go out; Parallel = Remaining bulbs stay lit.\\n3) Household Use: Parallel circuits are used in house wiring so appliances operate independently."),

    (111, "Sound Pitch vs Loudness Factors", "LO-SCI2", "Medium",
     "Explain the difference between Sound Pitch and Sound Loudness, including the wave property that controls each.",
     "1) Pitch: Describes how high or low a sound is; controlled by Wave Frequency (Hz). High frequency = High pitch.\\n2) Loudness: Describes how loud or soft a sound is; controlled by Wave Amplitude (dB). High amplitude = Loud sound."),

    (112, "Solar vs Lunar Eclipse Mechanics", "LO-SCI3", "Hard",
     "Differentiate between a Solar Eclipse and a Lunar Eclipse regarding: 1) Alignment order of Sun, Earth, Moon, 2) Moon phase required, 3) Time of day it occurs.",
     "1) Alignment: Solar = Sun - Moon - Earth; Lunar = Sun - Earth - Moon.\\n2) Moon Phase: Solar = New Moon; Lunar = Full Moon.\\n3) Time of Occurrence: Solar = Daytime; Lunar = Nighttime."),

    (113, "Rock Types Classification & Formation", "LO-SCI2", "Medium",
     "List the 3 main types of rocks categorized by their formation process, and briefly describe how each type is formed.",
     "1) Igneous Rocks: Formed from the cooling and solidification of molten magma or lava.\\n2) Sedimentary Rocks: Formed from accumulation, compaction, and cementation of rock sediments.\\n3) Metamorphic Rocks: Formed when existing rocks are transformed by intense heat and pressure."),

    (114, "Frictional Force Advantages & Disadvantages", "LO-SCI2", "Medium",
     "State 2 advantages and 2 disadvantages of frictional force in daily life.",
     "Advantages:\\n1) Allows us to walk without slipping.\\n2) Enables vehicle brakes to stop moving cars.\\nDisadvantages:\\n1) Causes wear and tear on machine parts and shoe soles.\\n2) Produces unwanted heat and energy loss in engines."),

    (115, "Global Warming Causes & Mitigations", "LO-SCI4", "Hard",
     "Explain the cause of Global Warming and outline 3 actionable strategies to mitigate its environmental impact.",
     "Cause: Excess greenhouse gases (mainly CO2) from human activity trap heat in Earth's atmosphere, causing average global temperature rise.\\n3 Strategies:\\n1) Switch to renewable energy (solar/wind) instead of fossil fuels.\\n2) Reforestation and planting trees to absorb atmospheric CO2.\\n3) Practice 3Rs (Reduce, Reuse, Recycle) to conserve energy and materials.")
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

print(f"Successfully generated pure English Science Grade 6 quiz files at {file_path} and {alt_file_path}!")
