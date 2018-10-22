redis streams.

this example show how to use redis streaming with consumer group, and redis pubsub.



### Requirements

* Python 3.5.2+
* Redis 5.0 (latest stable version)
* use https://github.com/aio-libs/aioredis


### Installation

* Clone the repo
* install requirements with `pip3 install -r requirements.txt`

redis Stream, requires Redis 5, released Oct 17 2018
* To produce data `python3 producer.py`
* To start a consumer `python3 consumer.py <consumer_name>`

redis PubSub:
 * To produce data: `python3  pubsub/publisher.py`
 * To consume data: `python3 pubsub/subscriber.py`
 
   
### Streaming test output
start 4 consumers will load balanced all consumers in the consumer group.
   >python consumer.py consumer1
   >python consumer.py consumer2
   >python consumer.py consumer3
   >python consumer.py consumer4
   
 notice the id is skiping every 4th. there are 4 consumers running in the example
 
	> python3 consumer.py consumer4
	Consumer group already exists
	processing [(b'temperature', b'1540231226640-0', OrderedDict([(b'id', b'410'), (b'temperature', b'24'), (b'humidity', b'11')]))]
	processing [(b'temperature', b'1540231226877-0', OrderedDict([(b'id', b'415'), (b'temperature', b'20'), (b'humidity', b'17')]))]
	processing [(b'temperature', b'1540231227014-0', OrderedDict([(b'id', b'418'), (b'temperature', b'27'), (b'humidity', b'10')]))]
	processing [(b'temperature', b'1540231227309-0', OrderedDict([(b'id', b'423'), (b'temperature', b'29'), (b'humidity', b'11')]))]
	processing [(b'temperature', b'1540231227467-0', OrderedDict([(b'id', b'426'), (b'temperature', b'22'), (b'humidity', b'15')]))]
	processing [(b'temperature', b'1540231227664-0', OrderedDict([(b'id', b'430'),

### pubsub test output
	  starting 4 consumers, all consumers are notified of all messages.
	  recieve message...
	 data:  b"{'id': 401, 'temperature': b'25', 'humidity': b'13'}" from Channel: b'temperature' 
	recieve message...
	 data:  b"{'id': 402, 'temperature': b'26', 'humidity': b'14'}" from Channel: b'temperature' 
	recieve message...
	 data:  b"{'id': 403, 'temperature': b'23', 'humidity': b'11'}" from Channel: b'temperature' 
	recieve message...
	 data:  b"{'id': 404, 'temperature': b'21', 'humidity': b'11'}" from Channel: b'temperature' 
	recieve message...
	 data:  b"{'id': 405, 'temperature': b'23', 'humidity': b'11'}" from Channel: b'temperature' 


### references:
   https://redis.io/topics/streams-intro  
   https://redis.io/topics/pubsub
       
##
### License


Distributed under the MIT License
