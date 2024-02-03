
nts = 'ACGT'

print(" ", end='') # print first space in 1st row

for nt in nts: 
	print(" ", nt, end='') # print 1st row

print() 
	
for nt1 in nts:
	print(nt1, end='') # print nt in column
	
	for nt2 in nts:
		if nt1 == nt2: print(" +1", end='')
		else: print(" -1", end='')
	print() 