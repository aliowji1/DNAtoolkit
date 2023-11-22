def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [line.strip() for line in f.readlines()]


def gc_content(seq):
    """GC content in a DNA/RNA Sequence"""
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

# == read data from the file (FASTA file formatted)
 #storing file conents in a list
FASTAFile = readFile("test_data/gc_content.txt")
#Dictionary for labels + data
FASTADict = {}
#String for holding current label
FASTALabel = "" 

print(FASTAFile)
# == clean/prepare data

#Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line 
print(FASTADict)
#Using Dictionary Comprehension to generate a new dictionary with GC content 
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items() }
print(RESULTDict  )

#looking for max value in values of new dictionary
MaxGCKey = max(RESULTDict, key=RESULTDict.get)

#== collect results
print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')