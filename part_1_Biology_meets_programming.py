#In the end, put what you learned in personal projects Curriculum Vitae and Linked in
#Descriptions of all functions: 
#-Write them down:

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



"""Notes:

Ch. 1 Where in the Genome does replication begin?

Replication begins in a genomic region called the replication origin (denoted ori) and 
is performed by molecular copy machines called DNA polymerases. 
Locating ori presents an important task not only for understanding how cells replicate 
but also for various biomedical problems. For example, some gene therapy methods use 
genetically engineered mini-genomes, which are called viral vectors because they are 
able to penetrate cell walls (just like real viruses). 

The idea of gene therapy is to intentionally infect a patient who lacks a crucial gene
with a viral vector containing an artificial gene that encodes a therapeutic protein.
Once inside the cell, the vector replicates and eventually produces many molecules of 
the therapeutic protein, which in turn treats the patient’s disease. To ensure that the 
vector actually replicates inside the cell, biologists must know where ori is in the
vector’s genome and ensure that the genetic manipulations that they perform do not affect it.

ori has only been experimentally located in a handful of species. 

Research has shown that the region of the bacterial genome encoding ori is typically
a few hundred nucleotides long. Our plan is to begin with a bacterium in which ori is
known, and then determine what makes this genomic region special in order to design 
a computational approach for finding ori in other bacteria.

The initiation of replication is mediated by DnaA, a protein that binds to a short 
segment within the ori known as a DnaA box. You can think of the DnaA box as a message 
within the DNA sequence telling DnaA: “bind here!” 

 We have added reason to look for frequent words in the ori because for various biological 
processes, certain nucleotide strings appear surprisingly often in small regions of the genome. 
This is often because certain proteins can only bind to DNA if a specific string of nucleotides 
is present, and if there are more occurrences of the string, then it is more likely that binding 
will successfully occur. (It is also less likely that a mutation will disrupt the binding process.)

The final k-mer of a string of length n begins at position n-k; for example, the final 3-mer 
of "GACCATACTG", which has length 10, begins at position 10 - 3 = 7. This observation implies 
that the window should slide between position 0 and position len(Text)-len(Pattern).

To find the most frequent k-mers in a string Text, we would like to create a mapping like the example 
below for Text = "CGATATATCCATAG" and k = 3, where we map each k-mer appearing in  Text to its number 
of occurrences in  Text.  We call this structure a frequency map

"ATGATCAAG" and its reverse complement "CTTGATCAT" indeed represent DnaA boxes in Vibrio cholerae. 
Our computational conclusion makes sense biologically because the DnaA protein that binds to DnaA 
boxes and initiates replication does not care which of the two strands it binds to.

Different bacteria may use different DnaA boxes as “hidden messages” to the DnaA protein.

We think of a k-mer as a “clump” if it appears many times within a short interval of the genome. 
More formally, given integers Land t, a k-mer Pattern forms an (L, t)-clump inside a (longer) 
string Genome if there is an interval of Genome of length L in which this k-mer appears at least
 t times. (This definition assumes that the k-mer completely fits within the interval.) 
For example, "TGCA" forms a (25, 3)-clump in the following Genome:
gatcagcataagggtccCTGCAATGCATGACAAGCCTGCAGTtgttttac

The semiconservative hypothesis suggested that each parent strand acts as a template for the 
synthesis of a daughter strand. As a result, each of the two daughter molecules contains one parent 
strand and one newly synthesized strand. The conservative hypothesis proposed that the entire 
double-stranded parent DNA molecule serves as a template for the synthesis of a new daughter molecule,
resulting in one molecule with two parent strands and another with two newly synthesized strands. 
The dispersive hypothesis proposed that some mechanism breaks the DNA backbone into pieces and 
splices intervals of synthesized DNA, so that each of the daughter molecules is a patchwork of
old and new double-stranded DNA.

Meselson and Stahl's insight relied on the fact that one isotope of nitrogen, Nitrogen-14 (14N), 
is lighter and more abundant than Nitrogen-15 (15N). Knowing that the DNA molecular structure
naturally contains 14N , Meselson and Stahl grew E. coli for many rounds of replication in a 
15N medium, which caused the bacteria to gain weight as they absorbed the heavier isotope into 
their DNA.
When they were confident that the bacterial DNA was saturated with 15N, they transferred these heavy 
E. coli cells to a less dense 14N medium.

The brilliance of the Meselson-Stahl experiment is that all newly synthesized DNA would contain 
exclusively 14N, and the three existing hypotheses for DNA replication predicted different outcomes 
for how this 14N isotope would be incorporated into DNA. Specifically, after one round of replication, 
the conservative model predicted that half the E. coli DNA would still have only 15N and therefore be 
heavier, whereas the other half would have only 14N and be lighter. Yet when they attempted to separate 
the E. coli DNA according to weight by using a centrifuge after one round of replication, all of the 
DNA had the same density! Just like that, they had refuted the conservative hypothesis once and for all.

Unfortunately, this experiment was not able to eliminate either of the other two models, 
as you can see that both the dispersive and semiconservative hypotheses predicted that all of 
the DNA after one round of replication would have the same density.

Let’s first consider the dispersive model, which says that each daughter strand of DNA is 
formed by half mashed up pieces of the parent strand, and half new DNA. If this hypothesis were 
true, then after two replication cycles, any daughter strand of DNA should contain about 25% 
15N and about 75% 14N. In other words, all the DNA should still have the same density. 
And yet when Meselson and Stahl spun the centrifuge after two rounds of E. coli replication, 
this is not what they observed!
Instead, they found that the DNA divided into two different densities. This is exactly 
what the semiconservative model predicted: after one cycle, every cell should possess
one 14N strand and one 15N strand; after two cycles, half of the DNA molecules should 
have one 14N strand and one 15N strand, while the other half should have two 14N strands, 
producing the two different densities they noticed.
"""
