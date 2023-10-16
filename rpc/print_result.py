file_path = 'result/balance1'

with open(file_path, 'r') as file:
    lines = file.readlines()

input_amount = 0.0
output_amount = 0.0

for line in lines:
    if line.startswith('value(out)'):
        output_amount += float(line.split(':')[-1].strip())
    elif line.startswith('value(in)'):
        input_amount += float(line.split(':')[-1].strip())

print(f'input : {input_amount:.8f} BTC')
print(f'output : {output_amount:.8f} BTC')
