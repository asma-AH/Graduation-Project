from faker import Faker
#from hotel.models import User
import csv
import psycopg2

from hotel.models import User



fake = Faker()
csvfile = "C:\\Users\\Nadir Pervez\\Documents\\Graduation-Project\\GG.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for _ in range(10):
        print(fake.name())  # adding it to DB
        b = User(firstname=fake.name())
        writer.writerow([fake.name()])
        b.save()

