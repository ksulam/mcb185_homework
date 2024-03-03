import sys
import gzip
import mcb185
import dogma
seq = sys.argv[1]
mini = int(sys.argv[2])
w = 3


def translation(seq, f):
	aminoacids = []
	
	for i in range(f, len(seq), 3):
		aminoacids.append(dogma.translate(seq[i:i+3]))
		
	return ''.join(aminoacids)


# picking proteins that begin with M and are >= 100 length		
def profinder(seq, mini):
	proteins = []
	aalist = seq.split('*') #split amino acids, removing last one
	aalist.pop()
	for aas in aalist: 
		start = aas.find('M')
		if aas and len(aas[start:]) >= mini and start >= 0: #length from M is >= 100
			proteins.append(aas[start:])
			
	return proteins 


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	translatedstrands = []
	
	for s in range(0, 3):
		translatedstrands.append(translation(seq, s))
		translatedstrands.append(translation(dogma.revcomp(seq), s))
	
	#selecting proteins from each strand
	finalproteins = []
	for strand in translatedstrands:
		finalproteins.append(profinder(strand, mini)) 

	
	proteincount = 0	
	for protein in finalproteins:
		for singleprotein in protein: 
			print(f'>{defline[0:11]}-prot-{proteincount}')
			print(singleprotein)
			proteincount +=1
		
		
		

	
