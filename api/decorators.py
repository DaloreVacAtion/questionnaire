import datetime
import inspect
import logging

from django.db import connection, reset_queries
import time
import functools


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Функция: {func.__name__}")
        print(f"Кол-во запросов: {end_queries - start_queries}")
        print(f"Завершилась за: {(end - start):.2f}s")
        return result

    return inner_func


def logger_decorator(mobile):
    def wrap(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if mobile:
                logger = logging.getLogger('mobile.api')
            else:
                logger = logging.getLogger('site.api')
            func_args = inspect.signature(func).bind(*args, **kwargs).arguments
            func_name = func.__name__
            logger.debug('function name = %s' % func_name)
            logger.debug('request headers = %s' % func_args['request'].headers)
            logger.debug('request path = %s' % func_args['request'].path)
            logger.debug('request method = %s' % func_args['request'].method)
            if func_args['request'].method == 'GET':
                logger.debug('request query param = %s' % func_args['request'].query_params)

            logger.debug('request data = %s' % func_args['request'].data)
            start = datetime.datetime.now()
            logger.debug('into the function = %s' % start)
            retval = func(*args, **kwargs)
            end = datetime.datetime.now()
            logger.debug('return from function = %s' % end)

            logger.debug('response data = %s' % retval.data)
            logger.debug('response status code = %s' % retval.status_code)
            logger.debug('response headers = %s\n' % retval.items())
            return retval

        return wrapper

    return wrap
