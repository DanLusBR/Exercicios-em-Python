### Soma de vetores
## Faça um programa que leia um número inteiro N e depois leia N números reais. Armazene os números lidos em um vetor. Em seguida, mostre na tela o valor do vetor (em uma linha), a soma e a média dos elementos do vetor.

n = int(input("Quantos numeros voce vai digitar?: "))

vetor = [0.0 for _ in range(n)]

for i in range(n):
    vetor[i] = float(input("Digite um numero: "))

soma = 0.0
for i in range(n):
    soma += vetor[i]

media = soma / n

print("\nVALORES = ", end="")
for i in range(n):
    print(f"{vetor[i]:.1f}", end=" ")

print(f"\nSOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")