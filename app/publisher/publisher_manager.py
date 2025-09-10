from pathlib import Path
from metadata import Metadata
from kafka_files.producer import Producer
from logging_config.logger import Logger

class PublisherManager:
    def __init__(self, path):
        self.directory_path = Path(rf"{path}")
        self.file_paths = [str(entry) for entry in self.directory_path.iterdir() if entry.is_file()]
        self.logger = Logger.get_logger()

    def publish_to_kafka(self, topic):
        for file_path in self.file_paths:
            metadata = Metadata(rf"{file_path}").get_metadata()
            Producer().publish_message(topic, metadata)


