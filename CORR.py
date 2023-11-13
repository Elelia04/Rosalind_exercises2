from Bio import SeqIO
from Hamm_funct import hamming_dist as hd 
from compl_funct import compl

def corr(str_seq):
    
    #Creating a dictionary containing the reverse complements
    rev_dict={"A": "T", "T": "A", "C": "G", "G": "C"}

    corrections = []
    correct_seq =[]
    incorrect_seq= []

    for seq in str_seq:
        reversed_seq = compl(seq) #generating the reverse complement
        if str_seq.count(seq) + str_seq.count(reversed_seq) >= 2: #Checking if the current seq or the reverse compl appears at least twice
            correct_seq.append(seq)
        else:
            incorrect_seq.append(seq)

    for i in incorrect_seq:
        for c in correct_seq:
            rev_cr = compl(c) #compl seq of correct 
            if hd(i, c) == 1:
                corrections.append((i, c))
                break
            if hd(i, rev_cr) == 1:
                corrections.append((i, rev_cr))
                break
    return corrections

#Opening the file reading FASTA format
if __name__ == "__main__":
    seq_name, seq_string = [], []
    with open ("CORR.txt",'r') as fas:
        for seq_rec in SeqIO.parse(fas,'fasta'):
            seq_name.append(str(seq_rec.name))
            seq_string.append(str(seq_rec.seq))
    
    output = corr(seq_string)

    for ircorr, corrc in output:
        print("{}->{}".format(ircorr, corrc))