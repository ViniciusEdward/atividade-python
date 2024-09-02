"Escreva um programa que calcule a soma dos números ímpares de 1 a 9 utilizando um laço `for`."
import os
os.system("cls || clear")
impares = 0
soma = 0

for numero in range(1,11,2):
    print(f"{numero}")
    if numero % 2 != 0:
     impares = impares + 1
    soma += numero

print(f"IMPARES: {impares}")
print(f"Soma: {soma}")