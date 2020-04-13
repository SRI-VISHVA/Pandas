import random
from string import ascii_uppercase, ascii_lowercase


def generate_random_name():
    f_f = random.randint(4, 20)
    l_f = random.randint(4, 20)
    f1_name = ''.join(random.choice(ascii_uppercase) for i in range(1))
    f_name = ''.join(random.choice(ascii_lowercase) for i in range(f_f - 1))
    l1_name = ''.join(random.choice(ascii_uppercase) for i in range(1))
    l_name = ''.join(random.choice(ascii_lowercase) for i in range(l_f - 1))
    return f1_name + f_name + " " + l1_name + l_name


# generate_random_name()

# ALPHA_LIST = list(ascii_lowercase)


# def generate_random_name_2():
#     fn_length = random.randint(4, 20)
#     ln_length = random.randint(4, 20)
#     fn = ''
#     for index in range(1, fn_length):
#         fn += random.choice(ALPHA_LIST)
#
#     ln = ''
#     for index in range(1, ln_length):
#         ln += random.choice(ALPHA_LIST)
#
#     full_name = fn.capitalize() + ' ' + ln.capitalize()
#     print(full_name)
#
#
# generate_random_name_2()
