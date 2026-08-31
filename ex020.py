import random

lista = []
for i in range(0, 4):
    nome = str(input("Digite o nome do aluno: "))
    lista.append(nome)
random.shuffle(lista)
print(f"A ordem escolhida é: {lista}")