import csv
import time
from datetime import datetime

header = ['first_name', 'last_name', 'email']

emails = []
first_names = []
last_names = []

data = [first_names, last_names, emails]

base_part = "test"
domain = "example.com"
random_part = datetime.now().strftime("%m%d%Y%H%M%S")
for i in range(100):

    email = f"{base_part}{random_part}@{domain}"
    first_name, last_name = f"{base_part}{random_part}", f"{base_part}{random_part}"

    emails.append(email)
    first_names.append(first_name)
    last_names.append(last_name)

    time.sleep(1)

with open(f"C:/Users/IT0054/Desktop/test_data_{random_part}.csv", 'w', newline='\n', encoding='utf-8') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerow(data)

    # f.write('\n'.join(first_names))
