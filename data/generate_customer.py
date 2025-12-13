import csv
import random
from datetime import datetime, timedelta
import faker

fake = faker.Faker()

countries = ["USA", "Canada", "UK", "Germany", "France", "Australia", "India"]

with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id", "first_name", "last_name", "signup_date", "country", "age"])

    for i in range(1, 201):  # 200 rows
        first = fake.first_name()
        last = fake.last_name()
        signup_date = fake.date_between(start_date='-2y', end_date='today')
        country = random.choice(countries)
        age = random.randint(18, 70)

        writer.writerow([i, first, last, signup_date, country, age])
