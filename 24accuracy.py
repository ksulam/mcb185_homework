def performance(tp, tn, fp, fn):
	
	total = tp + tn + fp + fn
	assert(total > 0) 	# denominator cannot be zero 
	
	accuracy = (tp + tn) / total
	f1 = 2 * tp / (2 * tp + fp + fn)
	
	return accuracy, f1
	
	
print(performance(5, 0, 2, 3))
print(performance(5, 1, 0, 0))

