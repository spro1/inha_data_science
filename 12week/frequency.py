import nltk
import collections
import requests

from bs4 import BeautifulSoup

# page content 추출
url = "https://en.wikipedia.org/wiki/Piano"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
content = soup.find("div", class_="mw-body")

# word 추출
# body text data split
freq1 = nltk.tokenize.word_tokenize(content.text)
# change lower word
freq1 = [w.lower() for w in freq1]
# count
freq1_cnt = collections.Counter(freq1)
# print(freq1_cnt)

# 표제어 추출
lm = nltk.WordNetLemmatizer()
# remove stopwords
freq2 = [lm.lemmatize(w) for w in freq1 if w not in nltk.corpus.stopwords.words("english") and w.isalnum()]
# count
freq2_cnt = collections.Counter(freq2)
print(freq2_cnt.most_common(100))
