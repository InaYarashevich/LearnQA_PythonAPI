import requests

class TestEx11:
    def test_check_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)

        assert response.status_code == 200, "Wrong response code"
        print(dict(response.cookies))

        expected_cookie = "HomeWork"
        expected_cookie_value = "hw_value"
        actual_cookie_value = response.cookies.get('HomeWork')

        assert expected_cookie in response.cookies, "There is no such cookie"
        assert actual_cookie_value == expected_cookie_value, "There is no such cookie value"
