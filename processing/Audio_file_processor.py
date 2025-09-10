import base64

from dal.mongo_dal import MongoDAL
from logging_config.logger import Logger
import speech_recognition as sr
from dal.elastic_dal import ElasticsearchDal
import json

class AudioFileProcessor:
    def __init__(self, file):
        self.file = file
        self.logger = Logger.get_logger()

    def audio_transcription(self):
        try:
            r = sr.Recognizer()
            audio_data = sr.AudioData(self.file, sample_rate=16000, sample_width=2)
            text = r.recognize_google(audio_data)
            self.logger.info("Transcription completed successfully")
            return text
        except Exception as e:
            self.logger.error(f"Failed to transcribe the file, error: {e}")
    @staticmethod
    def encryption_key_base64(encrypted_text):
        decoded_bytes = base64.b64decode(encrypted_text)
        decoded_string = decoded_bytes.decode('utf-8')
        decoded_list = decoded_string.split(",")
        return decoded_string
