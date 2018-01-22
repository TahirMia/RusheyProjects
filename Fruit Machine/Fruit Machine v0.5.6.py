import random

def fruit_machine():

    start = input("\nPlease press enter to start or 9 to quit:")
    if start  == "9":
        exit()
    while True:
        
        wheel = ["banana", "cherry", "apple", "pear "]

        wheel1pick = random.choice(wheel)
        wheel2pick = random.choice(wheel)
        wheel3pick = random.choice(wheel)

        print(wheel1pick," | ", wheel2pick," | ", wheel3pick)

        if wheel1pick == wheel2pick == wheel3pick:
            print("\nJackpot!!!")
            fruit_machine()
        elif wheel1pick == wheel3pick:
            print("\nGrandma's Teeth!!!")
            fruit_machine()


fruit_machine()

