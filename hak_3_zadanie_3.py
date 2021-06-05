import requests

print('Выполняется запрос')

response = requests.delete('http://206.189.44.36:8900/students/1/')

requests.get('http://206.189.44.36:8900/students/1/')

response.status_code

if response.status_code == 204:
    print('Success!')
elif response.status_code != 204:
    print(response.text)