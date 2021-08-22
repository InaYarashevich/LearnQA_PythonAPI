import requests

response1 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response1.text)
print(response1.status_code)
response2 = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": "HEAD"})
print(response2.text)
print(response2.status_code)
response3 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method": "GET"})
print(response3.text)
print(response3.status_code)

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
maps = [{'method': 'GET'}, {'method': 'POST'}, {'method': 'PUT'}, {'method': 'DELETE'}]
print('Checking GET')
for data in maps:
    requests.get(url, params=data)
    print(data, requests.get(url, params=data).text, sep=' - ')
print('Checking POST')
for data in maps:
    requests.post(url, data=data)
    print(data, requests.post(url, data=data).text, sep=' - ')
print('Checking PUT')
for data in maps:
    requests.put(url, data=data)
    print(data, requests.put(url, data=data).text, sep=' - ')
print('Checking DELETE')
for data in maps:
    requests.delete(url, data=data)
    print(data, requests.delete(url, data=data).text, sep=' - ')
