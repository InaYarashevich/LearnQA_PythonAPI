import csv
import time
from datetime import datetime

header = ['first_name', 'last_name', 'email']

emails = []
first_names = []
last_names = []

for i in range(100):
    base_part = "test"
    domain = "example.com"
    random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    email = f"{base_part}{random_part}@{domain}"
    first_name = f"{base_part}{random_part}"
    last_name = f"{base_part}{random_part}"
    emails.append(email)
    first_names.append(first_name)
    last_names.append(last_name)
    time.sleep(1)

with open('C:/Users/IT0054/Desktop/emails.csv', 'w', newline='\n', encoding='utf-8') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    f.write('\n'.join(emails))

