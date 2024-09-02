"Crie um programa que ajude um usuário a controlar seus gastos mensais. O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. O programa deve exibir o total gasto e o valor  excedente."
import os 
os.system("cls || clear")

numero = 5000
gastos_diarios = 0
num_contador = int(input("Digite a quantidade de vezes que deseja multiplicar (máx 100): "))
while True:
        for i in range(num_contador):
              numero_digitado = int(input("Digite um número: "))
              numero += numero_digitado
              if numero > 5000:
                     break
        print(f"Total: {numero}")
        break