def Fasta_seq(Fasta_input):
    sequences = Fasta_input.split('>')
    seq_list = []
    
    for seq in sequences:
        if seq:
            a = seq.split('\n')
            DNAseq = ''.join(a[1:])
            seq_list.append(DNAseq)
            
    return seq_list

def Fasta_str(Fasta_input):
    sequences = Fasta_input.split('>')
    fasta = []
    
    for seq in sequences:
        if seq:
            a = seq.split('\n')
            Fasta_seq = ''.join(a[0])
            fasta.append(Fasta_seq)
            
    return fasta 