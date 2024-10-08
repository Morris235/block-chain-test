import time

from api.v1.client import binance_client


def binance_server_timestamp():
    server_time = binance_client().get_server_time()
    server_timestamp = server_time['serverTime']
    return server_timestamp

def api_server_time():
    current_time = int(time.time() * 1000)
    return current_time