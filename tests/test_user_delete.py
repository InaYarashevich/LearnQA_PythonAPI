import time
import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserDelete(BaseCase):
    def test_delete_vinkotov_user(self):
        # LOGIN AS vinkotov@example.com
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response, "user_id")

    # DELETE AS vinkotov@example.com
        response1 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response1, 400)

    # CHECK DELETED vinkotov@example.com
        response2 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    def test_delete_just_created_user(self):

        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response2, "user_id")

        #   DELETE
        response = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response, 200)

        # GET DELETED USER
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response4,
            "id",
            user_id,
            "There is no such user"
        )

    def test_delete_other_user(self):
        # REGISTER THE FIRST USER
        register_data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = register_data['email']
        password = register_data['password']
        time.sleep(5)

        # REGISTER THE SECOND USER
        register_data2 = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data2)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email2 = register_data2['email']
        password2 = register_data2['password']
        user_id1 = self.get_json_value(response1, "id")

        # LOGIN AS THE FIRST USER
        login_data1 = {
            'email': email,
            'password': password
        }
        response4 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data1)

        auth_sid1 = self.get_cookie(response4, "auth_sid")
        token1 = self.get_header(response4, "x-csrf-token")

        Assertions.assert_code_status(response4, 200)

        # LOGIN AS THE SECOND USER
        login_data2 = {
            'email': email2,
            'password': password2
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data2)

        auth_sid2 = self.get_cookie(response2, "auth_sid")
        token2 = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method2 = self.get_json_value(response2, "user_id")

        Assertions.assert_code_status(response2, 200)

        # DELETE THE SECOND USER BY THE FIRST USER
        response3 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method2}",
            headers={"x-csrf-token": token1},
            cookies={"auth_sid": auth_sid1}
        )
        Assertions.assert_code_status(response3, 200)

        # GET THE SECOND USER'S DETAILS
        response5 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method2}",
            headers={"x-csrf-token": token2},
            cookies={"auth_sid": auth_sid2}
        )
        Assertions.assert_code_status(response5, 200)
        Assertions.assert_json_value_by_name(
            response5,
            "id",
            user_id1,
            "Wrong id of the user"
        )
        print(response5.text)

