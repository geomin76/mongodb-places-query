from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def main():
    return "Hello World"

@app.route("/query", methods=['GET', 'POST'])
@cross_origin()
def query():
    url = "mongodb+srv://{0}:{1}@{2}/{3}?retryWrites=true&w=majority".format(os.environ['USER'], os.environ['PASS'], os.environ['URL'], os.environ['DB'])
    client = MongoClient(url)
    db = client.places
    collection = db.places
    ls = []
    for x in collection.find():
        ls.append({
            "name": x['name'],
            "lat": x["lat"],
            "lng": x["lng"]
        })
    print(ls)
    return jsonify(ls)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)