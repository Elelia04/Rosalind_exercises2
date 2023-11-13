def hamming_dist(a,b):
    count_mut = 0
    
    if len(a) == len(b):
        for base in range(0, len(a)):
            if a[base] != b[base]:
                count_mut += 1
                
    return count_mut