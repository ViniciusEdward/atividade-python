"Desenvolva um programa que conte quantos números negativos foram inseridos pelo usuário usando um laço while. O programa deve parar quando o usuário inserir 0 ou um número positivo. Mostre a quantidade de números negativos."
import os 
os.system("cls || clear")
contador = 0

while True:
    nota = float(input("Escreva um número: "))
    if nota < 0:
        contador += 1
    else:
        nota == 0 or nota > 0 
        print("Número inválido")
        break


print(f"contador: {contador}")