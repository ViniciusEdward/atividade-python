"Crie um programa que peça ao usuário para inserir números inteiros até que a soma dos números ímpares inseridos seja maior que 200. O programa deve exibir o total de números ímpares inseridos e a soma desses números. "

import os
os.system("cls || clear")

impares = 0
contador = 0

while impares <= 200:
    numero = int(input("Digite um numero inteiro: "))

    if numero % 2 != 0:
        impares += numero
        contador += 1

    print(f"numero digitado: {impares}")
print(f"Vezes repetidas: {contador}")
