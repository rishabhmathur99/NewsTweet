from flask import Flask, jsonify, request

from keyword_decompose import get_keywords
from api import getArticles

app = Flask(__name__)


@app.route('/findContext', methods = ['GET', 'POST'])
def findContext():
    words = get_keywords(request.data)
    articles = getArticles(words)
    
    return jsonify(articles)


if __name__ == '__main__':
    app.run()
