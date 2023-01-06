import pandas
data = pandas.read_csv("./Day_25/a.csv")
# print(type(data))
# print(type(data['temp']))
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# avg_temp = sum(temp_list)/len(temp_list)
# print(f"average temperature: {avg_temp}")

print(data["temp"].mean())

print(data['temp'].max())

#get data in colums
print(data["condition"])
print(data.condition)

#get data in rows
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)


#create a dataframe from scratch

data_dict = {
    "students":["Amy","James","Angela"],
    "scores":[76,56,65],
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Day_25/new_data.csv")