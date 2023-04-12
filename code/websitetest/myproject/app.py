from flask import Flask, render_template
import chrome_bookmarks
import random

### this is a bookmark manager using flash, 
# it can access your bookmarks, has a search function and display a random link 

# to activate:  source websitetest/myproject/bin/activate
# must be above websitetest folder, then 'flask run' inside the myproject folder
# confusing, i must have set it up wrong. 

bookmarks_url = []

# for folder in chrome_bookmarks.folders:
#     print(folder.name)
#     print(folder.folders)

for url in chrome_bookmarks.urls:
    bookmarks_url.append(url.url)


# sets up the website for python

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')

#renders html page
def index():
    return render_template("index.html")


@app.route('/run_code', methods=['POST'])
def run_code():
    #this is for a random bookmark
    result = "\n".join(map(str, random.choice(bookmarks_url)))
    return result

@app.route('/run_all', methods=['POST'])
def run_all():
    # this is for all bookmark responses. 
    result = "\n".join(map(str, bookmarks_url))
    return result


if "__name__" == "__main__":
    app.run(debug=True)
    app.logger.info("Flask app is running")