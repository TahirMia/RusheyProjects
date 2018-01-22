from random import choice
word = choice(["code", "club"])
guessed = []
wrong = []
tries = 20
while tries >0:
    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter   
        else:
            out = out + "-----"
    if out == word:
        break
    print("Guess the word, enter 1 letter at a time:", out)
    print(tries, "chances left")
    guess = input()
    if guess in guessed or guess in wrong:
        print("Already guessed", guess)  
    elif guess in word:
        print("Yay")
        guessed.append(guess)    
    else:
        print("Nope")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("You guessed", word)
else:
    print("You didn't get", word)
