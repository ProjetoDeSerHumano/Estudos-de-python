dias = int(input('Quantos dias você ficou com o carro alugado? '))
km = float(input('Quantos km você rodou com o carro alugado? '))
preco = (dias * 60) + (km * 0.15)
print(f'O preço a pagar pelo aluguel do carro é de R$ {preco:.2f}')