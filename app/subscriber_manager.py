from dal.elastic_dal import ElasticsearchDal
from dal.mongo_dal import MongoDAL
from kafka_files.consumerr import Consumer
import hashlib
import json

class SubscriberManager:
    def __init__(self, topic):
        self.topic = topic
        self.consumer = Consumer(self.topic)
    def get_events(self):
        events = self.consumer.get_consumer_events()
        return events

    @staticmethod
    def create_id(event):
        hash_object = hashlib.sha256()
        hash_object.update(event.encode('utf-8'))
        content_id = hash_object.hexdigest()
        return content_id

    def push_to_mongo_and_elastic(self, db,  index):
        events = self.get_events()
        elastic_conn = ElasticsearchDal(index)
        mongo_conn = MongoDAL( db_name=db)
        for event in events:
            value = json.loads(event.value)
            hash_id = (self.create_id
                       (str(value["name"]) + str(value["size"]) + str(value["creation_date"])))
            elastic_conn.insert_one(value, hash_id)
            mongo_conn.push_audio_to_mongo_with_id(value["file_path"], hash_id)