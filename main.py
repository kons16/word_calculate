from flask import Flask, render_template, request
from flask import jsonify
import json
from gensim.models import KeyedVectors
from gensim.models.word2vec import Word2Vec
import re

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/postdata", methods=["POST"])
def post_data():
    if request.method == "POST":
        sentense = request.form["sentense"]
        sentense = sentense.split(" ")
        # print(sentense)     # ['a', '+', 'b', '=', '']
        sentense.remove('')   # 末尾を削除
        kekka = calc(sentense)
        print(kekka)
        return jsonify(ResultSet=json.dumps(kekka))


@app.route("/similar", methods=["GET"])
def similar():
    return render_template("similar.html")


@app.route("/postsimilar", methods=["POST"])
def post_similar():
    if request.method == "POST":
        word = request.form["word"]
        kekka = calc_similar(word)
        print(kekka)
        return jsonify(ResultSet=json.dumps(kekka))


@app.route("/why_calc")
def why_calc():
    return render_template("why_calc.html")


# 単語の分散表現を獲得し計算を行う関数
def calc(word_list):
    # file_name = "../entity_vector/entity_vector.model.bin"
    # model = KeyedVectors.load_word2vec_format(file_name, binary=True)
    model_path = '../entity/shiroyagi/word2vec.gensim.model'
    model = Word2Vec.load(model_path)

    positive = []
    negative = []
    for i in range(len(word_list)-2):
        if i == 0:
            positive.append(word_list[i])
        if word_list[i+1] == "-":
            negative.append(word_list[i+2])
        elif word_list[i+1] == "+":
            positive.append(word_list[i+2])

    # print(positive, negative)
    # out = model.most_similar(positive=positive, negative=negative)
    out = model.most_similar(positive=positive, negative=negative)
    return out


# 類似単語を取得する関数
def calc_similar(word):
    model_path = '../entity/shiroyagi/word2vec.gensim.model'
    model = Word2Vec.load(model_path)
    out = model.most_similar(positive=word)
    return out


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010, debug=True)
