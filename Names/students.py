import names
from time import sleep

students = []

homeroom = 3000

nameid = homeroom

# for random full names, use names.get_full_name() gender="male/female" is optional.
# for random first names, use names.get_first_name() gender="male/female" is optional.
# for random last names, use names.get_last_name() gender="male/female" is optional.

while nameid != 0:
    students.append(names.get_first_name(gender=""))
    nameid -= 1
students = list(set(students))

for i in range(len(students)):
    print(i + 1, students[i])
    sleep(0.01)
print(f"You removed {homeroom - i} duplicates.")
