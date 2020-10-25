import requests
from bs4 import BeautifulSoup

result = requests.get('https://dbkpop.com/db/all-k-pop-idols')

soup = BeautifulSoup(result.text)

table_body = soup.find('tbody')
print(table_body.prettify())