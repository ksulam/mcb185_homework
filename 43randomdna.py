import random 


for i in range(4):
	i += 1
	print(f'\n>seq-{i}')
	nt = random.randint(30, 60)

	for j in range(nt):
		print(random.choice('ACGT'), end='')

