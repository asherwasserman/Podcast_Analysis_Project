from kafka import KafkaProducer
import json



class Producer:

    def __init__(self):
        self.producer = self.get_producer_config()

    def get_producer_config(self):
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8') if isinstance(v, str) else v,
            key_serializer=lambda k: k.encode('utf-8') if isinstance(k, str) else k
        )
        return producer

    def publish_message(self, topic, message):
        self.producer.send(topic, value=message)
        self.producer.flush()
        self.producer.close(timeout=999999)


    def publish_message_with_key(self, topic, key, message):
        self.producer.send(topic, key=key, value=message)