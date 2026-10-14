grades = {}
total = 0
count = 0
print("Enter the name and grade for each student.")
answer = input("Do you want to enter a student? (Yes/No): ")
while answer.lower() == "yes":
    entry = input("Enter name and grade separated by a comma: ")
    entryAsList = entry.split(",")
    name = entryAsList[0]
    grade = int(entryAsList[1])
    grades.update({name: grade})
    answer = input("Do you want to enter another student? (Yes/No): ")
print()
print(f"{'Student Name':10} {'Grade':>6}")
for name in grades:
    print(f"{name:10} {grades[name]:>6}")
    total = total + grades[name]
    count = count + 1
class_average = total / count
print()
print(f"{'Class Average':10} {class_average:>6.2f}")