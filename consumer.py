import sys
import asyncio
import time
import aioredis
import random
import uvloop
import yaml

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()

async def process_message(redis, loop, group, consumer, streams):
    start = time.time()
    records = 0
    while True:
        result = await redis.xread_group(group, consumer, streams, count=1, latest_ids=['>'])
        if result:
            records += 1
            print(f"processing {result}")
            #time.sleep(1)
        else:
            print("Timeout")
            break
    end = time.time()
    print(f"Reading {records} records took {end - start} seconds")

async def main(consumer):
    
    stream = open('config.yaml', 'r')    
    config=yaml.load(stream)
    redis = await aioredis.create_redis('redis://'+config['redis_host'], loop=loop)
    streams = [config['redis_topic']]
    consumerGroup = config['redis_topic']+'-cg'

    for stream in streams:
        exists = await redis.exists(stream)
        if not exists:
            await redis.xadd(stream, {b'foo': b'bar'})

        try:
            await redis.xgroup_create(stream, consumerGroup)
        except aioredis.errors.ReplyError as e:
            print("Consumer group already exists")

    await process_message(redis, loop, consumerGroup, consumer, streams)
    redis.close()
    await redis.wait_closed()

if len(sys.argv) < 2:
    print("Consumer name is required")
    exit(1)

consumer = sys.argv[1]
loop.run_until_complete(main(consumer))
