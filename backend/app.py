import pandas as pd
from flask import Flask
from flask_cors import CORS, cross_origin
import json

app = Flask("app")

CORS(app)

app = Flask(__name__)

@app.route('/boba', methods=['GET'])
@cross_origin()
def get_boba():
    url = 'https://docs.google.com/spreadsheets/d/1s_9upDvvm-TKQOJUeghcTgNj8SpZYJrsTlDrphA8NQQ/gviz/tq?tqx=out:csv&sheet=boba'
    df = pd.read_csv(url)
    names = list(df["Name"])
    count = {person: names.count(person) for person in names}
    count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
    print(count)
    return  json.dumps(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
