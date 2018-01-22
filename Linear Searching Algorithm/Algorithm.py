textfile=open("N:\\KS4\\Computer Science\\Python\\Linear Searching Algorithm\\names.txt","r")
#print(textfile.read())
f=textfile.read()
trgt=input("enter a name")
if trgt in f:
    print(trgt,"found")
else:
    print(trgt,"not Found")
