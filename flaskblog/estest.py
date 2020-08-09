from elasticsearch import Elasticsearch
es = Elasticsearch()


# def query_index('post', 'hello', page, per_page):
#     if not current_app.elasticsearch:
#         return [], 0
#     search = current_app.elasticsearch.search(
#         index=index,
#         body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
#               'from': (page - 1) * per_page, 'size': per_page})
#     ids = [int(hit['_id']) for hit in search['hits']['hits']]
#     return ids, search['hits']['total']['value']



search = es.search(
        index='post',
        body={'query': {'multi_match': {'query': 'Hello', 'fields': ['*']}}})



ids = [int(hit['_id']) for hit in search['hits']['hits']]
print(search)