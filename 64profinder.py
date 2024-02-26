import sys
import gzip
import mcb185
import dogma

seq = sys.argv[1]
mini = int(sys.argv[2])
w = 3



def rollingtranslation(seq):
	aminoacids = []
	for s in range(3):
		for i in range(s, len(seq), 3):
			aminoacids.append(dogma.translate(seq[i:i+3]))
		
	return ''.join(aminoacids)

# picking proteins that begin with M and are >= 100 length		
def profinder(seq, mini):
	proteins = []
	aalist = seq.split('*') #split amino acids, removing last one
	aalist.pop()
	for aas in aalist:#splitting proteins based on stop codon 
		start = aas.find('M')
		if aas and len(aas[start:]) >= mini and start >= 0: #length from M is >= 100
			proteins.append(aas[start:])
			
	return proteins 



for defline, seq in mcb185.read_fasta(sys.argv[1]):
	translatedstrand1 = rollingtranslation(seq) 
	translatedstrand2 = rollingtranslation(dogma.revcomp(seq)) 
	
	#selecting proteins from each strand
	finalproteins1 = profinder(translatedstrand1, mini) 
	finalproteins2 = profinder(translatedstrand2, mini)

	#combining proteins from each strand to one
	for protein in finalproteins2:	
		finalproteins1.append(protein)
	

	proteincount = 0	
	for protein in finalproteins1:
		print(f'>{defline[0:11]}-prot-{proteincount}')
		print(protein)
		#print(len(protein))
		proteincount +=1
	
	
	

	
