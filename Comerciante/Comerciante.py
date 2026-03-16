## Comerciante
## Faça um programa para ler nome, preço de compra e preço de venda de N produtos. O programa deve mostrar quantos produtos proporcionaram lucro menor que 10%, entre 10% e 20% e maior que 20%. Além disso, deve mostrar o valor
## total investido (soma dos preços de compra), o valor total da venda (soma dos preços de venda) e o lucro total.

n: int; abaixo: int; entre: int; acima: int
vtotalcompra: float; vtotalvenda: float; lucrototal: float

n = int(input("Serao digitados dados de quantos produtos?: "))

nomes: list[str] = [0 for x in range(n)]
pcompra: list[float] = [0 for x in range(n)]
pvenda: list[float] = [0 for x in range(n)]
porcentagemlucros: list[float] = [0 for x in range(n)]

abaixo: int = 0
entre: int = 0
acima: int = 0
vtotalcompra: float = 0
vtotalvenda: float = 0
lucrototal: float = 0

for i in range(n):
	print(f"Produto {i + 1}:")
	nomes[i] = str(input("Nome: "))
	pcompra[i] = float(input("Preco de compra: "))
	pvenda[i] = float(input("Preco de venda: "))

for i in range(n):
	porcentagemlucros[i] = (pvenda[i] - pcompra[i]) / pcompra[i] * 100.0

abaixo = 0
entre = 0
acima = 0

for i in range(n):
	if porcentagemlucros[i] < 10.0:
		abaixo = abaixo + 1
	elif porcentagemlucros[i] < 20.0:
		entre = entre + 1
	else:
		acima = acima + 1

vtotalcompra = 0
vtotalvenda = 0

for i in range(n):
	vtotalcompra = vtotalcompra + pcompra[i]
	vtotalvenda = vtotalvenda + pvenda[i]

lucrototal = vtotalvenda - vtotalcompra

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")
print(f"Valor total de compra: {vtotalcompra:.2f}")
print(f"Valor total de venda: {vtotalvenda:.2f}")
print(f"Lucro total: {lucrototal:.2f}")