"""
matrix = [
	[1, 2, 3],
	[4, 5, 6], 
	[7, 8 ,9],

]

print(matrix)
print(matrix[2][0]) #first is row #, second is column #

import json 

person = {
	'name': 'Katelyn',
	'age': 22,
	'pets': ['Kobe', 'Mochi', 'Milo'],
	'family': {'Allie': 'sister',
				'Malia': 'cousin',
		}
	}
	
print(person)


people = []
people.append(person)
print(people[0]['family']['Allie'])

people[0]['made this up'] = 'hello' #adding new thing to json 

people[0]['pets'].append('Beyonce') #adding Beyonce to pets
print(json.dumps(person, indent=4)) 
"""
"""

import json 
import sys
import mcb185

k = int(sys.argv[2])

kloc = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	chrom = words[0]
	
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k] #making kmers 
		if kmer not in kloc: kloc[kmer] = {}
		#kloc[kmer].append((chrom, i)) #appending chromosome and seq position 
		if chrom not in kloc[kmer]: kloc[kmer][chrom] = [] #organizes by kmer then chrom 
		kloc[kmer][chrom].append(i)
		
print(json.dumps(kloc, indent = 4))
			
"""
import gzip
import mcb185
import json
import sys 
#getting introns from A.thalianaGFF file 
def print_pwm(pwm, ma, iden, de):
	print('MATRIX', ma)
	print('XX')		
	print('ID', iden)	
	print('XX')	
	print('DE', de)
	print('PO')
	for i, n in enumerate(accs):
		a = n['A']
		c = n['C']
		g = n['G']
		t = n['T']
		print(f'{i+1:<8}{a:<8}{g:<8}{t:<8}]')

introns = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		print(f[2])
		if f[2] != 'intron': continue #skipping over anything not intron
		print(line)
		chrom = f[0]
		beg = int(f[3]) -1 
		end = int(f[3]) -1
		strand = f[6]
		score = int(f[5])
		introns.append((chrom, beg, end, strand, n))
		#if chrom not in introns: 
			#introns[chrom] = []
			#introns[chrom].append({
			#	'beg': beg,
			#	'end': end. 
			#	'strand': strand. 
			#	'count': n})
dons = []	
accs = []
dlen = 6
alen = 8
for i in range(dlen):
	dons.append({'A':0, 'C':0, 'G':0, 'T':0})		
for i in range(aclen):
	accs.append({'A':0, 'C':0, 'G':0, 'T':0})		
rules = ['GTAG', 'GCAG', 'ATAC']	
for defline, seq in mcb185.read_fasta(sys.argv[2]):
	for c, b, e, s, n in introns:
		if chrom == c:
			iseq = seq[b:e+1] 
			if not iseq.startswith('GT'):
				print(iseq)
			if s == '-': iseq = mcb185.anti_seq(iseq)
			don = iseq[:6]
			accs = iseq[-8:]
			for i, nt in enumerate(dons):
				dons[i][nt] += 1 
			for i, nt in enumerate(accs):
				accs[i][nt] += 1 


print(dons, 'mad' 'kl01', 'hello')				
#print(json.dumps(dons, indent=4))#prints as tuple but can append dict 
