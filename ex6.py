import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
i = 0
if response.history:
    for resp in response.history:
        i += 1
        print(resp.status_code, resp.url)
    print("Количество редиректов: ", i)
    print("Итоговый URL:")
    print(response.status_code, response.url)

