import requests
from bs4 import BeautifulSoup

result = requests.get('https://dantri.com.vn/')
soup = BeautifulSoup(result.text)

# print(soup.prettify())

# print(result)

# print(result.text)

div_tag = soup.find('div', {'class': 'highlight-event'})
# print(div_tag)

# h2 = div_tag.find('h2')
# print(h2.text.strip())

ul = div_tag.find('ul')

titles_list = ul.find_all('li')
for titles in titles_list:
    content = title.find('a')
    print(content.text.strip())
    print(content['href'])