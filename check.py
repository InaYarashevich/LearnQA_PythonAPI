import requests

payload = {"login": "super_admin", "password": "welcome"}
response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
cookie_value = response.cookies.get('auth_cookie')
cookies = {'auth_cookie': cookie_value}
response_check = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
if response_check.text == "You are authorized":
    print(response_check.text)