from dotenv import load_dotenv
from dal.mongo_dal import MongoDAL
from dal.elastic_dal import ElasticsearchDal
from processing.Audio_file_processor import AudioFileProcessor
from processing.processor import Processor
from logging_config.logger import Logger
import os


class ProcessorManager:
    def __init__(self, index,  db_name):
        self.elastic = ElasticsearchDal(index=index)
        self.db_name = db_name
        self.logger = Logger.get_logger()

    def convert_and_update(self):
        data_with_id = MongoDAL(db_name=self.db_name).extract_audio_with_id_from_mongodb()
        for file_id, binary_file in data_with_id.items():
            text = AudioFileProcessor(binary_file).audio_transcription()
            self.elastic.update_document(file_id, {"content_text": text})
            self.upload_processing_results(file_id, text )

    @staticmethod
    def get_danger_percentages(text, dangerous_words, super_dangerous_words):
        dangerous = Processor(text, dangerous_words)
        dangerous_word = dangerous.find_dangerous_words()
        dangerous_expressions = dangerous.find_expression(dangerous.get_word_pairs())
        dangerous_percentage = (len(dangerous_word + dangerous_expressions)) / len(dangerous.text_list) / 2 * 100
        super_dangerous = Processor(text, super_dangerous_words)
        super_dangerous_word = super_dangerous.find_dangerous_words()
        super_dangerous_expressions = super_dangerous.find_expression(dangerous.get_word_pairs())
        super_dangerous_percentage = (len(super_dangerous_word + super_dangerous_expressions)) / len(super_dangerous.text_list) * 100
        return dangerous_percentage + super_dangerous_percentage

    @staticmethod
    def is_bds(percentage):
        if percentage >= 5:
            return True
        else:
            return False

    @staticmethod
    def danger_level(percentage):
        if percentage < 5:
            return "none"
        elif 20 > percentage >= 5:
            return "medium"
        else:
            return "high"

    def upload_processing_results(self, doc_id, text):
        dangerous_words = Processor.encryption_key_base64("RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")
        super_dangerous_words = Processor.encryption_key_base64("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
        percentage = self.get_danger_percentages(text, dangerous_words, super_dangerous_words)
        is_bds = self.is_bds(percentage)
        danger_level = self.danger_level(percentage)
        self.elastic.update_document(doc_id, {"risk_percentages": percentage, "is_bds" : is_bds, "danger_level": danger_level})