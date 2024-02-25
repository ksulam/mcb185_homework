import dogma
import sys
import gzip
import mcb185

seq = sys.argv[1]
w = int(sys.argv[2])
s = 1

#set initial window position to 1st 1000 nts
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	window = seq[:w+1]
	#print(window)

	ccount = window.count('C')
	gcount = window.count('G')

	gc_comp = (ccount + gcount) / w
	gc_skew = (gcount - ccount) / (gcount + ccount)
	i=0
	print(f'{i}\t{gc_comp:.3f}\t{gc_skew:.3f}')
	
	for i in range(1, len(seq) - w + 1, s): # move window 1 nt at a time
		leftnt = seq[i - 1] 
		rightnt = seq[i + w - 1]

		if leftnt == 'C': 
			ccount -= 1
		if leftnt == 'G':
			gcount -= 1
		if rightnt == 'C':
			ccount += 1
		if rightnt == 'G':
			gcount += 1
		 
		gc_comp = (ccount + gcount) / w
		gc_skew = (gcount - ccount) / (gcount + ccount)
		print(f'{i}\t{gc_comp:.3f}\t{gc_skew:.3f}')
		
