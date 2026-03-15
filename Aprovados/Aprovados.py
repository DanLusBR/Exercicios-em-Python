## Aprovados
## Fazer um programa para ler um número inteiro N e depois os dados (nome, primeira e segunda nota) de N alunos. Em seguida, mostrar os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
## igual a 6.0.

n: int
media: float

n = int(input("Quantos alunos serao digitados?: "))

nomes: [str] = [0 for x in range(n)] # type: ignore
notas1: [float] = [0 for x in range(n)] # type: ignore
notas2: [float] = [0 for x in range(n)] # type: ignore     

for i in range(n):
	print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno:")
	nomes[i] = str(input())
	notas1[i] = float(input())
	notas2[i] = float(input())

print("Alunos aprovados:")

for i in range(n):
	media = (notas1[i] + notas2[i]) / 2

	if media >= 6.0:
		print(nomes[i])