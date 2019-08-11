from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
import datetime

from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client['adtech']


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for page in range(1, 3, 1): #범위 수정
    page_url = "https://adexchanger.com/page/{}/?s=ad+tech&search_order=date".format(page)
    data = requests.get(page_url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    articles = soup.select('#adexchanger-content > article > div > div')

    for news in articles:
        if not news.a == None:

            doc = {}

            a_date = news.select('div > span > a')[1]
            a_date.p.decompose()
            a_date = a_date.text.strip().replace(' ...','')
            a_date = datetime.datetime.strptime(a_date, '%b, %d, %Y')

            doc['date'] = a_date
            doc['title'] = news.select('div > span > a')[0].text
            doc['link'] = news.select('div > small > a')[0].text

            db.articles.insert_one(doc)






