import csv

#reading file
ifile = open("username.csv", "r")
readCSV = csv.reader(ifile)
#printing file
for row in readCSV:
    #print(row)
    #print(row[0])
    print(row[0], row[1], row[2], row[3])
