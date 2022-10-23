from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
from flask_cors import CORS, cross_origin

elastic = Elasticsearch(hosts=['http://localhost:9200'])
print(f"Connected to ElasticSearch cluster {elastic.info().body['cluster_name']}")

app = Flask(__name__)
CORS(app)

MAX_SIZE = 5


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=['GET'])
@cross_origin()
def search_autocomplete():
    query = request.args["q"].lower()
    payload = {
        "match": {
          "title": query
        }
    }

    resp = elastic.search(index="movies", query=payload, size=MAX_SIZE)
    return [result['_source']['title'] for result in resp['hits']['hits']]


if __name__ == "__main__":
    app.run(debug=True)
