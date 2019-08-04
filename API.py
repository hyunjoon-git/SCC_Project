from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db = client['adtech']


## HTML을 주는 부분
#@app.route('/')
#def home():
#    return 'This is Home!'


#@app.route('/mypage')
#def mypage():
#    return render_template('index.html')


## API 역할을 하는 부분
#@app.route('/post', methods=['POST'])
#def post():
#    global articles  # 이 함수 안에서 나오는 articles 글로벌 변수를 가리킵니다.

    #date_receive = request.form['date_give']
    #link_receive = request.form['link_give']  # 클라이언트로부터 url을 받는 부분
    #title_receive = request.form['title_give']  # 클라이언트로부터 comment를 받는 부분

    #article = {'date': date_receive, 'link': link_receive, 'title': title_receive}  # 받은 걸 딕셔너리로 만들고,

    #rticles.append(article)  # 넣는다

    #return jsonify({'result': 'success'})


@app.route('/post', methods=['GET'])
def view():
   posts = db.articles.find({},{'_id':0})
   return jsonify({'result':'success', 'articles':list(posts)})

if __name__ == '__main__':
   app.run('127.0.0.1',port=5000,debug=True)