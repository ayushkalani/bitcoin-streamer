import sys
import os
import time, traceback
import json
PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,PACKAGE_ROOT)
from commons.logger import Logger
from config.initializers import KAFKA_BROKER, KAFKA_TOPIC,KAFKA_CONSUMER_GROUP_ID
from kafka import KafkaConsumer

logger = Logger().get_logger("test")

class Consumer(object):
    def __init__(self):
      """Tries to establing the Kafka consumer connection"""
      try:
          logger.debug("Creating new kafka consumer using brokers: " +
                              KAFKA_BROKER + ' and topic ' +
                              KAFKA_TOPIC)
          self.kafka_consumer = KafkaConsumer(
            group_id=KAFKA_CONSUMER_GROUP_ID,
            bootstrap_servers=KAFKA_BROKER,
            consumer_timeout_ms=1000
          ) 
          self.kafka_consumer.subscribe([KAFKA_TOPIC])
      except KeyError as e:
          logger.error('Missing setting named ' + str(e),
                              {'ex': traceback.format_exc()})
      except:
          logger.error("Couldn't initialize kafka consumer for topic",
                              {'ex': traceback.format_exc()})
          raise

if __name__ == "__main__":
  consumer = Consumer()
  while True:
      consumer.kafka_consumer.poll()
      for message in consumer.kafka_consumer:
          logger.info('Datapoint from kafka:')
          try:
              json_message = json.loads(message.value.decode())
              logger.info('Datapoint from kafka: %s', json_message)
          except json.JSONDecodeError:
              logger.error("Failed to decode message from Kafka, skipping..")
          except Exception as e:
              logger.error("Generic exception while pulling datapoints from Kafka")