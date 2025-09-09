from logging import exception

from kafka import KafkaProducer
from logging_config.logger import Logger
import json



class Producer:

    def __init__(self):
        self.logger = Logger.get_logger()
        self.producer = self.get_producer_config()

    def get_producer_config(self):
        try:
            producer = KafkaProducer(
                bootstrap_servers='localhost:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8') if isinstance(v, str) else v,
                key_serializer=lambda k: k.encode('utf-8') if isinstance(k, str) else k
            )
            return producer
        except Exception as e:
            self.logger.error(f"Failed to connect to Kafka, error:{e}")

    def publish_message(self, topic, message):
        try:
            self.producer.send(topic, value=message)
            self.producer.flush()
            self.producer.close(timeout=999999)
            self.logger.info("the massage was sent successfully")
        except Exception as e:
            self.logger.error(f"Sending to Kafka failed, error: {e}")


    def publish_message_with_key(self, topic, key, message):
        self.producer.send(topic, key=key, value=message)