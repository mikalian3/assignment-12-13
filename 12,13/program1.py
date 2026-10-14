def load_names(names):
    for i in range(10):
        name = input(f"Enter last name {i + 1}: ")
        names.append(name)
    return names
def display_names(names):
    print("Names in order:")
    for item in names:
        print(item)
def display_names_reverse(names):
    print("Names in reverse order:")
    i = len(names) - 1
    while i >= 0:
        print(names[i])
        i = i - 1
last_names = []
last_names = load_names(last_names)
print(last_names)
print()
display_names(last_names)
print()
display_names_reverse(last_names)