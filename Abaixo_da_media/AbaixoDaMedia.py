## Abaixo da média
## Fazer um programa para ler um número inteiro N e depois um vetor V de N números reais. Em seguida, mostrar a média do vetor V e mostrar todos os elementos do vetor que estejam abaixo da média, com uma casa decimal.

n: int
soma: float; media: float

n = int(input("Quantos elementos vai ter o vetor?: "))

vetor: [float] = [0 for x in range(n)] # type: ignore

for i in range(n):
	vetor[i] = float(input("Digite um numero: "))

soma = 0

for i in range(n):
	soma = soma + vetor[i]


media = soma / n

print(f"\nMEDIA DO VETOR = {media:.3f}")
print("ELEMENTOS ABAIXO DA MEDIA:")

for i in range(n):
	if vetor[i] < media:
		print(f"{vetor[i]:.1f}")