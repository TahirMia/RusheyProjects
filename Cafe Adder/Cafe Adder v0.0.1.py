###File IO locations
print("Welcome to the cafe\n")
textfile=open("N:\KS4\Computer Science\Python\Cafe Adder\Cafe.txt", "w")
textfile.write("Here is the menu...\n\n\
Coffee-£2\n\
Cake-£2\n\
Chocolate-£1\n\
Toast-£1\n\
Muffin-£1\n\
English Breakfast-£4\n\
Egg-£1\n\
Donut-£1\n")
textfile.close()
textfile=open("N:\KS4\Computer Science\Python\Cafe Adder\Cafe.txt", "r")
print(textfile.read())
textfile.close()
print()
Menu=[["Coffee", "2"], ["Cake", "2"], ["Chocolate", "1"], ["Toast", "1"], ["Muffin", "1"], ["English Breakfast", "4"], ["Egg", "1"], ["Donut", "1"]]
costs=[]
choice=""
tries=1
textfile=open("N:\KS4\Computer Science\Python\Cafe Adder\bill.txt", "w")
textfile.write("Here is the bill\n")
while choice=="":
    found=0
    choice=input("What would you like to order? Case sensitive\n")
    MenuLen=len(Menu)
    for i in range (0, MenuLen):
        if choice==Menu[i][0]:
            found=1
            cost=Menu[i][1]
            costs.append(float(cost))
            textfile=open("N:\KS4\Computer Science\Python\Cafe Adder\bill.txt", "a")
            length=len(choice)
            spaces=11-length
            textfile.write(choice+(" "*spaces)+"£"+cost+"\n")
            textfile.close()
            print("You have ordered a ", choice)
            left=5-tries
            order1=input("Would you like anything else?(Y/N)You can order "+str(left)+" more items.\n")
            if order1=="Y" and tries<5:
                choice=""
                tries=tries+1
            else:
                break
    if found==0:
        print("This choice isn't recognised")
        choice=""

Total=sum(costs)
print("Are you eating in or taking out?")
location=input()
if location=="taking out":
    Total=Total*1.2
else:
    print("You are eating in.")
pensioner=input("Are you a pensioner?(Y/N)")
if pensioner=="Y":
    Total=Total*0.8
Total=round(Total, 2)
Total=str(Total)
Total_len=len(Total)
if Total_len==3 or 4:
    Total=Total+"0"
textfile=open("N:\KS4\Computer Science\Python\Cafe Adder\bill.txt", "r")
print(textfile.read())
print("The total cost of your order is £",str(Total))
