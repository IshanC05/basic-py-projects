import requests
from   bs4 import BeautifulSoup

url  = 'https://www.merriam-webster.com/word-of-the-day'
r    = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
word = soup.h1.text
meaning = soup.find('p').get_text()
print(word.title() + ' - ' + meaning[2:])