# with open("./Day_25/a.csv") as DataFile:
#     list = DataFile.readlines()
#     print(list)

import csv
with open("./Day_25/a.csv") as DataFile:
    data = csv.reader(DataFile)
    temperatures = []
    for row in data:
        print(row)
        if row[1]!='temp':
            temperatures.append(int(row[1]))
        
    print(temperatures)



import pandas
data = pandas.read_csv("./Day_25/a.csv")
print(data)
print(data["temp"])