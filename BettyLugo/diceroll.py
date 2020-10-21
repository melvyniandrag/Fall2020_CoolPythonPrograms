from random import randint
repeat = True
while repeat:
    print("you rolled a",randint(1,6))
    print("roll again?")
    repeat = ("yes") in input().lower()
