import string
import random
import functools


def generate_random_mobile():
    a = functools.partial(random.randint, 0, 9)
    return ("+{}-{}{}{}-{}{}{}-{}{}{}{}".format(a(), a(), a(), a(), a(), a(), a(), a(), a(), a(), a()))


# print(generate_random_mobile())

def generate_random_mobile_2():
    x = list(string.digits)
    m = ''
    for item in range(0, 10):
        if random.choice(x) != 0:
            m += random.choice(x)

    return m


def generate_random_mobile_3():
    x = list(string.digits)
    m = ''
    count = 1
    for item in range(0, 10):
        if count == 1:
            m += random.choice(x[1:])
        else:
            m += random.choice(x)
        count += 1
    return m


def generate_random_mobile_4():
    x = list(string.digits)
    m = str(random.choice(x[1:]))
    for item in range(0, 9):
        m += random.choice(x)
    return m

# TODO to calculate time when x is not declared and list(string.digits) is used directly in for loop.
