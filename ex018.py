import math 

an = float(input("Digite o ângulo que você deseja: "))
print(f"O seno de {an} é {math.sin(math.radians(an)):.2f}")
print(f"O cosseno de {an} é {math.cos(math.radians(an)):.2f}")
print(f"O tangente de {an} é {math.tan(math.radians(an)):.2f}")