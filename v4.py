from nltk.text import Text

from bs4 import BeautifulSoup 

import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from urllib.request import urlopen
from urllib import response
url = "http://nrs-projects.humboldt.edu/~st10/s20cs328/328lect15-1/328lect15-1-projected_txt.html"

# download web page
html = urlopen(url).read()

soup = BeautifulSoup(html)

# remove html element tags
page = soup.get_text()

#print(type(page))

#nltk 
tokens = word_tokenize(page)
textList = Text(tokens)
textList.concordance('sjat')
#response = textList.concordance('z')
if 'sjat' in textList:
    print("exists")
else:
    print("dne")

#for i in textList:
 #   print(i)