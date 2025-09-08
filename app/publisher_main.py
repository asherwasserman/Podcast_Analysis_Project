from app.publisher_manager import PublisherManager

PublisherManager(r"C:\Users\user1\Desktop\podcasts").publish_to_kafka("test_topic")