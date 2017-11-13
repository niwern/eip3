for i in range(5):
	print(i)

for i in range(3,6):
	print(i)

for i in range(2, 7, 2):
	print(i)

str = 'Einfuehrung in die Programmierung' # Der Kompiler akzepiert keine Umlaute
for i in range(len(str)):
	print(str[i])

i = 0
while i < 5:
	print(i)
	i += 1

for j in range(1, 6):
	print("* " * j)
for i in range(4, 0, -1):
	print("* " * i)