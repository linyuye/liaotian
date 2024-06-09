import redis

def redis_conn_pool():
    try:
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, password='123456')
        r = redis.Redis(connection_pool=pool)
        
        # 测试连接是否成功
        if r.ping():
            print("Connected to Redis successfully!")
        else:
            print("Failed to connect to Redis.")
            
    except redis.ConnectionError as e:
        print(f"Failed to connect to Redis: {e}")
        return None
        
    return r

def view_redis_content():
    r = redis_conn_pool()
    if not r:
        return

    # 获取所有键
    keys = r.keys('*')
    print(f"Total keys: {len(keys)}")
    
    # 查看每个键的类型和值
    for key in keys:
        key_type = r.type(key).decode("utf-8")
        print(f"Key: {key}, Type: {key_type}")
        
        if key_type == 'string':
            value = r.get(key)
            print(f"Value: {value}")
        elif key_type == 'list':
            values = r.lrange(key, 0, -1)
            print(f"Values: {values}")
        elif key_type == 'set':
            values = r.smembers(key)
            print(f"Values: {values}")
        elif key_type == 'hash':
            values = r.hgetall(key)
            print(f"Values: {values}")
        elif key_type == 'zset':
            values = r.zrange(key, 0, -1, withscores=True)
            print(f"Values: {values}")
        else:
            print("Unknown type")

if __name__ == "__main__":
    view_redis_content()
