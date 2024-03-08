import random 
size = 100
words = []
for i in range(size):
	token = []
	for i in range(10):
		token.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
		words.append(token)
	
	
seq = sys.argv[1]	
for i in range(100000):
	if word in words:
		print(found)
		idx = words.index(word)
		
kcount = {}
k = 3
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)
	for in range(len(seq) -k +1)
		kmer = [i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
		
for kmer, n in kcount.


-- 
seq = ""
w = 5
def gc(s):
	g = ss.count('G')
	c = ss.count('C')
	return (g+c)/len(s)
for i in range(len(seq) -w +1):
	ss =seq[i:i+w]
	print(ss, gc(ss))


g = seq[0:w].count('G')
c = seq[0:w].count('c')

for i in range(len(seq) -w)
	off = seq[i]
	on = seq[i+w]
	
	if off == 'C': c-= 1
	elif off == 'G': g -= 1
	
	if on == 'C': c += 1
	elif off == 'G': g+= 1
	comp = (c+g) / w
	if (g+c) > 0: skew = (g-c)/(g+c)
	else: skew = 0