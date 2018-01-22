tries=1
account=input("Please enter a 8 digit account number.\n")
while tries>0:
      weight=[8,7,6,5,4,3,2,1]
      mult=[]
      for i in range (8):
            num=(int(account[i])*weight[i])
            mult.append(num)
            total=sum(mult)
      modulus=total%11
      if modulus==0:
            print("This account number is valid.")
            break
      else:
            print("Invalid account number.")
      account=input("Please enter your account number again.\n")
