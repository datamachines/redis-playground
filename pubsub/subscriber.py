import redis
import time
import traceback
import yaml


def myHandler(message):
    print("recieve message...")
    # Checks for message
    if message:
        print (" data:  %s from Channel: %s " % (message['data'], message['channel']) )  
                                           
if __name__ == '__main__':
    
    try:
        stream = open('config.yaml', 'r')    
        config=yaml.load(stream)
        r = redis.StrictRedis(host=config['redis_host'], port=config['redis_port'])                          # Connect to local Redis instance

        p = r.pubsub()                                                              # See https://github.com/andymccurdy/redis-py/#publish--subscribe
        p.subscribe(**{config['redis_topic']: myHandler})
        # the event loop is now running in the background processing messages
        thread = p.run_in_thread(sleep_time=0.001)
                                              
      


    except Exception as e:
        print("catch a  EXCEPTION !!!!!!!!!")
        print(str(e))
        print(traceback.format_exc())
         
        # when it's time to shut it down...
        thread.stop()
    