def load_students(names, scores):
    for i in range(10):
        name = input(f"Enter last name {i + 1}: ")
        score = int(input(f"Enter exam score for {name}: "))
        names.append(name)
        scores.append(score)
    return names, scores

def display_high_low(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print(f"Highest score: {names[high_index]} - {high_var}")
    print(f"Lowest score:  {names[low_index]} - {low_var}")
last_names = []
exam_scores = []
last_names, exam_scores = load_students(last_names, exam_scores)
print(last_names)
print(exam_scores)
print()
display_high_low(last_names, exam_scores)