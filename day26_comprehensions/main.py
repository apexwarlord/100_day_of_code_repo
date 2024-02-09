# names = ["alex", "beth", "caroline", "david", "freddie", "gabriel", "harry"]
#
# my_list = [name.upper() for name in names if len(name) > 5]


# import gc
#
# with open('file1.txt') as f1, open('file2.txt') as f2:
#     f1, f2 = f1.readlines(), f2.readlines()
# result = [n.strip() for n in f1 if n in f2]
# print(result)
# print(gc.get_stats())
# result2 = [n.strip() for n in open('file1.txt').readlines() if n in open('file2.txt').readlines()]
# print(gc.get_stats())
# print(result2)

# grades = {'Alex': 69, 'Bob': 80, 'Carol': 70, 'Dave': 60, 'Eve': 50, 'Fred': 40, 'Ginny': 40}
#
# passers = {name: grade for name, grade in grades.items() if grade > 59}
# print(passers)

sentence = "What is the Airspeed Velocity of an Unladen Swallow"

my_dict = {word: len(word) for word in sentence.split()}

print(my_dict)

weather_c = {
    'student': ['Alice', 'Bob', 'Charlie'],
    'score': [87, 96, 80],
}

# f_dict = {day: temp*9/5+32 for day, temp in weather_c.items()}
# print(f_dict)

import pandas

weather_d_f = pandas.DataFrame(weather_c)
print(weather_d_f)

for index, row in weather_d_f.iterrows():
    print(row.student, row.score)
