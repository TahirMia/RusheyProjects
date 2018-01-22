from decimal import *
mes=input("What is your units? Gallons or Litres")
if mes == litres:    
    #Car Journey Exercise
    length=Decimal(input("What is the length of your journey(Miles)? "))
    ##print(length)#+"Miles")
    miles=Decimal(input("What is the Miles Per Litre of your car? "))
    ###print(miles)#+" Miles")
    petrol=Decimal(input("What is the cost of 1 litre of fuel for your car? "))
    ####print(petrol)
    final=(length/miles)*petrol
    print (float("{0:.2f}".format(final)))

    #####
elif mes == gallons:
    
    #Car Journey Exercise
    lengthG=Decimal(input("What is the length of your journey(Gallons)? "))
    ##print(length)#+"Miles")
    milesG=Decimal(input("What is the Gallons Per Litre of your car? "))
    ###print(miles)#+" Miles")
    petrolG=Decimal(input("What is the cost of 1 Gallon of fuel for your car? "))
    ####print(petrol)
    finalG=(lengthG/milesG)*petrolG
    print (float("{0:.2f}".format(finalG)))

#####


"""


#Car Journey Exercise
length=Decimal(input("What is the length of your journey(Miles)? "))
##print(length)#+"Miles")
miles=Decimal(input("What is the Miles Per Litre of your car? "))
###print(miles)#+" Miles")
petrol=Decimal(input("What is the cost of 1 litre of fuel for your car? "))
####print(petrol)
final=(length/miles)*petrol
print (float("{0:.2f}".format(final)))

#####

""""
