import mcb185
import gzip
import sys
file = sys.argv[1]

coord = []
data = []

with gzip.open(file, 'rt') as fp:

	for line in fp:
		line = line.rstrip()
		
		if 'join' in line: continue #ignore regions with join
		if 'complement(join' in line: continue
		
		if 'CDS' in line and '..' in line:
			#complement
			b = line.find('(')
			e = line.find(')')
			if 'complement' in line: #for "-" strand 
				comps = line[b+1:e]
				start, end = comps.split("..")
				coord.append([int(start), int(end), 'rev'])
				#print(coord)
			
			else:
				#positive strand
				words = line.split()
				start, end = words[1].split('..')
				coord.append([int(start), int(end), 'fwd'])#appending index and strand
				#print(coord)	
		
		if 'ORIGIN' in line:
			for line in fp:
				nts = line.split()	
				for nt in nts[1:]: #skipping numbers at beginning of line
					data.append(nt)
		seq = ''.join(data) #creating genome sequence		

revcomp = mcb185.anti_seq(seq)


#kozak count
kozakcount = [] 
for i in range(0, 14):
	kozakcount.append({'a': 0, 'c': 0, 'g': 0, 't': 0})
	
for start, end, strand in coord:
	if "fwd" in strand:
		kfwd = seq[start-9:start+5] 

		for i, nt in enumerate(kfwd):
			kozakcount[i][nt] += 1 #adding to count 
	
	elif "rev" in strand:
		krev = revcomp[end-6:end+8]
		for i, nt in enumerate(krev):
			kozakcount[i][nt] += 1 #adding to count


#printing in transfac format 
print('AC', 'E.coli')
print('XX')
print('ID', 'E.Coli Kozak')
print('XX')
print('DE', 'unit 9: 83kozak.py')
print(f'{"PO":<8} {"a":<8} {"c":<8} {"g":<8} {"t":<8}')

for i in range(len(kozakcount)):
	print(f'{i+1:<8} {kozakcount[i]["a"]:<8}', end='')
	print(f'{kozakcount[i]["c"]:<8}', end='')
	print(f'{kozakcount[i]["g"]:<8}', end='')
	print(f'{kozakcount[i]["t"]:<8}')
print('XX')
