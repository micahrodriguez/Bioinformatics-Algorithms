def CountWithPseudocounts(Motifs):
	count = {}
	k = len(Motifs[0])  #k = horizontal dimensions
	for symbol in "ACGT":
		count[symbol] = []
		for j in range(k): #j = column numbers
			count[symbol].append(1)
	t = len(Motifs) #t = vertical dimensions
	for i in range(t): #i = row numbers
		for j in range(k):
			symbol = Motifs[i][j]
			count[symbol][j] += 1
	return count

print(str("Count with Pseudocounts: ") + str(CountWithPseudocounts(['AACGTA','CCCGTT', 'CACCTT', 'GGATTA','TTCCGG'])))

def ProfileWithPseudocounts(Motifs):
	profile = {}
	k = len(Motifs[0])
	t = len(Motifs)
	for symbol in "ACGT":
		profile[symbol] = []
		for j in range(k):
			profile[symbol].append(0)
		for i in range(t):
			for j in range(k):
				profile[symbol][j] = CountWithPseudocounts(Motifs)[symbol][j]/(t+4)
	return profile


print(str("Profile with Pseudocounts: ") + str(ProfileWithPseudocounts(['AACGTA','CCCGTT', 'CACCTT', 'GGATTA','TTCCGG'])))

Count = CountWithPseudocounts
Profile = ProfileWithPseudocounts



def Consensus(Motifs):
	k = len(Motifs[0])
	count = Count(Motifs)
	consensus = ""
	for j in range(k):
		m = 0
		frequentSymbol = ""
		for symbol in "ACGT":
			if count[symbol][j] > m:
				m = count[symbol][j]
				frequentSymbol = symbol
		consensus += frequentSymbol
	return consensus
def Score(Motifs):
	score = 0
	k = len(Motifs[0])
	t = len(Motifs)
	for j in range(k):
		for i in range(t):
			if Motifs[i][j] != Consensus(Motifs)[j]:
				score += 1
	return score
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
def GreedyMotifSearch(Dna, k, t):
	BestMotifs = []
	for i in range(0, t):
		BestMotifs.append(Dna[i][0:k])
	n = len(Dna[0])
	for i in range(n-k+1):
		Motifs = []
		Motifs.append(Dna[0][i:i+k])
		for j in range(1, t):
			P = Profile(Motifs[0:j])
			Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
		if Score(Motifs) < Score(BestMotifs):
			BestMotifs = Motifs
	return BestMotifs
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
	return GreedyMotifSearch(Dna, k, t)


from part_5_Biology_Meets_Programming import RandomMotifs, Motifs


### 
def RandomizedMotifSearch(Dna, k, t):
	N = 0
	M = RandomMotifs(Dna, k, t)
	BestMotifs = M
	while True:
		Profile = ProfileWithPseudocounts(M)
		M = Motifs(Profile, Dna, k)
		if Score(M) < Score(BestMotifs):
			BestMotifs = M
			N+= 1
		else:
			N+=1
			print(BestMotifs)
			return N

Dna123 = ['ATGAGGTC',
'GCCCTAGA',
'AAATAGAT',
'TTGTGCTA']

print(str("HIIII: ") + str(RandomizedMotifSearch(Dna123, 3, 4)))

dna = [
'TTACCTTAAC',
'GATGTCTGTC',
'ACGGCGTTAG',
'CCCTAACGAG',
'CGTCAGAGGT']

dna22= ['GGCGTTCAGGCA',
'AAGAATCAGTCA',
'CAAGGAGTTCGC',
'CACGTCAATCAC',
'CAATAATATTCG']


print(str('Greedy Motif Search with Pseudocounts: ') + str(GreedyMotifSearchWithPseudocounts(dna, 4, 5)))






Dna11=["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

print(str('Randomized Motif Search: ') + str(RandomizedMotifSearch(Dna11, 8, 5)))
print(str('2nd Randomized Motif Search: ') + str(RandomizedMotifSearch(dna22, 3, 5)))




Dna1 =["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC", "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG", "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC", "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC", "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG", "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA", "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA", "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG", "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG", "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]
print('bye')
k = 15
t = 10
print(GreedyMotifSearchWithPseudocounts(Dna1, 15, 10))
43
print('hi')



import random


def RandomMotifs_Quizz(Dna, k, t):
    # place your code here.
    randomMotifs = []
 
    randomMotifs.append("GTG")
    randomMotifs.append("CCC")
    randomMotifs.append("ATA")
    randomMotifs.append("GCT")
 
    return randomMotifs
 
 
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch_Quizz(Dna, k, t):
    # insert your code here
 
    M = RandomMotifs_Quizz(Dna, k, t)
    BestMotifs = M
 
    Profile = ProfileWithPseudocounts(M)
    M = Motifs(Profile, Dna, k)
    print (M)
 
    print (Score(M))
    print (Score(BestMotifs))
 
    return
 
 
import sys
 
# 3. Assume we are given the following strings Dna:
DNA1 = "ATGAGGTC"
DNA2 = "GCCCTAGA"
DNA3 = "AAATAGAT"
DNA4 = "TTGTGCTA"
 
Dna = [ DNA1, DNA2, DNA3, DNA4 ]
 
 
# Then, assume that RandomizedMotifSearch begins by randomly choosing the following 3-mers Motifs of Dna:
"""
CCA
CCT
CTT
TTG
"""
 
# What are the 3-mers after one iteration of RandomizedMotifSearch? 
# In other words, what are the 3-mers Motifs(Profile(Motifs), Dna)? 
# Please enter your answer as four space-separated strings.
 
 
# set t equal to the number of strings in Dna and k equal to 3
k = 3
t = 4
print(str("BYEEE") + str(RandomizedMotifSearch_Quizz(Dna, k, t)))

