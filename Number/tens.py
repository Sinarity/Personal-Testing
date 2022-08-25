from random import randrange
from time import sleep
from colorama import Fore

i = 5
while i > 0:
    print("", i, end="", flush=True)
    print("\r", end="", flush=True)
    sleep(1)
    i -= 1

attempts = 1

while True:
    i = randrange(0, 1000000)
    j = randrange(0, 1000000)
    if i != j:
        print(
            Fore.WHITE + f" #{attempts} | {i} is not equal to {j}.", end="", flush=True
        )
        print("\r", end="  ", flush=True)
        attempts += 1
    else:
        print("", end=" ", flush=True)
        sleep(1)
        print(Fore.GREEN + f"        #{attempts} | {i} is equal to {j}.")
        print(Fore.LIGHTMAGENTA_EX + "========================================================")
        print(
            Fore.RED
            + f"It took {attempts:,} attempts to match i and j together."
            + Fore.RESET
        )
        break
