import math

print("Aufgabenteil (2)")
k_0 = input("Geben Sie das Startkapital ein: ")
p = input("Geben Sie den Zinssatz ein: ")
n = input("Geben Sie den Anlagezeitraum (in Jahren) ein: ")
p = p/100.0
n = int(n//1)	# nur ganzzahlige eingaben
k = k_0 * (1 + p)**n
print("Kapital nach {0} Jahren: {1}".format(n, k))

print("Aufgabenteil (3)")
k_0 = input("Geben Sie das Startkapital ein: ")
k = input("Geben Sie das endgueltige Kapital ein: ")
p = input("Geben Sie den Zinssatz ein: ")
p = p/100.0
n = math.log(float(k)/k_0, 1+p)
print("Anlagezeitraum: "+ str(int(math.ceil(n))) +" Jahre")	# Da nur am Ende des Jahres die Zinsen ausgegeben werden, wird nach oben gerundet

# TODO es fehlt noch Aufgabenteil (1) und (4)