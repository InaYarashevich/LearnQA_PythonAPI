import requests

class TestEx11:
    def test_check_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)

        assert response.status_code == 200, "Wrong response code"
        print(dict(response.cookies))

        cookie = "HomeWork"
        cookie_value = response.cookies.get('HomeWork')
        
        assert cookie in response.cookies, "There is no such cookie"
        assert cookie_value == "hw_value", "There is no such cookie value"
