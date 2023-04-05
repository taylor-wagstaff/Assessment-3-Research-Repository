# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import random
from bs4 import BeautifulSoup


url = "https://www.economist.com/"

def generate_poem_words():
  # url= input("What is the url?  ")
  response = requests.get(url)


  # encoder 
  response.encoding = 'utf-8'  # set the encoding to utf-8
  encoding = response.encoding


  html = response.content.decode(encoding)
  # beautiful soup is parser for data, give varibles
  soup = BeautifulSoup(html, "html.parser")
  h3_tags = soup.find_all('h3')
  images = soup.find_all('img')

  # varible to store url
  imageSources = []

  for image in images:
      imageSources.append(image.get("src"))


  # print(imageSources)




  # varible to store all headlines
  headlines = []

  # iterate over all h3 tags
  for h3_tag in h3_tags:
      h = h3_tag.get_text()
      #store in varible
      headlines.append(h)






  all_headlines = ' '.join(map(str, headlines))
  split_words = all_headlines.split()
  words_to_remove = ['The', 'the', 'and', 'And', 'A','a']

  for x in words_to_remove:
      while x in split_words:
          split_words.remove(x)



  random_headline = random.sample(split_words,  min(9, len(split_words)))
  # new_headlines = ' '.join(map(str, random_headline))


  poem_words = []
  # print random words from all headlines from website 
  for words in random_headline:
      w = words
      poem_words.append(w)

  print(poem_words)

  new_words = [word.replace('’', "'") for word in poem_words]

  poem_str = "<br>".join(new_words)

  return poem_str





###### server ######


hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Economist Headline Poem Generator</title></head>", "utf-8"))
        self.wfile.write(bytes('<meta http-equiv="refresh" content="5">', "utf-8"))
        self.wfile.write(bytes("<style>", "utf-8"))
        self.wfile.write(bytes("body { font-family:	Times New Roman, serif; font-size: 30px; background-color: red; color: white; }", "utf-8"))
        self.wfile.write(bytes("</style></head>", "utf-8"))
        self.wfile.write(bytes("<p>Economist Poem Generator: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes(f"<h1>{poem_words}</h1>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        while True:
          poem_words = generate_poem_words()
          # webServer.serve_forever()
          webServer.handle_request()
          
         
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")