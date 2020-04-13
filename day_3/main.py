import csv
import timeit
import os
from day_2.date import get_random_date
from day_2.name import generate_random_name
from day_2.bloodgroup import generate_random_blood
from day_2.country import generate_random_country
from day_2.employment import generate_random_E_status
from day_2.gender import generate_random_gender
from day_2.marital import generate_random_M_status
from day_2.mobile import generate_random_mobile
from day_2.qualification import generate_random_qualification
from day_2.salary import generate_random_sal
from day_2.date import get_random_date1
from day_3.functions import sizeof_fmt

n = input("Please Enter the corresponding number:\n1. Create a New Data Set\n2. Use an exsisting Data Set\n>>>")

if int(n) == 1:
    start_time = timeit.default_timer()
    print("Creating a New Data Set...")
    with open('D:\project\Pandas\day_2\employee_file.csv', mode='w', newline='') as csv_file:
        fieldnames = ['Id', 'Name', 'Mobile', 'Gender', 'D-O-B', 'Qualification', 'Blood Group', 'Marital Status',
                      'Country',
                      'Employement status', 'Salary']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # write header
        writer.writeheader()
        # write 50000 rows
        for i in range(0, 50000):
            writer.writerow(
                {'Id': i+1, 'Name': generate_random_name(), 'Mobile': generate_random_mobile(),
                 'Gender': generate_random_gender(),
                 'D-O-B': get_random_date1(), 'Qualification': generate_random_qualification(),
                 'Blood Group': generate_random_blood(), 'Marital Status': generate_random_M_status(),
                 'Country': generate_random_country(), 'Employement status': generate_random_E_status(),
                 'Salary': generate_random_sal()})
            i = i + 1
    print("New Data Set Created")
    csv_file.close()
    print(timeit.default_timer() - start_time)
    # print(os.path.getsize("D:\project\Pandas\day_2\employee_file.csv"))
    print(sizeof_fmt(os.path.getsize("D:\project\Pandas\day_2\employee_file.csv")))
elif int(n) == 2:
    start_time = timeit.default_timer()
    input_file = open("D:\project\Pandas\day_2\employee_file.csv", "r+")
    reader_file = csv.reader(input_file)
    n = len(list(reader_file))
    with open('D:\project\Pandas\day_2\employee_file.csv', mode='a', newline='') as csv_file:
        fieldnames = ['Id', 'Name', 'Mobile', 'Gender', 'D-O-B', 'Qualification', 'Blood Group', 'Marital Status',
                      'Country',
                      'Employement status', 'Salary']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow(
            {'Id': n-1, 'Name': generate_random_name(), 'Mobile': generate_random_mobile(),
             'Gender': generate_random_gender(),
             'D-O-B': get_random_date(), 'Qualification': generate_random_qualification(),
             'Blood Group': generate_random_blood(), 'Marital Status': generate_random_M_status(),
             'Country': generate_random_country(), 'Employement status': generate_random_E_status(),
             'Salary': generate_random_sal()})
    print(timeit.default_timer() - start_time)
    print(sizeof_fmt(os.path.getsize("D:\project\Pandas\day_2\employee_file.csv")))
else:
    print("Enter a Valid Option")
