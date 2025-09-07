from elasticsearch import Elasticsearch, helpers
class ElasticsearchDal:

    def __init__(self, index):
        self.es = Elasticsearch("http://localhost:9200")
        self.index_name = index

    def mapping_configuration(self, mapping):
        self.es.options(ignore_status=[400, 404]).indices.delete(index=self.index_name)
        self.es.indices.create(index=self.index_name,body=mapping)

    def insert_one(self, doc, doc_id=None):
        res = self.es.index(index=self.index_name, id=doc_id, document=doc)
        return res["_id"]

    def get_by_id(self, doc_id):
        try:
            return self.es.get(index=self.index_name, id=doc_id)["_source"]
        except:
            return None

    def update_document(self, doc_id, fields):
        res = self.es.update(index=self.index_name, id=doc_id, doc={"doc": fields})
        return res

    def add_mapping_fields(self, mapping):
        self.es.indices.put_mapping(index=self.index_name,body=mapping)

    def get_mapping(self):
        mappings = self.es.indices.get_mapping(index=self.index_name)
        return mappings

    def delete_document(self, doc_id):
        self.es.delete(index=self.index_name, id=doc_id, ignore=[400, 404])

    def search(self, query, size=10):
        res = self.es.search(index=self.index_name, query=query, size=size)
        return res["hits"]["hits"]

    def delete_index(self):
        self.es.options(ignore_status=[400, 404]).indices.delete(index=self.index_name)