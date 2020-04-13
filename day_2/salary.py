import random

sal = ["less than 50000", "50000 - 100000", "100001 - 300000", "300001-500000", "500001 - 1000000", "1000001 - 2500000",
       "More than 2500000"]


def generate_random_sal():
    return random.choice(sal)


# print(generate_random_sal())
