import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    data = [

        (
        "test",
        "",
        "test",
        "test@example.com",
        "123"
         ),
        ("",
         "test",
         "test",
         "test1@example.com",
         "123"
         ),
        ("test",
         "test",
         "",
         "test2@example.com",
         "123"
         ),
        ("test",
         "test",
         "test",
         "",
         "123"
         ),
        ("test",
         "test",
         "test",
         "test3@example.com",
         ""
         )
    ]
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@exampe.com'
        data = self.prepare_registration_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_user_with_incorrect_email(self):
        data = self.prepare_registration_data1()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format"

    def test_user_with_short_name(self):
        data = self.prepare_registration_data2()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short"

    def test_user_with_long_name(self):
        data = self.prepare_registration_data3()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long"

    @pytest.mark.parametrize('username, firstName, lastName, email, password', data)
    def test_parameter_check(self, username, firstName, lastName, email, password):
        url = 'https://playground.learnqa.ru/api/user/'
        data = {
            'username': username,
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'password': password
        }

        response = requests.post(url, data=data)

        Assertions.assert_code_status(response, 200)

