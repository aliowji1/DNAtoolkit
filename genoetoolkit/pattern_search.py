from re import findall
from time import perf_counter

#Generic for loop solution
def count_kmer_loop (sequence, kmer):
        """Counts repeating kmers in the sequence. Includes overlappling k-mers"""
        kmer_count = 0
        for position in range(len(sequence) - (len(kmer) -1)):
            if sequence[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count

#List comprehension 
def count_kmer_listcomp(sequence, kmer):
     kmer_list = [sequence[pos:pos + len(kmer)]
                for pos in range(len(sequence) - (len(kmer) - 1 ))]
     return kmer_list.count(kmer )

#RegExp
def count_kmer_regexp(sequence, kmer):
     return len(findall(f'(?=({ kmer}))', seq))

#test

seq = "AAATTAAAAAC" * 1000
kmer = "AAA"

start_time = perf_counter()
print("Loop k-mer count: ", end = '')
print(count_kmer_loop(seq, kmer))
elapsed_time = perf_counter()
print(f'loop took: {(elapsed_time) - (start_time):.5f}s\n')  

start_time = perf_counter()
print("List Comprehension k-mer count: ", end = '')
print(count_kmer_listcomp(seq, kmer))
elapsed_time = perf_counter()
print(f'list took: {(elapsed_time) - (start_time):.5f}s\n')  

start_time = perf_counter()
print("Reg Exp  k-mer count: ", end = '')
print(count_kmer_regexp(seq, kmer))
elapsed_time = perf_counter()
print(f'Reg Exp  took: {(elapsed_time) - (start_time):.5f}s\n')  

