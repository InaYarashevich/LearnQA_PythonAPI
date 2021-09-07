import requests
import json
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestTask16(BaseCase):
    def test_get_another_user(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'Ina',
            'lastName': 'Test',
            'email': 'testQA3@example.com'
            }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        parsed_response = response.json()
        user_id = parsed_response["id"]
        print(user_id)

        data1 = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data1)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        print(response2.text)
        expected_fields = ["username"]
        Assertions.assert_json_has_keys(response2, expected_fields)
        Assertions.assert_json_has_not_key(response2, "email")
        Assertions.assert_json_has_not_key(response2, "firstName")
        Assertions.assert_json_has_not_key(response2, "lastName")
