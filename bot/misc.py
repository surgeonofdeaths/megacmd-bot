from redis import asyncio as aioredis

redis = aioredis.Redis.from_url("redis://localhost:6379/0")

# SET user:id:navtree:title_id "long_title"

# if len(title) > 55:
#    redis.set()
# else:
#    callback_data
