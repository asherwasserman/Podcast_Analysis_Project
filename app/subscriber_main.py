from app.subscriber_manager import SubscriberManager

SubscriberManager("test_topic").push_to_mongo_and_elastic("podcast_details","a", "test_topic")
