
"""Ch 1.2 and 1.3: Hidden Messages in the Replication Origin"""

ori = 'ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC'



"""
count = 0
for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1 
"""

m = 'CGATATATCCATAG'
pattern = 'ATA'

count = 0
for i in range(len(m)-len(pattern)+1):
        if m[i:i+len(pattern)] == pattern:
            count = count+1 

print(count)

#Putting it all together:
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

print(PatternCount('GCGCG', 'GCG'))
print(PatternCount(ori, 'TGATCA'))

""""""

sequence = "GATCCAGATCCCCATAC"
twoMers = {}
i = 0
for i in range(len(sequence)-2+1) :

    current = sequence[i: i+2]
    print(current)
    if current in twoMers:
        count = twoMers.get(current)
        twoMers[current] = count + 1
    else:
        twoMers[current] = 1
        
print(twoMers)

""""""

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    print('Text=', Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        print('i=', i, 'Pattern=', Pattern)
        freq[Pattern] = 0
    return freq
FrequencyMap('ATCGATCG', 2)
""""""
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

print("frequency map:")
print(FrequencyMap('CGATATATCCATAG', 3))

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words

print('FrequentWords: ')
print(FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))

#1.4 Some Hidden Messages are More Surprising than Others

def Reverse(Pattern):
	return Pattern[::-1]

print(Reverse('ATCGATCG'))

def Complement(Pattern):
	basepairs = {"A": "T", "G":"C", "T":"A", "C":"G"}
	complementary = ""
	for base in Pattern:
		complementary += basepairs.get(base)
	return complementary
print(Complement('ATCGATCG'))

def ReverseComplement(Pattern):
	reversed = Reverse(Pattern)
	rev_complemented = Complement(reversed)
	return rev_complemented

print(ReverseComplement('ATCGATCG'))

print(Reverse('ATGATCAAG'))
print(Complement('ATGATCAAG'))
print(ReverseComplement('ATGATCAAG'))

"""

	
def PatternMatching(Genome, Pattern):
	position = ''
	current_pos = 0
	for i in range(len(Genome) - len(Pattern) + 1):
		if Pattern == Genome[i: i+len(Pattern)]:
			position += str(current_pos) + " "
		current_pos = i + 1
	return position

"""
def PatternMatching(Pattern, Genome):
    position = []
    pos = 0
    for i in range(len(Genome) - len(Pattern) + 1):
        if Pattern == Genome[i: i+len(Pattern)]:
            position.append(pos)
        pos = i + 1
    return position



print(PatternMatching('AAA', 'AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT'))
print(PatternCount("GACCATCAAAACTGATAAACTACTTAAAAATCAGT", "AAA"))

print(True or not False and False)
print(FrequentWords('TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT', 3))
print(ReverseComplement('CCAGATC'))

