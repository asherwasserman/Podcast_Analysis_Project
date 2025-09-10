from app.publisher.publisher_manager import PublisherManager
from dotenv import load_dotenv
import os


load_dotenv()
file_path = os.getenv("FILE_PATH")
topic = os.getenv("TOPIC_NAME")

PublisherManager(rf"{file_path}").publish_to_kafka(topic)