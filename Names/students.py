import names
from time import sleep

students = []

homeroom = 3000

nameid = homeroom

while nameid != 0:
    students.append(names.get_full_name(gender="male"))
    nameid-=1
students = list(set(students))

for i in range(len(students)):
    print(i +1, students[i])
    sleep(0.01)
print(f"You removed {homeroom - i} duplicates.")
    
    