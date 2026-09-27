import re
import json
import os

def parse_quiz_file(md_filename, output_json, title_name):
    if not os.path.exists(md_filename):
        print(f"File {md_filename} does not exist.")
        return

    with open(md_filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split main sections
    mcq_match = re.search(r'# Section A: Multiple Choice Questions.*?(?=# Section B:)', content, re.DOTALL)
    tf_match = re.search(r'# Section B: True / False Questions.*?(?=# Section C:)', content, re.DOTALL)
    sc_match = re.search(r'# Section C: Scenario-Based Questions.*?(?=# Section D:)', content, re.DOTALL)
    sa_match = re.search(r'# Section D: Short Answer Questions.*?(?=# Answer Key|## Answer Key|\Z)', content, re.DOTALL)

    mcq_raw = mcq_match.group(0) if mcq_match else ''
    tf_raw = tf_match.group(0) if tf_match else ''
    sc_raw = sc_match.group(0) if sc_match else ''
    sa_raw = sa_match.group(0) if sa_match else ''

    questions = []

    # 1. Parse MCQ (ข้อ 1-60)
    mcq_blocks = re.split(r'#### ข้อ (\d+)', mcq_raw)[1:]
    for i in range(0, len(mcq_blocks), 2):
        q_num = int(mcq_blocks[i])
        block = mcq_blocks[i+1]
        
        topic = re.search(r'\* \*\*หัวข้อ\*\*:\s*(.*)', block)
        lo = re.search(r'\* \*\*จุดประสงค์การเรียนรู้\*\*:\s*(.*)', block)
        diff = re.search(r'\* \*\*ระดับความยาก\*\*:\s*(.*)', block)
        prompt = re.search(r'\* \*\*โจทย์\*\*:\s*(.*)', block)
        ans = re.search(r'\* \*\*คำตอบที่ถูกต้อง\*\*:\s*([ก-งA-D])', block)
        exp = re.search(r'\* \*\*คำอธิบาย\*\*:\s*(.*)', block)
        
        # Options
        options = {}
        for opt in ['ก', 'ข', 'ค', 'ง']:
            opt_m = re.search(rf'\* {opt}\.\s*(.*)', block)
            if opt_m:
                options[opt] = opt_m.group(1).strip()
        
        questions.append({
            'id': q_num,
            'section': 'MCQ',
            'sectionName': 'Section A: Multiple Choice',
            'topic': topic.group(1).strip() if topic else '',
            'learningObjective': lo.group(1).strip() if lo else '',
            'difficulty': diff.group(1).strip() if diff else 'Medium',
            'question': prompt.group(1).strip() if prompt else '',
            'options': options,
            'correctAnswer': ans.group(1).strip() if ans else '',
            'explanation': exp.group(1).strip() if exp else '',
            'points': 1
        })

    # 2. Parse True/False (ข้อ 61-90)
    tf_blocks = re.split(r'#### ข้อ (\d+)', tf_raw)[1:]
    for i in range(0, len(tf_blocks), 2):
        q_num = int(tf_blocks[i])
        block = tf_blocks[i+1]
        
        topic = re.search(r'\* \*\*หัวข้อ\*\*:\s*(.*)', block)
        lo = re.search(r'\* \*\*จุดประสงค์การเรียนรู้\*\*:\s*(.*)', block)
        diff = re.search(r'\* \*\*ระดับความยาก\*\*:\s*(.*)', block)
        stmt = re.search(r'\* \*\*ข้อความ\*\*:\s*(.*)', block)
        ans = re.search(r'\* \*\*คำตอบ\*\*:\s*(True|False|ถูก|ผิด)', block, re.IGNORECASE)
        exp = re.search(r'\* \*\*คำอธิบาย\*\*:\s*(.*)', block)
        
        ans_val = True if ans and ('true' in ans.group(1).lower() or 'ถูก' in ans.group(1)) else False
        
        questions.append({
            'id': q_num,
            'section': 'TF',
            'sectionName': 'Section B: True / False',
            'topic': topic.group(1).strip() if topic else '',
            'learningObjective': lo.group(1).strip() if lo else '',
            'difficulty': diff.group(1).strip() if diff else 'Medium',
            'question': stmt.group(1).strip().strip('"') if stmt else '',
            'options': {'True': 'จริง (True)', 'False': 'เท็จ (False)'},
            'correctAnswer': 'True' if ans_val else 'False',
            'explanation': exp.group(1).strip() if exp else '',
            'points': 1
        })

    # 3. Parse Scenario-Based (ข้อ 91-105)
    sc_blocks = re.split(r'#### ข้อ (\d+)', sc_raw)[1:]
    for i in range(0, len(sc_blocks), 2):
        q_num = int(sc_blocks[i])
        block = sc_blocks[i+1]
        
        topic = re.search(r'\* \*\*หัวข้อ\*\*:\s*(.*)', block)
        lo = re.search(r'\* \*\*จุดประสงค์การเรียนรู้\*\*:\s*(.*)', block)
        diff = re.search(r'\* \*\*ระดับความยาก\*\*:\s*(.*)', block)
        scen = re.search(r'\* \*\*สถานการณ์\*\*:\s*(.*)', block)
        q = re.search(r'\* \*\*คำถาม\*\*:\s*(.*)', block)
        ans = re.search(r'\* \*\*คำตอบ\*\*:\s*(.*?)(?=\* \*\*คำอธิบาย\*\*|$)', block, re.DOTALL)
        exp = re.search(r'\* \*\*คำอธิบาย\*\*:\s*(.*)', block)
        
        questions.append({
            'id': q_num,
            'section': 'Scenario',
            'sectionName': 'Section C: Scenario-Based',
            'topic': topic.group(1).strip() if topic else '',
            'learningObjective': lo.group(1).strip() if lo else '',
            'difficulty': diff.group(1).strip() if diff else 'Hard',
            'scenario': scen.group(1).strip() if scen else '',
            'question': q.group(1).strip() if q else '',
            'correctAnswer': ans.group(1).strip() if ans else '',
            'explanation': exp.group(1).strip() if exp else '',
            'points': 2
        })

    # 4. Parse Short Answer (ข้อ 106-115)
    sa_blocks = re.split(r'#### ข้อ (\d+)', sa_raw)[1:]
    for i in range(0, len(sa_blocks), 2):
        q_num = int(sa_blocks[i])
        block = sa_blocks[i+1]
        
        topic = re.search(r'\* \*\*หัวข้อ\*\*:\s*(.*)', block)
        lo = re.search(r'\* \*\*จุดประสงค์การเรียนรู้\*\*:\s*(.*)', block)
        diff = re.search(r'\* \*\*ระดับความยาก\*\*:\s*(.*)', block)
        q = re.search(r'\* \*\*โจทย์\*\*:\s*(.*)', block)
        exp_ans = re.search(r'\* \*\*แนวคำตอบที่คาดหวัง\*\*:\s*(.*)', block, re.DOTALL)
        
        questions.append({
            'id': q_num,
            'section': 'ShortAnswer',
            'sectionName': 'Section D: Short Answer',
            'topic': topic.group(1).strip() if topic else '',
            'learningObjective': lo.group(1).strip() if lo else '',
            'difficulty': diff.group(1).strip() if diff else 'Medium',
            'question': q.group(1).strip() if q else '',
            'correctAnswer': exp_ans.group(1).strip() if exp_ans else '',
            'explanation': 'ประเมินตามการอธิบายหลักการและความถูกต้องของขั้นตอน/ตัวอย่าง',
            'points': 3
        })

    dataset = {
        'title': title_name,
        'meta': {
            'totalQuestions': len(questions),
            'totalScore': sum(q['points'] for q in questions),
            'passingPercentage': 80,
            'passingScore': int(sum(q['points'] for q in questions) * 0.8),
            'sections': [
                {'key': 'MCQ', 'name': 'Section A: Multiple Choice (ปรนัย)', 'count': len([q for q in questions if q['section'] == 'MCQ']), 'pointsPerQuestion': 1, 'totalPoints': sum(q['points'] for q in questions if q['section'] == 'MCQ')},
                {'key': 'TF', 'name': 'Section B: True / False (ถูก / ผิด)', 'count': len([q for q in questions if q['section'] == 'TF']), 'pointsPerQuestion': 1, 'totalPoints': sum(q['points'] for q in questions if q['section'] == 'TF')},
                {'key': 'Scenario', 'name': 'Section C: Scenario-Based (สถานการณ์จำลอง)', 'count': len([q for q in questions if q['section'] == 'Scenario']), 'pointsPerQuestion': 2, 'totalPoints': sum(q['points'] for q in questions if q['section'] == 'Scenario')},
                {'key': 'ShortAnswer', 'name': 'Section D: Short Answer (อัตนัย / อธิบายความรู้)', 'count': len([q for q in questions if q['section'] == 'ShortAnswer']), 'pointsPerQuestion': 3, 'totalPoints': sum(q['points'] for q in questions if q['section'] == 'ShortAnswer')}
            ]
        },
        'questions': questions
    }

    with open(output_json, 'w', encoding='utf-8') as out_f:
        json.dump(dataset, out_f, ensure_ascii=False, indent=2)
    
    print(f'Successfully parsed {len(questions)} questions from {md_filename} into {output_json}!')

if __name__ == '__main__':
    parse_quiz_file('Knowledge_Assessment_Quiz_Science_Gr6.md', 'quiz_data.json', 'แบบทดสอบประเมินผลความรู้วิทยาศาสตร์ ชั้น ป.6 (วิทยาศาสตร์Gr6-1 MidFi)')
    parse_quiz_file('Knowledge_Assessment_Quiz_Math_Gr6.md', 'quiz_math_data.json', 'แบบทดสอบประเมินผลความรู้คณิตศาสตร์ ชั้น ป.6 (คณิตศาสตร์ Gr6 - MidFinal)')
    parse_quiz_file('Knowledge_Assessment_Quiz_Thai_Gr6.md', 'quiz_thai_data.json', 'แบบทดสอบประเมินผลความรู้ภาษาไทย ชั้น ป.6 (ภาษาไทย Gr6 - MidFinal)')
    parse_quiz_file('Knowledge_Assessment_Programming_Thai_Gr6.md', 'quiz_programming_data.json', 'แบบทดสอบประเมินผลความรู้เทคโนโลยีการคำนวณ ชั้น ป.6 (Coding & CT Gr6 - MidFinal)')
