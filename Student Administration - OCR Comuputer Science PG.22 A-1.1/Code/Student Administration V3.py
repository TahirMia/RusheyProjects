from tkinter import *
import sys
#continue_more=True

top = Tk()
top.option_add( "*font", "lucida 14" )
top.title("Test00") # Change this to your name
top.configure(background='blue') # Choose your own background colour
top.geometry("1000x500") # Experiment with different sizes or your window
txt1 = Text(top, width=60, height=2)
txt1.configure(background='white')    # Choose your own colour
txt1.grid(row=5,column=5)              
txt2 = Text(top, width=60, height=6)
txt2.configure(background='white')    # Choose your own colour
txt2.grid(row=6,column=5)

txt1.delete(0.0, END)
txt1.insert(0.0,"Test")
txt2.delete(0.0, END)
txt2.insert(0.0,"test1")

"""
years=["7", "8", "9","10", "11", "12", "13"]
form=["RED", "GREEN", "BLUE", "YELLOW"]
print("Welcome to the student admin program")

numbers="1234567890"
forename_valid=True
surname_valid=True

while forename_valid==True:
    forename=str(input("What is the student's first name?\n"))
    if forename.isalpha():
        forename_valid=False
    else:
        print("Please enter a valid forename")


        

while surname_valid==True:
    surname=str(input("What is the student's secondname?\n"))
    if surname.isalpha():
        surname_valid=False
    else:
        print("Please enter a valid surname")


yeargroup=""
found=0
while yeargroup=="":
    yeargroup=input("What year is the student in?\n")
    yearLen=len(years)
    for i in range (0, yearLen):
        if yeargroup==years[i]:
            print("Thank you")
            found=1
    if found==0:
        print("Invalid entry. Try again.")
        yeargroup=""



formgroup=""
found=0

while formgroup=="":
    formgroup=input("What form would the student be in? \n")
    formgroup=formgroup.upper()
    formlen=len(form)
    for i in range (0, formlen):
        if formgroup==form[i]:
            print("Thank you")
            found=1
    if found==0:
        print("Invalid entry. Try again.")
        formgroup=""


textfile=open("N:\KS4\Computer Science\Python\Student Administration - OCR Comuputer Science PG.22 A-1.1\Code\Stored\student_data.txt", "a")
textfile.write(forename+ " " + surname + " " + yeargroup + formgroup + "\n")
textfile.close()


textfile=open("N:\KS4\Computer Science\Python\Student Administration - OCR Comuputer Science PG.22 A-1.1\Code\Stored\student_data.txt", "r")
print(textfile.read())
textfile.close()

#continue_more
while continue_more == True:
    continue1=input("Would you like to add another student? Y or N")
    continue1=continue1.upper()
    if continue1 == "Y":
        continue_more()
    else:
        continue_more=False
        sys.exit()
"""
