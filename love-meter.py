import os
import random
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    name1 = input("what is your name? ")
    name2 = input("what is your crush's name? ")
    number = random.randint(0, 100)
    print("calculating love meter...")
    print("your chance of love is " + str(number) + "%\n")