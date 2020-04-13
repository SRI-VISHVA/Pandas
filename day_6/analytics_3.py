# Objective
# To find the average age of male and female candidates using pandas

import pandas as pd
import numpy as np
from day_6.list_tuple import main_list
from datetime import date, datetime
from datetime import date

today = date.today()


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


id = []
age = []

# line_count = 0
for row in main_list:
    person = list(row)
    try:
        date_object = datetime.strptime(person[4], '%Y-%m-%d').date()
    except ValueError:
        break
    if person[3] == 'Male':
        age.append(calculate_age(date_object))
        id.append(person[0])
    else:
        pass
s = pd.Series(age, index=id)
print("Average age of Male: " + str(np.average(s.values)))

id = []
age = []

# line_count = 0
for row in main_list:
    person = list(row)
    try:
        date_object = datetime.strptime(person[4], '%Y-%m-%d').date()
    except ValueError:
        break
    if person[3] == 'Female':
        age.append(calculate_age(date_object))
        id.append(person[0])
    else:
        pass
s = pd.Series(age, index=id)
print("Average age of Female: " + str(np.average(s.values)))
