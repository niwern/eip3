a = 0
b = 0
# wenn a,b > 500 ist a oder b die Hypothenuse und keine Kathete mehr
for a in range(1, 500):			
	for b in range(1, 500):
		c = 1000 -a -b		# folgt aus: a+b+c = 1000
		if a*a + b*b == c*c and a < b:	# Es gilt immer a,b < c, da c die Hypothenuse ist.
			print("a = {0}, b = {1}, c = {2}".format(a, b, c))
