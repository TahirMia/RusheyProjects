S=[]
print("Welcome to the bubble sort algorithm")
i=1
while i<8:
    num=input("Please enter a number:")
    if num!=int:
        print("Invalid entry try again.")
        break
    else:
        S.append(num)
        i=i+1

N=len(S)
swapped=True
while swapped==True:
    swapped=False
    for x in range(1,N):
        if S[x-1]>S[x]:
            temp=S[x-1]
            S[x-1]=S[x]
            S[x]=temp
            swapped=True
            print(S)
            x=x+1
    print(S)
