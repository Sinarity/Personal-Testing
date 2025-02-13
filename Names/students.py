from time import sleep
from faker import Faker

fake = Faker()


students = []


homeroom = int(input("How many students are in your homeroom? "))


nameid = homeroom


for i in range(homeroom):
    students.append(fake.name())

# for random full names, use name()
# for random first names, use first_name()
# for random last names, use last_name() 
students = list(sorted(set(students)))
#removes duplicates

for i in range(len(students)):
    print(i + 1, students[i])
    sleep(0.01)
print(f"You removed {homeroom - i} duplicates.")
