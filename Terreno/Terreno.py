## Terreno
## Faça um programa que leia a largura, o comprimento e o valor do metro quadrado de um terreno. Em seguida, calcule e mostre a área do terreno e o preço do terreno.

largura: float; comprimento: float; valor: float; area: float; preco: float;

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do metro quadrado: "))

area = largura * comprimento

print(f"Area do terreno = {area:.2f}")

preco = area * valor

print(f"Preco do terreno = {preco:.2f}\n")