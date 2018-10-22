import redis
import time
import traceback
import yaml
import random
if __name__ == '__main__':
    try:

        stream = open('config.yaml', 'r')    
        config=yaml.load(stream)
        r = redis.StrictRedis(host=config['redis_host'], port=config['redis_port'])                          # Connect to local Redis instance

        p = r.pubsub()                                                   

        for i in range(1000):
            temperature = str(random.randrange(20, 30))
            humidity = str(random.randrange(10, 20))
        
            fields = {'id': i, 'temperature': temperature.encode('utf-8'),
                  'humidity': humidity.encode('utf-8')}
            r.publish(config['redis_topic'], fields)
            print("current number of subscribers: %s " % r.pubsub_numsub(config['redis_topic']))
            #print number of subscriptions to the pattern 
            #print (r.pubsub_numpat())
            #time.sleep(0.5)
       

        print("Done")
    except Exception as e:
        print("!!!!!!!!!! EXCEPTION !!!!!!!!!")
        print(str(e))
        print(traceback.format_exc())
