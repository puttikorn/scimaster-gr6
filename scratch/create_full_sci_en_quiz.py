import os

def generate_sci_en_quiz_from_pdf():
    # 60 MCQ Questions based on Science Gr6 -MidFinal.pdf (Separating Mixtures & Rocks/Minerals)
    mcq_questions = [
        # 1-12: Pure Substances vs. Mixtures & Homogeneous vs. Heterogeneous (Pages 1-9)
        ("Pure Substances vs Mixtures", "Identify pure substances vs mixtures.", "Easy",
         "Which of the following is considered a PURE SUBSTANCE because it contains only one type of particle?",
         ["Coffee", "Water", "Salad", "Wine"], "B",
         "Water is a pure substance containing only water molecules. Coffee, salad, and wine are mixtures."),

        ("Definition of Mixture", "Define what a mixture is.", "Easy",
         "What is a mixture?",
         ["A substance containing only one type of element", "A combination of two or more different substances mixed together", "A liquid that has completely boiled away", "A rock formed from magma"], "B",
         "A mixture consists of two or more different particles/substances mixed together physically."),

        ("Homogeneous Mixtures", "Identify characteristics of homogeneous mixtures.", "Easy",
         "Which characteristic best describes a HOMOGENEOUS mixture?",
         ["Components are visibly different and easily separated by eye", "The composition is uniform throughout the mixture", "It contains only one type of atom", "It always settles at the bottom"], "B",
         "A homogeneous mixture has a uniform appearance and composition throughout."),

        ("Examples of Homogeneous Mixtures", "Identify examples of homogeneous mixtures.", "Medium",
         "Which of the following is a HOMOGENEOUS mixture?",
         ["Muddy water", "Shrimp paste sauce", "Vinegar", "Cendol dessert"], "C",
         "Vinegar is a homogeneous mixture with a uniform appearance. Muddy water, shrimp paste sauce, and cendol are heterogeneous."),

        ("Heterogeneous Mixtures", "Identify characteristics of heterogeneous mixtures.", "Easy",
         "Which characteristic describes a HETEROGENEOUS mixture?",
         ["The components are uniformly distributed", "The composition is NOT uniform throughout and components are visibly different", "It cannot be separated", "It is identical to a pure substance"], "B",
         "Heterogeneous mixtures have a non-uniform composition with visibly distinct parts."),

        ("Soil as Heterogeneous Mixture", "Analyze why soil is a heterogeneous mixture.", "Medium",
         "Why is soil classified as a HETEROGENEOUS mixture?",
         ["Because it contains only one type of particle", "Because one sample may contain dirt while another contains grass, rocks, or earthworms", "Because it is completely uniform throughout", "Because it dissolves in water"], "B",
         "Soil is heterogeneous because its composition varies depending on the sample taken (dirt, grass, organic matter, worms)."),

        ("Classification of Mixtures", "Classify fish sauce and ketchup.", "Medium",
         "Fish sauce, tomato ketchup, and syrup all share which mixture classification?",
         ["Heterogeneous mixtures", "Homogeneous mixtures", "Pure elements", "Igneous mixtures"], "B",
         "Fish sauce, ketchup, and syrup have a uniform appearance throughout, making them homogeneous mixtures."),

        ("Classification of Mixtures", "Classify muddy water and cendol.", "Medium",
         "Muddy water, cendol dessert, and shrimp paste sauce are classified as:",
         ["Homogeneous mixtures", "Heterogeneous mixtures", "Pure substances", "Gaseous solutions"], "B",
         "These mixtures have visibly different components and non-uniform appearance, making them heterogeneous."),

        ("Pure Substance Examples", "Identify gold and salt as pure substances.", "Easy",
         "Which pair consists of PURE SUBSTANCES?",
         ["Gold ring and pure salt", "Coffee and tea", "Salad and soup", "Milk and soda"], "A",
         "A golden ring (gold) and pure salt (sodium chloride) consist of one type of particle/compound."),

        ("Component Definition", "Define component in a mixture.", "Easy",
         "What are the 'components' of a mixture?",
         ["The individual substances or items that are mixed together", "The heat required to boil the mixture", "The chemical symbols of elements", "The container holding the liquid"], "A",
         "Components are the distinct individual materials that come together to form a mixture."),

        ("Distinguishing Homogeneous vs Pure", "Differentiate homogeneous mixture from pure substance.", "Hard",
         "Why can a homogeneous mixture be easily confused with a pure substance?",
         ["Because both have a uniform appearance", "Because both are made of rocks", "Because both settle at the bottom", "Because both cannot be dissolved"], "A",
         "Both pure substances and homogeneous mixtures look completely uniform to the naked eye."),

        ("Liquid Mixture Classification", "Classify saline solution.", "Medium",
         "Saline solution (salt dissolved in water) is classified as a:",
         ["Homogeneous mixture", "Heterogeneous mixture", "Pure element", "Sediment"], "A",
         "Saline solution is a uniform mixture of dissolved salt in water (homogeneous)."),

        # 13-24: Methods for Separating Mixtures (Pages 10-20)
        ("Separation Method: Handpicking", "Identify conditions for handpicking.", "Easy",
         "When is HANDPICKING the most suitable method to separate a mixture?",
         ["When solid particles are dissolved in water", "When unwanted solids are mixed with wanted solids and their sizes/shapes are visibly different", "When separating salt from seawater", "When separating gas from liquid"], "B",
         "Handpicking is used when components are solid, visibly distinct, and large enough to pick by hand (e.g., shells on beach, husks from rice)."),

        ("Separation Method: Winnowing", "Identify winnowing process.", "Medium",
         "What is WINNOWING used for in agriculture?",
         ["Separating chaff or husk from grain using wind/air current", "Filtering coconut debris from milk", "Attracting iron clips with a magnet", "Heating saltwater to get salt"], "A",
         "Winnowing uses air flow/wind to blow away lighter chaff/husks from heavier grains."),

        ("Separation Method: Sieving", "Identify sieving process.", "Easy",
         "What property allows particles to be separated by SIEVING?",
         ["Difference in magnetic property", "Difference in particle size using a mesh/sieve", "Difference in boiling point", "Difference in color"], "B",
         "Sieving separates solid particles of varying sizes (e.g., sieving flour or sand)."),

        ("Separation Method: Filtration", "Identify filtration process.", "Easy",
         "FILTRATION is best used to separate:",
         ["A soluble solid dissolved in a liquid", "An insoluble solid from a liquid using a porous filter paper or cloth", "Two magnetic metals", "Two gases"], "B",
         "Filtration separates insoluble solid particles (like coconut pulp or tea leaves) from a liquid using a filter."),

        ("Separation Method: Evaporation", "Identify evaporation process.", "Easy",
         "Which method is used to separate dissolved salt from seawater in salt farming?",
         ["Filtration", "Evaporation", "Magnetic separation", "Handpicking"], "B",
         "Evaporation heats the mixture until the liquid solvent turns to vapor, leaving the soluble solid (salt) behind."),

        ("Separation Method: Sedimentation", "Identify sedimentation process.", "Medium",
         "What happens during SEDIMENTATION in muddy water?",
         ["The mud evaporates into air", "Heavier solid mud particles settle to the bottom over time, leaving a clear liquid layer on top", "A magnet attracts the mud", "The mud dissolves completely"], "B",
         "Sedimentation allows dense insoluble solids in a liquid to settle at the container bottom over time."),

        ("Separation Method: Magnetic Separation", "Identify magnetic separation.", "Easy",
         "Which tool is used to separate paper clips or iron nails from sand?",
         ["A sieve", "A filter paper", "A magnet", "A magnifying glass"], "C",
         "Magnetic separation uses a magnet to attract magnetic materials (iron clips/nails) away from non-magnetic sand."),

        ("Separation Application: Coconut Milk", "Select method for filtering coconut debris.", "Easy",
         "To separate black debris from freshly squeezed coconut milk, what method should be used?",
         ["Filtration using filter cloth", "Evaporation using solar heat", "Winnowing", "Magnetic separation"], "A",
         "Filtration through cloth traps solid debris while liquid coconut milk passes through."),

        ("Separation Application: Flour & Sand", "Select method for flour refinement.", "Easy",
         "To separate large lumps from fine flour, bakers use:",
         ["Sieving", "Sedimentation", "Evaporation", "Winnowing"], "A",
         "Sieving allows fine flour particles to pass through the mesh while trapping larger lumps."),

        ("Separation Application: Rice & Husk", "Select method for rice husk removal.", "Medium",
         "Removing light husks from harvested rice grains using wind is called:",
         ["Winnowing", "Sedimentation", "Filtration", "Evaporation"], "A",
         "Winnowing separates light rice husks from heavy rice grains via wind/air current."),

        ("Separation Application: Salt Farming", "Analyze solar heat in salt farms.", "Medium",
         "In solar salt farming, how does the Sun's energy produce salt crystals?",
         ["Solar heat causes water to evaporate, leaving solid salt crystals behind", "Solar light turns salt into gas", "Solar heat filters the seawater", "Solar energy attracts salt magnetically"], "A",
         "Solar heat evaporates the water solvent, leaving pure salt crystals behind."),

        ("Separation Application: Sand & Paper Clips", "Select method for sand and iron clips.", "Easy",
         "Paper clips mixed with sand can be most quickly separated by:",
         ["Using a magnet (Magnetic Separation)", "Handpicking one by one", "Evaporation", "Winnowing"], "A",
         "Magnetic separation rapidly attracts all iron paper clips out of the sand."),

        # 25-36: Rocks, Minerals & 3 Rock Types (Pages 21-27)
        ("Geologist Definition", "Define what a geologist studies.", "Easy",
         "What is a GEOLOGIST?",
         ["A scientist who studies plants and animals", "A scientist who studies the solid, liquid, and gaseous matter of Earth and its rock processes", "A scientist who studies weather patterns", "A doctor who treats skin"], "B",
         "A geologist is a scientist who studies Earth's rocks, minerals, and geological processes."),

        ("Fossil Definition", "Define fossils and their origin.", "Easy",
         "What are FOSSILS?",
         ["Man-made plastic models of animals", "Preserved remains or traces of ancient dead plants and animals found in rocks", "Crystals formed from magma", "Volcanic ash particles"], "B",
         "Fossils are preserved remains or impressions of ancient organisms found in rock layers."),

        ("Rock Definition", "Define rock and mineral composition.", "Easy",
         "What is a ROCK?",
         ["A synthetic plastic block", "A naturally occurring solid mass or combination of minerals", "A liquid chemical solution", "A frozen gas cube"], "B",
         "A rock is a naturally occurring solid mass composed of one or more minerals."),

        ("Three Rock Types", "Identify the 3 main categories of rocks.", "Easy",
         "What are the THREE main categories of rocks on Earth?",
         ["Igneous, Sedimentary, and Metamorphic", "Hard, Soft, and Medium", "Granite, Marble, and Gold", "Volcanic, Oceanic, and Desert"], "A",
         "The three primary rock classes are Igneous, Sedimentary, and Metamorphic rocks."),

        ("Igneous Rock Formation", "Explain how igneous rocks form.", "Medium",
         "How do IGNEOUS rocks form?",
         ["From compressed plant leaves", "Through the cooling and solidification of molten magma or lava", "From ocean water evaporation", "From high pressure on marble"], "B",
         "Igneous rocks form when molten rock (magma under crust or lava on surface) cools and solidifies."),

        ("Magma vs Lava", "Distinguish magma from lava.", "Medium",
         "What is the difference between MAGMA and LAVA?",
         ["Magma is cold; lava is hot", "Magma is molten rock UNDER Earth's surface; lava is molten rock ON Earth's surface", "Magma is solid; lava is gas", "There is no difference"], "B",
         "Magma is molten rock beneath Earth's crust; lava is molten rock that erupts onto Earth's surface."),

        ("Igneous Rock Examples", "Identify intrusive igneous rocks.", "Medium",
         "Granite, quartz, feldspar, and mica are examples of:",
         ["Igneous rocks formed from slow-cooling magma inside Earth's crust", "Sedimentary rocks from mud", "Metamorphic rocks from slate", "Fossils"], "A",
         "Granite and its component minerals (quartz, feldspar, mica) form from slow-cooling intrusive magma."),

        ("Volcanic Glass: Obsidian", "Identify obsidian and pumice.", "Medium",
         "Which igneous rock is a natural volcanic glass formed by extremely rapid cooling of lava?",
         ["Obsidian", "Limestone", "Marble", "Shale"], "A",
         "Obsidian is a volcanic glass formed when lava cools so rapidly that crystals cannot form."),

        ("Sedimentary Rock Formation", "Explain sedimentary rock formation.", "Medium",
         "How do SEDIMENTARY rocks form?",
         ["From direct volcanic lava cooling", "When layers of sediment (sand, silt, mud, organic remains) compress and cement over long periods", "From extreme heat melting rock inside the mantle", "From nuclear reactions"], "B",
         "Sedimentary rocks form when layers of accumulated sediment compress and cement together over time."),

        ("Sedimentary Rock Examples", "Identify sedimentary rock examples.", "Medium",
         "Shale, sandstone, limestone, conglomerate, and gypsum are all examples of:",
         ["Sedimentary rocks", "Igneous rocks", "Metamorphic rocks", "Molten rocks"], "A",
         "Shale, sandstone, limestone, conglomerate, and gypsum are major sedimentary rock types."),

        ("Limestone Origin", "Identify limestone calcium carbonate origin.", "Hard",
         "Limestone is a sedimentary rock formed primarily from:",
         ["Cooling lava", "Materials rich in calcium carbonate, such as ancient shells and marine skeletons", "Volcanic ash", "Compressed granite"], "B",
         "Limestone forms from accumulated shells, coral, and marine debris rich in calcium carbonate."),

        ("Metamorphic Rock Formation", "Explain metamorphic rock formation.", "Hard",
         "How do METAMorphic rocks form?",
         ["When igneous or sedimentary rocks are transformed by intense heat and pressure deep within Earth's crust without melting", "From ocean water freezing", "From dust blowing in wind", "From river sediments"], "A",
         "Metamorphic rocks form when existing rocks undergo intense heat and pressure, altering their mineral structure without fully melting."),

        # 37-48: Rock Cycle & Uses of Rocks and Minerals (Pages 25-32)
        ("Metamorphic Rock Parent Rocks", "Identify parent rocks of gneiss, slate, and marble.", "Hard",
         "Which metamorphic rock forms from the parent rock GRANITE under intense heat and pressure?",
         ["Gneiss", "Slate", "Marble", "Quartzite"], "A",
         "Gneiss is a foliated metamorphic rock that forms from granite."),

        ("Metamorphic Rock Parent Rocks", "Identify parent rock of slate.", "Hard",
         "SLATE is a metamorphic rock that forms from which parent sedimentary rock?",
         ["Shale", "Limestone", "Sandstone", "Basalt"], "A",
         "Slate forms when the sedimentary rock shale is subjected to heat and pressure."),

        ("Metamorphic Rock Parent Rocks", "Identify parent rock of marble.", "Hard",
         "MARBLE is a metamorphic rock formed from the transformation of:",
         ["Limestone", "Granite", "Pumice", "Obsidian"], "A",
         "Marble forms when limestone undergoes metamorphism under heat and pressure."),

        ("Metamorphic Rock Characteristics", "Identify characteristics of metamorphic rocks.", "Medium",
         "What is a key physical characteristic of many METAMORPHIC rocks?",
         ["They are soft and crumble easily in water", "They often have visible layered/foliated bands and are harder than their parent rocks", "They contain active lava", "They float on water"], "B",
         "Metamorphic rocks are generally harder than parent rocks and frequently display layered/foliated banding."),

        ("Pumice Property", "Identify floating volcanic rock.", "Medium",
         "Which light volcanic igneous rock has a porous structure filled with air bubbles that allows it to float on water?",
         ["Pumice", "Granite", "Gneiss", "Marble"], "A",
         "Pumice contains trapped volcanic gas bubbles, making it lightweight and porous enough to float on water."),

        ("The Rock Cycle", "Define the Rock Cycle concept.", "Medium",
         "What is the ROCK CYCLE?",
         ["A bicycle made of stone", "A continuous geological process by which rocks are created, transformed, destroyed, and reformed over time", "A single eruption of a volcano", "The rotation of Earth on its axis"], "B",
         "The Rock Cycle is the continuous process connecting the creation, transformation, and recycling of igneous, sedimentary, and metamorphic rocks."),

        ("Rock Cycle Transformations", "Analyze rock cycle pathways.", "Hard",
         "If a metamorphic rock is pushed deep into the Earth and subjected to extreme heat until it melts into magma, what type of rock will form when that magma cools?",
         ["Igneous rock", "Sedimentary rock", "Metamorphic rock", "Fossil rock"], "A",
         "When melted magma cools and solidifies, it forms an igneous rock."),

        ("Rock Cycle Transformations", "Analyze weathering and erosion in rock cycle.", "Hard",
         "When igneous rocks on Earth's surface undergo weathering and erosion by wind and water, what will the resulting sediments eventually become?",
         ["Sedimentary rock", "Magma", "Lava", "Metamorphic rock"], "A",
         "Sediments produced by weathering and erosion accumulate and compress into sedimentary rock."),

        ("Rock Uses: Construction", "Identify rock uses in building & construction.", "Easy",
         "Granite, limestone, and marble are widely used in daily life as:",
         ["Food additives", "Construction materials, flooring, countertops, and building decorations", "Fuel for cars", "Clothing fibers"], "B",
         "Granite, limestone, and marble are major construction materials for buildings, tiles, and monuments."),

        ("Rock Uses: Mortar and Pestle", "Identify granite mortar and pestle.", "Easy",
         "Which hard igneous rock is commonly used to make heavy kitchen mortar and pestle sets?",
         ["Granite", "Gypsum", "Shale", "Pumice"], "A",
         "Granite's hardness and durability make it ideal for kitchen mortar and pestle sets."),

        ("Mineral Uses: Aluminum", "Identify everyday uses of aluminum.", "Easy",
         "Aluminum is a metal derived from minerals used to make:",
         ["Cans, foil, electrical wiring, and aircraft parts", "Cement blocks", "Glass bottles", "Paper towels"], "A",
         "Aluminum is lightweight and corrosion-resistant, used for cans, foil, wiring, and transportation."),

        ("Mineral Uses: Lead & Copper", "Identify copper electrical wiring and lead batteries.", "Medium",
         "COPPER is widely used for ________, while LEAD is used for ________.",
         ["electrical wiring / car batteries and wire covering", "making glass / food packaging", "clothing / shoes", "fertilizer / plastic"], "A",
         "Copper is an excellent electrical conductor (wiring); Lead is dense and corrosion-resistant (batteries/shielding)."),

        # 49-60: Advanced Phonics & Applied Science Concepts (Pages 1-32)
        ("Weathering & Erosion", "Define weathering and erosion.", "Medium",
         "What process breaks down solid rocks into smaller sediment particles at Earth's surface?",
         ["Weathering and erosion", "Volcanic melting", "Magnetic pull", "Sedimentation"], "A",
         "Weathering (chemical/physical breakdown) and erosion (transport by wind/water) reduce rocks to sediments."),

        ("Conglomerate Formation", "Identify conglomerate sedimentary rock.", "Hard",
         "Which sedimentary rock forms when rounded gravel and sand particles are cemented together by iron oxide?",
         ["Conglomerate", "Basalt", "Slate", "Obsidian"], "A",
         "Conglomerate is a sedimentary rock composed of rounded gravel and sand cemented by iron oxide or calcite."),

        ("Gypsum Formation", "Identify gypsum origin.", "Hard",
         "GYPSUM is a sedimentary rock formed when:",
         ["Ocean water rich in calcium and sulfate evaporates and deposits minerals", "Granite melts inside mantle", "Lava cools in air", "Plant roots compress"], "A",
         "Gypsum forms by chemical precipitation/evaporation of calcium and sulfate from ocean water."),

        ("Sandstone Formation", "Identify sandstone quartz composition.", "Medium",
         "Sandstone is formed primarily from compressed grains of:",
         ["Quartz sand and silt", "Volcanic glass", "Dead dinosaurs", "Clay particles only"], "A",
         "Sandstone is a clastic sedimentary rock composed mainly of quartz sand grains."),

        ("Shale Formation", "Identify shale mud/clay origin.", "Medium",
         "Which sedimentary rock is formed from compressed fine mud and clay?",
         ["Shale", "Granite", "Pumice", "Gneiss"], "A",
         "Shale forms from the compaction of fine-grained mud and clay sediments."),

        ("Water Filtration Rocks", "Identify pumice for water filtration.", "Medium",
         "Because of its porous bubble structure, pumice can be used for:",
         ["Water filtration and abrasive polishing", "Making computer microchips", "Fueling rockets", "Baking bread"], "A",
         "Pumice's porous structure makes it useful as a filtration medium and abrasive agent."),

        ("Road Base Rocks", "Identify basalt for road construction.", "Medium",
         "BASALT is a dark, dense igneous rock commonly crushed and used for:",
         ["Road base construction and railway ballast", "Jewelry rings", "Writing paper", "Cosmetics"], "A",
         "Basalt is extremely tough and dense, making it ideal for crushed road bases and railway ballast."),

        ("Fossil Preservation Environment", "Identify rock type containing fossils.", "Hard",
         "In which type of rock are FOSSILS almost exclusively found?",
         ["Sedimentary rocks", "Intrusive igneous rocks", "High-grade metamorphic rocks", "Molten magma"], "A",
         "Fossils are preserved in sedimentary rocks because the gentle deposition of sediment does not destroy organism remains (unlike molten igneous or high-heat metamorphic processes)."),

        ("Salt Farm Process", "Analyze sea salt production method.", "Medium",
         "In sea salt production, seawater is trapped in shallow coastal fields. What natural energy source drives the separation process?",
         ["Solar heat (Sunlight)", "Wind turbines", "Magnetic fields", "Chemical explosives"], "A",
         "Solar heat from sunlight supplies the energy to evaporate water and crystallize sea salt."),

        ("Shrimp Paste Sauce Mixture", "Analyze Thai food mixture classification.", "Medium",
         "Thai 'Nam Prik Kapi' (Shrimp paste sauce) contains lime juice, fish sauce, sugar, chili, and turkey berries. It is classified as:",
         ["A heterogeneous mixture because chili and berries are visibly distinct", "A homogeneous mixture", "A pure substance", "An igneous solution"], "A",
         "Shrimp paste sauce has visibly distinct components (chili flakes, berries, liquid), making it heterogeneous."),

        ("Cendol Dessert Mixture", "Analyze Cendol mixture classification.", "Medium",
         "Thai Cendol (Lod Chong) contains coconut milk, pandan noodles, palm sugar, and ice. It is a:",
         ["Heterogeneous mixture", "Homogeneous mixture", "Pure element", "Geological sediment"], "A",
         "Cendol contains visibly distinct green noodles, coconut milk, and syrup, forming a heterogeneous mixture."),

        ("Science Unit Summary", "Summarize core Grade 6 Science modules.", "Easy",
         "Which two major topics comprise the Grade 6 Science curriculum module in the textbook?",
         ["Separating Mixtures & Rocks/Minerals (including Rock Cycle)", "Plant Anatomy & Electricity only", "Space travel & Chemistry lab", "Animal classification only"], "A",
         "The curriculum covers Unit 2 (Separating Mixtures) and Unit 3 (Rocks, Minerals, and the Rock Cycle).")
    ]

    # 30 True/False Questions based on Science Gr6 -MidFinal.pdf
    tf_questions = [
        # 61-90 True/False
        ("Pure Substance Particle Count", "Recall pure substance definition.", "Easy",
         "A pure substance contains only one type of particle.", "True",
         "Pure substances (like pure water or pure gold) consist of identical particles throughout."),

        ("Mixture Definition", "Recall mixture definition.", "Easy",
         "A mixture contains two or more different substances mixed together.", "True",
         "Mixtures combine two or more distinct substances physically."),

        ("Homogeneous Uniformity", "Recall homogeneous characteristics.", "Easy",
         "A homogeneous mixture has a uniform appearance throughout.", "True",
         "Homogeneous mixtures are uniform in composition and visual appearance."),

        ("Heterogeneous Uniformity", "Recall heterogeneous characteristics.", "Easy",
         "A heterogeneous mixture has a uniform composition throughout.", "False",
         "Heterogeneous mixtures do NOT have a uniform composition; components are visibly distinct."),

        ("Soil Classification", "Recall soil mixture type.", "Medium",
         "Soil is an example of a homogeneous mixture.", "False",
         "Soil is a HETEROGENEOUS mixture because its sample composition varies (dirt, sand, organic matter)."),

        ("Vinegar Classification", "Recall vinegar mixture type.", "Easy",
         "Vinegar is an example of a homogeneous mixture.", "True",
         "Vinegar is a uniform solution of acetic acid in water."),

        ("Handpicking Condition", "Recall handpicking requirement.", "Easy",
         "Handpicking can be used when solid materials in a mixture are visibly different in size or shape.", "True",
         "Visible differences in shape/size allow items to be separated by hand."),

        ("Winnowing Function", "Recall winnowing wind function.", "Medium",
         "Winnowing uses wind to separate heavy chaff from light grain.", "False",
         "Winnowing uses wind to blow away LIGHT chaff/husks from HEAVY grains."),

        ("Sieving Requirement", "Recall sieving particle size rule.", "Easy",
         "Sieving separates solid particles of different sizes using a mesh or sieve.", "True",
         "Sieving relies on size differences relative to sieve mesh openings."),

        ("Filtration Solubility", "Recall filtration solubility requirement.", "Medium",
         "Filtration is used to separate a soluble solid that is completely dissolved in a liquid.", "False",
         "Filtration separates INSOLUBLE solids from liquid. Dissolved soluble solids require EVAPORATION."),

        ("Evaporation Process", "Recall evaporation process.", "Easy",
         "Evaporation separates a dissolved solid from a liquid by heating the mixture until the liquid turns into gas.", "True",
         "Evaporation drives off the liquid solvent as gas, leaving solid residue behind."),

        ("Sedimentation Density", "Recall sedimentation settling.", "Easy",
         "Sedimentation is the process where heavier insoluble solids settle down at the bottom of a liquid over time.", "True",
         "Gravity causes dense insoluble particles to settle to the container bottom."),

        ("Magnetic Attraction", "Recall magnetic separation rule.", "Easy",
         "A magnet can separate iron paper clips from sand because iron is a magnetic material.", "True",
         "Magnetic separation works because iron is attracted to magnets while sand is non-magnetic."),

        ("Geologist Study Scope", "Recall geologist definition.", "Easy",
         "A geologist is a scientist who studies rocks, minerals, and Earth processes.", "True",
         "Geology is the study of Earth's solid materials and geological processes."),

        ("Fossil Presence in Igneous Rock", "Recall fossil preservation environment.", "Hard",
         "Fossils are commonly found intact inside igneous rocks that formed from hot liquid magma.", "False",
         "Extreme heat of molten magma destroys plant/animal remains. Fossils are found in SEDIMENTARY rocks."),

        ("Three Rock Categories", "Recall 3 rock classes.", "Easy",
         "The three main types of rocks are igneous, sedimentary, and metamorphic rocks.", "True",
         "These are the three fundamental geological rock classes."),

        ("Igneous Magma Origin", "Recall igneous formation.", "Easy",
         "Igneous rocks form from the cooling and hardening of magma or lava.", "True",
         "Igneous rocks originate from molten rock cooling."),

        ("Magma Location", "Recall magma vs lava location.", "Easy",
         "Magma is molten rock found on top of Earth's surface.", "False",
         "Magma is molten rock UNDER Earth's surface. On the surface, it is called LAVA."),

        ("Granite Cooling Rate", "Recall granite slow cooling.", "Medium",
         "Granite forms inside Earth's crust when magma cools slowly, producing a coarse-grained texture.", "True",
         "Slow underground cooling allows large crystal grains (quartz, feldspar, mica) to grow in granite."),

        ("Obsidian Cooling Rate", "Recall obsidian rapid cooling.", "Medium",
         "Obsidian forms when lava cools so rapidly that no crystals form, resulting in natural volcanic glass.", "True",
         "Rapid surface cooling creates non-crystalline obsidian glass."),

        ("Sedimentary Compaction", "Recall sedimentary compaction.", "Easy",
         "Sedimentary rocks form when layers of sediment compress and cement together over time.", "True",
         "Compaction and cementation of accumulated sediments produce sedimentary rock."),

        ("Limestone Shell Origin", "Recall limestone origin.", "Medium",
         "Limestone is a sedimentary rock rich in calcium carbonate from ancient shells and skeletons.", "True",
         "Limestone originates from marine organism shells and calcium carbonate deposits."),

        ("Metamorphic Heat and Pressure", "Recall metamorphic formation conditions.", "Medium",
         "Metamorphic rocks are formed when existing rocks melt completely into liquid magma.", "False",
         "Metamorphic rocks undergo physical/chemical changes from heat and pressure WITHOUT melting. If they melt completely, they become magma/igneous."),

        ("Gneiss Parent Rock", "Recall gneiss parent rock.", "Hard",
         "Gneiss is a metamorphic rock formed from granite.", "True",
         "Gneiss is the metamorphic product of granite."),

        ("Slate Parent Rock", "Recall slate parent rock.", "Hard",
         "Slate is a metamorphic rock formed from shale.", "True",
         "Slate forms when the sedimentary rock shale undergoes low-grade metamorphism."),

        ("Marble Parent Rock", "Recall marble parent rock.", "Hard",
         "Marble is a metamorphic rock formed from limestone.", "True",
         "Marble forms from metamorphosed limestone."),

        ("Pumice Floating Property", "Recall pumice density.", "Medium",
         "Pumice is a porous volcanic rock that can float on water.", "True",
         "Trapped gas cavities make pumice lighter than water, allowing it to float."),

        ("The Rock Cycle Continuity", "Recall Rock Cycle continuous nature.", "Easy",
         "The Rock Cycle is a continuous process that transforms rocks from one type to another.", "True",
         "The Rock Cycle continuously recycles Earth's crustal rocks."),

        ("Granite Kitchen Use", "Recall granite mortar use.", "Easy",
         "Granite is commonly used to make heavy kitchen mortar and pestle sets because it is hard and durable.", "True",
         "Granite's hardness makes it ideal for crushing food in mortar and pestle sets."),

        ("Copper Electrical Use", "Recall copper electrical conductivity.", "Easy",
         "Copper is a metal widely used for electrical wiring in homes and appliances.", "True",
         "Copper's high electrical conductivity makes it the standard material for electrical wiring.")
    ]

    # 15 Scenario-Based Questions based on Science Gr6 -MidFinal.pdf
    scenario_questions = [
        # 91-105 Scenario-Based Questions (2 pts each)
        ("Saline Solution vs Muddy Water Scenario (Pages 5-7)", "Compare homogeneous vs heterogeneous liquid mixtures.", "Hard",
         "Student Ben has two glass beakers: Beaker A contains table salt completely dissolved in clear water (Saline Solution). Beaker B contains pond dirt stirred into water (Muddy Water).",
         "Classify both beakers as homogeneous or heterogeneous, describe their visual appearance, and state which method (Filtration or Evaporation) will recover pure salt from Beaker A.",
         "Beaker A is HOMOGENEOUS (uniform appearance). Beaker B is HETEROGENEOUS (visibly distinct particles). EVAPORATION must be used to recover pure salt from Beaker A (filtration cannot separate dissolved salt).",
         "Dissolved homogeneous solutions require evaporation; insoluble heterogeneous suspensions can be filtered or settled."),

        ("Coconut Milk Processing Scenario (Page 13 Filtration)", "Analyze filtration process in Thai cooking.", "Hard",
         "Chef Somchai is preparing coconut milk for green curry. After grating fresh coconut meat and squeezing it with warm water, he passes the mixture through a fine filter cloth to separate black shell debris from the liquid.",
         "Identify the separation method used, explain why filter cloth works, and state what remains on the cloth versus what passes into the bowl.",
         "Method: FILTRATION. The filter cloth acts as a porous barrier with tiny openings. Black shell debris and coarse pulp remain on top of the cloth (residue), while liquid white coconut milk passes through (filtrate).",
         "Porous filter traps insoluble residue while letting liquid filtrate pass through."),

        ("Solar Salt Farm Scenario (Page 13 Evaporation)", "Analyze solar evaporation in Samut Sakhon salt farms.", "Hard",
         "In Samut Sakhon province, salt farmers pump seawater into large, flat coastal fields during the dry season and leave it exposed under the blazing Sun for weeks.",
         "Describe the physical transformation occurring during solar salt farming, identify the separation method, and name the natural energy source driving the change.",
         "Method: EVAPORATION. Solar heat (heat energy from the Sun) causes liquid water to evaporate into water vapor gas, leaving solid sodium chloride (salt crystals) deposited on the field floor.",
         "Solar thermal energy evaporates liquid solvent, leaving dissolved solid solute."),

        ("Beach Sand Cleanup Scenario (Pages 12 & 14)", "Combine handpicking, sieving, and magnetic separation.", "Hard",
         "Volunteers cleaning a sandy beach find a mixture containing: (1) large plastic bottles, (2) rusty iron nails, and (3) tiny shell fragments mixed with fine sand.",
         "Design a 3-step separation plan selecting the best method for each component (Handpicking, Sieving, Magnetic Separation).",
         "Step 1: HANDPICKING to pick out large plastic bottles. Step 2: MAGNETIC SEPARATION with a magnet to attract rusty iron nails. Step 3: SIEVING with a mesh sieve to separate shell fragments from fine sand.",
         "Matches material physical properties (size, magnetism, visible appearance) to optimal separation techniques."),

        ("River Sediment to Sedimentary Rock Scenario (Pages 24-25)", "Trace sedimentary rock formation timeline.", "Hard",
         "A mountain river carries silt, sand, gravel, and organic mud down to a calm river delta. Over thousands of years, layers of these materials pile up on the seabed.",
         "Explain the multi-stage process that transforms these loose river sediments into solid sedimentary rock (such as sandstone or shale).",
         "1. Deposition: River drops sediments at delta. 2. Accumulation: Layers build up over time. 3. Compaction: Weight of upper layers squeezes out water and air. 4. Cementation: Mineral dissolved in water (like iron oxide or calcite) glues grains into solid rock.",
         "Sedimentary rock formation sequence: Weathering -> Erosion -> Deposition -> Compaction -> Cementation."),

        ("Granite to Gneiss Metamorphism Scenario (Page 25)", "Analyze metamorphic rock transformation under heat & pressure.", "Hard",
         "Deep inside Earth's crust, a body of granite rock is subjected to intense tectonic heat and crushing pressure without melting into liquid magma.",
         "Name the metamorphic rock produced by this transformation, describe its physical appearance changes, and explain why it does NOT become an igneous rock.",
         "Product: GNEISS. Appearance: Develops distinct light and dark foliated mineral bands and becomes harder than granite. It is NOT igneous because it underwent solid-state alteration without fully melting into magma.",
         "Solid-state metamorphic change under heat/pressure produces foliated gneiss from granite parent rock."),

        ("Pumice Floating Experiment Scenario (Page 26)", "Analyze density and structure of pumice vs granite.", "Hard",
         "During a science experiment, a student drops two igneous rocks of equal size into a basin of water: Rock X (Granite) sinks immediately to the bottom, while Rock Y (Pumice) floats on the surface.",
         "Explain the structural and cooling rate differences during formation that cause Rock Y to float while Rock X sinks.",
         "Rock X (Granite) formed from slow-cooling magma deep underground, creating a dense, solid crystalline structure. Rock Y (Pumice) formed from explosive lava filled with trapped gas bubbles that cooled rapidly, leaving porous air cavities that lower its density below water.",
         "Trapped volcanic gas cavities give pumice high porosity and low bulk density."),

        ("Fossil Discovery in Rock Layers Scenario (Page 26)", "Analyze why fossils are found in sedimentary rocks.", "Hard",
         "Paleontologists searching for dinosaur bones find fossils in sandstone and shale strata, but never in obsidian or basalt layers.",
         "Explain the geological reasons why fossils are preserved in sedimentary rocks but destroyed in igneous rocks.",
         "Sedimentary rocks form by gentle sediment accumulation at low temperatures, burying and preserving bone structures intact. Igneous rocks form from molten magma/lava at extreme temperatures (over 700°C) which incinerates organic remains completely.",
         "High molten temperatures of igneous rock destroy organic remains; gentle sedimentary burial preserves fossils."),

        ("Shrimp Paste & Cendol Classification Scenario (Page 7 Table)", "Analyze Thai culinary mixtures.", "Hard",
         "Look at two Thai dishes: Dish 1 is Syrup (water + sugar). Dish 2 is Cendol / Lod Chong (coconut milk + pandan noodles + palm sugar + ice).",
         "Compare the visual appearance and mixture classification of Dish 1 and Dish 2, explaining why they differ.",
         "Dish 1 (Syrup) has a uniform clear appearance, making it a HOMOGENEOUS mixture. Dish 2 (Cendol) has visibly distinct green noodles and liquid layers, making it a HETEROGENEOUS mixture.",
         "Uniform appearance = homogeneous; Visibly distinct components = heterogeneous."),

        ("Winnowing Farmers Scenario (Page 11 Winnowing)", "Analyze winnowing physical principles.", "Hard",
         "Thai rice farmers toss harvested paddy into the air on a windy afternoon. The heavy rice grains fall straight down onto a mat, while the light husks blow away to the side.",
         "Explain the physical principles of mass and air resistance that make winnowing an effective separation technique.",
         "Winnowing relies on mass and density differences under moving air currents. Heavy rice grains have greater mass/momentum and fall vertically, while light hollow husks have high surface area and low mass, allowing wind to carry them away.",
         "Air currents separate low-mass/high-surface husks from dense rice grains."),

        ("Magnet Cleanup in Scrap Yard Scenario (Page 14)", "Analyze magnetic separation in recycling.", "Hard",
         "A metal recycling yard uses a giant crane equipped with a powerful electromagnet to separate iron and steel scraps from crushed aluminum cans and plastic debris.",
         "Explain why the electromagnet attracts iron/steel but leaves aluminum cans behind, and state the advantage of using an electromagnet over a permanent magnet.",
         "Iron and steel are ferromagnetic materials attracted by magnetic fields; aluminum is non-magnetic. An electromagnet can be turned on to pick up iron and turned off to drop it into recycling bins.",
         "Ferromagnetic attraction + switchable electromagnetic control."),

        ("Sedimentation vs Filtration of Muddy Water Scenario (Pages 13-14)", "Compare sedimentation and filtration speed & clarity.", "Hard",
         "A hiking group needs clean water from a muddy stream. Option A is letting the muddy water sit in a bucket for 2 hours (Sedimentation). Option B is pouring the stream water through a portable camping filter (Filtration).",
         "Compare Option A and Option B in terms of time required, clarity of water obtained, and fine particle removal.",
         "Option A (Sedimentation) takes hours for heavy mud to settle, but fine floating particles remain suspended. Option B (Filtration) works immediately, trapping all fine suspended particles in the filter pores to produce clear water faster.",
         "Filtration provides immediate fine particle capture; sedimentation requires long settling times."),

        ("Rock Cycle Metamorphic to Igneous Pathway Scenario (Page 29 Diagram)", "Trace metamorphic rock melting pathway.", "Hard",
         "Follow a rock along the Rock Cycle: A layer of slate (metamorphic rock) is pushed deep into a subduction zone, melts into liquid magma, and later erupts onto the surface as lava.",
         "Name the new rock category formed when this lava solidifies, and name two possible rock examples (one glass-like, one porous).",
         "New category: IGNEOUS ROCK. Glass-like example: Obsidian. Porous floating example: Pumice (or Basalt for dense surface rock).",
         "Melting metamorphic rock into magma/lava produces igneous rock upon cooling."),

        ("Home Electrical & Construction Materials Scenario (Page 30 Table)", "Match daily objects to rocks and minerals.", "Hard",
         "Inspect items in a modern home: (1) Electrical wiring inside walls, (2) Granite kitchen countertops, (3) Aluminum soda cans, and (4) Marble bathroom tiles.",
         "Identify the rock or mineral source for each of the 4 items and categorize them as metallic mineral, igneous rock, or metamorphic rock.",
         "1. Electrical wiring: COPPER (metallic mineral). 2. Kitchen countertop: GRANITE (igneous rock). 3. Soda cans: ALUMINUM / Bauxite (metallic mineral). 4. Bathroom tiles: MARBLE (metamorphic rock).",
         "Direct mapping of household items to geological source materials."),

        ("Making Salt vs Making Sugar Syrup Scenario (Page 13 Evaporation)", "Analyze evaporation vs solution preparation.", "Hard",
         "In Experiment A, salt water is heated until all liquid disappears, leaving white crystals. In Experiment B, sugar is added to hot water and stirred until all crystals disappear.",
         "Identify which experiment demonstrates 'Evaporation' to separate a mixture, and explain what happened to the liquid solvent in Experiment A.",
         "Experiment A demonstrates EVAPORATION. Heating caused the liquid water solvent to absorb thermal energy, change phase into water vapor gas, and escape into the air, leaving solid salt crystals behind.",
         "Evaporation phase change drives off solvent, recovering solid solute.")
    ]

    # 10 Short Answer Questions based on Science Gr6 -MidFinal.pdf
    short_answer_questions = [
        # 106-115 Short Answer Questions (3 pts each)
        ("Homogeneous vs Heterogeneous Distinction", "Define and contrast homogeneous and heterogeneous mixtures.", "Hard",
         "Define 'Homogeneous Mixture' and 'Heterogeneous Mixture', and provide two everyday examples for each type from the Grade 6 unit.",
         "1. Homogeneous Mixture: A mixture with a uniform appearance and composition throughout (e.g., vinegar, syrup, fish sauce, saline solution). 2. Heterogeneous Mixture: A mixture with a non-uniform composition and visibly distinct parts (e.g., soil, muddy water, shrimp paste sauce, cendol).",
         "Clear definitions and two accurate examples for both mixture types."),

        ("Six Separation Methods Summary", "Summarize 6 mixture separation methods with examples.", "Hard",
         "List 4 of the 6 mixture separation methods studied (Handpicking, Winnowing, Sieving, Filtration, Evaporation, Sedimentation, Magnetic Separation), describe how each works, and give one example.",
         "1. Handpicking: Separating visibly distinct solids by hand (e.g., shells on beach). 2. Sieving: Separating solids of different sizes using mesh (e.g., flour). 3. Filtration: Separating insoluble solids from liquid using a filter (e.g., coconut milk debris). 4. Evaporation: Heating to vaporize liquid solvent and recover dissolved solid (e.g., sea salt farming). 5. Magnetic Separation: Using magnet to attract magnetic solids (e.g., iron clips from sand).",
         "Accurate descriptions and examples for at least 4 separation methods."),

        ("Solar Salt Farming Evaporation Explanation", "Explain solar heat evaporation in salt farming.", "Hard",
         "Explain how solar evaporation is used in sea salt farming to produce solid salt crystals from seawater.",
         "Seawater containing dissolved salt is pumped into shallow coastal fields. Heat energy from the Sun causes liquid water to evaporate into water vapor gas. As water disappears, dissolved salt reaches saturation and crystallizes into solid salt crystals on the ground floor.",
         "Detailed explanation of solar thermal energy, phase change of water solvent, and salt crystallization."),

        ("Three Rock Types Summary", "Describe 3 rock types and their formation processes.", "Hard",
         "Name the 3 main types of rocks (Igneous, Sedimentary, Metamorphic) and describe how each type forms.",
         "1. Igneous Rocks: Formed from the cooling and solidification of molten magma underground or lava on Earth's surface. 2. Sedimentary Rocks: Formed from the accumulation, compaction, and cementation of rock sediments, sand, and organic remains over time. 3. Metamorphic Rocks: Formed when existing rocks undergo high heat and intense pressure deep within Earth's crust without melting.",
         "Names and accurate formation descriptions for all 3 rock types."),

        ("Parent Rocks to Metamorphic Transformation", "Trace 3 parent rocks to metamorphic equivalents.", "Hard",
         "Name 3 metamorphic rocks (Gneiss, Slate, Marble) and identify the original parent rock from which each formed.",
         "1. Gneiss forms from the parent rock GRANITE. 2. Slate forms from the parent rock SHALE. 3. Marble forms from the parent rock LIMESTONE.",
         "Correct matching of 3 metamorphic rocks to their exact parent rocks."),

        ("Magma vs Lava and Intrusive vs Extrusive Igneous Rocks", "Compare magma vs lava and cooling rates.", "Hard",
         "Explain the difference between magma and lava, and compare the cooling rates and crystal textures of granite versus obsidian or pumice.",
         "Magma is molten rock inside Earth's crust; lava is molten rock on Earth's surface. Granite forms from slow-cooling magma underground, resulting in large, coarse crystal grains. Obsidian and pumice form from rapid-cooling lava on the surface, producing non-crystalline volcanic glass or porous light rock.",
         "Explains magma vs lava location, cooling rate differences, and resulting crystal textures."),

        ("The Rock Cycle Explanation", "Explain the Rock Cycle processes.", "Hard",
         "Explain what the Rock Cycle is and describe two ways a rock can transform from one category to another.",
         "Definition: The Rock Cycle is the continuous geological process where rocks are created, transformed, destroyed, and reformed over time. Transformation 1: Igneous rock undergoes weathering/erosion into sediment, which compacts into Sedimentary rock. Transformation 2: Sedimentary rock is subjected to intense heat and pressure to become Metamorphic rock.",
         "Clear definition of Rock Cycle and two valid transformation pathways."),

        ("Fossil Formation and Preservation Environment", "Explain fossil formation and sedimentary rock association.", "Hard",
         "Explain how fossils are formed and why they are almost exclusively found in sedimentary rocks rather than igneous or metamorphic rocks.",
         "Fossils form when dead plants/animals are buried quickly under layers of sediment (mud, sand, silt) which compress into rock over millions of years. They are found in sedimentary rocks because gentle sediment deposition preserves bones/shells, whereas extreme heat of igneous magma incinerates remains and intense metamorphic heat/pressure crushes them.",
         "Explains quick sediment burial and why heat/pressure of other rock types destroys organic remains."),

        ("Daily Life Applications of Rocks and Minerals", "List 4 rocks/minerals and their practical uses.", "Hard",
         "List 4 different rocks or minerals and state one specific practical use for each in our daily lives.",
         "1. Granite: Used for kitchen countertops, building construction, and mortar & pestle sets. 2. Marble: Used for decorative tiles, statues, and architecture. 3. Copper: Used for electrical wiring and appliances. 4. Aluminum: Used for soda cans, foil, and aircraft construction (or Pumice for water filtration / Basalt for road base).",
         "4 distinct rocks/minerals with accurate real-world applications."),

        ("Filtration vs Evaporation Comparison", "Contrast filtration and evaporation separation mechanisms.", "Hard",
         "Compare FILTRATION and EVAPORATION: What type of mixture does each separate, and what physical property does each rely on?",
         "1. Filtration separates INSOLUBLE solid particles from a liquid (e.g., coconut milk debris), relying on PARTICLE SIZE relative to filter pores. 2. Evaporation separates a SOLUBLE solid dissolved in a liquid (e.g., salt water), relying on DIFFERENCES IN BOILING POINT / PHASE CHANGE temperatures (liquid vaporizes, solid remains).",
         "Accurate comparison of mixture solubility types (insoluble vs soluble) and physical separation mechanisms (particle size vs boiling point/phase change).")
    ]

    # Assemble Markdown text matching template structure
    lines = []
    lines.append("# แบบทดสอบประเมินผลความรู้ Science Assessment Grade 6 In English language")
    lines.append("")
    lines.append("> **คำชี้แจง**: แบบทดสอบนี้ใช้สำหรับประเมินผลสัมฤทธิ์ทางการเรียนรู้วิทยาศาสตร์ Grade 6 (Science Gr.6 - English Edition) ครอบคลุม Unit 2 (Separating Mixtures) และ Unit 3 (Rocks, Minerals & The Rock Cycle) อ้างอิงจากแบบเรียน Science Gr6 -MidFinal.pdf ครอบคลุม 4 ส่วน จำนวนรวม 115 ข้อ คะแนนเต็ม 150 คะแนน")
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

    for filepath in ["Knowledge_Assessment_Science_En_Gr6.md", "Knowledge_Assessment_Science_Gr6.md"]:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Generated {filepath} successfully from Science EN PDF OCR content!")

if __name__ == "__main__":
    generate_sci_en_quiz_from_pdf()
