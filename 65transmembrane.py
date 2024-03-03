import sys
import gzip
import mcb185
import dogma

seq = sys.argv[1]


def avgkdhydro(seq):
	KD = 0
	for i in seq:
		if i == 'A': KD += 1.8
		elif i == 'C' or i == 'U': KD += 2.5
		elif i == 'D' or i == 'E' or i == 'N' or i == 'Q': KD += -3.5
		elif i == 'F': KD += 2.8
		elif i == 'G': KD += -0.4
		elif i == 'H': KD += -3.2
		elif i == 'I': KD += 4.5
		elif i == 'K': KD += -3.9
		elif i == 'L': KD += 3.8
		elif i == 'M': KD += 1.9
		elif i == 'P': KD += -1.6
		elif i == 'R': KD += -4.5
		elif i == 'S': KD += -0.8
		elif i == 'T': KD += -0.7
		elif i == 'V': KD += 4.2
		elif i == 'W': KD += -0.9
		elif i == 'Y': KD += -1.3
	return KD / len(seq)


# make sure first 30 AA has 8AA sequence with KD>=2.5
def signalpep(seq, wlen):
	for i in range(len(seq) - wlen +1):
		window = seq[i:i+wlen]
		if wlen == 8 and avgkdhydro(window) >= 2.5 and window.find('P') == -1:
			return True	
		if wlen == 11 and avgkdhydro(window) >= 2 and window.find('P') == -1:
			return True

	return False

proteincount = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if signalpep(seq[:30], 8) and signalpep(seq[30:], 11):
		print(defline)
		proteincount += 1
		
print("Protein count:", proteincount)

# how to select proteins that do not contain P in signalpep and transmem area
# how to avoid appending proteins already in the list





