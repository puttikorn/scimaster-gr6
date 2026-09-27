import os

file_path = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1/Knowledge_Assessment_Mathematics_Gr6.md"

header = """# Knowledge Assessment Quiz: Mathematics Grade 6 (Midterm & Final Assessment)

---

## Document Summary (Mathematics Grade 6 Curriculum & Assessment Summary)

This assessment document compiles comprehensive learning content and evaluation questions for Mathematics Grade 6, covering 5 core units:

### 1. Unit 1: Numbers & Factors (GCF & LCM)
* **Place Value & Operations**: Place values up to 10,000,000, rounding off, prime factorization
* **GCF & LCM**: Finding Greatest Common Factor (GCF) and Least Common Multiple (LCM) using prime factorization and division method, real-world application problems

### 2. Unit 2: Fractions, Decimals & Percentages
* **Fraction Operations**: Addition, subtraction, multiplication, and division of fractions and mixed numbers
* **Decimals & Percentages**: Operations with decimals, converting between fractions, decimals, and percentages, calculating percentage discount, profit, and loss

### 3. Unit 3: Ratios & Proportions
* **Ratios**: Equivalent ratios, simplifying ratios ($a : b$)
* **Proportions & Real-world Applications**: Solving proportion word problems, scale drawing applications on maps

### 4. Unit 4: 2D Geometry & Circles
* **Polygons**: Triangles (area = 1/2 × base × height, sum of interior angles = 180°), Quadrilaterals (area of parallelogram, rhombus, trapezoid)
* **Circles**: Circumference ($C = 2\\pi r = \\pi d$) and Area ($A = \\pi r^2$) using $\\pi = 22/7$ or $3.14$

### 5. Unit 5: 3D Solids, Volume & Data Analysis
* **3D Geometry & Volume**: Volume and surface area of rectangular prisms and cubes ($V = \\text{length} \\times \\text{width} \\times \\text{height}$)
* **Data Analysis**: Reading and interpreting bar graphs, line graphs, and pie charts (circle graphs)

---

## Learning Objectives Mapping

* **LO-MATH1**: Basic mathematical concepts, definitions, place value, and formulas (Remember / Understand)
* **LO-MATH2**: Performing numerical operations, fraction/decimal/ratio calculations (Apply)
* **LO-MATH3**: Multi-step problem solving, GCF/LCM applications, and geometric proofs (Analyze)
* **LO-MATH4**: Real-world financial math, spatial reasoning, data interpretation, and multi-concept scenarios (Evaluate / Create)

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
    # 1-15: Numbers, Factors, GCF & LCM
    (1, "Numbers & Factors", "LO-MATH1", "Easy",
     "What is the Greatest Common Factor (GCF) of 12 and 18?",
     "2", "3", "6", "12", "ค",
     "Factors of 12 = {1, 2, 3, 4, 6, 12}; Factors of 18 = {1, 2, 3, 6, 9, 18}. The greatest common factor is 6."),

    (2, "Numbers & Factors", "LO-MATH1", "Easy",
     "What is the Least Common Multiple (LCM) of 4 and 6?",
     "12", "18", "24", "36", "ก",
     "Multiples of 4 = {4, 8, 12, 16, 20...}; Multiples of 6 = {6, 12, 18, 24...}. The least common multiple is 12."),

    (3, "Numbers & Factors", "LO-MATH1", "Easy",
     "Which of the following numbers is a prime number?",
     "15", "21", "29", "33", "ค",
     "29 has only two factors (1 and 29), making it a prime number."),

    (4, "Place Value", "LO-MATH1", "Easy",
     "In the number 5,842,910, what is the value of the digit 8?",
     "800", "80,000", "800,000", "8,000,000", "ค",
     "The digit 8 is in the hundred-thousands place, so its value is 800,000."),

    (5, "Numbers & Factors", "LO-MATH2", "Medium",
     "Find the prime factorization of 60.",
     "2 × 3 × 10", "2 × 2 × 3 × 5", "4 × 3 × 5", "2 × 5 × 6", "ข",
     "60 = 4 × 15 = 2² × 3 × 5 = 2 × 2 × 3 × 5."),

    (6, "Numbers & Factors", "LO-MATH2", "Medium",
     "What is the GCF of 24, 36, and 48?",
     "6", "8", "12", "24", "ค",
     "Common factors of 24, 36, 48 are 1, 2, 3, 4, 6, 12. The highest is 12."),

    (7, "Numbers & Factors", "LO-MATH2", "Medium",
     "Three alarm clocks ring at intervals of 4, 6, and 8 minutes. If they ring together at 8:00 AM, when will they next ring together?",
     "8:12 AM", "8:16 AM", "8:24 AM", "8:48 AM", "ค",
     "Find LCM of 4, 6, and 8. LCM(4, 6, 8) = 24 minutes. So they ring next at 8:24 AM."),

    (8, "Rounding Numbers", "LO-MATH1", "Easy",
     "Round off 4,785,320 to the nearest hundred-thousand.",
     "4,700,000", "4,780,000", "4,800,000", "5,000,000", "ค",
     "The ten-thousands digit is 8 (>=5), so round up to 4,800,000."),

    (9, "Numbers & Factors", "LO-MATH3", "Hard",
     "The product of two numbers is 180, and their GCF is 3. What is their LCM?",
     "30", "45", "60", "90", "ค",
     "Formula: Number A × Number B = GCF × LCM. So 180 = 3 × LCM -> LCM = 180 / 3 = 60."),

    (10, "Numbers & Factors", "LO-MATH2", "Medium",
     "Teacher Jane has 30 apples and 45 oranges. She wants to pack them into identical fruit bags with no leftover. What is the maximum number of bags she can make?",
     "5", "10", "15", "30", "ค",
     "Maximum identical bags = GCF(30, 45) = 15 bags."),

    # 11-25: Fractions & Decimals
    (11, "Fractions", "LO-MATH1", "Easy",
     "Simplify the fraction 18/24 to its lowest terms.",
     "2/3", "3/4", "4/5", "6/8", "ข",
     "Divide numerator and denominator by GCF(18, 24) = 6 -> (18÷6)/(24÷6) = 3/4."),

    (12, "Fractions", "LO-MATH2", "Easy",
     "Calculate: 3/5 + 1/2.",
     "4/7", "7/10", "11/10 (1 1/10)", "4/10", "ค",
     "Common denominator is 10: (3×2)/10 + (1×5)/10 = 6/10 + 5/10 = 11/10 = 1 1/10."),

    (13, "Fractions", "LO-MATH2", "Medium",
     "Calculate: 2 1/3 - 1 3/4.",
     "7/12", "5/12", "1 1/12", "2/3", "ก",
     "2 1/3 = 7/3 = 28/12; 1 3/4 = 7/4 = 21/12. Difference = 28/12 - 21/12 = 7/12."),

    (14, "Fractions", "LO-MATH2", "Medium",
     "Calculate: 4/9 × 3/8.",
     "12/72 (1/6)", "7/17", "1/4", "1/2", "ก",
     "(4 × 3) / (9 × 8) = 12 / 72 = 1/6."),

    (15, "Fractions", "LO-MATH2", "Medium",
     "Calculate: 5/6 ÷ 2/3.",
     "5/9", "5/4 (1 1/4)", "10/18", "4/5", "ข",
     "5/6 × 3/2 = (5×3)/(6×2) = 15/12 = 5/4 = 1 1/4."),

    (16, "Decimals", "LO-MATH1", "Easy",
     "Convert 0.75 into a fraction in its simplest form.",
     "1/4", "1/2", "3/4", "4/5", "ค",
     "0.75 = 75/100 = 3/4."),

    (17, "Decimals", "LO-MATH2", "Easy",
     "Calculate: 14.25 + 6.8.",
     "20.05", "21.05", "21.5", "20.95", "ข",
     "14.25 + 6.80 = 21.05."),

    (18, "Decimals", "LO-MATH2", "Medium",
     "Calculate: 3.5 × 0.4.",
     "0.14", "1.4", "14.0", "0.014", "ข",
     "35 × 4 = 140. Two decimal places -> 1.40 = 1.4."),

    (19, "Decimals", "LO-MATH2", "Medium",
     "Calculate: 12.6 ÷ 0.3.",
     "4.2", "42", "420", "0.42", "ข",
     "Shift decimal: 126 ÷ 3 = 42."),

    (20, "Fractions to Decimals", "LO-MATH1", "Easy",
     "Convert the fraction 3/8 into a decimal.",
     "0.375", "0.38", "0.625", "0.3", "ก",
     "3 ÷ 8 = 0.375."),

    (21, "Percentages", "LO-MATH2", "Easy",
     "What is 25% of 240?",
     "40", "50", "60", "80", "ค",
     "25% = 1/4 -> 240 / 4 = 60."),

    (22, "Percentages", "LO-MATH2", "Medium",
     "A jacket costs $80. If it is on sale at a 20% discount, how much is the discount?",
     "$12", "$16", "$20", "$64", "ข",
     "Discount = 20% of $80 = 0.20 × 80 = $16."),

    (23, "Percentages", "LO-MATH3", "Hard",
     "A book was bought for $150 and sold for $180. What is the percentage profit?",
     "15%", "20%", "25%", "30%", "ข",
     "Profit = $180 - $150 = $30. Percentage profit = (30 / 150) × 100% = 20%."),

    (24, "Percentages", "LO-MATH2", "Medium",
     "Express 0.45 as a percentage.",
     "4.5%", "45%", "450%", "0.45%", "ข",
     "0.45 × 100% = 45%."),

    (25, "Decimals", "LO-MATH2", "Medium",
     "Rope A is 4.85 meters long and Rope B is 2.3 meters long. How much longer is Rope A than Rope B?",
     "2.55 meters", "2.15 meters", "2.45 meters", "2.65 meters", "ก",
     "4.85 - 2.30 = 2.55 meters."),

    # 26-40: Ratios, Proportions & Scale
    (26, "Ratios", "LO-MATH1", "Easy",
     "Simplify the ratio 15 : 25 to its simplest form.",
     "2 : 3", "3 : 5", "5 : 3", "3 : 4", "ข",
     "Divide both sides by 5: (15÷5) : (25÷5) = 3 : 5."),

    (27, "Ratios", "LO-MATH2", "Medium",
     "The ratio of boys to girls in a class is 3 : 4. If there are 12 boys, how many girls are there?",
     "9", "12", "16", "20", "ค",
     "3 units = 12 -> 1 unit = 4. Girls = 4 units = 4 × 4 = 16 girls."),

    (28, "Ratios", "LO-MATH2", "Medium",
     "Divide $100 between Alice and Bob in the ratio 2 : 3. How much money does Bob get?",
     "$40", "$50", "$60", "$70", "ค",
     "Total parts = 2 + 3 = 5 parts. 1 part = $100 / 5 = $20. Bob's share = 3 parts × $20 = $60."),

    (29, "Proportions", "LO-MATH2", "Medium",
     "If 5 notebooks cost $15, how much will 8 notebooks cost?",
     "$20", "$24", "$25", "$30", "ข",
     "Cost per notebook = $15 / 5 = $3. 8 notebooks = 8 × $3 = $24."),

    (30, "Scale Drawing", "LO-MATH3", "Hard",
     "On a map with a scale of 1 : 50,000, two towns are 4 cm apart. What is the actual distance between the two towns in kilometers?",
     "1 km", "2 km", "4 km", "20 km", "ข",
     "Actual distance = 4 cm × 50,000 = 200,000 cm = 2,000 m = 2 km."),

    (31, "Ratios", "LO-MATH2", "Medium",
     "In a fruit basket, the ratio of apples to oranges is 5 : 2. If there are 35 fruits in total, how many apples are there?",
     "10", "14", "25", "30", "ค",
     "Total parts = 5 + 2 = 7 parts. 1 part = 35 / 7 = 5. Apples = 5 parts × 5 = 25 apples."),

    (32, "Proportions", "LO-MATH2", "Medium",
     "A car travels 180 km in 3 hours at a constant speed. How far will it travel in 5 hours?",
     "240 km", "300 km", "360 km", "400 km", "ข",
     "Speed = 180 / 3 = 60 km/h. Distance in 5 hours = 60 × 5 = 300 km."),

    (33, "Ratios", "LO-MATH1", "Easy",
     "Which of the following ratios is equivalent to 4 : 7?",
     "8 : 12", "12 : 21", "16 : 24", "20 : 30", "ข",
     "Multiply both terms of 4 : 7 by 3 -> (4×3) : (7×3) = 12 : 21."),

    (34, "Ratios & Mixtures", "LO-MATH3", "Hard",
     "To make fruit punch, fruit juice and water are mixed in the ratio 1 : 4. If you have 500 mL of fruit juice, how much fruit punch can you make in total?",
     "2,000 mL", "2,500 mL", "3,000 mL", "1,500 mL", "ข",
     "Juice = 1 part = 500 mL. Water = 4 parts = 2,000 mL. Total punch = 1 + 4 = 5 parts = 2,500 mL."),

    (35, "Scale Drawing", "LO-MATH2", "Medium",
     "The actual length of a swimming pool is 25 meters. If represented on a blueprint with a scale of 1 : 500, what is its length on the blueprint in centimeters?",
     "2 cm", "5 cm", "10 cm", "50 cm", "ข",
     "25 m = 2,500 cm. Blueprint length = 2,500 cm / 500 = 5 cm."),

    # 36-50: Geometry (Triangles, Quadrilaterals, Circles, Volume)
    (36, "Triangles", "LO-MATH1", "Easy",
     "What is the sum of interior angles in any triangle?",
     "90°", "180°", "270°", "360°", "ข",
     "The sum of interior angles in any triangle is always 180°."),

    (37, "Triangles Area", "LO-MATH2", "Easy",
     "Calculate the area of a triangle with a base of 10 cm and a height of 6 cm.",
     "16 cm²", "30 cm²", "60 cm²", "120 cm²", "ข",
     "Area = 1/2 × base × height = 1/2 × 10 × 6 = 30 cm²."),

    (38, "Quadrilaterals", "LO-MATH1", "Easy",
     "What is the formula for calculating the area of a parallelogram?",
     "base × height", "1/2 × base × height", "length × width × height", "side × side", "ก",
     "Area of parallelogram = base × height."),

    (39, "Trapezoid Area", "LO-MATH2", "Medium",
     "Calculate the area of a trapezoid with parallel sides of length 6 cm and 10 cm, and a perpendicular height of 5 cm.",
     "40 cm²", "50 cm²", "80 cm²", "160 cm²", "ก",
     "Area = 1/2 × (sum of parallel sides) × height = 1/2 × (6 + 10) × 5 = 1/2 × 16 × 5 = 40 cm²."),

    (40, "Circles Circumference", "LO-MATH2", "Medium",
     "Find the circumference of a circle with a radius of 7 cm. (Use π = 22/7)",
     "22 cm", "44 cm", "88 cm", "154 cm", "ข",
     "Circumference = 2 × π × r = 2 × (22/7) × 7 = 44 cm."),

    (41, "Circles Area", "LO-MATH2", "Medium",
     "Find the area of a circle with a radius of 7 cm. (Use π = 22/7)",
     "44 cm²", "88 cm²", "154 cm²", "308 cm²", "ค",
     "Area = π × r² = (22/7) × 7 × 7 = 154 cm²."),

    (42, "Circles Diameter", "LO-MATH1", "Easy",
     "If the radius of a circle is 12 cm, what is its diameter?",
     "6 cm", "18 cm", "24 cm", "36 cm", "ค",
     "Diameter = 2 × radius = 2 × 12 = 24 cm."),

    (43, "Volume of Rectangular Prism", "LO-MATH2", "Easy",
     "Calculate the volume of a box measuring 5 cm long, 4 cm wide, and 3 cm high.",
     "12 cm³", "60 cm³", "94 cm³", "120 cm³", "ข",
     "Volume = length × width × height = 5 × 4 × 3 = 60 cm³."),

    (44, "Volume of Cube", "LO-MATH2", "Medium",
     "What is the volume of a cube with edge length of 4 cm?",
     "16 cm³", "48 cm³", "64 cm³", "96 cm³", "ค",
     "Volume of cube = side³ = 4 × 4 × 4 = 64 cm³."),

    (45, "Surface Area of Cube", "LO-MATH3", "Hard",
     "Calculate the total surface area of a cube with an edge length of 5 cm.",
     "100 cm²", "125 cm²", "150 cm²", "300 cm²", "ค",
     "A cube has 6 square faces. Area of 1 face = 5 × 5 = 25 cm². Total surface area = 6 × 25 = 150 cm²."),

    (46, "Angles in Triangle", "LO-MATH2", "Medium",
     "In a triangle, two interior angles measure 50° and 70°. What is the measure of the third angle?",
     "50°", "60°", "70°", "80°", "ข",
     "Third angle = 180° - (50° + 70°) = 180° - 120° = 60°."),

    (47, "Rhombus Area", "LO-MATH2", "Medium",
     "Calculate the area of a rhombus whose diagonals measure 8 cm and 12 cm.",
     "20 cm²", "48 cm²", "96 cm²", "192 cm²", "ข",
     "Area of rhombus = 1/2 × product of diagonals = 1/2 × 8 × 12 = 48 cm²."),

    (48, "Circles Circumference", "LO-MATH2", "Medium",
     "A circular bicycle wheel has a diameter of 70 cm. What distance does it travel in one complete revolution? (Use π = 22/7)",
     "110 cm", "220 cm", "440 cm", "3850 cm", "ข",
     "Distance in 1 revolution = Circumference = π × d = (22/7) × 70 = 220 cm."),

    (49, "Perimeter & Area", "LO-MATH3", "Hard",
     "A rectangular garden has a perimeter of 36 meters. If its length is 10 meters, what is its area?",
     "80 m²", "90 m²", "100 m²", "160 m²", "ก",
     "Perimeter = 2 × (length + width) -> 36 = 2 × (10 + width) -> 10 + width = 18 -> width = 8 m. Area = 10 × 8 = 80 m²."),

    (50, "3D Solids", "LO-MATH1", "Easy",
     "How many faces does a rectangular prism (cuboid) have?",
     "4", "6", "8", "12", "ข",
     "A rectangular prism has 6 faces."),

    # 51-60: Data Analysis, Statistics & Word Problems
    (51, "Statistics (Mean)", "LO-MATH1", "Easy",
     "Find the average (mean) of the numbers: 12, 15, 18, 20, 25.",
     "15", "18", "19", "20", "ข",
     "Mean = (12 + 15 + 18 + 20 + 25) / 5 = 90 / 5 = 18."),

    (52, "Statistics (Range)", "LO-MATH1", "Easy",
     "What is the range of the test scores: 65, 78, 82, 45, 90, 88?",
     "23", "45", "45 to 90", "90", "ข",
     "Range = Maximum - Minimum = 90 - 45 = 45."),

    (53, "Data Analysis (Pie Chart)", "LO-MATH2", "Medium",
     "In a pie chart representing 200 students' favorite sports, the section for Football covers 40%. How many students chose Football?",
     "40", "60", "80", "100", "ค",
     "Number of students = 40% of 200 = (40/100) × 200 = 80 students."),

    (54, "Data Analysis (Bar Graph)", "LO-MATH2", "Easy",
     "A bar graph shows Monday sales: 30 books, Tuesday: 45 books, Wednesday: 25 books. What is the total sales over 3 days?",
     "75", "85", "100", "120", "ค",
     "Total = 30 + 45 + 25 = 100 books."),

    (55, "Word Problems (Financial)", "LO-MATH2", "Medium",
     "Tom bought 3 shirts at $15 each and paid with a $50 bill. How much change should he receive?",
     "$5", "$10", "$15", "$35", "ก",
     "Total cost = 3 × $15 = $45. Change = $50 - $45 = $5."),

    (56, "Word Problems (Mixed)", "LO-MATH3", "Hard",
     "A water tank contains 120 liters of water. If water is drained out at 4.5 liters per minute for 20 minutes, how much water remains in the tank?",
     "30 liters", "40 liters", "90 liters", "110 liters", "ก",
     "Drained volume = 4.5 × 20 = 90 liters. Remaining water = 120 - 90 = 30 liters."),

    (57, "Statistics (Mean)", "LO-MATH3", "Hard",
     "The average score of 4 students is 80. If a 5th student scores 90, what is the new average score of all 5 students?",
     "82", "84", "85", "86", "ก",
     "Sum of 4 scores = 4 × 80 = 320. New sum = 320 + 90 = 410. New average = 410 / 5 = 82."),

    (58, "Probability Concepts", "LO-MATH1", "Easy",
     "A fair 6-sided die is rolled. What is the probability of rolling an even number?",
     "1/6", "1/3", "1/2", "2/3", "ค",
     "Even numbers on a die = {2, 4, 6} (3 outcomes out of 6). Probability = 3/6 = 1/2."),

    (59, "Word Problems (Speed)", "LO-MATH2", "Medium",
     "A runner completes a 400-meter track in 80 seconds. What is his average speed in meters per second (m/s)?",
     "4 m/s", "5 m/s", "6 m/s", "8 m/s", "ข",
     "Speed = Distance / Time = 400 / 80 = 5 m/s."),

    (60, "Data Analysis (Pie Chart)", "LO-MATH2", "Medium",
     "In a pie chart, the angle of the central sector representing Vanilla ice cream is 90°. What fraction of the total pie chart does Vanilla represent?",
     "1/6", "1/4", "1/3", "1/2", "ข",
     "Full circle angle = 360°. Fraction = 90° / 360° = 1/4.")
]

tf_questions = [
    # 61-90 True/False
    (61, "Numbers & Factors", "LO-MATH1", "Easy",
     "The number 1 is a prime number.",
     "False", "Incorrect. 1 is neither prime nor composite because it has only 1 factor."),

    (62, "Numbers & Factors", "LO-MATH1", "Easy",
     "The GCF of two prime numbers is always 1.",
     "True", "Correct. Prime numbers have no common factors other than 1."),

    (63, "Numbers & Factors", "LO-MATH1", "Easy",
     "The LCM of two numbers can never be smaller than either of the two numbers.",
     "True", "Correct. LCM is a common multiple, so it must be >= both numbers."),

    (64, "Fractions", "LO-MATH1", "Easy",
     "When adding two fractions, we add both numerators together and both denominators together.",
     "False", "Incorrect. We must find a common denominator and add numerators only."),

    (65, "Fractions", "LO-MATH2", "Medium",
     "To divide by a fraction, we multiply by its reciprocal.",
     "True", "Correct. Division by a fraction equals multiplying by its inverted reciprocal (a/b ÷ c/d = a/b × d/c)."),

    (66, "Decimals", "LO-MATH1", "Easy",
     "0.5 is equal in value to 0.50 and 0.500.",
     "True", "Correct. Trailing zeros after decimal point do not change the numerical value."),

    (67, "Percentages", "LO-MATH1", "Easy",
     "50% of a number is equivalent to dividing that number by 2.",
     "True", "Correct. 50% = 50/100 = 1/2."),

    (68, "Ratios", "LO-MATH1", "Easy",
     "The ratio 2 : 3 is equivalent to the ratio 6 : 9.",
     "True", "Correct. Multiplying both terms of 2 : 3 by 3 yields 6 : 9."),

    (69, "Ratios", "LO-MATH1", "Easy",
     "Ratios can only be written between two numbers and cannot compare three numbers.",
     "False", "Incorrect. Three-part ratios exist, e.g., a : b : c = 2 : 3 : 5."),

    (70, "Geometry (Triangles)", "LO-MATH1", "Easy",
     "An equilateral triangle has three sides of equal length and three angles of 60° each.",
     "True", "Correct. All sides equal and all angles 60° define an equilateral triangle."),

    (71, "Geometry (Triangles)", "LO-MATH1", "Easy",
     "A right-angled triangle can have an obtuse angle (> 90°).",
     "False", "Incorrect. A right triangle has one 90° angle, leaving the remaining two angles acute (< 90°)."),

    (72, "Geometry (Quadrilaterals)", "LO-MATH1", "Easy",
     "A square is a special type of rectangle where all four sides are equal.",
     "True", "Correct. A square satisfies all properties of a rectangle with equal side lengths."),

    (73, "Geometry (Circles)", "LO-MATH1", "Easy",
     "The radius of a circle is half the length of its diameter.",
     "True", "Correct. r = d / 2."),

    (74, "Geometry (Circles)", "LO-MATH2", "Medium",
     "If the radius of a circle is doubled, its area is also doubled.",
     "False", "Incorrect. Area = π r². If radius is doubled (2r), area becomes π (2r)² = 4 π r² (quadrupled)."),

    (75, "Volume & 3D", "LO-MATH1", "Easy",
     "The volume of a rectangular prism is calculated by multiplying length × width × height.",
     "True", "Correct. Volume = l × w × h."),

    (76, "Volume & 3D", "LO-MATH2", "Medium",
     "1 liter is equal to 1,000 cubic centimeters (cm³).",
     "True", "Correct. 1 L = 1,000 cm³ (or 1,000 mL)."),

    (77, "Statistics", "LO-MATH1", "Easy",
     "The mean (average) of a set of numbers is found by dividing the sum of the numbers by the total count of numbers.",
     "True", "Correct. Mean = Total Sum / Total Count."),

    (78, "Statistics", "LO-MATH1", "Easy",
     "The range of a dataset is the middle number when the data is ordered from smallest to largest.",
     "False", "Incorrect. Range = Maximum - Minimum. The middle number is called the Median."),

    (79, "Financial Math", "LO-MATH2", "Medium",
     "Selling an item at a price lower than its cost price results in a profit.",
     "False", "Incorrect. Selling below cost price results in a loss."),

    (80, "Percentages", "LO-MATH2", "Medium",
     "A 10% discount followed by another 10% discount is equivalent to a single 20% discount.",
     "False", "Incorrect. Successive discounts apply to reduced prices: $100 -> $90 -> $81 (19% total discount)."),

    (81, "Angles", "LO-MATH1", "Easy",
     "An acute angle is an angle that measures less than 90°.",
     "True", "Correct. Acute angles are strictly between 0° and 90°."),

    (82, "Angles", "LO-MATH1", "Easy",
     "The sum of angles at a point on a straight line is 360°.",
     "False", "Incorrect. Angles on a straight line sum to 180°. A full turn at a point is 360°."),

    (83, "Geometry", "LO-MATH1", "Easy",
     "A circle has infinitely many lines of symmetry.",
     "True", "Correct. Any line passing through the center of a circle is a line of symmetry."),

    (84, "Scale Drawing", "LO-MATH2", "Medium",
     "A map scale of 1 : 100 means that 1 cm on the map represents 1 meter in real life.",
     "True", "Correct. 100 cm = 1 meter."),

    (85, "Numbers & Factors", "LO-MATH1", "Easy",
     "Every even number greater than 2 is a composite number.",
     "True", "Correct. All even numbers > 2 are divisible by 2, hence composite."),

    (86, "Fractions", "LO-MATH2", "Medium",
     "3/4 is greater than 4/5.",
     "False", "Incorrect. 3/4 = 0.75; 4/5 = 0.80. Thus 4/5 is greater than 3/4."),

    (87, "Decimals", "LO-MATH2", "Medium",
     "Multiplying a decimal by 10 moves the decimal point one place to the left.",
     "False", "Incorrect. Multiplying by 10 moves the decimal point one place to the RIGHT."),

    (88, "Probability", "LO-MATH1", "Easy",
     "The probability of an impossible event is 0.",
     "True", "Correct. Probability ranges from 0 (impossible) to 1 (certain)."),

    (89, "Geometry (Quadrilaterals)", "LO-MATH1", "Easy",
     "The opposite sides of a parallelogram are equal in length and parallel.",
     "True", "Correct. Definition of a parallelogram includes opposite sides being parallel and equal."),

    (90, "Data Analysis", "LO-MATH1", "Easy",
     "The sum of all percentage sectors in a complete pie chart must equal 100%.",
     "True", "Correct. A complete pie chart represents a whole (100% or 360°).")
]

sc_questions = [
    # 91-105 Scenario
    (91, "Financial Math Scenario", "LO-MATH4", "Hard",
     "Sarah visits a store during a sale. A handbag original price is $200. The store offers a 20% discount. Sarah has a VIP coupon for an extra 10% off the discounted price. How much will Sarah pay for the handbag?",
     "Question: Calculate Sarah's final purchase price after applying both discounts sequentially.",
     "Step 1: First discount = 20% of $200 = $40. Price after 1st discount = $200 - $40 = $160.\\nStep 2: VIP coupon = 10% of $160 = $16. Final price = $160 - $16 = $144.\\nSarah will pay $144.",
     "Explanation: Successive discounts apply step-by-step to reduced balances."),

    (92, "GCF / LCM Application Scenario", "LO-MATH3", "Hard",
     "A baker has 48 chocolate cookies and 72 vanilla cookies. He wants to pack them into gift boxes such that every box has the exact same number of chocolate cookies and vanilla cookies, with no cookies leftover. What is the maximum number of boxes he can make, and how many of each cookie will be in each box?",
     "Question: Find the maximum number of gift boxes and the contents of each box.",
     "Step 1: Find GCF(48, 72). 48 = 2⁴ × 3; 72 = 2³ × 3². GCF = 2³ × 3 = 24 boxes.\\nStep 2: Chocolate cookies per box = 48 / 24 = 2. Vanilla cookies per box = 72 / 24 = 3.\\nResult: Maximum 24 boxes, each containing 2 chocolate and 3 vanilla cookies.",
     "Explanation: GCF determines maximum identical groupings."),

    (93, "Scale Drawing Scenario", "LO-MATH3", "Hard",
     "On a city architectural map drawn to a scale of 1 : 2,000, a rectangular park is measured as 6 cm long and 4 cm wide. Calculate the actual area of the park in square meters.",
     "Question: Determine the actual park area in square meters (m²).",
     "Step 1: Actual length = 6 cm × 2,000 = 12,000 cm = 120 meters.\\nStep 2: Actual width = 4 cm × 2,000 = 8,000 cm = 80 meters.\\nStep 3: Actual Area = 120 m × 80 m = 9,600 m².",
     "Explanation: Convert dimensions to real scale first, then calculate area."),

    (94, "Circle Geometry Scenario", "LO-MATH4", "Hard",
     "A circular running track has an inner radius of 14 meters and an outer radius of 21 meters. Calculate the area of the running track path (ring area). (Use π = 22/7)",
     "Question: Calculate the area of the circular ring track path.",
     "Step 1: Inner Area = π × r₁² = (22/7) × 14 × 14 = 616 m².\\nStep 2: Outer Area = π × r₂² = (22/7) × 21 × 21 = 1,386 m².\\nStep 3: Track Area = Outer Area - Inner Area = 1,386 - 616 = 770 m².",
     "Explanation: Ring area = Outer Circle Area - Inner Circle Area."),

    (95, "Volume & Capacity Scenario", "LO-MATH4", "Hard",
     "A rectangular fish tank is 50 cm long, 30 cm wide, and 40 cm high. Currently, it is filled with water up to 3/4 of its total height. How many liters of water are in the fish tank?",
     "Question: Calculate the volume of water in the tank in liters (L).",
     "Step 1: Water height = 3/4 × 40 cm = 30 cm.\\nStep 2: Water volume = 50 × 30 × 30 = 45,000 cm³.\\nStep 3: Convert to liters (1 L = 1,000 cm³) -> 45,000 / 1,000 = 45 liters.",
     "Explanation: Volume = l × w × water height, converted from cm³ to L."),

    (96, "Fractions & Word Problem Scenario", "LO-MATH3", "Hard",
     "Mark has a monthly allowance. He spends 1/3 of his allowance on food and 1/4 on books. He saves the remaining $250. What is Mark's total monthly allowance?",
     "Question: Calculate Mark's total monthly allowance in dollars.",
     "Step 1: Fraction spent = 1/3 + 1/4 = 4/12 + 3/12 = 7/12.\\nStep 2: Fraction saved = 1 - 7/12 = 5/12.\\nStep 3: 5/12 of allowance = $250 -> Total allowance = 250 × 12 / 5 = $600.",
     "Explanation: Remaining fraction 5/12 represents $250."),

    (97, "Average & Statistics Scenario", "LO-MATH4", "Hard",
     "A student scored 75, 82, and 88 on her first three math tests. What minimum score must she get on her 4th test to achieve an overall average score of 85 across all four tests?",
     "Question: Calculate the required score on the 4th test.",
     "Step 1: Total required score for 4 tests = 4 × 85 = 340.\\nStep 2: Sum of first 3 test scores = 75 + 82 + 88 = 245.\\nStep 3: Required 4th score = 340 - 245 = 95.",
     "Explanation: Target Total - Current Sum = Required 4th score."),

    (98, "Ratio & Mixture Scenario", "LO-MATH3", "Hard",
     "A concrete mixture is made by mixing cement, sand, and gravel in the ratio 1 : 2 : 4 by weight. If a construction worker needs 1,400 kg of concrete mixture, how many kilograms of sand are needed?",
     "Question: Calculate the weight of sand required for 1,400 kg of concrete.",
     "Step 1: Total ratio parts = 1 + 2 + 4 = 7 parts.\\nStep 2: 1 part = 1,400 kg / 7 = 200 kg.\\nStep 3: Sand = 2 parts = 2 × 200 kg = 400 kg.",
     "Explanation: Divide total weight by sum of ratio parts, then multiply by sand's ratio part."),

    (99, "Speed & Time Distance Scenario", "LO-MATH4", "Hard",
     "Train A departs Station X towards Station Y at 60 km/h. At the same time, Train B departs Station Y towards Station X at 90 km/h. If the distance between Station X and Y is 300 km, after how many hours will the two trains meet?",
     "Question: Determine the time in hours when the two trains meet.",
     "Step 1: Combined closing speed = 60 km/h + 90 km/h = 150 km/h.\\nStep 2: Time to meet = Total distance / Combined speed = 300 km / 150 km/h = 2 hours.\\nThe trains will meet after 2 hours.",
     "Explanation: Objects moving towards each other add closing speeds."),

    (100, "Percentage Profit & Loss Scenario", "LO-MATH4", "Hard",
     "A merchant bought 100 T-shirts for $800 total. He sold 80 T-shirts at $12 each and the remaining 20 T-shirts at a discounted price of $7 each. Did he make a profit or loss, and what was his percentage profit/loss?",
     "Question: Calculate the net profit/loss and percentage profit/loss.",
     "Step 1: Total Cost = $800.\\nStep 2: Revenue = (80 × $12) + (20 × $7) = $960 + $140 = $1,100.\\nStep 3: Net Profit = $1,100 - $800 = $300 profit.\\nStep 4: Percentage Profit = (300 / 800) × 100% = 37.5%.",
     "Explanation: Total Revenue - Total Cost = Profit."),

    (101, "Trapezoid Area Field Scenario", "LO-MATH3", "Hard",
     "A farmer has a trapezoidal land field with parallel sides measuring 120 meters and 180 meters. The perpendicular distance between the parallel sides is 80 meters. Calculate the total area of the field in square meters.",
     "Question: Calculate the land field area in square meters.",
     "Step 1: Formula = 1/2 × (sum of parallel sides) × height.\\nStep 2: Area = 1/2 × (120 + 180) × 80 = 1/2 × 300 × 80 = 12,000 m².",
     "Explanation: Area of trapezoid formula: 1/2 (a + b) h."),

    (102, "Simple Interest Financial Scenario", "LO-MATH4", "Hard",
     "Mr. Brown deposits $5,000 into a savings account with a simple interest rate of 4% per year. How much total money (principal + interest) will he have in his account after 3 years?",
     "Question: Calculate the total account balance after 3 years.",
     "Step 1: Interest = Principal × Rate × Time = 5,000 × 0.04 × 3 = $600.\\nStep 2: Total Balance = $5,000 + $600 = $5,600.",
     "Explanation: Simple Interest I = P × r × t."),

    (103, "Pie Chart Angle Analysis Scenario", "LO-MATH3", "Hard",
     "In a school election survey of 720 students, the results are displayed in a pie chart. Candidate A's sector has a central angle of 135°. How many votes did Candidate A receive?",
     "Question: Calculate the number of votes Candidate A received.",
     "Step 1: Fraction of total circle = 135° / 360° = 3/8.\\nStep 2: Votes = 3/8 × 720 = 270 votes.",
     "Explanation: Sector angle / 360° × total population = sector count."),

    (104, "Perimeter & Area Optimization Scenario", "LO-MATH4", "Hard",
     "A gardener wants to fence a rectangular garden using 40 meters of fencing wire. What are the dimensions (length and width) that maximize the area of the garden, and what is that maximum area?",
     "Question: Identify the optimal dimensions and maximum area.",
     "Step 1: Perimeter = 2(l + w) = 40 m -> l + w = 20 m.\\nStep 2: Maximum area for a rectangle with fixed perimeter occurs when it is a square (l = w = 10 m).\\nStep 3: Maximum Area = 10 m × 10 m = 100 m².",
     "Explanation: A square maximizes rectangular area for a fixed perimeter."),

    (105, "Water Tank Rate & Capacity Scenario", "LO-MATH4", "Hard",
     "Pipe A fills an empty water tank in 6 hours, while Pipe B fills the same tank in 3 hours. If both Pipe A and Pipe B are opened simultaneously, how many hours will it take to fill the empty tank completely?",
     "Question: Calculate the time required for both pipes together to fill the tank.",
     "Step 1: Pipe A rate = 1/6 tank/hour. Pipe B rate = 1/3 tank/hour.\\nStep 2: Combined rate = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2 tank/hour.\\nStep 3: Time to fill tank = 1 / (1/2) = 2 hours.",
     "Explanation: Add individual rates (1/t₁ + 1/t₂) = combined rate 1/T.")
]

sa_questions = [
    # 106-115 Short Answer
    (106, "GCF & LCM Rules and Applications", "LO-MATH1", "Medium",
     "Explain the definitions of Greatest Common Factor (GCF) and Least Common Multiple (LCM). Show how to find the GCF and LCM of 12 and 18 step-by-step.",
     "1) GCF is the largest factor shared by numbers. LCM is the smallest non-zero multiple shared by numbers.\\n2) Prime factorizations: 12 = 2² × 3; 18 = 2 × 3².\\n3) GCF = 2 × 3 = 6.\\n4) LCM = 2² × 3² = 4 × 9 = 36."),

    (107, "Fraction Operations (Mixed Numbers)", "LO-MATH2", "Medium",
     "Show the step-by-step calculation to evaluate: 3 1/2 ÷ 1 3/4 × 2/5.",
     "Step 1: Convert to improper fractions: 3 1/2 = 7/2; 1 3/4 = 7/4.\\nStep 2: Division: (7/2) ÷ (7/4) = (7/2) × (4/7) = 28/14 = 2.\\nStep 3: Multiplication: 2 × (2/5) = 4/5.\\nFinal Answer: 4/5."),

    (108, "Circle Formulas Derivation & Calculation", "LO-MATH2", "Medium",
     "State the formulas for Circumference and Area of a circle. Calculate both for a circle with diameter = 14 cm (use π = 22/7).",
     "1) Radius r = 14 / 2 = 7 cm.\\n2) Circumference formula C = 2πr = 2 × (22/7) × 7 = 44 cm.\\n3) Area formula A = πr² = (22/7) × 7 × 7 = 154 cm²."),

    (109, "Ratio Partitioning Problem", "LO-MATH2", "Medium",
     "Three siblings share $450 in the ratio 2 : 3 : 4. Calculate how much money each sibling receives.",
     "1) Total parts = 2 + 3 + 4 = 9 parts.\\n2) Value of 1 part = $450 / 9 = $50.\\n3) 1st sibling (2 parts) = 2 × $50 = $100.\\n4) 2nd sibling (3 parts) = 3 × $50 = $150.\\n5) 3rd sibling (4 parts) = 4 × $50 = $200."),

    (110, "Percentage Discount & Sales Tax", "LO-MATH3", "Hard",
     "A TV has a list price of $500. It is discounted by 10%, and then a 7% sales tax is added to the discounted price. Calculate the final price paid.",
     "1) Discount = 10% of $500 = $50. Discounted price = $500 - $50 = $450.\\n2) Sales tax = 7% of $450 = 0.07 × 450 = $31.50.\\n3) Final price = $450 + $31.50 = $481.50."),

    (111, "Trapezoid & Triangle Geometry Proof/Area", "LO-MATH3", "Hard",
     "Explain how the area formula of a trapezoid Area = 1/2 × (a + b) × h is derived by dividing it into two triangles.",
     "A trapezoid with parallel sides 'a' and 'b' and height 'h' can be split along a diagonal into two triangles:\\n- Triangle 1 with base 'a' and height 'h' -> Area = 1/2 × a × h\\n- Triangle 2 with base 'b' and height 'h' -> Area = 1/2 × b × h\\nSum of areas = 1/2 a h + 1/2 b h = 1/2 (a + b) h."),

    (112, "Volume & Surface Area of Prisms", "LO-MATH2", "Medium",
     "A rectangular box has dimensions length = 8 cm, width = 5 cm, height = 4 cm. Calculate its Volume and Total Surface Area.",
     "1) Volume = l × w × h = 8 × 5 × 4 = 160 cm³.\\n2) Surface Area = 2(lw + lh + wh) = 2(8×5 + 8×4 + 5×4) = 2(40 + 32 + 20) = 2(92) = 184 cm²."),

    (113, "Data Analysis (Mean, Median, Mode, Range)", "LO-MATH3", "Hard",
     "For the dataset: 4, 7, 7, 8, 10, 12, 14, find the Mean, Median, Mode, and Range.",
     "1) Mean = (4 + 7 + 7 + 8 + 10 + 12 + 14) / 7 = 62 / 7 ≈ 8.86.\\n2) Median = Middle number in ordered 7 items = 4th item = 8.\\n3) Mode = Most frequent number = 7.\\n4) Range = Max - Min = 14 - 4 = 10."),

    (114, "Linear Equation Word Problem", "LO-MATH3", "Hard",
     "Solve the problem using an equation: '5 times a number plus 12 equals 47. Find the number.' Show all algebraic steps.",
     "1) Let x be the number.\\n2) Equation: 5x + 12 = 47.\\n3) Subtract 12 from both sides: 5x = 47 - 12 -> 5x = 35.\\n4) Divide by 5: x = 35 / 5 = 7.\\nThe number is 7."),

    (115, "Scale Drawing Map Calculations", "LO-MATH3", "Hard",
     "On a map with scale 1 : 200,000, the distance between Town A and Town B is 6.5 cm. Calculate the real-world distance in kilometers. Show steps.",
     "1) Map scale 1 : 200,000 means 1 cm on map = 200,000 cm in reality.\\n2) Real distance in cm = 6.5 cm × 200,000 = 1,300,000 cm.\\n3) Convert cm to meters: 1,300,000 / 100 = 13,000 meters.\\n4) Convert meters to kilometers: 13,000 / 1,000 = 13 km.\\nReal-world distance is 13 km.")
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

print(f"Successfully generated pure English Mathematics Grade 6 quiz file at {file_path}!")
