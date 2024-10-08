import time

from api.v1.client import client_info


def binance_server_timestamp():
    server_time = client_info().get_server_time()
    server_timestamp = server_time['serverTime']
    return server_timestamp

def api_server_time():
    current_time = int(time.time() * 1000)
    return current_time