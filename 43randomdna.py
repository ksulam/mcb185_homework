import random 
i = 0

def dna(sequence):
	for i in range(sequence):
		i += 1
		print(f'\n>seq-{i}')
		nt = random.randint(30, 60)

		for j in range(nt):
			print(random.choice('ACGT'), end='')

dna(4)
