#message analyzer
#demonstrate len() function and the "IN" opereation

#asks user for input
message = input("Enter your message text: ")

#prints out the message for the user
print("The length of your message is: ", len(message))

#tells the user what the most common letter is
print("The most common letter  in the english language, 'E'")

#says if the letter E is in the message typed in

if "e" in message:
    print("Is in your message. ")
else:
    print("Is not in your message")
