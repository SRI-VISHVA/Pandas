# List of list
# Tuple of tuple
import csv
import timeit

main_list = []
s2_t = timeit.default_timer()
with open('D:\project\Pandas\day_2\employee_file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # line_count = 0
    for row in csv_reader:
        person = list(row.values())
        main_list.append(person)
e2_t = timeit.default_timer()
csv_file.close()
# print(main_list)
# print('Time taken to create a list of lists: %f' % (e2_t - s2_t))
# print(abs((e2_t - s2_t) - (e1_t - s1_t)))

# main_tuple = ()
# s1_t = timeit.default_timer()
# with open('D:\project\Pandas\day_2\employee_file.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
    # for row in csv_reader:
    #     person = tuple(row.values())
    #     main_tuple += person,
# e1_t = timeit.default_timer()
# csv_file.close()
# print(main_tuple)
# print(type(e1_t - s1_t))
# print('Time taken to create tuple of tuples: %f' % (e1_t - s1_t))

# print(type(main_list))
# print(type(main_tuple))

# s_t = timeit.default_timer()
# for item in main_tuple:
#     pass
# print(timeit.default_timer()-s_t)
#
# s_t = timeit.default_timer()
# for item in main_list:
#     pass
# print(timeit.default_timer()-s_t)


# D:\project\Pandas\venv\Scripts\python.exe D:/project/Pandas/day_6/list_tuple.py
# Time taken to create a list of lists: 5.931704
# <class 'float'>
# Time taken to create tuple of tuples: 3758.193002
# <class 'list'>
# <class 'tuple'>
# 0.02227279999988241
# 0.04035229999999501
#
# Process finished with exit code 0
