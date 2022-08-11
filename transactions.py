import csv
from datetime import datetime, date, time, timedelta
import random

with open('C:/Users/IT0054/Desktop/transaction_03092022_1.csv', 'w', newline='\n', encoding='utf-8') as f:
    header = ['client_id', 'date', 'transaction_type', 'ticker', 'CUSIP', 'ISIN', 'lipper_id', 'amount',
              'currency', 'description']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()

    for i in range(1000):
        client_id = random.randint(5001, 5050)

        start_date = date(2022, 7, 25)
        end_date = datetime.today().date()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)

        random_date = start_date + timedelta(days=random_number_of_days)

        transaction_type = 'Buy'

        random_amount = round(random.uniform(10000.01, 5000000.99), 2)
        with open("C:/Users/IT0054/Desktop/instruments.csv") as csvfile:
            writer.writerow({'client_id': client_id, 'date': random_date, 'amount': random_amount,
                             'transaction_type': transaction_type})


