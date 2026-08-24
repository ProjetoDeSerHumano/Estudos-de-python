number = int(input("Digite um número para a tabuada: "))
print(f"Tabuada do {number}:")
for i in range(0, 11):
    print(f"{number} x {i} = {number * i}")
    