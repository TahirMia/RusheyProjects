import random

#think of number
computer_number = random.randint(1,100)

#function isit_name
def isit_same(target, number):
    if target==number:
        result="win"
    while target > number:
        result="low"
    else:
        result="high"
    return result
#start the game
print("Hello, Ive thought of a number between 1 to 100")
guess= int(input("Can you guess it?"))
high_low = isit_same(computer_number,guess)
while high_low != "win":
    if high_low == "low":
        guess=int(input("sorry you are too low. try again"))
    else:
        guess=int(input("sorry you are too high. try again"))

    high_low = isit_same(computer_number,guess)


#end game
    input("correct")
