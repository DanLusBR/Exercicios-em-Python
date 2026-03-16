## Consumo
## Faça um programa para ler a distância total percorrida por um automóvel e o total de combustível gasto. O programa deve calcular e mostrar o consumo médio do automóvel, com três casas decimais.

distancia: int
gasto: float; consumo: float

distancia = int(input("Distancia percorrida(Em Km): "))

gasto = float(input("Combustivel gasto(Em Litros): "))

consumo = distancia/gasto

print(f"Consumo medio = {consumo:.3f}")