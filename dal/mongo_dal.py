from pymongo import MongoClient
from logging_config.logger import Logger
from gridfs import GridFSBucket
import gridfs

class MongoDAL:
    def __init__(self,host="localhost", port=27017, db_name=None):
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

    def push_audio_to_mongo_with_id(self, file_path, _id):
        try:
            fs = gridfs.GridFS(self.db)
            with open(file_path, "rb") as f:
                file_id = fs.put(f, file_id=_id )
            self.logger.info("The audio files have been successfully uploaded to MongoDB")
        except Exception as e:
            self.logger.error(f"Uploading audio files to MongoDB failed, error:{e}")

    def extract_audio_with_id_from_mongodb(self):
        try:
            fs = GridFSBucket(self.db)
            data_dict = {}
            for grid_out in fs.find():
                file_id = grid_out.file_id
                file_content = grid_out.read()
                data_dict[file_id] = file_content
            self.logger.info("The audio file was successfully extracted from MongoDB")
            return data_dict
        except Exception as e:
            self.logger.error(f"Extracting information from MongoDB failed, error: {e}")