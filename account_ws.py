from api.v1.client import binance_client
import asyncio
import json
import websockets

async def account_websocket():
    # 바이낸스 API 키 설정
    market_uri = 'wss://stream.binance.com:9443/ws/' + 'btcusdt@aggTrade'
    # 사용자 데이터 스트림 listenKey는 생성 후 60분 동안만 유효. 단, 활성 listenKey에 PUT을 수행하면 유효 기간이 60분 연장
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


asyncio.run(account_websocket())

# # 프로그램이 종료되지 않도록 대기
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     ws_client.stop()