import csv
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

# write data to csv file
with open('employee_file.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Id', 'Name', 'Mobile', 'Gender', 'D-O-B', 'Qualification', 'Blood Group', 'Marital Status', 'Country', 'Employement status', 'Salary']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # write header
    writer.writeheader()
    # write 50000 rows
    for i in range(0, 50000):
        writer.writerow({'Id': i+1, 'Name': generate_random_name(), 'Mobile': generate_random_mobile(), 'Gender': generate_random_gender(), 'D-O-B': get_random_date(), 'Qualification': generate_random_qualification(), 'Blood Group': generate_random_blood(), 'Marital Status': generate_random_M_status(), 'Country': generate_random_country(), 'Employement status': generate_random_E_status(), 'Salary': generate_random_sal()})
        i = i + 1
csv_file.close()

