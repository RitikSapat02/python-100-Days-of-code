import pandas
data = pandas.read_csv("Day_25/squiral.csv")
grey_squiral_count = len(data[data["Primary Fur Color"]=="Gray"])
red_squiral_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squiral_count = len(data[data["Primary Fur Color"]=="Black"])

data_dict = {
    "Fur Color":["Grey","red","back"],
    "Count":[grey_squiral_count, red_squiral_count, black_squiral_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Day_25/count_squiral.csv")