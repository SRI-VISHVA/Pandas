import random
import datetime

a = []
for i in range(1930, 2019):
    a.append(i)


def get_random_date_year(year):
    # try to get a date
    try:
        return datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y')
    except ValueError:
        return get_random_date_year(year)


def get_random_date():
    year = random.choice(a)
    return get_random_date_year(year)


def get_random_month():
    month = random.randint(1, 12)
    return month


def get_random_day():
    day = random.randint(1, 31)
    return day


def get_random_year():
    year = random.choice(a)
    return year


def get_random_date1():
    try:
        x = datetime.date(year=get_random_year(), month=get_random_month(), day=get_random_day())
        return x
    except ValueError:
        pass
