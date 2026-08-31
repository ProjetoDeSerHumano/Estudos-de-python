nome = str(input("Digite seu nome completo: ")).strip()

print("Seu nome em maiusculo é " + nome.upper())
print("Seu nome em minusculo é " + nome.lower())
print("Seu nome tem " + str(len(nome) - nome.count(" ")) + " letras")
print("Seu primeiro nome é " + nome.split()[0])
print("Seu primeiro nome tem " + str(len(nome.split()[0])) + " letras")