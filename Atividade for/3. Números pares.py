" Desenvolva um programa que use um laço `for` para imprimir todos os números pares de 2 a 10."
import os 
os.system("cls || clear")
pares = 0
impares = 0

for i in range(2,11,2):
    print(f"{i}")
    if i % 2 == 0:
     pares = pares + 1


print(f"PARES: {pares}")
