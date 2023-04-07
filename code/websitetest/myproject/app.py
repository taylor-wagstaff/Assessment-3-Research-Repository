from flask import Flask, render_template
import chrome_bookmarks
import random

### this is a Random Bookmark Generator, using flash, it can access your
## bookmarks and display a random link 

# to activate:  source websitetest/myproject/bin/activate
# must be above websitetest folder

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
    result = "\n".join(map(str, random.choice(bookmarks_url)))
    return result

@app.route('/run_all', methods=['POST'])
def run_all():
    result = "\n".join(map(str, bookmarks_url))
    return result

# @app.route('/search', methods=['POST'])
# def search():
#     result = bookmarks_url
#     return result





if "__name__" == "__main__":
    app.run(debug=True)
    app.logger.info("Flask app is running")