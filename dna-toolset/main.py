from DNAToolkit import *
import random

rndDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50 )])
 
DNAStr =  validateSeq(rndDNAStr)

# print(countNucfrequency(DNAStr))
# print(transcription(DNAStr)) 


print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)} \n')
print(f'[2] + Nucleotide Frequency: {countNucfrequency(DNAStr)}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {DNAStr} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement] \n ")

print(f"[5] + GC Content: {gc_content(DNAStr)}%\n")
print('hello')

print(
    f"[6] + GC Content in subsection k = 5: {gc_content_subsec(DNAStr, k = 5)} \n")

print(f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)} \n')

print(f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")} \n')

print(f'[9] + Reading_frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)    

print('\n[10] + All prots in 6 open reading frames:')
for prot in all_proteins_from_orfs(NM_000207_3 , 0 , 0, True):
    print(f'{prot}')  
