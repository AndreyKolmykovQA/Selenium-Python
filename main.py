"""
Python tests api Andrey Kolmykov
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
# body = {
#     "trainer_token": "f1d31de7274e1eebfb71f921b5ade0b6",
#     "email": "pytonistik@yandex.ru",
#     "password": "iloveQA111"
# }

# response = requests.post(url=f'{URL}/trainers/reg', json=body, headers=HEADER, timeout=5)
# print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')

response = requests.get(url=f'{URL}/trainers', params = {'level': 3}, timeout = 5 )
print(f'Статус код: {response.status_code}.')

json_data = response.json()