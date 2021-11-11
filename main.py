from typing import Dict
from flask import Flask, render_template, request, jsonify
import json
from gensim.models import Word2Vec

app = Flask(__name__)

# モデルの読み込み
model_path = '../entity/word2vec.gensim.model'
model = Word2Vec.load(model_path)

# index はトップページを表示します
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# post_data は単語計算式を POST で受け取り、計算結果を返します
@app.route("/data", methods=["POST"])
def post_data():
    sentense = request.form["sentense"]
    sentense = sentense.split(" ")  # ['a', '+', 'b', '=', '']
    sentense.remove('')   # 末尾を削除
    kekka = calc(sentense)
    print(kekka)
    return jsonify(ResultSet=json.dumps(kekka))


# calc は単語の分散表現を獲得し計算を行います
def calc(word_list: list) -> Dict[str, float]:
    positive = []
    negative = []
    for i in range(len(word_list)-2):
        if i == 0:
            positive.append(word_list[i])
        if word_list[i+1] == "-":
            negative.append(word_list[i+2])
        elif word_list[i+1] == "+":
            positive.append(word_list[i+2])

    out = model.most_similar(positive=positive, negative=negative)
    return out


if __name__ == '__main__':
    app.run(port=8000, debug=True)

