import yaml
import os
import subprocess

with open("config/kafka.yml", 'rt') as f:
    kafka_config = yaml.safe_load(f.read())
KAFKA_BROKER = kafka_config["brokers"][0]
KAFKA_TOPIC = kafka_config["topic"]
KAFKA_CONSUMER_GROUP_ID = kafka_config["group_id"]

with open("config/redis.yml", 'rt') as f:
    redis_config = yaml.safe_load(f.read())

REDIS_SERVER = redis_config["host"]
REDIS_PORT = redis_config["port"]
REDIS_DB = redis_config["database"]

with open("config/logger.yml", 'rt') as f:
    LOGGER_CONFIG = yaml.safe_load(f.read())
filename = LOGGER_CONFIG["handlers"]["file_handler"]["filename"]

if not os.path.isfile(filename):
    cmd = "touch " + filename
    proc_handle = subprocess.Popen(cmd, bufsize=0, shell=True)
    proc_handle.communicate()
