import math

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h = math.hypot(co, ca)
print(f"A hipotenusa mede {h:.2f}")