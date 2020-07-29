from redis import StrictRedis,ConnectionPool
from config.initializers import REDIS_SERVER,REDIS_PORT,REDIS_DB

class RedisConnector(object):
    def __init__(self):
        self.redis_pool = ConnectionPool(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)

    def get_connection(self):
        return StrictRedis(connection_pool=self.redis_pool)
