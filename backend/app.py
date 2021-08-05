from numpy import ceil
import pandas as pd
from flask import Flask
from flask_cors import CORS, cross_origin
import json
from pymongo import MongoClient
import os

app = Flask("app")

mongoclient = MongoClient(os.getenv("MONGO_URL"))

db = mongoclient.boba_db

boba_count_db = db.boba_count

CORS(app)

app = Flask(__name__)

@app.route('/boba', methods=['GET'])
@cross_origin()
def get_boba():
    cursor = boba_count_db.find({})
    count = {}
    for document in cursor:
        user = document["user"]
        boba_count = document["boba_count"]
        count[user] = boba_count
    count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
    return  json.dumps(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
