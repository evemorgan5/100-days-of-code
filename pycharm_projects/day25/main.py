# with open("weather_data.csv") as weather_files:
#     data = weather_files.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# pandas better formatting
# pandas takes first row as names of columns

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# print(type(data))
# # dataframe
#
# print(type(data["temp"]))
# #every column is a series in pandas, like a list
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
#
# print(dprint(data["temp"].mean())ata["temp"].mean())
# print(data["temp"].max())
#
# print(data["conditions"])

# get data in row
# print(data[data["day"] == "Monday"])
#
# max_temp = data["temp"].max()
# print(data[data["temp"] == max_temp])

# print(data[data["temp"] == data["temp"].max()])
# #
# monday = data[data["day"] == "Monday"]
# monday_temp = int(monday["temp"])
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#how many squirels of each colors

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data[data["Primary Fur Color"] == "Gray"])

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print("No. Gray:", grey_squirrels_count)
print("No. Black:", black_squirrels_count)
print("No. Red:", red_squirrels_count)


# create dictionary
data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrels_count, black_squirrels_count, red_squirrels_count]
}

# create df
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)
