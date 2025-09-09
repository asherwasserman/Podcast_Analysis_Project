from logging import exception

from elasticsearch import Elasticsearch, helpers
from logging_config.logger import Logger
class ElasticsearchDal:
    def __init__(self, index):
        self.logger = Logger.get_logger()
        try:
            self.es = Elasticsearch("http://localhost:9200")
            self.logger.info("Login success to elastic search")
        except Exception as e :
            self.logger.error(f"Failed to connect to elastic search, error:{e}")
        self.index_name = index

    # inserts one document to your index
    def insert_one(self, doc, doc_id=None):
        try:
            res = self.es.index(index=self.index_name, id=doc_id, document=doc)
            self.logger.info(f"Document successfully added to your {self.index_name} index")
            return res["_id"]
        except Exception as e:
            self.logger.error(f"Failed to add document, error:{e}")

    def delete_document(self, doc_id):
        self.es.delete(index=self.index_name, id=doc_id, ignore=[400, 404])

    def search(self, query, size=10):
        res = self.es.search(index=self.index_name, query=query, size=size)
        return res["hits"]["hits"]

    def delete_index(self):
        self.es.options(ignore_status=[400, 404]).indices.delete(index=self.index_name)