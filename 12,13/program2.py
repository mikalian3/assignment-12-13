def load_students(names, scores):
    for i in range(10):
        name = input(f"Enter last name {i + 1}: ")
        score = int(input(f"Enter exam score for {name}: "))
        names.append(name)
        scores.append(score)
    return names, scores

def display_students(names, scores):
    print(f"{'Last Name':12} {'Score':>6}")
    for i in range(len(names)):
        print(f"{names[i]:12} {scores[i]:>6}")

def display_students_reverse(names, scores):
    print(f"{'Last Name':12} {'Score':>6}")
    i = len(names) - 1
    while i >= 0:
        print(f"{names[i]:12} {scores[i]:>6}")
        i = i - 1
last_names = []
exam_scores = []
last_names, exam_scores = load_students(last_names, exam_scores)
print(last_names)
print(exam_scores)
print()
print("Students in order:")
display_students(last_names, exam_scores)
print()
print("Students in reverse order:")
display_students_reverse(last_names, exam_scores)