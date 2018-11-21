#Motifs.py

"""
t = the vertical dimension of motifs (i.e. the number of rows in motifs)
k = horizontal dimension of motifs (i.e., the number of characters in each row of Motifs)
i refers to row numbers and j refers to column numbers

For a given choice of Motifs, we can construct a 4 x k count matrix, denoted Count(Motifs), 
counting the number of occurrences of each nucleotide in each column of the motif matrix; 
element (i,j) of Count(Motifs) stores the number of times that nucleotide i appears in column j of Motifs.


"""

#Go to onlinepythontutor for visualization
def Count(Motifs):
	count = {}
	k = len(Motifs[0])  #k = horizontal dimensions
	for symbol in "ACGT":
		count[symbol] = []
		for j in range(k): #j = column numbers
			count[symbol].append(0)
	t = len(Motifs) #t = vertical dimensions
	for i in range(t): #i = row numbers
		for j in range(k):
			symbol = Motifs[i][j]
			count[symbol][j] += 1
	return count
print(str("Count: ") + str(Count(['AACGTA','CCCGTT', 'CACCTT', 'GGATTA','TTCCGG'])))

def Profile(Motifs):
	profile = {}
	k = len(Motifs[0])  #k = horizontal dimensions
	for symbol in "ACGT":
		profile[symbol] = []
		for j in range(k): #j = column numbers
			profile[symbol].append(0)
	t = len(Motifs) #t = vertical dimensions
	for i in range(t): #i = row numbers; t = vertical dimensions
		for j in range(k):
			symbol = Motifs[i][j]
			profile[symbol][j] += 1/t
	return profile

print(str("Profile: ") + str(Profile(['AACGTA','CCCGTT', 'CACCTT', 'GGATTA','TTCCGG'])))

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

print(str("Consensus: ") + str(Consensus(['AACGTA','CCCGTT', 'CACCTT', 'GGATTA','TTCCGG'])))

def Score(Motifs):
	score = 0
	k = len(Motifs[0])
	t = len(Motifs)
	for j in range(k):
		for i in range(t):
			if Motifs[i][j] != Consensus(Motifs)[j]:
				score += 1
	return score

print(str("Score: ") + str(Score(['AACGTA','CCCGTT', 'CACCTT', 'GGATTA','TTCCGG'])))



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


text1 = 'ACGGGGATTACC'
profile1 = {
    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
    }
text2 = 'TCGTGGATTTCC'
text3 = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
Profile3 = { 
  'A': [0.2, 0.2, 0.3, 0.2, 0.3],
  'C': [0.4, 0.3, 0.1, 0.5, 0.1],
  'G': [0.3, 0.3, 0.5, 0.2, 0.4],
  'T': [0.1, 0.2, 0.1, 0.1, 0.2]
}


print(str("Pr:") + str(Pr(text2, profile1)))
print(str("Most probable Kmer:") + str(ProfileMostProbableKmer(text3, 5, Profile3)))


# Read: http://www.mrgraeme.co.uk/greedy-motif-search/

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



Dna1 = [
"GGCGTTCAGGCA", 
"AAGAATCAGTCA", 
"CAAGGAGTTCGC",
"CACGTCAATCAC", 
"CAATAATATTCG"
]


print(str("Greedy Motif Search: ") + str(GreedyMotifSearch(Dna1, 3, 5)))

Dna4 = [
"GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC",
"CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG",
"ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC",
"GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC",
"GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG",
"CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA",
"GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA",
"GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG",
"GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG",
"TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"
]

# set t equal to the number of strings in Dna and k equal to 15

# Call GreedyMotifSearch(Dna, k, t) and store the output in a variable called Motifs
output = GreedyMotifSearch(Dna4, 15, 10)
                           
# Print the Motifs variable
print(output)
# Print Score(Motifs)
print(Score(output))

import math
def Entropy(motifs):
    entropy = 0
    for i in range(len(motifs)):
        for j in motifs[i]:
            if j == 0:
                entropy += 0
            else:
                entropy += j*(math.log(j,2))
    return entropy *-1


profile =[
[0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
[0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
[0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
]
print(Entropy(profile))

profile2 = {
    'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
    }

print(Pr('CAGTGA', profile2))
"""
Quiz ans:
Brute force Search
False
CCGAGGACCGAAAUCAAC and CCACGUACUGAAAUUAAC
AGGTGA,ACGCGA,ACGTTA , TCGCGA, AAGCTA REDOOO
0.0108	
codon
"""