from decimal import *

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
