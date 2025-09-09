from dal.mongo_dal import MongoDAL
from logging_config.logger import Logger

import speech_recognition as sr

class Processor:
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
            self.logger.error("Failed to transcribe the file")

a = MongoDAL(db_name="podcast_details").extract_audio_with_id_from_mongodb()
b = Processor(a["188ebebde66b7acbf8c1d8b84a389eac23ea234b3c61b844390817574ebf16ed"]).audio_transcription()
print(b)