from urllib import urlopen
from urllib.request import urlopen
from lxml import etree
url = "http://nrs-projects.humboldt.edu/~st10/s20cs328/328ex-list.php"
response = urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response,htmlparser)
