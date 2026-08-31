import random

nome = []

for i in range(0, 4):
    nome.append(str(input("Digite o nome do aluno: ")))

lista = [nome[0], nome[1], nome[2], nome[3]]
escolhido = random.choice(lista)
print(f"O aluno escolhido é: {escolhido}")