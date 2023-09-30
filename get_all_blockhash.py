from bitcoin.rpc import RawProxy

# Bitcoin Core RPC 연결 설정
rpc_user = 'foo1'
rpc_password = 'password'
rpc_host = '127.0.0.1'
rpc_port = 8332  

# Bitcoin Core RPC 연결
proxy = RawProxy(service_url=f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}',timeout=60)

# block count(20230930)
blockcount = 809983

print('[')

# 블록체인의 모든 블록을 반복하여 주소와 관련된 트랜잭션을 검색
for block_height in range(1,10 + 1):
    print(f'\"{proxy.getblockhash(block_height)}\"',end=', ')
    
print(']')
