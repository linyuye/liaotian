import redis


def redis_conn_pool():
    try:
        pool = redis.ConnectionPool(host='172.24.83.246', port=6379, decode_responses=True, password='123456')
        r = redis.Redis(connection_pool=pool)
        
        # 测试连接是否成功
        if r.ping():
            print("Connected to Redis successfully!")
        else:
            print("Failed to connect to Redis.")
            
    except redis.ConnectionError as e:
        print(f"Failed to connect to Redis: {e}")
        
    return r


# 调用函数并测试连接
redis_conn_pool()
