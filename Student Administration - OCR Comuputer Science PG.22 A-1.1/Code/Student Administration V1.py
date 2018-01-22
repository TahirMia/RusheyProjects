#arrays
year_group=["7red", "7green", "7blue", "7yellow", "8red", "8green", "8blue", "8yellow", "9red", "9green", "9blue", "9yellow", "10red", "10green","10blue",\n\
            "10yellow","11red", "11green","11blue", "11yellow","12red", "12green","12blue", "12yellow","13red", "13green","13blue", "13yellow"]
#asks what year
yeargroup_ask=input("Please enter the tutor group you want to add a student to")
#finds in array
yeargroup_ask=yeargroup_ask.lower()
#error message
    if yeargroup_ask in year_group:
                x=0
else:
            print("Not valid try again")
            

            
