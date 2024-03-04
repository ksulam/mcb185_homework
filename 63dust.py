import sys
import gzip
import mcb185
import math 
w = int(sys.argv[2])
threshold = float(sys.argv[3])
seq = sys.argv[1]

# function calculating entropy
def shannon(a, t, c, g):
	total = a + t + c + g
	aprob = a / total
	tprob = t / total
	cprob = c / total
	gprob = g / total
	
	if aprob > 0: aexp = aprob * math.log2(aprob)
	else: aexp = 0 
		
	if tprob > 0: texp = tprob * math.log2(tprob)
	else: texp = 0
	
	if cprob > 0: cexp = cprob * math.log2(cprob)
	else: cexp = 0
	
	if gprob > 0: gexp = gprob * math.log2(gprob)
	else: gexp = 0
	
	entropy = -(aexp + texp + cexp + gexp)
	return entropy

def masking(seq):
	#print(len(seq))
	maskedseq = list(seq) #making list copy of sequence
	
	for i in range(0, len(seq) - w + 1, 1):	#stepping by 1 base	
		window = seq[i:i+w] 
		#print(window)
		a = window.count('A')
		t = window.count('T')
		c = window.count('C')
		g = window.count('G')
		entropy = shannon(a, t, c, g) 
			
		if entropy < threshold: # if window entropy < threshold
			for base in range(i, i + len(window)): #replace bases in window with N
				maskedseq[base] = 'N'
	
	return ''.join(maskedseq) #joining list to string

	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	#print(masking(seq))

	# printing defline and wrapped sequence
	print(f'>{defline}')
	finalseq = masking(seq)
	lines = []
	
	for i in range (0, len(finalseq), 60):
		lines.append(finalseq[i:i+60])
	for line in lines:
		print(line)



#double checking if lengths of OG seq and final is the same
#print(len(seq))
#print(len(finalseq))


