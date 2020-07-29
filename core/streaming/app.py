#!/usr/bin/env python
import sys
import os

PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,PACKAGE_ROOT)
import json
import time, traceback
import logging
import websocket
import threading
from commons.logger import Logger
from commons.hit_counter import HitCounter
from commons.redis_connector import RedisConnector  
from websocket import create_connection
from core.producer.producer import Producer

logger = Logger().get_logger("test")
transaction_counter = HitCounter()
time_counter=0

def stream():
    ws = websocket.WebSocket()
    ws = create_connection('wss://ws.blockchain.info/inv')
    ws.send(json.dumps({"op":"unconfirmed_sub"}))
    return ws

def persist_in_redis(r, stream='bitcoin'):
  try:
    global time_counter
    time_counter += 1
    data = { time_counter: transaction_counter.get_hit() }
    r.xadd(stream, data)
  except Exception as ex:
    logger.exception("An exception occured while persisting data to redis")

def every(delay, task, redis_conn):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task(redis_conn)
    except Exception:
      traceback.print_exc()
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay

if __name__ == "__main__":
    web_socket = stream()
    kafka_producer = Producer()
    redis_connector = RedisConnector()
    redis_conn = redis_connector.get_connection()
    threading.Thread(target=every, args=(60, persist_in_redis, redis_conn)).start()
    logger.info("Starting bitcoin Streamer\n")
    while True:
      try:
        result = web_socket.recv()
        transaction_counter.log_hits()
        kafka_producer.push(result)
      except:
        logger.exception("An exception occured")
        logger.error("Shutting down the Bitcoin Streamer")
        traceback.print_exc()
        sys.exit(1)