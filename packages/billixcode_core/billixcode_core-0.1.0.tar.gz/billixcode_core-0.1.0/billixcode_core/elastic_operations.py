from elasticsearch import Elasticsearch, exceptions

from data_operations import AbstractDataOperations


class ElasticOperations(AbstractDataOperations):

    def __init__(self, es_host='http://localhost:9200', es_user='', es_pass=''):
        super().__init__()
        self.es_host = es_host
        self.es_user = es_user
        self.es_pass = es_pass
        self.es = Elasticsearch(
            [self.es_host],
            basic_auth=(self.es_user, self.es_pass),
            verify_certs=False
        )

    def upsert(self, index_name=None, doc_id=None, document=None):
        try:
            # Check if the document exists
            if self.es.exists(index=index_name, id=doc_id):
                # Update the document if it exists
                response = self.es.update(index=index_name, id=doc_id, body={'doc': document})
                action = 'updated'
            else:
                # Insert the document if it does not exist
                response = self.es.index(index=index_name, id=doc_id, body=document)
                action = 'inserted'
            return {"action": action, "result": response}
        except exceptions.ConnectionError as e:
            print(f"Error connecting to Elasticsearch: {e}")
            return None
        except exceptions.RequestError as e:
            print(f"Error with the request to Elasticsearch: {e}")
            return None
