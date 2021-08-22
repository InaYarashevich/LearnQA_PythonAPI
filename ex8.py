import requests
import time

response_create_task = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
parsed_response = response_create_task.json()
print(response_create_task.text)
token = parsed_response["token"]
response_check_status = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={"token": token})
print(response_check_status.text)
time.sleep(7)
response_get_status = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={"token": token})
print(response_get_status.text)

