import sys
import gzip
import mcb185
import math 

w = int(sys.argv[2])
threshold = float(sys.argv[3])
seq = sys.argv[1]
def shannon(a, t, c, g):
	total = a + t + c + g

	aprob = a / len(window)
	tprob = t / len(window)
	cprob = c / len(window) 
	gprob = g / len(window) 	
	
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


window = seq[:w]
def masking(seq):
	maskedseq = []

	for i in range(0, len(seq) - w + 1, w):
		window = seq[i:i+w]
		#print(window)
		a = window.count('A')
		t = window.count('T')
		c = window.count('C')
		g = window.count('G')
		
		entropy = shannon(a,t,c,g)
			
		if  entropy < threshold:
			maskedseq.append('N'*len(window))
		else:
			maskedseq.append(window)
	return ''.join(maskedseq)


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(">",defline)
	masked = masking(seq)
	wrap_len = 60
	lines = []
	for i in range(0, len(masked), wrap_len):
		lines.append(masked[i:i+wrap_len])

	#print out the wrapped lines
	for line in lines:
		print(line)