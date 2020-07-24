from flask import Flask
from flask import jsonify
from flask import request

from data_parse import process_data, identifyNounPhrases
from api import getArticles

app = Flask(__name__)


@app.route('/findContext', methods = ['GET', 'POST'])
def findContext():
    tagged_words, hashtags = process_data(request.data)
    words = identifyNounPhrases(tagged_words)


    articles = getArticles(words)
    return jsonify(articles)


if __name__ == '__main__':
    app.run()
