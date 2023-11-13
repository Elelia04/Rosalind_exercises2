def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
file_path = 'TREE.txt' 
input_data = read_fasta_file(file_path)

a = input_data.split('\n')
n = int(a[0]) #number of nodes 
m = len(a)-1 #number of edges 

min_edges = n-1-m
print(min_edges)
