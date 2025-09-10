from logging import exception
from pathlib import Path
from datetime import datetime
from logging_config.logger import Logger
import json

class Metadata:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = Logger.get_logger()

    def get_metadata(self):
        metadata_dict = {}
        try:
            path = Path(self.file_path)
            stat  = path.stat()
            metadata_dict["file_path"] = self.file_path
            metadata_dict["name"] = path.name
            metadata_dict["file_extension"] = path.suffix
            metadata_dict["size"] = stat.st_size
            metadata_dict["creation_date"] = stat.st_ctime
            metadata = json.dumps(metadata_dict)
            return metadata
        except Exception as e:
            self.logger.error(f"Failed to extract metadata from file,  error:{e}")

metadat = Metadata( r"C:\Users\user1\Desktop\podcasts\download (1).wav")
print(metadat.get_metadata())
