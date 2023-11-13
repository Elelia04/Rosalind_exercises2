def compl(Dna_strand):

    DNA_compl = ''
    DNA_dict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    rev_DNA_strand = Dna_strand[::-1]

    for bs in rev_DNA_strand:
        if bs in DNA_dict:
            DNA_compl += DNA_dict[bs]
        else:
            DNA_compl += bs

    return DNA_compl

