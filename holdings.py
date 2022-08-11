import csv
from datetime import datetime, date, timedelta
import random
from csv import reader

with open('C:/Users/IT0054/Desktop/holdings_04152022_1.csv', 'w', newline='\n', encoding='utf-8') as f:
    header = ['client_id', 'effective_date', 'ticker', 'quantity', 'amount', 'description']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()

# with open("C:/Users/IT0054/Desktop/instruments.csv") as csvfile:
#
#     csvreader = reader(csvfile)
#     rows = []
#     for row in csvreader:
#         rows.append(row)
#     print(rows)
#     csvfile.close()

    for i in range(1000):
        client_id = random.randint(2001, 2050)

        start_date = date(2022, 2, 15)
        end_date = datetime.today().date()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)


        effective_date = start_date + timedelta(days=random_number_of_days)

        quantity = random.randint(1, 100)

        random_amount = round(random.uniform(10000.01, 1000000.99), 2)

        writer.writerow({'client_id': client_id, 'effective_date': effective_date,
                         'quantity': quantity, 'amount': random_amount})
