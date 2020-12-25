# dynamic routing

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import feedparser
import random
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {
    'bbc': "http://feeds.bbci.co.uk/news/rss.xml",
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640',
    'sohu': 'http://rss.news.sohu.com/rss/focus.xml'
}

@app.route("/")
@app.route("/<publication>")

def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][random.randrange(0,9,1)]
    return """<html>
        <body>
            <h1> RSS Headlines </h1>
            <h3> captured by yasen </h3>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>          
        </body>
    </html>""".format(first_article.get("title"), first_article.
    get("published"), first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)