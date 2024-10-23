#!/usr/bin/env python3
'''A module that provides utilities for caching requests and tracking usage.
'''
import redis
import requests
from functools import wraps
from typing import Callable

# Initialize Redis connection
cache_store = redis.Redis()
'''Redis instance for caching and tracking.
'''

def cache_tracker(func: Callable) -> Callable:
    '''Decorator that caches the result of a URL fetch and tracks the number of requests made.
    '''
    @wraps(func)
    def wrapper(url: str) -> str:
        '''Wrapper function to handle caching and request counting.
        '''
        cache_store.incr(f'calls:{url}')
        cached_response = cache_store.get(f'data:{url}')
        
        if cached_response:
            return cached_response.decode('utf-8')
        
        response_data = func(url)
        cache_store.set(f'calls:{url}', 0)
        cache_store.setex(f'data:{url}', 10, response_data)
        
        return response_data
    return wrapper

@cache_tracker
def fetch_content(url: str) -> str:
    '''Fetches the content of a web page, caches it, and tracks the number of times it's requested.
    '''
    return requests.get(url).text
