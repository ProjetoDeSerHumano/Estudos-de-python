valor = float(input("Digite o valor do produto: R$  "))
desconto = valor * 0.05
valor_final = valor - desconto  
print(f"O valor do produto com 5% de desconto é: R$ {valor_final:.2f}")