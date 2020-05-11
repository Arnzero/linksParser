# Input the url and q, q is one word for now

# download HTML of URL
#   grab all html links inside body tag

import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


from nltk.text import Text
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from urllib.request import urlopen
from urllib import response


### Iterate for the first four appends
#singleLink = "http://nrs-projects.humboldt.edu/~st10/s20cs328/328lect02-2/328lect02-2-projected_txt.html"
#q="TOO_MANY_ROWS"
singleLink ="http://nrs-projects.humboldt.edu/~st10/s20cs328/328lect14-1/js-ckbox-play_php.html"
q= "Cheddar"

from re import search


html = urlopen(singleLink).read()
content = soup(html, features="lxml")
page = content.get_text()
tokens = word_tokenize(page)

#filter out duplicate tokens
distinctTokens = list(dict.fromkeys(tokens))
textList = Text(distinctTokens)
#if q in textList:
#    textList.concordance(q)
if search(q ,page):
    textList.concordance(q)
    



