#no vowels
message = input("Enter a message: ")
vowels="aeiou"
new_message=""
for letter in message:
    if letter.lower() not in vowels:
        print()
        new_message += letter
#new_message=""
        print("A new string has been created:", new_message)
        print("your message without vowels is:", new_message)
input("press the enter key to exit")
exit()
    
