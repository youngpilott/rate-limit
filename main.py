import time
import random
from datetime import datetime
from rate_limiter import RateLimiter
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    redis_host = os.environ.get('REDIS_HOST', 'localhost')
    redis_port = int(os.environ.get('REDIS_PORT', 6379))
    window_size = int(os.environ.get('WINDOW_SIZE', 60))
    max_requests = int(os.environ.get('MAX_REQUESTS', 10))

    limiter = RateLimiter(redis_host, redis_port, window_size, max_requests)

    for i in range(30):
        key = os.environ.get('LIMITER_NAME', 'rate-limiter-1')
        check, time_check = limiter.is_allowed(key)
        if check:
            print(f"{datetime.fromtimestamp(time_check)}-Request {i+1}: Allowed")
        else:
            print(f"{datetime.fromtimestamp(time_check)}-Request {i+1}: Denied")
        random_sec = random.randint(1, 5)
        time.sleep(random_sec)