import collections
from collections import Counter
from structures import *
from utilties import colored

#check the sequence to make sure it is a DNA String

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def nucleotide_frequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict  
 
    #return dict(collections.Counter(seq))

def transcription(seq):
    """DNA -> RNA Transcription, Replace Thymine with Uracil"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """Swapping A with T, G with C. Reversing newly generated String """
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

def gc_content(seq):
    """GC content in a DNA/RNA Sequence"""
    return round((seq.count('G') + seq.count('C')) / len(seq) * 100)

def gc_content_subsec(seq, k = 20):
    """GC contnent in a DNA/RNA sub-sequence length k, k = 20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res

def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an amino acid sequence"""
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]

def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList= []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict

def gen_reading_frames(seq):
    """Generate the six reading frames of a DNA sequence, including the reverse complement"""
    frames = [] 
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq) , 0))
    frames.append(translate_seq(reverse_complement(seq) , 1))
    frames.append(translate_seq(reverse_complement(seq) , 2))
    return frames

def proteins_from_rf(aa_seq):
    """Compute all possible protein from aa seq and return a list of possible proteins"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            #STOP accumulating amino acids if _ - STOP was found
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            # START accumulating amino acids if M - START was found
            if aa == "M":
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return proteins

#Generate all RF
#Extract all prots
#Return a list sorted/unsorted

def all_proteins_from_orfs(seq, startReadPos = 0, endReadPos = 0, ordered = False):
    """Compute all possible proteins for all open reading frames"""
    """Protein search DB: http://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2"""
    """API can be used to pull a protein info"""
    if endReadPos > startReadPos:
        rfs = gen_reading_frames(seq[startReadPos: endReadPos])
    else:
        rfs = gen_reading_frames(seq)
    res = []
    for rf in rfs:
        prots = proteins_from_rf(rf)
        for p in prots:
            res.append(p)
    if ordered:
        return sorted(res, key = len, reverse = True)
    return res

  