# Objective
# To find the No of Unemployeed less than age of 50

import pandas as pd
from day_6.list_tuple import main_list
from datetime import date, datetime

today = date.today()


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


id = []
name = []

for row in main_list:
    person = list(row)
    try:
        date_object = datetime.strptime(person[4], '%Y-%m-%d').date()
    except ValueError:
        break
    if person[9] == 'No' and calculate_age(date_object) <= 50:
        name.append(person[1])
        id.append(person[0])
    else:
        pass

s = pd.Series(name, index=id)
print(s.size)
