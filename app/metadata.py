from pathlib import Path
from datetime import datetime
import json

class Metadata:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_metadata(self):
        metadata_list = []
        path = Path(self.file_path)
        stat  = path.stat()
        metadata_list.append({"file_path" :self.file_path})
        metadata_list.append({"name": path.name})
        metadata_list.append({"file_extension": path.suffix})
        metadata_list.append({"size": stat.st_size})
        metadata_list.append({"creation_date": stat.st_ctime})
        metadata = json.dumps(metadata_list)
        return metadata


metadat = Metadata( r"C:\Users\user1\Desktop\podcasts\download (1).wav")
print(metadat.get_metadata())
