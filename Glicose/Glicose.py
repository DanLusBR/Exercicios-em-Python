## Glicose
## Escreva um programa que leia a medida da glicose e classifique-a entre normal, elevado ou diabetes.

glicose: float
glicose = float(input("Digite a medida da glicose: "))

print("Classificacao: ", end="")

if glicose <= 100:
	print("Normal")
elif glicose <= 140:
	print("Elevado")
else:
	print("Diabetes")