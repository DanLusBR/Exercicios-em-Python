## Crescente ou Decrescente
## Faça um programa que leia uma quantidade indeterminada de pares de números inteiros. Para cada par, o programa deve dizer se eles estão em ordem crescente ou decrescente. O programa deve terminar quando os dois números forem ## iguais.

x: int; y: int

print("Digite dois numeros:")
x = int(input())
y = int(input())

while x != y:
	if x > y:
		print("DECRESCENTE!")
	else:
		print("CRESCENTE!")

	print("Digite dois numeros:")
	x = int(input())
	y = int(input())