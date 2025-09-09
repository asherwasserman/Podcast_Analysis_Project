from pymongo import MongoClient
from logging_config.logger import Logger
import gridfs

class MongoDAL:
    def __init__(self,host="localhost", port=27017, db_name=None, collection=None):
        self.logger = Logger.get_logger()
        try:
            self.client = MongoClient(host, port)
            self.logger.info("Connecting to MongoDB successfully")
        except Exception as e:
            self.logger.error(f"failed to connect to mongodb, error: {e}")
        try:
            self.db = self.client[db_name]
        except Exception as e:
            self.logger.error(f"db not exist, error: {e}")
        try:
            self.collection = self.db[collection]
        except Exception as e:
            self.logger.error(f"collection not exist, error: {e}")

    def get_collection(self):
        return list(self.collection.find({ }))

    def add_document(self, message):
        self.collection.insert_one(message)
        return {"status": "success", "message": "added"}

    def push_audio_to_mongo_with_id(self, file_path, _id):
        fs = gridfs.GridFS(self.db)
        with open(file_path, "rb") as f:
            file_id = fs.put(f, file_id=_id )