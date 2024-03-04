import sys
import gzip
import mcb185
import math 
w = int(sys.argv[2])
threshold = float(sys.argv[3])
seq = sys.argv[1]

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
	maskedseq = []
	maskcount = 0
	for i in range(0, len(seq) - w + 1, 1):
		
		if maskcount <= 0: # when no N's
			window = seq[i:i+w]
			#print(window)
			a = window.count('A')
			t = window.count('T')
			c = window.count('C')
			g = window.count('G')
			entropy = shannon(a, t, c, g)
			
			if entropy < threshold:
				maskedseq.append('N'*len(window))
				maskcount = w - 1 # must skip all newly added N's
			else:
				maskedseq.append(window[0])
		else:
			maskcount -= 1  # if N, keep skipping until no N
	maskedseq.append(seq[len(seq) - 3:len(seq)]) # adding last 3 since too short 
	return ''.join(maskedseq)



for defline, seq in mcb185.read_fasta(sys.argv[1]):
	#print(len(seq))	
	#print(len(masking(seq)))

	print(f'>{defline}')
	masked = masking(seq)
	lines = []
	for i in range(0, len(masked), 60):
		lines.append(masked[i:i+60])
	#print out the wrapped lines
	for line in lines:
		print(line)
