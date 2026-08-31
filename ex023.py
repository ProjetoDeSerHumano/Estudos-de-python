num = int(input("Digite um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"analisando o numero {num}")
print("Unidade: " + str(u))
print("Dezena: " + str(d))
print("Centena: " + str(c))
print("Milhar: " + str(m))