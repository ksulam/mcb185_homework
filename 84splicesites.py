import mcb185
import json
import gzip
import sys
import re

fasta = sys.argv[1] #C.elegans.fa.gz
gff = sys.argv[2] #C.elegans.gff.gz
#need seq file and _ file
#read all seq


def print_pwm(pwm, ac, id, desc):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('DE', desc)
	#print('PO   A   C   G   T')
	nts = 'ACGT'
	print('PO', end='\t')
	for nt in nts: 
		print(" ", nt, end='') 
	print()
	
	for i, dictionary in enumerate(pwm):
		print(i+1, end='\t')
		for nt, n in dictionary.items():
			print(int(n), end=' ')
		print()	
	print('XX')	
	print('//')
	
	
chrom = {}
for defline, seq in mcb185.read_fasta(fasta):
	#print(defline, len(seq)) 
	#save in dict
	chromID = defline.split()[0]
	chrom[chromID] = seq

#read all introns(features)
introns = []
with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.split('\t') #split on tabs
		c = f[0] #chromosome
		t = f[2] #type (intron or not)
		b = int(f[3]) -1 #begin integer
		e = int(f[4]) -1 #end integer
		n = f[5] #count
		s = f[6]  #strand
		if t != 'intron': continue
		if n == '.': continue
		n = float(n)
		introns.append((c, b, e, n, s)) #store as tuple


don = []  #donor seq
for i in range(6):
	don.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

acc = []  #acceptor seq
for i in range(7):
	acc.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})


for c, b, e, n, s in introns:
	if s == "+":
		intronseq = chrom[c][b:e+1] #begin - end seq from specific chr
	else:
		intronseq = mcb185.anti_seq(chrom[c][b:e+1]) #rev comp
	#print(intronseq[0:6], intronseq[-8:], s, n)
	
	dseq = intronseq[0:6]
	for i, nt in enumerate(dseq):
		#print(i, nt)
		don[i][nt] += 1 #adding to count 
	
	aseq = intronseq[-7:]
	for i, nt in enumerate(aseq):
		acc[i][nt] += 1
	
		
print_pwm(acc, 'ik001', 'ACC1', 'splice acceptor')
print_pwm(don, 'ik002', 'DON', 'splice acceptor')


