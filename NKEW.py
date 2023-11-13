from Bio import Phylo
import io

with open('NKEW.txt', 'r') as f:
    file_content = f.read()
    trimmed_content = file_content.strip() #removing whitespaces 
    pair = trimmed_content.split('\n\n')
    pairs = [c.split('\n') for c in pair]

for pair in pairs:   
    x, y = pair[1].split() 

    #reading the tree from the first line of c
    tree = Phylo.read(io.StringIO(pair[0]), 'newick') 

    #Calculation and print of distance 
    print(round(tree.distance(x, y)), end=' ') 

print()

