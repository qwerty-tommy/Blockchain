from bitcoin.rpc import RawProxy

# Bitcoin Core RPC 연결 설정
rpc_user = 'foo1'
rpc_password = 'password'
rpc_host = '127.0.0.1'
rpc_port = 8332

# 주소 설정
address_to_check = '1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK'

# Bitcoin Core RPC 연결
proxy = RawProxy(service_url=f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}',timeout=120)

balance = 0

# block count(20230930)
blockcount = 809983

# 블록체인의 모든 블록을 반복하여 주소와 관련된 트랜잭션을 검색
for block_height in range(blockcount + 1):
    block_hash = proxy.getblockhash(block_height)
    block = proxy.getblock(block_hash)
    
    for txid in block['tx']:
        
        if txid == block['tx'][0]:  # 코인베이스 트랜잭션인 경우 건너뛰기
            continue

        tx = proxy.getrawtransaction(txid, 1)  # 트랜잭션 세부 정보 가져오기
        for vout in tx['vout']:
            if 'addresses' in vout['scriptPubKey']:
                if address_to_check in vout['scriptPubKey']['addresses']:
                    print(tx, vout['value'] )
                    balance += vout['value']  # 출력에서 주소가 발견될 때 잔고 증가

print(f'주소 {address_to_check}의 잔고: {balance} BTC')
