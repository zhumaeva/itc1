import requests
from requests.api import request

response = requests.get('http://206.189.44.36:8900/students/')

result = response.json()

for user in result:

    print(user['age'], user['name'], user['phone'])

    if user['age']>18:
        print('Совершеннолетний')
    else:
        print('Несовершеннолетний')

    