import yaml
import os
import subprocess

# REDIS_SERVER='localhost'
# REDIS_PORT=6379
# REDIS_DB=15
# KAFKA_BROKER='localhost:9092'

with open("config/kafka.yml", 'rt') as f:
    kafka_config = yaml.safe_load(f.read())
KAFKA_BROKER = kafka_config["brokers"][0]

with open("config/redis.yml", 'rt') as f:
    redis_config = yaml.safe_load(f.read())

REDIS_SERVER = redis_config["host"]
REDIS_PORT = redis_config["port"]
REDIS_PASSWORD = redis_config["password"]

with open("config/logger.yml", 'rt') as f:
    LOGGER_CONFIG = yaml.safe_load(f.read())
filename = LOGGER_CONFIG["handlers"]["file_handler"]["filename"]

if not os.path.isfile(filename):
    cmd = "touch " + filename
    proc_handle = subprocess.Popen(cmd, bufsize=0, shell=True)
    proc_handle.communicate()
