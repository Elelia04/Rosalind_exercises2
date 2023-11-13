from Fasta_str import Fasta_str, Fasta_seq
from itertools import permutations

def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
file_path = 'GRPH.txt' 
Fasta_input = read_fasta_file(file_path)  

#Creating variables for sequences and FASTA identificators 
a = Fasta_seq(Fasta_input)
b = Fasta_str(Fasta_input)

overlap = 3  #k=3

#Pairs of indices for sequences
pairs = permutations(range(len(a)), 2)

for pair in pairs:
    i, j = pair
    if a[i][-overlap:] == a[j][:overlap]:
        print(b[i],b[j])

