from lib.my_requests import MyRequests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("Registration")
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

    @allure.story("Create user with valid data")
    @allure.description("This test registers user successfully")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post(f"/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.story("Create user with existing email")
    @allure.description("This test registers user with an existing email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@exampe.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post(f"/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.story("Create user with incorrect email format")
    @allure.description("This test registers user with broken email")
    @allure.severity(allure.severity_level.MINOR)
    def test_user_with_incorrect_email(self):
        data = self.prepare_registration_data1()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format"

    @allure.story("Create user with too short first name")
    @allure.description("This test registers user with too short first name")
    @allure.severity(allure.severity_level.MINOR)
    def test_user_with_short_name(self):
        data = self.prepare_registration_data2()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short"

    @allure.story("Create user with too long first name")
    @allure.description("This test registers user with too long name")
    @allure.severity(allure.severity_level.MINOR)
    def test_user_with_long_name(self):
        data = self.prepare_registration_data3()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long"

    @pytest.mark.parametrize('username, firstName, lastName, email, password', data)
    def test_parameter_check(self, username, firstName, lastName, email, password):
        data = {
            'username': username,
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'password': password
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)

