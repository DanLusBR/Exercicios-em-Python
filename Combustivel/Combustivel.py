## Combustivel
## Faça um programa que leia o tipo de combustível abastecido (codificado da seguinte forma: 1. Álcool, 2. Gasolina, 3. Diesel, 4. Fim).

codigo: int; alcool: int; gasolina: int; diesel: int

codigo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

alcool = 0
gasolina = 0
diesel = 0

while codigo != 4:
	if codigo == 1:
		alcool = alcool + 1
	elif codigo == 2:
		gasolina = gasolina + 1
	elif codigo == 3:
		diesel = diesel + 1
	codigo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")