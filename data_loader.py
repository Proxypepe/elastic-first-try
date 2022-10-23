import pandas as pd
from elasticsearch import Elasticsearch

if __name__ == '__main__':
    elastic_connector = Elasticsearch(hosts=['http://localhost:9200'])
    data: pd.DataFrame = pd.read_csv('tmdb_5000_movies.csv')
    for release_date, title, original_language in zip(data.release_date, data.title, data.original_language):
        doc = {
            'release_date': release_date,
            'original_language': original_language,
            'title': title
        }
        elastic_connector.index(index='movies', document=doc)
