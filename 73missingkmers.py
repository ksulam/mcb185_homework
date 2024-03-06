import sys
import mcb185
import dogma
import itertools

sequence = sys.argv[1]

# finding all kmers in seq and revcomp seq with length 'k'
k = 0
zero = False
while zero == False:
	
	#kmerfill = False
	#while kmerfill == False:
	kcount = {}
	
	for defline, seq in mcb185.read_fasta(sequence):
		for strand in [seq, dogma.revcomp(seq)]: 
			for i in range(len(strand) -k +1):
				kmer = strand[i:i+k]
				if kmer not in kcount: kcount[kmer] = 1
				else: 
					kcount[kmer] += 1	
		
		#making all possible kmers, size=k
		possiblekmers = []
		for nts in itertools.product('ATCG', repeat=k):
			kmer = ''.join(nts)
			possiblekmers.append(kmer)
		#print(possiblekmers)
			
		missingkmers = []	
		zerocount = 0 #how many kmers missing
		for kmer in possiblekmers:
			if kmer not in kcount: 
				#print(kmer)
				missingkmers.append(kmer)
				#print("k=",k, kmer)
				zerocount += 1
				zero = True

	if zero:
		print(f'{len(missingkmers)} missing kmers when k={k}')
		for kmer in missingkmers:
			print(kmer)
	k += 1	
		
		

	
"""	
		print(missingkmers)
		if zerocount >= 1:
			print('k=',k, )
		kmerfill = False
			
"""