x = input("Geben Sie eine Zahl x ein: ")
y = input("Geben Sie eine Zahl y ein: ")
z = input("Geben Sie eine Zahl z ein: ")

summe = x+y+z
print(summe)

x = input("Geben Sie eine Zahl x ein: ")
y = input("Geben Sie eine Zahl y ein: ")
z = input("Geben Sie eine Zahl z ein: ")

if x>y:
	y=x
if y>z:
	z=y
print(z)

x = input("Geben Sie eine Zahl x ein: ")
y = input("Geben Sie eine Zahl y ein: ")
z = input("Geben Sie eine Zahl z ein: ")

if x!=y and y!=z and z!=x:
	print(3)
elif x==y and y==z:
	print(1)
else:
	print(2)