import os

def generate_math_en_quiz():
    # 60 MCQ Questions
    mcq_questions = [
        # Golden Ratio & Basics (1-10)
        ("Golden Ratio Concept", "Understand the definition and mathematical origin of the Golden Ratio.", "Easy",
         "What is the mathematical symbol and approximate decimal value of the Golden Ratio?",
         ["$\Pi \approx 3.141$", "$\Phi \approx 1.618$", "$\Delta \approx 2.718$", "$\Theta \approx 1.414$"], "B",
         "The Golden Ratio is represented by the Greek letter Phi ($\Phi$) and is approximately equal to 1.618."),

        ("Golden Ratio Line Division", "Identify line segment ratio properties forming the Golden Ratio.", "Medium",
         "If a line segment of length $L$ is divided into a long part $a$ and a short part $b$, which equation defines the Golden Ratio $\Phi$?",
         ["$\\frac{a+b}{a} = \\frac{a}{b} = \\Phi$", "$\\frac{a}{b} = \\frac{b}{a+b} = \\Phi$", "$\\frac{a-b}{a} = \\frac{a}{b} = \\Phi$", "$\\frac{a+b}{b} = \\frac{b}{a} = \\Phi$"], "A",
         "By definition, the Golden Ratio occurs when the ratio of the whole length ($a+b$) to the long part ($a$) equals the ratio of the long part ($a$) to the short part ($b$)."),

        ("Golden Ratio Applications", "Recognize real-world occurrences of the Golden Ratio.", "Easy",
         "In which of the following fields is the Golden Ratio widely applied for visual harmony and proportion?",
         ["Architecture and Fine Art", "Subatomic Particle Physics", "Computer Operating Systems", "Chemical Element Periodicity"], "A",
         "Centuries of artists, architects, and designers have used the Golden Ratio ($\Phi \approx 1.618$) to create aesthetic balance."),

        ("Fraction to Decimal Conversion", "Convert fractions with denominator 100 to decimals.", "Easy",
         "What is the decimal equivalent of the fraction $\\frac{65}{100}$?",
         ["0.065", "0.65", "6.5", "65.0"], "B",
         "Dividing 65 by 100 shifts the decimal point two places to the left, yielding 0.65."),

        ("Decimal to Percentage Conversion", "Convert decimal numbers to percentages.", "Easy",
         "Convert $0.08$ into a percentage.",
         ["0.8%", "8%", "80%", "800%"], "B",
         "To express a decimal as a percentage, multiply by 100: $0.08 \\times 100\\% = 8\\%$."),

        ("Percentage to Fraction in Simplest Form", "Convert percentages into simplified fractions.", "Medium",
         "Express $75\\%$ as a fraction in its simplest form.",
         ["$\\frac{3}{4}$", "$\\frac{7}{5}$", "$\\frac{75}{10}$", "$\\frac{15}{20}$"], "A",
         "$75\\% = \\frac{75}{100}$. Dividing both numerator and denominator by 25 yields $\\frac{3}{4}$."),

        ("Percentage Representation", "Interpret visual grid models for percentages.", "Easy",
         "If a grid contains 100 equal squares and 42 of them are shaded blue, what percentage of the grid is shaded?",
         ["4.2%", "24%", "42%", "58%"], "C",
         "The shaded fraction is $\\frac{42}{100}$, which equals $42\\%$."),

        ("Unshaded Percentage", "Calculate the unshaded complement percentage.", "Easy",
         "If $35\\%$ of a square model is shaded green, what percentage remains unshaded?",
         ["35%", "55%", "65%", "75%"], "C",
         "The total area is $100\\%$. Unshaded percentage $= 100\\% - 35\\% = 65\\%$."),

        ("Ratio Definition", "Understand basic ratio terminology and notation.", "Easy",
         "How is the ratio of quantity $A$ to quantity $B$ expressed using standard ratio notation?",
         ["$A + B$", "$A : B$", "$A \\times B$", "$A - B$"], "B",
         "A ratio comparing quantity $A$ to quantity $B$ is written as $A : B$ or $\\frac{A}{B}$."),

        ("Equivalent Ratios Identification", "Determine equivalent ratios by multiplication or division.", "Medium",
         "Which ratio is equivalent to $4 : 7$?",
         ["$8 : 14$", "$12 : 18$", "$16 : 21$", "$4 : 14$"], "A",
         "Multiplying both terms of $4 : 7$ by 2 gives $(4 \\times 2) : (7 \\times 2) = 8 : 14$."),

        # Ratios, Simplest Forms, and Units (11-25)
        ("Simplest Form of Ratio", "Simplify ratios by dividing terms by their greatest common factor.", "Medium",
         "What is the simplest form of the ratio $24 : 36$?",
         ["$12 : 18$", "$6 : 9$", "$2 : 3$", "$4 : 6$"], "C",
         "The greatest common factor (GCF) of 24 and 36 is 12. Dividing both terms by 12 gives $2 : 3$."),

        ("Ratios with Same Units", "Write ratios comparing quantities measured in identical units.", "Easy",
         "Express the ratio of 15 kg of apples to 25 kg of oranges in simplest form.",
         ["$3 \\text{ kg} : 5 \\text{ kg}$", "$3 : 5$", "$5 : 3$", "$15 : 25$"], "B",
         "When quantities share the exact same unit (kg), units are omitted in the final ratio notation. $15 : 25 = 3 : 5$."),

        ("Ratios with Different Units", "Write ratios comparing quantities measured in different units.", "Medium",
         "How should the ratio of 6 books to 12 students be properly written?",
         ["$1 : 2$", "$1 \\text{ book} : 2 \\text{ students}$", "$6 : 12 \\text{ students}$", "$2 \\text{ students} : 1 \\text{ book}$"], "B",
         "When quantities have different units, the unit names must be explicitly specified alongside the simplified numbers: $1 \\text{ book} : 2 \\text{ students}$."),

        ("Non-Equivalent Ratios", "Identify ratios that are NOT equivalent.", "Medium",
         "Which of the following pair of ratios is NON-EQUIVALENT?",
         ["$3 : 5$ and $9 : 15$", "$2 : 9$ and $6 : 27$", "$5 : 8$ and $15 : 20$", "$7 : 10$ and $21 : 30$"], "C",
         "$5 : 8 = \\frac{5}{8} = 0.625$, while $15 : 20 = \\frac{3}{4} = 0.75$. They are non-equivalent."),

        ("Ratio Scaling Up", "Scale up ratios to solve proportional problems.", "Medium",
         "If the ratio of sugar to flour in a recipe is $2 : 5$, how many cups of flour are needed for 6 cups of sugar?",
         ["10 cups", "12 cups", "15 cups", "20 cups"], "C",
         "Scale factor $= 6 \\div 2 = 3$. Flour needed $= 5 \\times 3 = 15$ cups."),

        ("Ratio Scaling Down", "Scale down ratios to find unit amounts.", "Medium",
         "A map scale is $1 \\text{ cm} : 50 \\text{ km}$. If two cities are 300 km apart in reality, how far apart are they on the map?",
         ["5 cm", "6 cm", "10 cm", "12 cm"], "B",
         "Map distance $= 300 \\div 50 = 6$ cm."),

        ("Three-Quantity Ratios", "Express and simplify three-part ratios.", "Medium",
         "Simplify the three-part ratio $10 : 15 : 25$.",
         ["$2 : 3 : 5$", "$1 : 2 : 3$", "$5 : 10 : 15$", "$4 : 6 : 10$"], "A",
         "Dividing all three terms by 5 gives $(10/5) : (15/5) : (25/5) = 2 : 3 : 5$."),

        ("Finding Total Parts in Ratios", "Calculate total parts to divide a whole quantity.", "Easy",
         "A ribbon of length 80 cm is cut into two pieces in the ratio $3 : 5$. What is the total number of ratio parts?",
         ["3 parts", "5 parts", "8 parts", "15 parts"], "C",
         "Total ratio parts $= 3 + 5 = 8$ parts."),

        ("Dividing Quantity by Ratio", "Calculate the size of one portion given a ratio.", "Medium",
         "Divide 120 THB between Mark and Anna in the ratio $1 : 3$. How much money does Anna receive?",
         ["30 THB", "60 THB", "90 THB", "100 THB"], "C",
         "Total parts $= 1 + 3 = 4$. Each part $= 120 / 4 = 30$ THB. Anna gets 3 parts $= 3 \\times 30 = 90$ THB."),

        ("Finding Difference in Ratio Shares", "Calculate the difference between shares in a ratio.", "Hard",
         "The ratio of male to female employees in an office is $4 : 7$. If there are 35 female employees, how many more female employees are there than male employees?",
         ["15", "20", "25", "30"], "A",
         "Female parts $= 7 = 35 \\rightarrow 1 \\text{ part} = 5$. Male employees $= 4 \\times 5 = 20$. Difference $= 35 - 20 = 15$."),

        ("Percentage of a Quantity - Basic", "Calculate a basic percentage of a given number.", "Easy",
         "What is $20\\%$ of 250 THB?",
         ["25 THB", "50 THB", "75 THB", "100 THB"], "B",
         "$20\\% \\times 250 = 0.20 \\times 250 = 50$ THB."),

        ("Percentage of a Quantity - Intermediate", "Calculate fractional percentages of large amounts.", "Medium",
         "Find $45\\%$ of 800 meters.",
         ["320 m", "360 m", "400 m", "440 m"], "B",
         "$45\\% \\times 800 = \\frac{45}{100} \\times 800 = 45 \\times 8 = 360$ meters."),

        ("Finding Part-to-Whole Percentage", "Express a subset as a percentage of the whole group.", "Medium",
         "Out of 50 students in a class, 12 students wear glasses. What percentage of the class wears glasses?",
         ["12%", "24%", "36%", "48%"], "B",
         "Percentage $= \\frac{12}{50} \\times 100\\% = 24\\%$."),

        ("Complementary Percentage Calculation", "Determine remaining percentage in real-world contexts.", "Medium",
         "A fruit basket has 40 fruits. If 30% are apples and 20% are oranges, what percentage are bananas?",
         ["30%", "40%", "50%", "60%"], "C",
         "Bananas percentage $= 100\\% - (30\\% + 20\\%) = 50\\%$."),

        ("Percentage Increase Concept", "Identify the formula for percentage increase.", "Medium",
         "Which formula correctly calculates percentage increase?",
         ["$\\frac{\\text{Original Amount}}{\\text{New Amount}} \\times 100\\%$", "$\\frac{\\text{Amount of Increase}}{\\text{Original Amount}} \\times 100\\%$", "$\\frac{\\text{Amount of Increase}}{\\text{New Amount}} \\times 100\\%$", "$\\frac{\\text{New Amount - Original Amount}}{\\text{New Amount}} \\times 100\\%$"], "B",
         "Percentage increase $= \\frac{\\text{Amount of Increase}}{\\text{Original Amount}} \\times 100\\%$."),

        # Commercial Math: Profit, Loss, Discount (26-45)
        ("Cost Price and Selling Price Definitions", "Define basic commercial terms.", "Easy",
         "If a shopkeeper buys a shirt for 200 THB and sells it for 260 THB, what is the Cost Price (CP)?",
         ["60 THB", "200 THB", "260 THB", "460 THB"], "B",
         "Cost Price (CP) is the original price paid to acquire the item, which is 200 THB."),

        ("Profit Calculation", "Determine total profit in monetary terms.", "Easy",
         "A vendor buys a bag for 500 THB and sells it for 650 THB. What is the vendor's profit?",
         ["100 THB", "150 THB", "200 THB", "250 THB"], "B",
         "Profit $= \\text{Selling Price} - \\text{Cost Price} = 650 - 500 = 150$ THB."),

        ("Loss Calculation", "Determine total monetary loss.", "Easy",
         "A bicycle bought for 3,000 THB is resold for 2,400 THB. What is the loss amount?",
         ["400 THB", "500 THB", "600 THB", "700 THB"], "C",
         "Loss $= \\text{Cost Price} - \\text{Selling Price} = 3000 - 2400 = 600$ THB."),

        ("Profit Percentage Formula", "Calculate profit percentage relative to cost price.", "Medium",
         "What is the profit percentage if an item costing 400 THB is sold for 500 THB?",
         ["20%", "25%", "30%", "33.3%"], "B",
         "Profit $= 100$ THB. Profit $\% = \\frac{100}{400} \\times 100\\% = 25\\%$."),

        ("Loss Percentage Formula", "Calculate loss percentage relative to cost price.", "Medium",
         "An electronic gadget costing 1,000 THB is sold for 800 THB. What is the loss percentage?",
         ["15%", "18%", "20%", "25%"], "C",
         "Loss $= 200$ THB. Loss $\% = \\frac{200}{1000} \\times 100\\% = 20\\%$."),

        ("Calculating SP from Cost Price and Profit %", "Find selling price given profit percentage.", "Medium",
         "A book costs 150 THB to produce. If the publisher sells it at a $20\\%$ profit, what is the selling price?",
         ["170 THB", "180 THB", "190 THB", "200 THB"], "B",
         "Selling Price $= 150 \\times (1 + 0.20) = 150 \\times 1.20 = 180$ THB."),

        ("Calculating SP from Cost Price and Loss %", "Find selling price given loss percentage.", "Medium",
         "A merchant sells shoes that cost 800 THB at a loss of $15\\%$. What is the selling price?",
         ["640 THB", "680 THB", "700 THB", "720 THB"], "B",
         "Selling Price $= 800 \\times (1 - 0.15) = 800 \\times 0.85 = 680$ THB."),

        ("Marked Price Definition", "Understand marked price (list price) concept.", "Easy",
         "The price printed on a product tag before any price reduction is called the:",
         ["Cost Price", "Selling Price", "Marked Price", "Discount Price"], "C",
         "The Marked Price (or List Price) is the advertised tag price before applying discounts."),

        ("Discount Amount Calculation", "Calculate discount amount from marked price.", "Easy",
         "A coat has a marked price of 1,200 THB. If the store gives a $25\\%$ discount, what is the discount amount?",
         ["250 THB", "300 THB", "350 THB", "400 THB"], "B",
         "Discount Amount $= 1200 \\times 0.25 = 300$ THB."),

        ("Selling Price After Discount", "Calculate final price paid after discount.", "Medium",
         "What is the final selling price of a watch marked at 2,000 THB with a $30\\%$ discount?",
         ["1,400 THB", "1,500 THB", "1,600 THB", "1,700 THB"], "A",
         "Selling Price $= 2000 \\times (1 - 0.30) = 2000 \\times 0.70 = 1400$ THB."),

        ("Discount Percentage Formula", "Calculate discount percentage from MP and SP.", "Medium",
         "A toy with a marked price of 500 THB is sold for 400 THB. What is the discount percentage?",
         ["10%", "15%", "20%", "25%"], "C",
         "Discount $= 500 - 400 = 100$ THB. Discount $\% = \\frac{100}{500} \\times 100\\% = 20\\%$."),

        ("Finding CP from SP and Profit %", "Work backwards to find cost price from selling price.", "Hard",
         "A laptop is sold for 18,000 THB, yielding a $20\\%$ profit for the store. What was the cost price of the laptop?",
         ["14,400 THB", "15,000 THB", "16,000 THB", "16,500 THB"], "B",
         "Cost Price $= \\frac{\\text{Selling Price}}{1 + \\text{Profit}\\%} = \\frac{18000}{1.20} = 15,000$ THB."),

        ("Finding MP from SP and Discount %", "Calculate original marked price given discount price.", "Hard",
         "After receiving a $10\\%$ discount, Sarah paid 900 THB for a jacket. What was the original marked price?",
         ["990 THB", "1,000 THB", "1,050 THB", "1,100 THB"], "B",
         "Marked Price $= \\frac{\\text{Selling Price}}{1 - \\text{Discount}\\%} = \\frac{900}{0.90} = 1,000$ THB."),

        ("Successive Discounts Concept", "Understand how two consecutive percentage discounts work.", "Hard",
         "A item marked at 1,000 THB gets a $10\\%$ discount, followed by another $10\\%$ discount on the reduced price. What is the final price?",
         ["800 THB", "810 THB", "820 THB", "850 THB"], "B",
         "First reduction $= 1000 \\times 0.90 = 900$ THB. Second reduction $= 900 \\times 0.90 = 810$ THB."),

        ("Value Added Tax (VAT) Calculation", "Compute total price including 7% VAT.", "Medium",
         "A dinner bill at a restaurant costs 1,000 THB before tax. If a $7\\%$ VAT is added, what is the total bill?",
         ["1,050 THB", "1,070 THB", "1,100 THB", "1,700 THB"], "B",
         "Total Bill $= 1000 \\times 1.07 = 1,070$ THB."),

        # Simple Interest & Financial Math (46-60)
        ("Simple Interest Variables", "Identify principal, rate, and time in simple interest formula.", "Easy",
         "In the simple interest formula $I = P \\times R \\times T$, what does the letter $P$ stand for?",
         ["Percentage", "Profit", "Principal", "Payment"], "C",
         "$P$ stands for Principal, which is the initial sum of money invested or borrowed."),

        ("Simple Interest Formula Identification", "Recall the standard simple interest formula.", "Easy",
         "Which formula correctly calculates Simple Interest ($I$)?",
         ["$I = P + R + T$", "$I = P \\times R \\times T$", "$I = \\frac{P \\times T}{R}$", "$I = P \\times (1 + R)^T$"], "B",
         "Simple Interest is calculated using $I = P \\times R \\times T$."),

        ("Calculating Annual Simple Interest", "Compute interest earned for 1 year.", "Easy",
         "Calculate the simple interest on a principal of 10,000 THB at an annual interest rate of $5\\%$ for 1 year.",
         ["50 THB", "500 THB", "1,000 THB", "5,000 THB"], "B",
         "$I = 10000 \\times 0.05 \\times 1 = 500$ THB."),

        ("Calculating Multi-Year Simple Interest", "Compute interest earned over several years.", "Medium",
         "How much simple interest accumulates on 20,000 THB invested at $4\\%$ per annum for 3 years?",
         ["800 THB", "1,600 THB", "2,400 THB", "3,200 THB"], "C",
         "$I = 20000 \\times 0.04 \\times 3 = 2,400$ THB."),

        ("Total Amount Formula", "Compute total accumulated balance.", "Easy",
         "What is the total amount ($A$) accumulated when Principal ($P$) and Simple Interest ($I$) are combined?",
         ["$A = P \\times I$", "$A = P - I$", "$A = P + I$", "$A = \\frac{P}{I}$"], "C",
         "The total accumulated balance is the sum of the principal and interest: $A = P + I$."),

        ("Accumulated Balance Calculation", "Find total balance after interest.", "Medium",
         "If 50,000 THB is deposited into a bank account paying $2\\%$ annual simple interest, what is the total balance after 2 years?",
         ["51,000 THB", "52,000 THB", "53,000 THB", "54,000 THB"], "B",
         "Interest $= 50000 \\times 0.02 \\times 2 = 2,000$ THB. Total Balance $= 50000 + 2000 = 52,000$ THB."),

        ("Interest Rate Conversion", "Convert percentage interest rate to decimal for calculation.", "Easy",
         "When substituting an annual interest rate of $3.5\\%$ into $I = P \\times R \\times T$, what value of $R$ should be used?",
         ["3.5", "0.35", "0.035", "0.0035"], "C",
         "$R = 3.5\\% = \\frac{3.5}{100} = 0.035$."),

        ("Calculating Time in Months", "Convert months into years for simple interest formula.", "Medium",
         "If money is borrowed for 6 months, what fractional value of $T$ (years) must be substituted into $I = P \\times R \\times T$?",
         ["0.2 years", "0.5 years", "0.6 years", "6 years"], "B",
         "$T = \\frac{6 \\text{ months}}{12 \\text{ months}} = 0.5$ years."),

        ("Short-Term Interest Calculation", "Compute interest for a fraction of a year.", "Hard",
         "Calculate the interest on 40,000 THB at $6\\%$ per annum for 6 months.",
         ["1,200 THB", "1,800 THB", "2,400 THB", "4,800 THB"], "A",
         "$I = 40000 \\times 0.06 \\times 0.5 = 1,200$ THB."),

        ("Bank Loan Total Repayment", "Calculate total amount repaid on a bank loan.", "Medium",
         "A farmer borrows 100,000 THB from a bank at $5\\%$ annual simple interest. If he repays the entire loan in 2 years, how much does he pay back in total?",
         ["105,000 THB", "110,000 THB", "115,000 THB", "120,000 THB"], "B",
         "Interest $= 100000 \\times 0.05 \\times 2 = 10,000$ THB. Total Repayment $= 100000 + 10000 = 110,000$ THB."),

        ("Finding Principal from Interest", "Solve for principal given interest, rate, and time.", "Hard",
         "What principal amount will earn 600 THB in simple interest at $3\\%$ per annum over 2 years?",
         ["8,000 THB", "10,000 THB", "12,000 THB", "15,000 THB"], "B",
         "$P = \\frac{I}{R \\times T} = \\frac{600}{0.03 \\times 2} = \\frac{600}{0.06} = 10,000$ THB."),

        ("Finding Interest Rate", "Determine annual interest rate given $I$, $P$, and $T$.", "Hard",
         "An investment of 15,000 THB generates 1,800 THB of interest over 2 years. What is the annual simple interest rate?",
         ["4%", "5%", "6%", "8%"], "C",
         "$R = \\frac{I}{P \\times T} = \\frac{1800}{15000 \\times 2} = \\frac{1800}{30000} = 0.06 = 6\\%$."),

        ("Financial Comparison", "Compare two savings options based on simple interest.", "Hard",
         "Bank A offers $4\\%$ interest for 2 years on 10,000 THB. Bank B offers $3\\%$ interest for 3 years on 10,000 THB. Which bank yields more total interest?",
         ["Bank A yields 100 THB more interest than Bank B.", "Bank B yields 100 THB more interest than Bank A.", "Both banks yield equal interest.", "Bank A yields 200 THB more interest than Bank B."], "B",
         "Bank A Interest $= 10000 \\times 0.04 \\times 2 = 800$ THB. Bank B Interest $= 10000 \\times 0.03 \\times 3 = 900$ THB. Bank B yields $900 - 800 = 100$ THB more."),

        ("Multi-step Financial Profit Problem", "Combine commercial discount and interest.", "Hard",
         "A seller buys a TV for 10,000 THB, marks it up by $30\\%$, and then offers a $10\\%$ discount. What is the seller's final profit?",
         ["1,700 THB", "1,800 THB", "2,000 THB", "2,700 THB"], "A",
         "Marked Price $= 10000 \\times 1.30 = 13,000$ THB. Selling Price $= 13000 \\times 0.90 = 11,700$ THB. Profit $= 11,700 - 10,000 = 1,700$ THB."),

        ("Comprehensive Ratio & Percentage Problem", "Solve multi-step ratio and percentage distribution.", "Hard",
         "In a school of 600 students, the ratio of boys to girls is $2 : 3$. If $20\\%$ of the boys join the math club, how many boys are in the math club?",
         ["48 boys", "54 boys", "60 boys", "72 boys"], "A",
         "Total parts $= 2 + 3 = 5$. Boys $= \\frac{2}{5} \\times 600 = 240$. Boys in math club $= 240 \\times 0.20 = 48$ boys."),

        ("Multi-Step Percentage Discount & Tax", "Compute price after consecutive discount and tax.", "Hard",
         "An item marked at 5,000 THB is given a $20\\%$ discount. A $7\\%$ VAT is then added to the discounted price. What is the final price paid?",
         ["4,000 THB", "4,280 THB", "4,350 THB", "5,000 THB"], "B",
         "Discounted price $= 5000 \\times 0.80 = 4,000$ THB. With $7\\%$ VAT $= 4000 \\times 1.07 = 4,280$ THB."),

        ("Simple Interest Time in Days", "Calculate interest for a fraction of a year given in days.", "Hard",
         "If 73,000 THB is deposited at $5\\%$ annual simple interest for 73 days (using a 365-day year), how much interest is earned?",
         ["365 THB", "730 THB", "1,460 THB", "3,650 THB"], "B",
         "Time $T = \\frac{73}{365} = 0.2$ years. Interest $= 73000 \\times 0.05 \\times 0.2 = 730$ THB."),

        ("Three-Part Ratio Allocation", "Divide a total amount into a three-part ratio.", "Medium",
         "A sum of 900 THB is split among A, B, and C in the ratio $2 : 3 : 4$. How much does B receive?",
         ["200 THB", "300 THB", "400 THB", "450 THB"], "B",
         "Total parts $= 2 + 3 + 4 = 9$. One part $= 900 / 9 = 100$ THB. B gets 3 parts $= 3 \\times 100 = 300$ THB."),

        ("Finding Original Price before Percentage Increase", "Determine initial value given percentage increase.", "Hard",
         "A salary increased by $10\\%$ to become 22,000 THB. What was the original salary?",
         ["19,800 THB", "20,000 THB", "20,500 THB", "21,000 THB"], "B",
         "Original salary $= 22000 / 1.10 = 20,000$ THB."),

        ("Map Scale Linear Distance", "Calculate actual linear distance from map scale.", "Medium",
         "On a map with a scale of $1 : 100,000$, two towns are 4.5 cm apart. What is the actual distance between the two towns in kilometers?",
         ["4.5 km", "45 km", "450 km", "0.45 km"], "A",
         "Actual distance $= 4.5 \\text{ cm} \\times 100,000 = 450,000 \\text{ cm} = 4,500 \\text{ m} = 4.5$ km.")
    ]

    # 30 True/False Questions
    tf_questions = [
        ("Golden Ratio Irrationality", "Verify mathematical classification of Phi.", "Easy",
         "The Golden Ratio ($\Phi \\approx 1.618$) is mathematically classified as an irrational number.", "True",
         "The Golden Ratio cannot be expressed as a simple fraction of two integers, making it an irrational number with non-repeating infinite decimals."),

        ("Golden Ratio Visual Aesthetic", "Understand visual proportion principles.", "Easy",
         "Designers and architects use the Golden Ratio because shapes proportioned according to $\Phi$ are naturally pleasing to the human eye.", "True",
         "For centuries, Golden Ratio proportions have been recognized in art and design for creating natural visual harmony."),

        ("Percentage Base Definition", "Identify the standard baseline for percentages.", "Easy",
         "A percentage is a ratio that compares a number to 10.", "False",
         "By definition, a percentage is a fraction or ratio expressed with a denominator of 100 (per cent = per hundred)."),

        ("Decimal to Percentage Multiplier", "Check correct conversion factor.", "Easy",
         "To convert any decimal number to a percentage, you must divide the decimal by 100.", "False",
         "To convert a decimal to a percentage, you must MULTIPLY by 100 (e.g., $0.45 \\times 100\\% = 45\\%$)."),

        ("Fraction Decimal Equivalence", "Check numerical equivalence between fraction and decimal.", "Easy",
         "The fraction $\\frac{3}{5}$ is equal to $0.60$ or $60\\%$.", "True",
         "$\\frac{3}{5} = \\frac{60}{100} = 0.60 = 60\\%$."),

        ("Simplest Form Ratio Rule", "Verify condition for simplified ratios.", "Medium",
         "A ratio $a : b$ is in its simplest form when the greatest common factor of $a$ and $b$ is 1.", "True",
         "When terms share no common factor other than 1, the ratio cannot be reduced further and is in simplest form."),

        ("Ratio Order Importance", "Verify order dependency in ratios.", "Easy",
         "The ratio $2 : 5$ expresses the exact same comparison as the ratio $5 : 2$.", "False",
         "Ratios are order-dependent. $2 : 5$ means 2 parts of A for every 5 parts of B, which is different from $5 : 2$."),

        ("Ratio Unit Omission Rule", "Verify unit notation rules for identical units.", "Medium",
         "When writing the ratio of two quantities with the same units of measurement, the units should be omitted in the final ratio.", "True",
         "Because the units cancel out when comparing quantities of the same dimension, units are omitted (e.g. 5 m to 10 m is $1 : 2$)."),

        ("Different Units Ratio Rule", "Verify unit notation rules for different units.", "Medium",
         "When comparing 4 pencils to 8 notebooks, it is correct to write the simplified ratio as simply $1 : 2$ without any unit names.", "False",
         "When quantities have different units, the unit labels MUST be included: $1 \\text{ pencil} : 2 \\text{ notebooks}$."),

        ("Equivalent Ratio Multiplication", "Verify scaling property of ratios.", "Easy",
         "Multiplying both terms of a ratio by the same non-zero number produces an equivalent ratio.", "True",
         "Multiplying or dividing both antecedent and consequent by the same non-zero number preserves their proportional value."),

        ("Cost Price Definition", "Check definition of cost price.", "Easy",
         "The Cost Price (CP) is the price at which an item is sold to a customer.", "False",
         "The Cost Price is the cost incurred by the seller to acquire or produce the item. The price sold to a customer is the Selling Price (SP)."),

        ("Profit Condition", "Identify conditions yielding profit.", "Easy",
         "A business makes a profit whenever the Selling Price is greater than the Cost Price ($\\text{SP} > \\text{CP}$).", "True",
         "Profit occurs when revenue exceeds cost ($\\text{Profit} = \\text{SP} - \\text{CP} > 0$)."),

        ("Loss Condition", "Identify conditions yielding financial loss.", "Easy",
         "A financial loss occurs when the Cost Price exceeds the Selling Price ($\\text{CP} > \\text{SP}$).", "True",
         "When an item is sold for less than its acquisition cost, a loss is incurred ($\\text{Loss} = \\text{CP} - \\text{SP}$)."),

        ("Profit Percentage Base", "Verify baseline value for profit percentage calculation.", "Medium",
         "Profit percentage is always calculated based on the Selling Price of the product.", "False",
         "Profit percentage is calculated based on the COST PRICE (CP), using $\\text{Profit}\\% = \\frac{\\text{Profit}}{\\text{CP}} \\times 100\\%$."),

        ("Discount Application Base", "Verify baseline value for discount calculation.", "Medium",
         "A discount is calculated as a percentage of the Marked Price (List Price).", "True",
         "Discounts are reductions applied to the tag price or Marked Price (MP)."),

        ("Discount Reduction Effect", "Understand effect of discount on price.", "Easy",
         "Applying a discount reduces the final selling price below the marked price.", "True",
         "Discount $= \\text{Marked Price} - \\text{Selling Price}$, so SP is always lower than MP when discount $> 0$."),

        ("Successive Discount Addition Fallacy", "Identify common misconception about successive discounts.", "Hard",
         "Two consecutive discounts of $10\\%$ and $10\\%$ are equivalent to a single single discount of $20\\%$.", "False",
         "Consecutive discounts are applied sequentially. Two $10\\%$ discounts result in a total reduction of $19\\%$ ($0.90 \\times 0.90 = 0.81$), not $20\\%$."),

        ("Simple Interest Linear Nature", "Verify constant annual interest property.", "Medium",
         "In simple interest, the amount of interest earned each year remains constant throughout the investment period.", "True",
         "Simple interest is calculated only on the original principal every period, so the yearly interest amount is constant."),

        ("Principal Definition", "Verify definition of principal.", "Easy",
         "The Principal ($P$) is the total interest accumulated at the end of a bank loan term.", "False",
         "The Principal is the initial amount of money deposited or borrowed, not the interest earned."),

        ("Interest Rate Time Period", "Verify annual basis of interest rates.", "Easy",
         "Unless specified otherwise, interest rates in financial problems are quoted per annum (per year).", "True",
         "Standard financial rates are annual rates ($R\\%$ p.a.)."),

        ("Simple Interest Time Variable Unit", "Verify unit of time in simple interest formula.", "Medium",
         "In the formula $I = P \\times R \\times T$, time ($T$) must always be expressed in years.", "True",
         "When $R$ is an annual interest rate, $T$ must be converted into years (e.g. 6 months $= 0.5$ years)."),

        ("Total Accumulated Amount Formula", "Check formula for total accumulated balance.", "Easy",
         "The total balance $A$ in a savings account after earning simple interest is given by $A = P + I$.", "True",
         "Total Accumulated Amount equals the initial Principal plus total Simple Interest ($A = P + I$)."),

        ("Zero Interest Scenario", "Analyze zero rate condition.", "Easy",
         "If the annual interest rate is $0\\%$, the accumulated balance after 5 years equals the original principal.", "True",
         "With $R = 0\\%$, $I = 0$, so $A = P + 0 = P$."),

        ("Percentage Greater Than 100%", "Understand percentages exceeding 100%.", "Medium",
         "A percentage value can exceed $100\\%$ when an amount more than doubles or increases significantly.", "True",
         "Percentages above $100\\%$ represent values greater than the original baseline whole (e.g., $250\\%$ of 10 is 25)."),

        ("Map Scale Comparison", "Evaluate map ratio scale representation.", "Medium",
         "A map scale of $1 : 10,000$ means that 1 cm on the map represents 100 meters in real life.", "True",
         "$10,000 \\text{ cm} = 100 \\text{ meters}$, so 1 cm on map $= 100$ meters in reality."),

        ("Ratio Comparison via Cross-Multiplication", "Verify cross-multiplication technique for ratio equivalence.", "Medium",
         "To check if two ratios $\\frac{a}{b}$ and $\\frac{c}{d}$ are equivalent, one can check if $a \\times d = b \\times c$.", "True",
         "Cross-multiplication ($a \\cdot d = b \\cdot c$) is a valid algebraic test for proportional equivalence."),

        ("Markup Definition", "Define commercial markup.", "Medium",
         "Markup is the amount added to the cost price of goods to cover overhead and provide profit.", "True",
         "Markup $= \\text{Selling Price} - \\text{Cost Price}$ before selling."),

        ("Value Added Tax Addition", "Understand VAT addition to net price.", "Easy",
         "Value Added Tax (VAT) increases the total purchase price paid by the end consumer.", "True",
         "VAT is an indirect consumption tax added on top of the net sales price."),

        ("Simple Interest vs Compound Interest", "Distinguish simple interest from compounding.", "Hard",
         "Simple interest calculates interest on both the principal and previously earned interest.", "False",
         "Simple interest calculates interest ONLY on the principal. Calculating interest on interest is called Compound Interest."),

        ("Ratio Scaling Invariance", "Verify proportionality under uniform scaling.", "Medium",
         "If the ratio of boys to girls in a school is $3 : 4$, doubling the total number of students will change the ratio to $6 : 8$, which simplifies back to $3 : 4$.", "True",
         "Uniformly scaling both groups maintains the underlying simplified ratio of $3 : 4$.")
    ]

    # 15 Scenario-Based Questions
    sc_questions = [
        ("School Demographics & Ratios", "Solve multi-step ratio and percentage distribution problems.", "Hard",
         "An international school in Bangkok has 500 students in Grade 6. The ratio of Thai students to foreign exchange students is $7 : 3$. Among the foreign exchange students, $60\\%$ are from Asian countries.",
         "Calculate (a) the total number of foreign exchange students, and (b) how many foreign exchange students are from Asian countries.",
         "First, calculate foreign students: Total parts $= 7 + 3 = 10$. Foreign parts $= 3$. Foreign students $= \\frac{3}{10} \\times 500 = 150$ students. Second, calculate Asian foreign students: $60\\%$ of $150 = 0.60 \\times 150 = 90$ students. Therefore, there are 150 foreign exchange students, and 90 of them are from Asian countries.",
         "Step 1: Total parts $= 7 + 3 = 10$. Foreign exchange students $= \\frac{3}{10} \\times 500 = 150$. Step 2: Asian foreign exchange students $= 150 \\times 60\\% = 90$ students."),

        ("Golden Ratio Architectural Design", "Apply Golden Ratio formula to architectural structure design.", "Hard",
         "An architect is designing a rectangular window frame based on the Golden Ratio ($\Phi \\approx 1.618$). The shorter side (height) of the window frame is designed to be 1.5 meters.",
         "What should be the exact length of the longer side (width) of the window frame to satisfy the Golden Ratio?",
         "To satisfy the Golden Ratio $\\Phi = \\frac{\\text{Longer Side}}{\\text{Shorter Side}} \\approx 1.618$, we multiply the shorter side by 1.618. Longer Side $= 1.5 \\text{ m} \\times 1.618 = 2.427$ meters (or approximately 2.43 meters).",
         "Golden Ratio formula: $\\frac{\\text{Length}}{\\text{Height}} = 1.618 \\rightarrow \\text{Length} = 1.5 \\times 1.618 = 2.427$ meters."),

        ("Commercial Math - Electronics Store Markup and Discount", "Determine final profit after markup and promotional discount.", "Hard",
         "A store owner purchases a tablet computer from a distributor for 8,000 THB. He marks up the price by $40\\%$ to set the Marked Price. During a holiday promotion, he advertises a $15\\%$ discount on the Marked Price.",
         "Find (a) the Marked Price, (b) the actual Selling Price after discount, and (c) the net profit in THB.",
         "Marked Price $= 8,000 \\times (1 + 0.40) = 8,000 \\times 1.40 = 11,200$ THB. Selling Price $= 11,200 \\times (1 - 0.15) = 11,200 \\times 0.85 = 9,520$ THB. Net Profit $= \\text{Selling Price} - \\text{Cost Price} = 9,520 - 8,000 = 1,520$ THB.",
         "1. $\\text{MP} = 8,000 \\times 1.4 = 11,200$ THB. 2. $\\text{SP} = 11,200 \\times 0.85 = 9,520$ THB. 3. $\\text{Profit} = 9,520 - 8,000 = 1,520$ THB."),

        ("Bank Savings & Simple Interest Comparison", "Compare interest yields across two banking institutions.", "Hard",
         "Narin has 100,000 THB in savings. Bank X offers a simple interest rate of $3.5\\%$ per annum for a 2-year fixed deposit. Bank Y offers a simple interest rate of $2.5\\%$ per annum for a 3-year term.",
         "Calculate the total interest earned from both options and state which bank yields more total interest.",
         "Bank X Interest $= 100,000 \\times 0.035 \\times 2 = 7,000$ THB. Bank Y Interest $= 100,000 \\times 0.025 \\times 3 = 7,500$ THB. Bank Y yields 500 THB more interest than Bank X over their respective full terms.",
         "Bank X: $I = 100,000 \\times 0.035 \\times 2 = 7,000$ THB. Bank Y: $I = 100,000 \\times 0.025 \\times 3 = 7,500$ THB. Bank Y yields 500 THB more overall."),

        ("Business Loan Repayment & Monthly Installments", "Calculate monthly loan repayment installments.", "Hard",
         "A small business owner borrows 240,000 THB from a commercial bank at an annual simple interest rate of $6\\%$. The loan agreement requires full repayment of principal and interest over a 2-year period in equal monthly installments.",
         "Calculate (a) total interest charged, (b) total repayment amount, and (c) the monthly installment payment.",
         "Total interest $I = 240,000 \\times 0.06 \\times 2 = 28,800$ THB. Total repayment $= 240,000 + 28,800 = 268,800$ THB. Total months $= 2 \\times 12 = 24$ months. Monthly installment $= 268,800 \\div 24 = 11,200$ THB per month.",
         "1. $I = 240,000 \\times 0.06 \\times 2 = 28,800$ THB. 2. Total $= 268,800$ THB. 3. Monthly $= 268,800 / 24 = 11,200$ THB."),

        ("Agricultural Crop Yield Ratio", "Solve multi-variable agricultural yield proportion problems.", "Hard",
         "A farmer divides his 60-rai plot of land into three sections for growing Rice, Corn, and Vegetables in the ratio $5 : 3 : 2$.",
         "How many rai are allocated to growing Rice, and what percentage of the total farm land is dedicated to Vegetables?",
         "Total ratio parts $= 5 + 3 + 2 = 10$ parts. Value of 1 part $= 60 \\div 10 = 6$ rai. Rice land $= 5 \\times 6 = 30$ rai. Vegetable land $= 2 \\times 6 = 12$ rai. Vegetable percentage $= \\frac{2}{10} \\times 100\\% = 20\\%$.",
         "Rice allocation $= \\frac{5}{10} \\times 60 = 30$ rai. Vegetable percentage $= \\frac{2}{10} \\times 100\\% = 20\\%$."),

        ("Real Estate Property Sales & Commission", "Calculate realtor commission and seller net proceeds.", "Hard",
         "A real estate broker sells a condominium for 3,500,000 THB. The broker charges a $3\\%$ sales commission fee, and government transfer tax is $2\\%$ of the selling price.",
         "Calculate the total fees (commission + tax) and the net amount received by the property owner.",
         "Commission $= 3,500,000 \\times 0.03 = 105,000$ THB. Transfer Tax $= 3,500,000 \\times 0.02 = 70,000$ THB. Total fees $= 105,000 + 70,000 = 175,000$ THB (or $5\\%$ of selling price). Net proceeds $= 3,500,000 - 175,000 = 3,325,000$ THB.",
         "Total Fee Percentage $= 3\\% + 2\\% = 5\\%$. Total deductions $= 3,500,000 \\times 0.05 = 175,000$ THB. Net proceeds $= 3,325,000$ THB."),

        ("Water Reservoir Storage Percentage", "Calculate water volume changes and percentage capacity.", "Hard",
         "A town reservoir has a total capacity of 1,200,000 cubic meters ($m^3$). At the start of the dry season, it was filled to $85\\%$ of its capacity. During the dry season, $360,000 m^3$ of water was used.",
         "Calculate (a) the initial volume of water, (b) the remaining volume of water, and (c) the remaining water percentage relative to total capacity.",
         "Initial volume $= 1,200,000 \\times 0.85 = 1,020,000 m^3$. Remaining volume $= 1,020,000 - 360,000 = 660,000 m^3$. Remaining percentage $= \\frac{660,000}{1,200,000} \\times 100\\% = 55\\%$.",
         "1. Initial $= 1,020,000 m^3$. 2. Remaining $= 660,000 m^3$. 3. Remaining percentage $= \\frac{660,000}{1,200,000} \\times 100\\% = 55\\%$."),

        ("Multi-step Department Store Cash Discount", "Compute final price with successive member and cash discounts.", "Hard",
         "A customer buys a designer handbag marked at 15,000 THB. The store offers a storewide $20\\%$ discount. If the customer holds a VIP membership card, an additional $10\\%$ discount is applied to the reduced price.",
         "Calculate the final amount paid by the VIP customer and the total effective discount percentage.",
         "First discount price $= 15,000 \\times (1 - 0.20) = 15,000 \\times 0.80 = 12,000$ THB. VIP discount price $= 12,000 \\times (1 - 0.10) = 12,000 \\times 0.90 = 10,800$ THB. Total discount $= 15,000 - 10,800 = 4,200$ THB. Effective discount percentage $= \\frac{4,200}{15,000} \\times 100\\% = 28\\%$.",
         "1. Price after 20% off $= 12,000$ THB. 2. Price after VIP 10% off $= 10,800$ THB. Total effective discount $= 28\\%$."),

        ("Factory Production Defect Rates", "Calculate non-defective product quantities and percentages.", "Hard",
         "A factory produces 4,000 electronic components daily. Quality control inspects a batch and finds that $2.5\\%$ of components are defective. Non-defective components are packed into boxes of 50 units each.",
         "How many non-defective components are produced daily, and how many full boxes can be packed?",
         "Defective components $= 4,000 \\times 0.025 = 100$ components. Non-defective components $= 4,000 - 100 = 3,900$ components. Full boxes packed $= 3,900 \\div 50 = 78$ boxes.",
         "1. Defective $= 100$. 2. Non-defective $= 3,900$. 3. Full boxes $= 3,900 / 50 = 78$ boxes."),

        ("Hotel Staff Foreign Language Competency", "Solve nested percentage demographics.", "Hard",
         "A luxury resort in Phuket employs 200 staff members. $45\\%$ of staff are male. $80\\%$ of all staff members can speak fluent English, while $25\\%$ of English speakers can also speak Chinese.",
         "Calculate (a) total female staff members, (b) total English-speaking staff, and (c) staff members who speak both English and Chinese.",
         "Female staff $= 200 \\times (1 - 0.45) = 200 \\times 0.55 = 110$ females. English speakers $= 200 \\times 0.80 = 160$ staff. Dual speakers (English & Chinese) $= 160 \\times 0.25 = 40$ staff.",
         "1. Female staff $= 110$. 2. English-speaking staff $= 160$. 3. English + Chinese speaking staff $= 40$."),

        ("Car Depreciation and Resale Value", "Calculate monetary loss and depreciation percentage.", "Hard",
         "A company purchased a delivery van for 750,000 THB. After 4 years of operation, the van was sold as a used vehicle for 450,000 THB.",
         "Calculate (a) the total depreciation loss in THB, (b) the overall percentage loss relative to original cost, and (c) average annual depreciation in THB.",
         "Total loss $= 750,000 - 450,000 = 300,000$ THB. Percentage loss $= \\frac{300,000}{750,000} \\times 100\\% = 40\\%$. Average annual depreciation $= 300,000 \\div 4 = 75,000$ THB per year.",
         "1. Total loss $= 300,000$ THB. 2. Loss percentage $= 40\\%$. 3. Annual loss $= 75,000$ THB/year."),

        ("Simple Interest Investment Term Calculation", "Determine required investment duration to double capital.", "Hard",
         "An investor places 50,000 THB into a fixed income government bond offering a simple interest rate of $5\\%$ per annum.",
         "How many years must the principal remain invested to earn exactly 25,000 THB in interest (reaching a total balance of 75,000 THB)?",
         "Annual interest earned $= 50,000 \\times 0.05 = 2,500$ THB per year. Time required $T = \\frac{\\text{Target Interest}}{\\text{Annual Interest}} = \\frac{25,000}{2,500} = 10$ years.",
         "Using $T = \\frac{I}{P \\times R} = \\frac{25,000}{50,000 \\times 0.05} = \\frac{25,000}{2,500} = 10$ years."),

        ("Map Scale Distance & Travel Time", "Calculate real distance and travel time from map scale.", "Hard",
         "On a tourist map with scale $1 : 250,000$, the distance between a hotel and a national park entrance is measured as 8 cm. A tour bus travels at an average speed of 50 km/h.",
         "Calculate (a) real-world distance in km, and (b) travel time in minutes.",
         "Real distance $= 8 \\text{ cm} \\times 250,000 = 2,000,000 \\text{ cm} = 20,000 \\text{ m} = 20$ km. Travel time $= \\frac{\\text{Distance}}{\\text{Speed}} = \\frac{20 \\text{ km}}{50 \\text{ km/h}} = 0.4 \\text{ hours} = 0.4 \\times 60 = 24$ minutes.",
         "1. Real distance $= 8 \\times 250,000 = 2,000,000 \\text{ cm} = 20$ km. 2. Travel time $= \\frac{20}{50} = 0.4 \\text{ h} = 24$ minutes."),

        ("Multi-item Profit & Loss Balance", "Calculate net profit/loss across multiple transaction items.", "Hard",
         "A trader buys two smartphones: Model A for 10,000 THB and Model B for 15,000 THB. He sells Model A at a $20\\%$ profit and sells Model B at a $10\\%$ loss.",
         "Calculate (a) total cost price, (b) overall selling price, and (c) net profit or loss in THB and overall percentage.",
         "Total Cost Price $= 10,000 + 15,000 = 25,000$ THB. Selling Price A $= 10,000 \\times 1.20 = 12,000$ THB (Profit $+2,000$). Selling Price B $= 15,000 \\times 0.90 = 13,500$ THB (Loss $-1,500$). Overall Selling Price $= 12,000 + 13,500 = 25,500$ THB. Net Profit $= 25,500 - 25,000 = +500$ THB. Net Profit Percentage $= \\frac{500}{25,000} \\times 100\\% = 2\\%$.",
         "1. Total CP $= 25,000$ THB. 2. SP A $= 12,000$, SP B $= 13,500 \\rightarrow$ Total SP $= 25,500$ THB. 3. Net Profit $= 500$ THB ($2\\%$ profit).")
    ]

    # 10 Short Answer Questions
    sa_questions = [
        ("Golden Ratio Definition & Significance", "Explain the Golden Ratio and its significance in nature and design.", "Hard",
         "Define the Golden Ratio ($\Phi$), state its approximate numerical value, and explain why it has been widely used by artists, architects, and designers throughout history.",
         "(1) The Golden Ratio ($\Phi \\approx 1.618$) is an irrational mathematical constant formed when the ratio of a whole segment to its longer part equals the ratio of the longer part to the shorter part ($\\frac{a+b}{a} = \\frac{a}{b}$). (2) It occurs naturally in biological patterns such as spiral shells, leaf arrangements, and galaxy formations. (3) Designers and architects use it because proportions based on $\Phi$ generate inherent visual balance, harmony, and aesthetic appeal to human perception."),

        ("Comparing Ratios with Identical vs Different Units", "Explain unit rules when writing ratios.", "Medium",
         "Explain the fundamental difference in writing conventions between a ratio comparing quantities with identical units versus a ratio comparing quantities with different units. Give one example for each.",
         "(1) For quantities with identical units (e.g. 5 kg to 15 kg), units cancel out and are omitted in the final ratio notation ($1 : 3$). (2) For quantities with different units (e.g. 100 km driven in 2 hours), unit names must be explicitly written alongside the simplified numbers ($50 \\text{ km} : 1 \\text{ hour}$ or 50 km per hour)."),

        ("Distinguishing Profit Percentage from Loss Percentage", "Explain how profit percentage and loss percentage are calculated.", "Medium",
         "State the exact formulas for Profit Percentage and Loss Percentage. Explain what baseline value both formulas use and why that baseline is chosen.",
         "(1) Profit Percentage $= \\frac{\\text{Selling Price} - \\text{Cost Price}}{\\text{Cost Price}} \\times 100\\%$. (2) Loss Percentage $= \\frac{\\text{Cost Price} - \\text{Selling Price}}{\\text{Cost Price}} \\times 100\\%$. (3) Both formulas use the Cost Price (CP) as the denominator baseline because financial gain or loss is evaluated relative to the original capital invested to acquire the asset."),

        ("Single Discount vs Successive Discounts", "Analyze the mathematical difference between single and successive discounts.", "Hard",
         "Why is a single discount of $30\\%$ NOT mathematically equal to two successive discounts of $20\\%$ and $10\\%$? Show the calculations for a product marked at 1,000 THB to prove your answer.",
         "(1) Single $30\\%$ discount: Selling Price $= 1,000 \\times (1 - 0.30) = 700$ THB. (2) Successive $20\\%$ then $10\\%$ discounts: After first discount $= 1,000 \\times 0.80 = 800$ THB. After second discount $= 800 \\times 0.90 = 720$ THB. (3) Explanation: The second discount ($10\\%$) is calculated on the reduced price (800 THB) rather than the original marked price (1,000 THB), making consecutive discounts yield a higher final price (720 THB vs 700 THB)."),

        ("Simple Interest Formula Breakdown", "Detail the simple interest formula components and unit requirements.", "Medium",
         "Write down the simple interest formula $I = P \\times R \\times T$. Define each variable clearly and state the required units of time ($T$) when interest rate ($R$) is quoted per annum.",
         "(1) $I$ = Simple Interest amount in currency (e.g. THB). (2) $P$ = Principal (initial capital deposited or borrowed). (3) $R$ = Annual Interest Rate (expressed as a fraction or decimal, e.g. $5\\% = 0.05$). (4) $T$ = Time duration, which MUST be measured in years (e.g. 6 months $= 0.5$ years)."),

        ("Map Scale Interpretation and Real-world Application", "Explain how to interpret and convert map scale ratios.", "Medium",
         "Explain what a map scale ratio of $1 : 50,000$ represents. Describe step-by-step how to calculate the actual ground distance in kilometers if the distance measured on the map is 6 centimeters.",
         "(1) $1 : 50,000$ means 1 unit of distance on the map represents 50,000 identical units of actual distance on the ground. (2) Step 1: Multiply map measurement by scale factor: $6 \\text{ cm} \\times 50,000 = 300,000 \\text{ cm}$. (3) Step 2: Convert centimeters to meters ($300,000 \\div 100 = 3,000 \\text{ m}$). (4) Step 3: Convert meters to kilometers ($3,000 \\div 1,000 = 3 \\text{ km}$). The actual ground distance is 3 km."),

        ("Evaluating Financial Deposit vs Loan Rates", "Analyze banking simple interest from borrower vs saver perspectives.", "Hard",
         "Explain why a bank charges a higher simple interest rate on loans ($R_{loan} = 7\\%$) than it pays to depositors on savings accounts ($R_{savings} = 1.5\\%$). Describe the financial impact on both parties.",
         "(1) The difference between loan interest rate and savings deposit interest rate (net interest margin) represents the bank's primary source of revenue to cover operational costs and generate profit. (2) For savers, lower deposit rates mean slow capital growth. (3) For borrowers, higher loan rates increase the total cost of borrowing, requiring them to repay significantly more than the original principal borrowed."),

        ("Multi-step Ratio Word Problem Strategy", "Outline step-by-step strategy for solving part-to-part ratio division.", "Hard",
         "Describe the general three-step mathematical procedure used to divide a total quantity of 360 items among three groups according to the ratio $2 : 3 : 4$. Provide the final numerical share for each group.",
         "(1) Step 1: Find total ratio parts $= 2 + 3 + 4 = 9$ parts. (2) Step 2: Find the value of 1 part $= 360 \\div 9 = 40$ items. (3) Step 3: Multiply each ratio term by the value of 1 part: Group 1 $= 2 \\times 40 = 80$ items, Group 2 $= 3 \\times 40 = 120$ items, Group 3 $= 4 \\times 40 = 160$ items."),

        ("Percentage Increase vs Percentage Decrease", "Compare percentage change concepts and baseline principles.", "Medium",
         "Compare the procedures for calculating Percentage Increase versus Percentage Decrease. Explain why both calculations divide by the original starting amount rather than the new final amount.",
         "(1) Percentage Increase $= \\frac{\\text{New Amount} - \\text{Original Amount}}{\\text{Original Amount}} \\times 100\\%$. (2) Percentage Decrease $= \\frac{\\text{Original Amount} - \\text{New Amount}}{\\text{Original Amount}} \\times 100\\%$. (3) Both procedures divide by the Original Amount because percentage change measures the relative magnitude of growth or reduction compared to the initial baseline state."),

        ("Real-World Financial Planning and Simple Interest Applications", "Discuss real-world utility of simple interest calculations in household budgeting.", "Hard",
         "Discuss how understanding ratios, percentages, and simple interest empowers individuals to make informed personal financial decisions when buying products on installment or taking bank loans.",
         "(1) Understanding percentages allows consumers to calculate true discount savings and compare store promotions accurately. (2) Mastery of simple interest equations enables individuals to compute total repayment costs, avoid predatory loan terms, and evaluate borrowing costs before taking bank credit. (3) Ratios assist in effective household budget planning by allocating income appropriately across savings, fixed expenses, and flexible investments.")
    ]

    # Generate Markdown Content
    md = []
    md.append("# Mathematics Assessment Grade 6 (Mathematics Gr.6 - MidFinal)")
    md.append("")
    md.append("> **Assessment Information**")
    md.append("> - **Subject**: Mathematics (English Edition)")
    md.append("> - **Grade Level**: Grade 6 (Primary 6)")
    md.append("> - **Source Material**: Mathematics Gr6-MidFinal.pdf (60 Pages)")
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

    output_path = "Knowledge_Assessment_Mathematics_Gr6.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"Successfully generated {output_path} with 115 questions!")

if __name__ == "__main__":
    generate_math_en_quiz()
