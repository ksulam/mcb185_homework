import sys
import gzip
import mcb185
import dogma

proteinlen = int(sys.argv[2])
seq = sys.argv[1]
w = 6


def translation(seq):
	translatedseq = []
	
	for i in range(0, len(seq) - w + 1, w):
		window = seq[i:i+w]
		translatedseq.append(dogma.translate(seq))
	
	return ''.join(translatedseq)
	
	
	

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(">",defline)
	aaseq = translation(seq)
	print(aaseq)
	
	
"""	
def findingprotein(protein_seq)	
	start = 'M'
	stop = '*'
	genes = []
	
	for frame in protein_seq:
		genestart = frame.find(start)
		geneend = frame.find(end)
		
	return genes
		
"""
	