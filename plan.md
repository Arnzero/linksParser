#### Plan goes here

## Function -> takes in URL and keyword string 

# The URL collects all the links
#   open each link and use NLTK on each link and 
#   match the string

# The top 3 links with the best match to the string
# are returned.


# with NLTK open the link, save the object
#   parse it and match it
#   gg too easy

# do we wanna fix the FLASK 

# 




## 1 INPUT(url, q) where q is one word for now
## 2 download HTML of URL
##      - grab all HTML links inside body tag via XPATH
##      - for links, Iteratively append links to make ABSOLUTE  URLS
## 3 Iterate through each link till we have 4 matches within links
##      -Check if word exists per link
##      -save link to array till we reach 4
##      -If it has a match then it must have a concordance via NLTK
## 4 Display concordances of these links
##      Make a flask application ??