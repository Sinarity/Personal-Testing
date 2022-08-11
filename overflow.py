from time import sleep

i = 1

for i in range(50):
    print(i)
    sleep(0.1)
    i += i
