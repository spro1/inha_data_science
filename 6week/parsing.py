import requests
from bs4 import BeautifulSoup

url = "https://www.seas.harvard.edu/"
# user agent 추가
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
# url data get
req = requests.get(url, headers=header)

# res code check
# print(req.status_code)

# parsing
soup = BeautifulSoup(req.text, 'html.parser')
print("학과명 리스트\n--------------------")
for i in soup.find_all('span', class_='teaching-area__title'):
    print(i.text)
