## Menor de três
## Faça um programa que leia três valores inteiros e mostre o menor deles.

a: int; b: int; c: int; menor: int

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a < b and a < c:
	menor = a
elif b < c:
	menor = b
else:
	menor = c

print(f"MENOR = {menor}")