# Aufgabenteil (2)
k_0 = input("Geben Sie das Startkapital ein: ")
p = input("Geben Sie den Zinssatz ein: ")
n = input("Geben Sie den Anlagezeitraum (in Jahren) ein: ")

p = p/100.0
print(p)
k = k_0 * (1 + p)**n

print(k)

# TODO es fehlt noch Aufgabenteil (1), (3) und (4)