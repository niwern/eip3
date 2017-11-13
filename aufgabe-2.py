import math

# Aufgabenteil (2)
def a_2_2(k_0, p, n):
	print(p)
	k = k_0 * (1 + p)**n
	print(k)

def a_2_3(k_0, k, p): # Ausgabe stimmt nicht!!
	n = math.log(float(k), (1.0 + float(p))) - math.log(float(k_0), (1.0 + float(p)))
	print(n)

def a_2_4():
	pass

def main():
	print("Aufgabenteil (2) : ")
	k_0 = input("Geben Sie das Startkapital ein: ")
	p = input("Geben Sie den Zinssatz ein: ")
	n = input("Geben Sie den Anlagezeitraum (in Jahren) ein: ")
	p = p/100.0
	a_2_2(k_0, p, n)

	print("Aufgabenteil (3) : ")
	k_0 = input("Geben Sie das Startkapital ein: ")
	k = input("Geben Sie das endgueltige Kapital ein: ")
	p = input("Geben Sie den Zinssatz ein: ")
	a_2_3(k_0, k, p)

erg = math.log(1024, 2)
print(erg)
#a_2_3(100, 120, 1)
# TODO es fehlt noch Aufgabenteil (1), (3) und (4)