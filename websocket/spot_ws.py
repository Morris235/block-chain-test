from api.v1.client import binance_client
import asyncio
import json
import websockets

async def connect_websocket():
    # 바이낸스 API 키 설정
    market_uri = 'wss://stream.binance.com:9443/ws/' + 'btcusdt@aggTrade'
    user_uri = 'wss://stream.binance.com:9443/ws/' + binance_client().stream_get_listen_key()
    test_uri = 'wss://testnet.binance.vision/ws-api/v3'
    async with websockets.connect(user_uri) as websocket:
        print(websocket.response_headers)
        while True:
            data = await websocket.recv()
            print(data)
            message = json.loads(data)

            # 입출금 이벤트인 경우 처리
            if message['e'] == 'outboundAccountPosition':
                print(message)
                # 여기에 입출금 이벤트 처리 로직 작성 (예: 데이터베이스 저장, 알림 전송 등)


asyncio.run(connect_websocket())

# # 프로그램이 종료되지 않도록 대기
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     ws_client.stop()