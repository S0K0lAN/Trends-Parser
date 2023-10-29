from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests

def getArticlesAsObjects(url):
    res = BeautifulSoup(requests.get(url).text, 'html.parser')
    RBCArticlesCont = res.find('div', class_='js-news-feed-list').find_all('a', class_="news-feed__item")

    OBjectsArticles = []
    for el in RBCArticlesCont:
        article = {
            "link": el.attrs['href'],
            "header": el.find("span", class_ = 'news-feed__item__title').contents[0].replace('\n', ''),
            "date": el.find("span", class_ = 'news-feed__item__date-text').contents[1]
        }
        OBjectsArticles.append(article)
    return OBjectsArticles

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    url = request.args.get('link')
    response = jsonify({'content': getArticlesAsObjects(url)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == '__main__':
    app.run()


