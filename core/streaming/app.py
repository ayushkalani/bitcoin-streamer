#!/usr/bin/env python
import sys
import os

PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,PACKAGE_ROOT)

import json
import time
import logging
import thread
import websocket
from commons.logger import Logger
from commons.hit_counter import HitCounter
from websocket import create_connection
from core.producer.producer import Producer
logger = Logger().get_logger("test")


if __name__ == "__main__":
    ws = websocket.WebSocket()
    ws = create_connection('wss://ws.blockchain.info/inv')
    ws.send(json.dumps({"op":"unconfirmed_sub"}))
    logger.info("Starting bitcoin Streamer\n")
    kafka_producer = Producer('bitcoin-stream-1')
    hc = HitCounter()
    while True:
        try:
            result = ws.recv()
            hc.log_hits()
            kafka_producer.push(result)
            logger.debug(hc.get_hit())
        except Exception as e:
            logger.exception("An exception occured")
            break