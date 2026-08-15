# # give me the temp data from csv
# # import csv

# # with open("./weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []

# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# # print(temperatures)


# # Do the same but with pandas
# import pandas

# data = pandas.read_csv("./weather_data.csv")

# # Two primary data structures in pandas. Series and DataFrame/
# # The whole table is the DataFrame and each column is a series.
# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = data["temp"].to_list()
# # # in vanilla python
# # print(round(sum(temp_list) / len(temp_list), 2))
# # # in pandas
# # print(round(data['temp'].mean(), 2))

# # find the maximum value of data in pandas
# # print(data['temp'].max())
# # find row of data for monday
# # print(data[data.day == 'Monday'])
# # find the row of data for highest temp of the week
# # print(data[data.temp == data.temp.max()])
# # print monday's temp but in farenheit
# # temp_celcius = data[data.day == 'Monday'].temp[0]
# # print(temp_celcius * 1.8 + 32)

# # create a dataframe from scratch
# # data_dict = {
# #     "students": ["Amy", "James", "Angela", "Sourav"],
# #     "scores": [76, 56, 65, 88]
# # }

# # data = pandas.DataFrame(data_dict)
# # print(data)
# # create and add the data to csv file
# # data.to_csv("student_score.csv")

# find the total number of squirrels for each fur color and create a csv file with that dataframe
# import pandas
# data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
# cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
# black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])
# # print(grey_squirrels_count)
# # print(cinnamon_squirrels_count)
# # print(black_squirrels_count)

# data_dict = {"Fur Color": ["Grey", "Cinnamon", "Black"],
#                  "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]}

# data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv("squirrel_color_count.csv")

