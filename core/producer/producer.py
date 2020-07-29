import os
import sys
import json
from kafka import KafkaProducer
from commons.logger import Logger
from config.initializers import KAFKA_BROKER,KAFKA_TOPIC

PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,PACKAGE_ROOT)
logger = Logger().get_logger("test")

class Producer(object):

  def __init__(self, topic=KAFKA_TOPIC):
    self.producer = KafkaProducer(
                      bootstrap_servers=KAFKA_BROKER,
                      value_serializer=lambda m: json.dumps(m).encode('ascii'))
    self.topic = topic

  def push(self, json_data):
    self.producer.send(self.topic, json_data)

