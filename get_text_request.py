from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text", params={"name":"User"})

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")
