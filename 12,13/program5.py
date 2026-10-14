def compute_student_averages(grades):
    averages = {}
    for name in grades:
        total = 0
        for g in grades[name]:
            total = total + g
        averages.update({name: total / 3})
    return averages
def compute_class_averages(grades):
    totals = [0, 0, 0]
    count = 0
    for name in grades:
        for i in range(3):
            totals[i] = totals[i] + grades[name][i]
        count = count + 1
    class_averages = []
    for i in range(3):
        class_averages.append(totals[i] / count)
    return class_averages
grades = {}
print("Enter the name and three grades for each student.")
answer = input("Do you want to enter a student? (Yes/No): ")

while answer.lower() == "yes":
    entry = input("Enter name and three grades separated by commas: ")
    entryAsList = entry.split(",")
    scores = []
    for i in range(1, len(entryAsList)):
        scores.append(int(entryAsList[i]))
    name = entryAsList[0]
    grades.update({name: scores})
    answer = input("Do you want to enter another student? (Yes/No): ")
student_averages = compute_student_averages(grades)
class_averages = compute_class_averages(grades)
print()
print(f"{'Student':10} {'Exam 1':>8} {'Exam 2':>8} {'Exam 3':>8} {'Average':>9}")
for name in grades:
    g = grades[name]
    print(f"{name:10} {g[0]:>8} {g[1]:>8} {g[2]:>8} {student_averages[name]:>9.2f}")
print(f"{'Class Avg':10} {class_averages[0]:>8.2f} {class_averages[1]:>8.2f} {class_averages[2]:>8.2f}")