from dotenv import load_dotenv
from dal.mongo_dal import MongoDAL
from dal.elastic_dal import ElasticsearchDal
from processing.processor import Processor
from logging_config.logger import Logger
import os

load_dotenv()
elastic_host = os.getenv("ELASTIC_HOST")
db_nam = os.getenv("DB_NAME")

class ConvertToTextManager:
    def __init__(self, index,  db_name):
        self.elastic = ElasticsearchDal(index=index)
        self.db_name = db_name
        self.logger = Logger.get_logger()

    def convert_and_update(self):
        data_with_id = MongoDAL(db_name=self.db_name).extract_audio_with_id_from_mongodb()
        for file_id, binary_file in data_with_id.items():
            text = Processor(binary_file).audio_transcription()
            self.elastic.update_document(file_id, {"content_text": text})



ConvertToTextManager("test_topic", db_nam).convert_and_update()