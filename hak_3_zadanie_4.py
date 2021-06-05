import requests
from bs4 import BeautifulSoup

url = 'https://softech.kg/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')



recommended = soup.find_all('div', class_='box-heading')
for i in recommended:
    product_name = soup.find_all('div', class_='name')
    product_price = soup.find_all('div', class_='price')
    product_title = soup.find_all('div', class_='description-small')
    
    for name in product_name:
        print('Название: ', name.text)
    for price in product_price:
        print('Цена: ', price.text)
    for title in product_title:
        print('Описание: ',title.text)