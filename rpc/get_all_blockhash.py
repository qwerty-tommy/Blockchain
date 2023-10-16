from bitcoin.rpc import RawProxy

rpc_user = 'foo1'
rpc_password = 'password'
rpc_host = '127.0.0.1'
rpc_port = 8332  

proxy = RawProxy(service_url=f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}',timeout=60)

for block_height in range(700000,800000):
    print(f'\"{proxy.getblockhash(block_height)}\"',end=', ')
    
