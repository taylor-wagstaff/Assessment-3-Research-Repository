import requests
from bs4 import BeautifulSoup

### A web scraper is an api, 
### an Api for a website that doesnt have an api. 

url = "https://pixelford.com/blog/"


response = requests.get(url)

html = response.content
# beautiful soup is parser for data, give varibles
soup = BeautifulSoup(html, "html.parser")
a_tags = soup.find_all('a', class_='entry-title-link')


for a_tag in a_tags:
    print(a_tag.get_text())

titles = list(map(lambda a_tag: a_tag.get_text(), a_tags))
print(titles)