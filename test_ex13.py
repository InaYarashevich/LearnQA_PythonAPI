import pytest
import requests
import json

class TestEx13:
    user_agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('user_agent', user_agents)
    def test_check_user_agent(self, user_agent):

        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {"User-Agent": user_agent}

        response = requests.get(url, headers=headers)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()

        assert "platform" in response_dict, "There is no key 'platform' in the response"
        assert "browser" in response_dict, "There is no key 'browser' in the response"
        assert "device" in response_dict, "There is no key 'device' in the response"

        expected = [{'platform': 'Mobile', 'browser': 'No', 'device': 'Android', 'user_agent': user_agent},
                    {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS', 'user_agent': user_agent},
                    {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown', 'user_agent': user_agent},
                    {'platform': 'Web', 'browser': 'Chrome', 'device': 'No', 'user_agent': user_agent},
                    {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone', 'user_agent': user_agent}
        ]

        assert response_dict in expected, f"Response is not correct for '{user_agent}' User-Agent"


















