import os
import sys
import yaml
from kafka import KafkaProducer
from commons.logger import Logger

PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,PACKAGE_ROOT)
logger = Logger().get_logger("test")

with open("config/kafka.yml", 'rt') as f:
    KAFKA_CONFIG = yaml.safe_load(f.read())

class Producer(object):

  def __init__(self, topic='bitcoin-stream-1'):
    self.producer = KafkaProducer(bootstrap_servers='localhost:9092')
    self.topic = topic

  def push(self, json_data):
    self.producer.send(self.topic, json_data)

