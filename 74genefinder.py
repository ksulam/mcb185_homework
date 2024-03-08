# focus on 3 diff frames 
import mcb185
import sys
import dogma 

mainseq = sys.argv[1]
minlength = int(sys.argv[2])

def genefinder(s, minl):
	geneloc = []

	for frame in range(3):
		frameseq = s[frame:]
		i = frame

		while i < len(frameseq):	
			startcodon = frameseq[i:i+3]
			
			if startcodon == 'ATG':
				start = i #first letter of start codon	
				
				for j in range(i, len(frameseq) -2, 3):
					stopcodon = frameseq[j:j+3]
					
					if stopcodon == 'TAA' or stopcodon == 'TAG' or stopcodon == 'TGA':
						stop = j 
					
						if stop - start >= minl:
							geneloc.append((start, stop))		
						
						i = stop
						break
			i += 3 
	return geneloc


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)	
	revseq = dogma.revcomp(seq)
	#printing for forward strand
	geneloc_forward = genefinder(seq, minlength)
	for nt in geneloc_forward:
		print("+", nt[0], nt[1], "-")

	#printing for revcomp strand
	geneloc_rev = genefinder(revseq, minlength)
	for nt in geneloc_rev:
		print("-", nt[0], nt[1], "+")

"""
geneloc_forward = genefinder(mainseq, minlength)
for nt in geneloc_forward:
	print("+", nt[0], nt[1], "-")
#printing for revcomp strand
geneloc_rev = genefinder(revseq, minlength)
for nt in geneloc_rev:
	print("-", nt[0], nt[1], "+")

print(len(geneloc_forward))
"""

	