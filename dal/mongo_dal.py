from pymongo import MongoClient
import gridfs

class MongoDAL:
    def __init__(self,host="localhost", port=27017, db_name=None, collection=None):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection]

    def get_collection(self):
        return list(self.collection.find({ }))

    def add_document(self, message):
        self.collection.insert_one(message)
        return {"status": "success", "message": "added"}

    def push_audio_to_mongo_with_id(self, file_path, _id):
        fs = gridfs.GridFS(self.db)
        with open(file_path, "rb") as f:
            file_id = fs.put(f, file_id=_id )