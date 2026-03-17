## Diagonal Negativos
## Ler uma matriz quadrada de ordem N, contendo números inteiros. Em seguida, mostrar a diagonal principal e a quantidade de valores negativos da matriz.

n = int(input("Qual a ordem da matriz?: "))

matriz = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("DIAGONAL PRINCIPAL:")

for i in range(n):
    print(matriz[i][i], end=" ")

qtdnegativos = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] < 0:
            qtdnegativos += 1

print(f"\nQUANTIDADE DE NEGATIVOS = {qtdnegativos}")