def find_overlap_k(seq1, seq2):
    min_len = min(len(seq1), len(seq2))
    count = 0 
    letters = []

    for k in range(1, min_len + 1):
        if seq1[-k:] == seq2[:k]:
            count += 1
    
    return count

sequence1 = 'AAATAAA'
sequence2 = 'AAATTTT'

print(find_overlap_k(sequence1,sequence2))

