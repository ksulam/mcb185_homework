import gzip
lengths = []

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': 
			words = line.split()
		if words[2] == 'CDS': 
			beg = int(words[3])
			end = int(words[4])
			lengths.append(end - begin + 1)