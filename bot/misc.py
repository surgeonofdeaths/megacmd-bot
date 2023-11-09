from redis import asyncio as aioredis

redis = aioredis.Redis(host='localhost', port=6379, db=0)

# SET user:id:navtree:title_id "long_title"

# if len(title) > 55:
#    redis.set()
# else:
#    callback_data
