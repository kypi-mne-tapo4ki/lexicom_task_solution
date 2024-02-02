import redis.asyncio as redis

redis_client = redis.Redis(host="redis", decode_responses=True)
