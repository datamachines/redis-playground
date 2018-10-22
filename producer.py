import asyncio
import time
import aioredis
import random
import uvloop
import yaml

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

loop = asyncio.get_event_loop()
RECORDS = 1000
async def add_message_with_sleep(redis, loop, stream):
    start = time.time()
    records = RECORDS + 1
    
    for i in range(records):
        temperature = str(random.randrange(10, 40))
        humidity = str(random.randrange(10, 30))
        
        fields = {'id': i, 'temperature': temperature.encode('utf-8'),
                  'humidity': humidity.encode('utf-8')}
        await redis.xadd(stream, fields)
    end = time.time()
    print("Inserting %s records took %d seconds"% (RECORDS, end-start))

async def main():
    stream = open('config.yaml', 'r')    
    config=yaml.load(stream)
    redis = await aioredis.create_redis('redis://'+config['redis_host'], loop=loop)
    stream = config['redis_topic']
    await add_message_with_sleep(redis, loop, stream)
    redis.close()
    await redis.wait_closed()

loop.run_until_complete(main())
