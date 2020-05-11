import nltk, re, pprint
from urllib.request import urlopen
url = "http://nrs-projects.humboldt.edu/~st10/s20cs328/328lect15-1/328lect15-1-projected_txt.html"
raw = urlopen(url).read()
print(type(raw))
print(len(raw))

#natural language string
nls = nltk.clean_html(raw)

tokens = nltk.word_tokenize(raw)
print(tokens)

