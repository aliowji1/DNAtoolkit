dna_str_1 = "TTCGATCCATTG"
dna_str_2 = "ATCAATCGATCG"

#loop approach
def h_d_loop(str_1, str_2):
    h_distance = 0
    for postion in range (len (str_1)):
        if str_1[postion] != str_2[postion]:
            h_distance += 1
    return h_distance

#set approach
def h_d_set(str_1, str_2):
    nucleotide_set_1 = set([(x, y) for x, y in enumerate(str_1)])
    nucleotide_set_2 = set([(x, y) for x, y in enumerate(str_2)])

    print(nucleotide_set_1.difference(nucleotide_set_2))
    return len(nucleotide_set_1.difference(nucleotide_set_2))

#zip approach
def h_d_zip(str_1, str_2):
   
    return len([(n1, n2) for n1, n2 in zip(str_1, str_2)  if n1 !=  n2 ])



#test
print("Loop Hamming Distance: ", end= '')
print(h_d_loop(dna_str_1, dna_str_2)) 


print("Set Hamming Distance: ")
print(h_d_set(dna_str_1, dna_str_2)) 

print("Zip  Hamming Distance: ")
print(h_d_zip(dna_str_1, dna_str_2))