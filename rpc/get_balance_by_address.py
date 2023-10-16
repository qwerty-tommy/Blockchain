from bitcoin.rpc import RawProxy
import json

rpc_user = 'foo1'
rpc_password = 'password'
rpc_host = '127.0.0.1'
rpc_port = 8332
address_to_check = '1Cdid9KFAaatwczBwBttQcwXYCpvK8h7FK'
proxy = RawProxy(service_url=f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}',timeout=120)

with open("result/blockhash5", "r") as file:
    block_hashes = json.load(file)

for block_hash in block_hashes:
    block=proxy.getblock(block_hash)

    for txid in block['tx']:
        print(txid)
        if txid == block['tx'][0]:  
            continue

        tx = proxy.getrawtransaction(txid, 1)

        for vin in tx['vin']:
            vin_txid = vin['txid']
            vin_vout = vin['vout']
            vin_tx = proxy.getrawtransaction(vin_txid, 1)
            vin_value = vin_tx['vout'][vin_vout]['value']
            
            if 'address' in vin_tx['vout'][vin_vout]['scriptPubKey']:
                if address_to_check in vin_tx['vout'][vin_vout]['scriptPubKey']['address']:
                    print(block['height'])
                    balance -= vin_value
                    with open("result/balance1", "a") as output:
                        output.write(f"blockhash : {block_hash}\ntxid : {txid}\nvalue(in) : {vin_value}\n\n")

        for vout in tx['vout']:
            if 'address' in vout['scriptPubKey']:
                if address_to_check in vout['scriptPubKey']['address']:
                    print(block['height'])
                    balance += vout['value'] 
                    with open("result/balance1", "a") as output:
                        output.write(f"blockhash : {block_hash}\ntxid : {txid}\nvalue(out) : {vout['value']}\n\n")
