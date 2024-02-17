import gzip
import sys
import math
#  ~/Code/MCB185/data/A.thaliana.gff.gz 
# Chr1	TAIR10	gene	3631	5899	.	+	.	ID=AT1G01010;Note=protein_coding_gene;Name=AT1G01010
gffpath = sys.argv[1]
feature = sys.argv[2]
#fp = gzip.open("A.thaliana.gff.gz", "rt")

featurecount = 0
lengths = []

with gzip.open(gffpath, 'rt') as fp:
    for line in fp:
    	words = line.split()
    	#print(line)
    	if words[2] == feature: 
    		featurecount += 1 #count
    		beg = int(words[3])
    		end = int(words[4])
    		lengths.append(end - beg + 1)  

# count 
print("Count:", featurecount)

# min, max
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
mini, maxi = minmax(lengths)  
print("Minimum:", mini)	
print("Maximum:", maxi)
	   
   
# mean   
sumlengths = 0
for val in lengths: 
	sumlengths += val		  	
mean = sumlengths / len(lengths)

print("Mean:", mean)		

# standard deviation  sqrt(sum of (x- mean)^2 / (n))
sumofsquareddiff = 0
for val in lengths:
	sumofsquareddiff += (val - mean) ** 2

stdev = math.sqrt(sumofsquareddiff / len(lengths)) 

print("Standard Deviation:", stdev)
	
	

# median 
for val in lengths:
	lengths.sort()
	if len(lengths) % 2 == 0: # if length is even, take average of 2 middle numbers
		x1 = lengths[len(lengths) // 2 -1]
		x2 = lengths[len(lengths) // 2]
		med = (x1 + x2) / 2
	else: 
		med = lengths[len(lengths) // 2]

print("Median:", med)

# sum 
print("Sum:", sumlengths)
#gunzip -c A.thaliana.gff.gz 
