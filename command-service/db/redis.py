import redis.asyncio as redis
import os
 
REDIS_URL = os.environ.get('REDIS_URL')
redis = redis.from_url(REDIS_URL, decode_responses=True)
