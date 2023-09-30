from bitcoin.rpc import RawProxy

rpc_user='foo1'
rpc_password='password'
rpc_cookie=f'{rpc_user}:{rpc_password}'
rpc_host = '127.0.0.1' 
rpc_port = 8332  

# Bitcoin Core 노드에 연결
p = RawProxy(service_url=f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}', timeout=60)
#p = RawProxy(service_url=f'http://cookie:{rpc_cookie}@{rpc_host}:{rpc_port}')

info=p.getblockchaininfo()

print(info['blocks'])
