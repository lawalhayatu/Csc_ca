def calculate_percentage(score, total):
    return (score / total) * 100


def run_quiz():
    # 1. Setup: list of dictionaries
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "correct_answer": "C"
        },
        {
            "question": "Which language is used for web apps?",
            "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
            "correct_answer": "B"
        },
        {
            "question": "What is 5 + 3?",
            "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "correct_answer": "C"
        }
    ]

    score = 0

    # 2. Execute: loop through questions
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        # Display options
        for option in q["options"]:
            print(option)

        # 3. Interact: get user input
        answer = input("Enter your answer (A/B/C/D): ").upper()

        # 4. Evaluate
        if answer == q["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {q['correct_answer']}")

    # 5. Output result
    total_questions = len(questions)
    percentage = calculate_percentage(score, total_questions)

    print("\n--- Quiz Finished ---")
    print(f"Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 50:
        print("Result: PASS 🎉")
    else:
        print("Result: FAIL ❌")


# Run the quiz
if __name__ == "__main__":
    run_quiz()