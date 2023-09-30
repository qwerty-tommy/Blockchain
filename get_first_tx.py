from bitcoin.rpc import RawProxy
import json
import decimal

# Bitcoin Core RPC 연결 설정
rpc_user = 'foo1'
rpc_password = 'password'
rpc_host = '127.0.0.1' 
rpc_port = 8332  

# Bitcoin Core RPC 연결
proxy = RawProxy(service_url=f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}')

txid="01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff0704ffff001d0104ffffffff0100f2052a0100000043410496b538e853519c726a2c91e61ec11600ae1390813a627c66fb8be7947be63c52da7589379515d4e0a604f8141781e62294721166bf621e73a82cbf2342c858eeac00000000"
tx = proxy.decoderawtransaction(txid)

def decimal_to_float(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

# JSON 형식으로 이쁘게 출력
print(json.dumps(tx, indent=4, default=decimal_to_float))

# bitcoin.rpc.InvalidAddressOrKeyError: {'code': -5, 'message': 'The genesis block coinbase is not considered an ordinary transaction and cannot be retrieved'}
# fk