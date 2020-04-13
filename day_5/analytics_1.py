# Objective
# To find the number of male candidates in the given data using pd.Series

# s

# s1
# 1     M
# 2     F
# 3     M
import csv
import pandas as pd
import numpy as np

# Create a list of list from csv
# From the list of list create the data for Series
# Pass the data to Series


id = []
gender = []

with open('D:\project\Pandas\day_2\employee_file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # line_count = 0
    for row in csv_reader:
        person = list(row.values())

        if person[3] == 'Male':
            gender.append(person[3])
            id.append(person[0])
        else:
            pass

# print(gender)
# print(id)
s = pd.Series(gender, index=id)
print(s.size)
# a = [['44606', 'Zuatlnnqdqnheyirx Jycvcxpfliovjny', '+4-578-119-3913', 'Male', '1943-04-25', 'Bachelor of Arts: BA',
#       'A RhD positive (A+)', 'Yes', 'Bulgaria', 'No', '1000001 - 2500000'],
#      ['44607', 'Mroewx Iyyefhrbutdhi', '+4-904-761-9979', 'Female', '1973-08-09', 'Bachelor of Commerce: Bcom',
#       'A RhD positive (A+)', 'Yes', 'Western Sahara', 'Yes', '1000001 - 2500000']]
#
# id = []
# gender = []
# for item in a:
#     id.append(item[0])
#     if item[3] == 'Male':
#         gender.append(item[3])
#     else:
#         gender.append(np.nan)
# print(gender)
# print(id)
# s = pd.Series(gender, index=id)
# print(s)
# print(s.index.dtype)
# for item in s['44606']:
#     print(item)
