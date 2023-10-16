from bitcoin.rpc import RawProxy

# Bitcoin Core RPC 연결 설정
rpc_user = 'foo1'
rpc_password = 'password'
rpc_host = '127.0.0.1'  # Bitcoin Core가 실행 중인 컴퓨터의 IP 주소 또는 호스트명
rpc_port = 8332  # Bitcoin Core의 RPC 포트 (기본값은 8332)

# Bitcoin Core RPC 연결
proxy = RawProxy(service_url=f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}')

txid="4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"
tx = proxy.getrawtransaction(txid, 1)  # 트랜잭션 세부 정보 가져오기

print(tx)

# bitcoin.rpc.InvalidAddressOrKeyError: {'code': -5, 'message': 'The genesis block coinbase is not considered an ordinary transaction and cannot be retrieved'}
# fk