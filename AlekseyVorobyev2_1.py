def get_grade(score, best_score):
    if score >= best_score - 10:
        return 'A', 4.0
    elif score >= best_score - 20:
        return 'B', 3.0
    elif score >= best_score - 30:
        return 'C', 2.0
    elif score >= best_score - 40:
        return 'D', 1.0
    else:
        return 'F', 0.0

def main():
    while True:
        try:
            total_students = int(input("Total number of students: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    scores = []
    while len(scores) < total_students:
        try:
            score = int(input(f"Enter score for student {len(scores) + 1}: "))
            if score < 0 or score > 100:
                raise ValueError
            scores.append(score)
        except ValueError:
            print("Please enter a valid score between 0 and 100.")
    best_score = max(scores)
    for i, score in enumerate(scores):
        grade, gpa = get_grade(score, best_score)
        print(f"Student {i + 1} score is {score}, grade is {grade}, and GPA is {gpa}")

if __name__ == '__main__':
    main()
