import math
a = 0
b = 0
while a+b < 500:
	for a in range(500):
		for b in range(500):
			c_sqr = a**2 + b**2
			c = math.sqrt(c_sqr)
			if (a + b + c) == 1000:
				print(a, b, int(c))