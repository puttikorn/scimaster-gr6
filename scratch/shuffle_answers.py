import json
import random
import glob
import os

def analyze_and_shuffle_quiz(json_filepath):
    if not os.path.exists(json_filepath):
        print(f"File not found: {json_filepath}")
        return

    with open(json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data.get('questions', [])
    mcq_questions = [q for q in questions if q.get('section') == 'MCQ']
    
    if not mcq_questions:
        print(f"No MCQ questions found in {json_filepath}")
        return

    # Count initial distribution
    counts = {}
    for q in mcq_questions:
        ans = q.get('correctAnswer', '')
        counts[ans] = counts.get(ans, 0) + 1
    
    print(f"\n--- {os.path.basename(json_filepath)} ---")
    print(f"Total MCQ: {len(mcq_questions)}")
    print(f"Initial Distribution: {counts}")

    # Prepare target answers for perfect balance
    n = len(mcq_questions)
    letters = ['ก', 'ข', 'ค', 'ง']
    # If letters are A, B, C, D in some files
    if any(q.get('correctAnswer') in ['A', 'B', 'C', 'D'] for q in mcq_questions):
        letters = ['A', 'B', 'C', 'D']

    target_list = []
    base_count = n // len(letters)
    rem = n % len(letters)
    for i, l in enumerate(letters):
        target_list.extend([l] * (base_count + (1 if i < rem else 0)))

    # Seed for deterministic reproducibility
    random.seed(42)
    random.shuffle(target_list)

    # Re-shuffle options for each MCQ question
    for idx, q in enumerate(mcq_questions):
        curr_ans = q.get('correctAnswer')
        options = q.get('options', {})
        
        if curr_ans not in options:
            continue

        correct_text = options[curr_ans]
        wrong_texts = [v for k, v in options.items() if k != curr_ans]
        random.shuffle(wrong_texts)

        target_ans = target_list[idx]
        
        new_options = {}
        wrong_idx = 0
        for l in letters:
            if l == target_ans:
                new_options[l] = correct_text
            else:
                new_options[l] = wrong_texts[wrong_idx]
                wrong_idx += 1

        q['options'] = new_options
        q['correctAnswer'] = target_ans

    # Verify new distribution
    new_counts = {}
    for q in mcq_questions:
        ans = q.get('correctAnswer', '')
        new_counts[ans] = new_counts.get(ans, 0) + 1

    print(f"New Distribution: {new_counts}")

    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully updated {json_filepath}")

if __name__ == '__main__':
    project_dir = "/Users/puttikornleawalit/Documents/Document/Personal/Student/MidFinal-GR6-2026_0.1"
    json_files = glob.glob(os.path.join(project_dir, "quiz*.json"))
    for jf in sorted(json_files):
        analyze_and_shuffle_quiz(jf)
