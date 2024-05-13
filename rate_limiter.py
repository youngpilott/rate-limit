import redis
import time
import random
import os
from datetime import datetime

class RateLimiter:
    def __init__(self, redis_host, redis_port, window_size, max_requests):
        self.redis_client = redis.Redis(host=redis_host, port=redis_port)
        self.window_size = window_size
        self.max_requests = max_requests

    def is_allowed(self, key):
        current_time = int(time.time())
        key_prefix = f'{key}:'
        window_start = current_time - self.window_size
        # Remove old entries from the sorted set
        self.redis_client.zremrangebyscore(key_prefix, '-inf', window_start)

        # Count the number of requests in the sliding window
        count = self.redis_client.zcard(key_prefix)

        # If the count exceeds the maximum requests, deny the request
        if count >= self.max_requests:
            return False, current_time

        # Add the allowed request timestamp to the sorted set
        self.redis_client.zadd(key_prefix, {current_time: current_time})

        return True, current_time