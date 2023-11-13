Fasta_str = '''>Rosalind_3611
ATGTTGAACTCAGCCAAGGGTCGTACATGCCCGGCCATATTTCCCTTATGACCCCCAGTC
TGCGAATATATTAAGGACACCTGTGCGTGACTTTACGTACCTATGATAGTTAGGCAATTC
ATTTCCCTGCTAAGCCACACGCGTGACTTGTAGTTTGCTGACTGCGTGCGAATGGACTTG
GCATGATCCTTGTTCTATCTTAATCTTTATGGAGGTCGTTCCCACCTACAACCAAAACTA
GGGAATGAAGAAGCTACGCGGGTTCCTCCCATTACTGCCACAACTTCAACGTGAATACAA
GTCTCGAGTCTGACAACTCCGCCTTGCTACCGCTGAACGATGTGTCTGGCTTTAAACTCC
CTGGAGCTAGATGTAATCGCGCACTTATATATAACATATGCACCGACAGCTAAGCCAAAT
TCGCTGGGTTACCTATTTCGTGAATTAGCTTTCATGGTGTAGCGCCTTCGCTAATGGGGA
GCTCGACGATGATTTACGCAATTGAACCCCTCGCGAGTTTAACAAGGAGCAAGGAAACCC
CGGTCGCTTGTGCGACCTACATAAGCACCCGCCTGGATACGTTGGGCTTTACGCAAAAAA
GCGCCAGTTTCGACAGTTCGACGTGCCACATCCCGCACCACTTAATCCGAGTTATCTCCA
CAGAGGTCTCCACCTCTAGGTAGGTGTAGCCGGCAACTATTTCACGGGCGGGAAGTCAGT
GCGAGGGATGCTAAAAGTCGTCTAAGGTCTTCGAACACATACGCTTGCTTGCACTTCCGC
AGGATATCGCACCAACTAGCACCAACCCACCGGCCTTTAACTCCGCTACCATGGACACCC
ACAGAGTTATTCCCGGTCGGGGTGGTAACTAAGCCTGGCTATAGCCCACTGATACCTTCC
GATTTAGACAGTAGTTTTGAAGCGACACATAGTAGTAATGAAGAGAGGGATTTATTCCGC
GCTGTTGGCGGCAGACTAGAGTATCAATGTATTAG
>Rosalind_4049
TTCATGGTGTAGCGCCTTCGCTAATGGGGAGCTCGACGATGATT
>Rosalind_2955
TGCCACATCCCGCACCACTTAATCCGAGTTATCTCCA
>Rosalind_8113
GTGAATACAAGT
>Rosalind_8236
TACGTTGGGCTTTACG
>Rosalind_9247
CCCACCTACAACCAAAACTAGGGAATGAAGAAGCTAC
>Rosalind_9337
AAGCCAAATTCG
>Rosalind_5662
CCATGGACACCCACAGAGTTA
>Rosalind_8859
CTATGATAGTTAGGCAATTCATTTCCCTGCTAAGCCACACGCGTG
>Rosalind_9690
TGCGAATGGACTTGGCATGATCCTTGTTCT
>Rosalind_7868
GCGAGTTTAAC
>Rosalind_9468
AGTAGTTTTGAAGCGACACATAGTAGTAATGAAGAGAGGGATTT
>Rosalind_7465
CCCTTATGACCCCCAGTCTGCG
>Rosalind_0032
CTAGCACCAACC
>Rosalind_2836
CACGGGCGGGAAGTCAGTGCGAGGGATGCTAAAAGT
>Rosalind_6991
GGAGCTAGATGTA
'''

#Removing the Fasta format

def Fasta_rem(Fasta_input):
    sequences = Fasta_input.split('>')
    seq_list = []
    
    for seq in sequences:
        if seq:
            a = seq.split('\n')
            DNAseq = ''.join(a[1:])
            seq_list.append(DNAseq)

    return(seq_list)

fasta_seq = Fasta_rem(Fasta_str)

for intr in fasta_seq[1:]:
    fasta_seq[0] = fasta_seq[0].replace(intr, '') #RNA sequence after splicing 


#Changing Dna sequence into Rna
RNA_seq = ''
for el in fasta_seq[0]:
    if el == 'T':
        RNA_seq += 'U'
    else:
        RNA_seq += el 

cod_lst = []
Amino_seq = ''

#Dic from codons to aminoacids 
Codons_dict = {'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
              'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
              'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
              'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
              'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
              'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
              'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
              'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
              'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
              'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
              'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
              'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
              'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
              'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
              'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
              'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

#Going from codons to aminoacids 
for i in range(0, len(RNA_seq), 3):
    cod = RNA_seq[i:i+3]
    cod_lst.append(cod)
for el in cod_lst:
    if el in Codons_dict:
        Amino_seq += Codons_dict[el]

print(Amino_seq)



