import json
from kafka import KafkaConsumer


class Consumer:

    def __init__(self, topic):
        self.topic = topic
        self.consumer= self.get_consumer_events()
        self.event = None

    def get_consumer_events(self):
        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers='localhost:9092',
            group_id='my-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        return consumer