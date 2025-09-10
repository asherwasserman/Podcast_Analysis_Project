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
    def insert_one(self, doc, doc_id):
        try:
            res = self.es.index(index=self.index_name, id=doc_id, document=doc)
            self.logger.info(f"Document successfully added to your {self.index_name} index")
            return res["_id"]
        except Exception as e:
            self.logger.error(f"Failed to add document, error:{e}")

    def update_document(self, doc_id, fields):
        try:
            res = self.es.update(index=self.index_name, id=doc_id, doc=fields)
            if res:
                self.logger.info("Document updated successfully")
            return res
        except Exception as e:
            self.logger.error(f"Failed to update document, error:{e}")

    def insert_content_by_file_id(self, file_id, text):
        query_body = {
            "query": {
                "match": {
                    "file_id": file_id
                }
            },
            "script": {
                "source": f"ctx._source.{"content_text"} = params.new_val",
                "lang": "painless",
                "params": {
                    "new_val": text
                }
            }
        }
        response = self.es.update_by_query(index=self.index_name, body=query_body)
        return response

    def search(self, query, size=10):
        res = self.es.search(index=self.index_name, query=query, size=size)
        return res["hits"]["hits"]

    def delete_index(self):
        self.es.options(ignore_status=[400, 404]).indices.delete(index=self.index_name)

