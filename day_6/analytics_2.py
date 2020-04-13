# Objective
# To find the No of Male Candidate Of age between 18-24 in employee_file.csv using pandas

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
    if person[3] == 'Male' and 18 <= calculate_age(date_object) <= 24:
        name.append(person[1])
        id.append(person[0])
    else:
        pass

s = pd.Series(name, index=id)
print(s.size)
