# data = []
#
# with open('weather_data.csv') as weather_file:
#     weather_file.readline()
#     for line in weather_file.readlines():
#         data.append(line.strip().split(','))
#
# print(data)


# import csv
#
# with open('weather_data.csv') as weather_file:
#     weather = csv.reader(weather_file)
#     for row in weather:
#         if row[1].isnumeric():
#             print(row[1])

import pandas

# data = pandas.read_csv('weather_data.csv')

# data_temp_list = data['temp'].to_list()
# print(round(sum(data_temp_list) / len(data_temp_list), 2))
# print(data[data.temp == data.temp.max()])

# print(data[data.day == 'Monday'].temp)

"create a dataframe with pandas"
# my_dict = {"name": ['Joe', 'Bob', 'Charlie'], 'score': [95, 85, 71]}
# my_csv = pandas.DataFrame(my_dict)
# print(my_csv)
# my_csv.to_csv('my_dict.csv')

# save the csv as pandas dataframe

raw_data = pandas.read_csv('raw_data.csv')
fur_data = raw_data['Primary Fur Color'].dropna().to_list()
unique_fur_colors = sorted(set(fur_data))
my_dict = {'Fur Color': [], 'Count': []}
for color in unique_fur_colors:
    my_dict['Count'].append(fur_data.count(color))
    my_dict['Fur Color'].append(color)

my_sq_data = pandas.DataFrame(my_dict)
my_sq_data.to_csv('my_sq_data.csv')

# print(raw_data['Primary Fur Color' == 'Gray'].count())




my_squirrel_dict = {'fur': [], 'count': []}
