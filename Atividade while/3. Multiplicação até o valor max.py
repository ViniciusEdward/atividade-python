"Escreva um programa que multiplique um número inicial por um fator dado pelo usuário até que o produto exceda 100. Exiba o produto final e o número de multiplicações realizadas."
import os 
os.system("cls || clear")
numero = 0
contador = 0
gastos = int(input("Digite a quantidade de vezes que você gasta mensalmente: "))
while True:
        for i in range(gastos):
              numero_digitado = int(input("Digite um número: "))
              numero += numero_digitado
              contador += 1
              if numero > 5000:
                     break
        print(f"Total: {numero}")
        print(f"Contador: {gastos}")
        break
        