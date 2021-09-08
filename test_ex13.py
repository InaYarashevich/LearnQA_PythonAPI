import requests
import pytest
import json


class TestCheckUserAgent:
    data = [
        (
            "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mobile",
            "No",
            "Android"
        ),
        (
            "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "Mobile",
            "Chrome",
            "iOS"
        ),
        (
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Googlebot",
            "Unknown",
            "Unknown"
        ),
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "Googlebot",
            "Chrome",
            "No"
        ),
        (
            "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "Mobile",
            "No",
            "iPhone"
        )
    ]

    @pytest.mark.parametrize('agent, platform, browser, device', data)
    def test_check_agent(self, agent, platform, browser, device):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {"user-agent": agent}

        response = requests.get(url, headers=data)
        obj = json.loads(response.text)

        actual_browser = obj.get("browser")
        actual_platform = obj.get("platform")
        actual_device = obj.get("device")

        assert actual_browser == browser, f"There is no '{browser}' browser in the response for '{agent}'"
        assert actual_device == device, f"There is no '{device}' device in the response for '{agent}'"
        assert actual_platform == platform, f"There is no '{platform}' platform in the response for '{agent}'"
