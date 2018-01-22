users=[["user1", "password1"], ["user2", "password2"], ["user3", "password3"]]
userEntry=""
found_Name=0
tries=1
while userEntry=="":
    userEntry=input("Please enter your username\n")
    usersLen=len(users)
    for i in range (0, usersLen):
        if userEntry == users[i][0]:
            found_Name=1
            while tries<=3:
                passwordEntry=input("Please enter your password\n")
                if passwordEntry == users[i][1]:
                    print("Username and password are correct.")
                    break
                else:
                    print("Sorry, the password is incorrect.")
                    userEntry=""
                    userEntry==""
                    tries=tries+1
                if tries==4:
                    print("You have now been blocked.")
    if found_Name==0:
        print("Username not recognised.")
        userEntry=""
    break  
