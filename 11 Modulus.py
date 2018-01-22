account=input("Please enter a 7 digit account number.\n")
weight=[8,7,6,5,4,3,2]
mult=[]
for i in range (7):
      num=(int(account[i])*weight[i])
      mult.append(num)
      total=sum(mult)
modulus=total%11
check_digit=11-modulus
print("The check digit is", check_digit,".")
print("So the full account number is", account+str(check_digit))
