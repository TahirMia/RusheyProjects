users=[["user1", "password1"],["user2", "password2"],["user3", "password3"]]
userEntry=""
found_Name=0
while userEntry=="":
      userEntry=input("Please enter your username.\n")
      userLen=len(users)
      for i in range (0, userLen):
            if userEntry in users[i]:
                  found_Name=1
                  passwordEntry=input("Please enter your password.")
                  if passwordEntry in users[i]:
                        print("Username and password are correct.")
                  else:
                        print("Sorry, the password is incorrect.")
                        userEntry=""
                        
      if found_Name==0:
            print("Username not recognised.")
            userEntry=""
