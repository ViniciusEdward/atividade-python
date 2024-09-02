"Escreva um programa que use um laço while para encontrar o primeiro número maior que 50 que seja divisível por 7. Exiba esse número."
import os, time
os.system("cls || clear")
numero = 51
while True:
    if numero % 7 == 0:
        print(f"Número: {numero}")
        break
        
    numero += 1
    