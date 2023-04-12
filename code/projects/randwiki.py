import requests
from bs4 import BeautifulSoup
import webbrowser


# a random image from wikipedia, reworked code. 
# Mangages to fetch a random image from wikipedia, I reworked a version 
# from a random article to an image. 

# Random Wikipedia Article Generator in Python
# https://www.codesnail.com/random-wikipedia-article-generator-in-python/

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    images = soup.find_all('img')

  # varible to store url
    imageSources = []

    for image in images:
        imageSources.append(image.get("src"))

    urlimage = imageSources[3]

    print(f"{title} \nDo you want to view it? (Y/N)")
    ans = input("").lower()

    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open("https:" + urlimage)
        print("https:" + urlimage)
        break
    elif ans == "n":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break