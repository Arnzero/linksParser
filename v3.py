import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from urllib.request import urlopen
from urllib import response
url = "http://nrs-projects.humboldt.edu/~st10/s20cs328/328lect15-1/328lect15-1-projected_txt.html"
response = request.urlopen(url)
raw = response.read().decode('utf8')

print(type(raw))
print(raw[:60])


tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])