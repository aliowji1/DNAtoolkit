# def countNucfrequency(seq):
#     tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
#     for nuc in seq:
#         tmpFreqDict[nuc] += 1
#     return tmpFreqDict  

# DNAString = "ATCGTCTGTG"
# result = countNucfrequency(DNAString)
# print( result )

#output should take string and give numbers, this is outputting a dictionary
#lets change print function

def countNucfrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict  

DNAString = "ATCGTCTGTG"
result = countNucfrequency(DNAString)
print( ''.join([str(val) for key, val in result.items()]))