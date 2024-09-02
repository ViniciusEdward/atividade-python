"Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`)."
import os
os.system("cls || clear")

num_linhas = 5
num_colunas = 20
contador = 0

for i in range(1):
    print("* * * * * * * * ")
    for j in range(10):
        print ("*             *")
        contador += 1
    if contador == 10:
        for i in range(1):
            print("* * * * * * * *")