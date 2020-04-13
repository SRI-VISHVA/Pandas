import random
import pycountry


def generate_random_country():
    a = len(pycountry.countries)
    i = random.randint(0, a - 1)
    list1 = list(pycountry.countries)
    return (list1[i].name)


# print(generate_random_country())
