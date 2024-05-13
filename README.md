# Sliding Window Rate Limiter with Redis

This Python code demonstrates a sliding window rate limiter implementation using Redis as a storage backend. Rate limiting is a technique used to control the rate of requests sent or received by a system to prevent overload.

## Description

The sliding window rate limiter algorithm allows a fixed number of requests to be processed within a specified time window. In this implementation, Redis is used to store timestamps of requests, and a sliding window approach is employed to determine if a new request should be allowed or denied based on the configured rate limits.

## Dependencies

- Python 3.x
- Redis (Redis server running locally or accessible)

## Installation

1. Clone the repository:


2. Install the required dependencies:
   ```
   $pip install -r requirements.txt


## Usage

1. Import the `RateLimiter` class into your Python code.
2. Initialize an instance of the `RateLimiter` class with appropriate parameters, including Redis host, port, window size, and maximum requests allowed within the window.
3. Use the `is_allowed()` method of the `RateLimiter` instance to check if a request is allowed or denied.

```python
from rate_limiter import RateLimiter

limiter = RateLimiter(redis_host='localhost', redis_port=6379, window_size=60, max_requests=10)
if limiter.is_allowed('user1')[0]:
    print("Request allowed")
else:
    print("Request denied")
