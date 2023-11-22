
class genomeToolkit:
    def __init__(self):
        print("Genome Toolkit initiated")
    
    def count_kmer(self, sequence, kmer):
        """Counts repeating kmers in the sequence. Includes overlappling k-mers"""
        kmer_count = 0
        for position in range(len(sequence) - (len(kmer) -1)):
            if sequence[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count
    
    def find_most_frequent_kmers(self, sequence, k_len):

        #1. Dictionary to store frequent kmers
        kmer_frequencies = {}
        #2. A loop to iterate through the DNA string and extract k-mers of a given length,
        #while also incrementing the frequency of each k-mer.
        for i in range(len(sequence) - k_len + 1):
            kmer = sequence[i:i+k_len]
            if kmer in kmer_frequencies:
                kmer_frequencies[kmer] += 1
            else:
                kmer_frequencies[kmer] = 1 
        #3. variable to store maximum value
        highest_frequency = max(kmer_frequencies.values( ))

        #list comprehension loop
        return [
            kmer for kmer, frequency in kmer_frequencies.items()
            if frequency == highest_frequency 
        ]