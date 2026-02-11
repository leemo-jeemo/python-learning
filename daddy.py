import os
os.system('cls' if os.name == 'nt' else 'clear')

while True: 
    name = input("what is your name? ")
    say = input("what do you want to say? ")
    if say == say.upper():
        print(say + ", DADDY " + name.upper())
    else: 
        print(say + ", daddy " + name)