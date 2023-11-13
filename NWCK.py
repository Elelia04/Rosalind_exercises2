def nwck(T, u, v):

    #Finding the indices
    u_index = T.find(u)
    v_index = T.find(v)

    m = []
    seq = ''

    for i in T[min(u_index, v_index):max(u_index, v_index)]:
        if i in [')', '(', ',']:
            m.append(i)

    for i in m:
        seq += i
    while '(,)' in seq:
        seq = seq.replace('(,)','')
    if seq.count('(') == len(seq):
        return len(seq) 
    if seq.count(',') == len(seq):
        return 2
    if seq.count(')') == len(seq):
        return len(seq)
    else:
        return seq.count(')') + seq.count('(') + 2

tree = []
if __name__ == '__main__':
    with open('NWCK.txt', 'r') as nw:
        for line in nw:
            line = line.strip()
            if len(line) > 0:
                tree.append(line.replace(';', ''))
        i = 0
        while i < len(tree):
            T = tree[i]
            x, y = tree[i+1].split(' ')
            print(nwck(T, x, y), end=" ")
            i += 2
        print()
