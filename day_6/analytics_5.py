# Objective
# Create a series with age_range vs population
import pandas as pd
from day_6.list_tuple import main_list
from datetime import date, datetime
import matplotlib.pyplot as plt


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
id = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

for row in main_list:
    person = list(row)
    try:
        date_object = datetime.strptime(person[4], '%Y-%m-%d').date()
    except ValueError:
        break
    if 0 < calculate_age(date_object) < 10:
        count[0] += 1
    elif 11 < calculate_age(date_object) < 20:
        count[1] += 1
    elif 21 < calculate_age(date_object) < 30:
        count[2] += 1
    elif 31 < calculate_age(date_object) < 40:
        count[3] += 1
    elif 41 < calculate_age(date_object) < 50:
        count[4] += 1
    elif 51 < calculate_age(date_object) < 60:
        count[5] += 1
    elif 61 < calculate_age(date_object) < 70:
        count[6] += 1
    elif 71 < calculate_age(date_object) < 80:
        count[7] += 1
    elif 81 < calculate_age(date_object) < 90:
        count[8] += 1
    elif 91 < calculate_age(date_object) < 100:
        count[9] += 1
    else:
        pass
s = pd.Series(count, index=id)
print(s)
s.plot.bar(x=s.index, y=s.values)
plt.show()
s.plot.line(x=s.index, y=s.values)
plt.show()
