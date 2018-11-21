
def Pr(Text, Profile):
	p = 1
	for i in range(len(Text)):
		p = p*Profile[Text[i]][i]
	return p

def ProfileMostProbableKmer(Text, k, Profile):
	mostprob = Text[0:k]
	p = 0
	for i in range(len(Text)-k+1):
		sequence = Text[i:i+k]
		x = Pr(sequence, Profile)
		if x>p:
			p = x
			mostprob = sequence
	return mostprob

def Motifs(Profile, Dna, k):
	motifs = []
	for x in Dna:
		motifs.append(ProfileMostProbableKmer(x, k, Profile))
	return motifs


DNA_ = ['AAGCCAAA', 
'AATCCTGG', 
'GCTACTTC',
'ATGTTTTG']


profile1= { 'A': [0.8, 0.0, 0.0, 0.2 ],'C': [ 0.0, 0.6, 0.2, 0.0], 'G': [ 0.2 ,0.2 ,0.8, 0.0], 'T': [ 0.0, 0.2, 0.0, 0.8]}   
dna1=['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']


print(str("Motifs: ") + str(Motifs(profile1, dna1, 4)))

import random
def RandomMotifs(Dna, k, t):
	randommot = []
	for x in Dna:
		y = random.randint(0, len(Dna[0])-k)
		randommot.append(x[y:y+k])
	return randommot

print(RandomMotifs(dna1, 3, 5))
print(random.randint(1, 5))

"""
If you lessen the number of frames being used, you can save time
"""

def Normalize(Probabilities):
	sum = 0
	for probability in Probabilities.values():
		sum += probability
	for nucleotide, probability in Probabilities.items():
		Probabilities[nucleotide] = probability/sum
	return Probabilities

Probability2 = {1: 0.22, 2: 0.54, 3:0.58, 4:0.36, 5:0.3}
print(str("Normalize probabilities: " + str(Normalize(Probability2)) ))

def WeightedDie(Probabilities):
	p = random.uniform(0, 1)
	for val in Probabilities:
		p -= Probabilities[val]
		if p <= 0:
			return val

def ProfileGeneratedString(Text, Profile, k):
	n = len(Text)
	probabilities = {}
	for i in range(0, n-k+1):
		probabilities[Text[i:i+k]] = Pr(Text[i:i+k], Profile)
	probabilities = Normalize(probabilities)
	return WeightedDie(probabilities)

"""
 GibbsSampler(Dna, k, t, N)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
        ﻿BestMotifs ← Motifs
        for j ← 1 to N
            i ← randomly generated integer between 1 and t
            Profile ← profile matrix formed from all strings in Motifs except for Motifi
            Motifi ← Profile-randomly generated k-mer in the i-th string
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
"""
from part_4_Biology_Meets_Programming import ProfileWithPseudocounts, Score
from random import randint, uniform

def GibbsSampler(dna, k, t, N):
	motifs = RandomMotifs(dna, k, t)
	best_motifs = motifs
	profile = ProfileWithPseudocounts(motifs)
	for i in range(N):
		i = random.randint(0, t-1)
		motifs.pop(i)
		motifs.insert(i, ProfileGeneratedString(dna[i], profile, k))
		

	return best_motifs


"""
def GibbsSampler(dna, k, t, N):
	motifs = RandomMotifs(dna, k, t)
	best_motifs = motifs
	profile = ProfileWithPseudocounts(motifs)
	for i in range(N):
		i = random.randint(0, t-1)
		motifs.pop(i)
		motifs.insert(i, ProfileGeneratedString(dna[i], profile, k))
		if Score(motifs) < Score(best_motifs): #not needed?
			best_motifs = motifs #not needed?
		

	return best_motifs
"""








		

Dnagibbs = [
'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 
'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']





Profile1 = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
Probability1 = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
Probability2 = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
print(str("Probability Generated String: ") + str(ProfileGeneratedString('AAACCCAAACCC', Profile1, 2)))
print(str("WeightedDie: ") + str(WeightedDie(Probability2)))
print(str("Normalize probabilities: " + str(Normalize(Probability1)) ))

longDNA = ["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC", "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG", "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC", "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC", "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG", "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA", "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA", "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG", "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG", "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]
print(str("Gibbs: ") + str(GibbsSampler(Dnagibbs, 8, 5, 100)))
BestMotifs = GibbsSampler(longDNA, 15, 10, 100)
print(20* BestMotifs)
print(Score(BestMotifs))
