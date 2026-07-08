import redis

r = redis.Redis(host='redis-server', port=6379, db=0)

r.publish('food_info', 'tuna Sandwich')

r.publish('food_info', 'Orange')

r.publish('food_info', 'Chocolate Cake')