from app.processor.processor_manager import ProcessorManager

from dotenv import load_dotenv
import os

load_dotenv()
elastic_host = os.getenv("ELASTIC_HOST")
db_name = os.getenv("DB_NAME")
index = os.getenv("INDEX")


ProcessorManager(index , db_name).convert_and_update()