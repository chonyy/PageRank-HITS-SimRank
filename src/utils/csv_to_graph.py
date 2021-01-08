with open('./dataset/IBM.csv') as f:
    lines = f.readlines()

pairs = []

for line in lines:
    nodes = line.strip().split(',')
    print(nodes)
    for node in nodes[1:]:
        pair = (nodes[0], node)
        pairs.append(pair)

with open('./dataset/IBM.txt', 'w') as f:
    for pair in pairs:
        f.write(f'{pair[0]},{pair[1]}\n')
