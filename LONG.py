from Fasta_str import Fasta_seq

#Removing the FASTA format
ros_text = open("LONG.txt", "r")
str1 = ros_text.read()
a = Fasta_seq(str1)

def LONG_funct(seq_list, sup_str=''):
    if not seq_list:
        return sup_str

    if not sup_str:
        sup_str = seq_list.pop(0)
        return LONG_funct(seq_list, sup_str)

    for i, d in enumerate(seq_list):
        for j in range(len(d) // 2): #checking for overlaps both at the beginning and at the end of the DNA string 
            prefix_overlap = d[j:]
            suffix_overlap = d[:len(d) - j]

            if sup_str.startswith(prefix_overlap):
                seq_list.pop(i) #removing current DNA string from the list of remaining strings 
                return LONG_funct(seq_list, d[:j] + sup_str)

            if sup_str.endswith(suffix_overlap):
                seq_list.pop(i)
                return LONG_funct(seq_list, sup_str + d[len(d) - j:])
                #updating superstring by appending the part not overlapping with it

print(LONG_funct(a))