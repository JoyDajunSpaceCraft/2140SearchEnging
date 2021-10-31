from elasticsearch import Elasticsearch

es = Elasticsearch()

result = es.indices.create(index='names')
print(result)