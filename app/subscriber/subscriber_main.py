from app.subscriber.subscriber_manager import SubscriberManager
from dotenv import load_dotenv
import os

load_dotenv()
_index = os.getenv("INDEX")
db_name = os.getenv("DB_NAME")
topic = os.getenv("TOPIC_NAME")

SubscriberManager(topic).push_to_mongo_and_elastic(_index, db_name)
