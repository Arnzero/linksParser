from bs4 import BeautifulSoup
import requests
import nltk

response = requests.get("http://nrs-projects.humboldt.edu/~st10/s20cs328/328ex-list.php").content
soup = BeautifulSoup(response, "html.parser")
text_tokens = nltk.tokenize.word_tokenize(soup.get_text())

print (text_tokens)