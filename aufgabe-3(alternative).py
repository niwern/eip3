def min(a, b):
	if a<b:
		return a
	else:
		return b

for counter in range(9):
		i=counter+1
		j=9-counter
		print("* "*min(i,j))