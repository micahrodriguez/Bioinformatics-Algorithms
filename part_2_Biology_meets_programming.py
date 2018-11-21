from part_1_Biology_meets_programming import PatternCount
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array

print(SymbolArray('AAAAGGGG', 'A'))

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(Genome[0:n//2], symbol)

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array
print(FasterSymbolArray('AAAAGGGG', 'A'))

def SkewArrayList(Genome):
	skew = [0]
	dict = {'C': -1, 'G': 1, 'A':0, 'T': 0}
	for i in range(len(Genome)):
		skew.append(dict[Genome[i]] + skew[i])
	return skew
print(SkewArrayList('CATGGGCATCGGCCATACGCC'))

def SkewArrayDictionary(Genome):
    skew = {} 
    skew[0] = 0
    for i in range (len(Genome)):
        if Genome[i] == "A" or Genome[i] == "T":
            skew[i + 1] = skew [i]
        elif Genome[i] == "G":
            skew[i + 1] = skew[i] + 1
        else:
            skew[i + 1] = skew[i] - 1
    return skew
print(SkewArrayDictionary('CATGGGCATCGGCCATACGCC'))

def MinimumSkew(Genome):
	positions = []
	x = SkewArrayDictionary(Genome)
	minimum = min(x.values())
	for i in x:
		if x[i] == minimum:
			positions.append(i)
	return positions
print(MinimumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'))

def MaximumSkew(Genome):
	positions = []
	x = SkewArrayDictionary(Genome)
	maximum = max(x.values())
	for i in x:
		if x[i] == maximum:
			positions.append(i)
	return positions
print(str("Max Skew:") + str(MaximumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')))



def HammingDistance(Genome1, Genome2):
	mismatches = 0
	for i in range(len(Genome1)):
		if Genome1[i] != Genome2[i]:
			mismatches += 1
	return mismatches

print('Hamming Distance:  ')
print(HammingDistance('GGGCCGTTGGT', 'GGACCGTTGAC'))

def ApproximatePatternMatching(Text, Pattern, d):
	positions = []
	for i in range(len(Text) - len(Pattern)+1):
		if HammingDistance(Pattern, Text[i: i+ len(Pattern)]) <= d:
			positions.append(i)
	return positions
print(ApproximatePatternMatching('CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT', 'ATTCTGGA', 3))

def ApproximatePatternCount(Text, Pattern, d):
	count = 0
	for i in range(len(Text)-len(Pattern)+1):
		if Text[i:i+len(Pattern)] == Pattern:
			count+= 1
		elif HammingDistance(Pattern, Text[i: i+ len(Pattern)]) <= d:
			count += 1
	return count


print(ApproximatePatternCount('AACAAGCATAAACATTAAAGAG', 'AAAAA', 1))
print(8.7//4)

print(MaximumSkew('GATACACTTCCCGAGTAGGTACTG'))

x=0
for y in range(0, 5):
	x+= y
print(x)

print(HammingDistance("TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC", "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"))

a = list(range(5))
b=a
a[2] = 12
print(b)



