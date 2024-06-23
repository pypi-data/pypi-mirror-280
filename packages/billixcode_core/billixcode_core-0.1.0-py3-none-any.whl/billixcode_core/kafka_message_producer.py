from abc import ABC
from dataclasses import asdict

from kafka import KafkaProducer
import json

from message_producer import AbstractMessageProducer


def serialize_to_json(obj):
    return json.dumps(asdict(obj)).encode('utf-8')


class KafkaEventProducer(AbstractMessageProducer):

    def __init__(self, bootstrap_servers='localhost:9092', topic=''):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=serialize_to_json
        )

    def emit(self, event):
        self.producer.send(self.topic, event)
        self.producer.flush()
        print(f"Event published to topic '{self.topic}': {event}")
