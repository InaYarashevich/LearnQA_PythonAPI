import requests

class TestEx12:
    def test_check_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"

        response = requests.get(url)

        assert response.status_code == 200, "Wrong response code"
        print(response.headers)

        expected_header = "x-secret-homework-header"
        expected_header_value = "Some secret value"
        actual_header_value = response.headers.get('x-secret-homework-header')

        assert expected_header in response.headers, "There is no such header in the response"
        assert actual_header_value == expected_header_value, "There is no such header value in the response"
