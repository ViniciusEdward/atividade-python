"Crie um programa que ajude um usuário a controlar seus gastos mensais. O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. O programa deve exibir o total gasto e o valor  excedente."
import os 
os.system("cls || clear")

orçamento = float(input("Digite o orçamento inicial para o mês: R$ "))
    

total_gasto = 0.0
gasto_diario = 0.0
    
print("\nDigite os gastos diários. Para encerrar, digite um valor negativo.")
    

while total_gasto <= orçamento:
        try:
            gasto_diario = float(input("Digite o valor do gasto diário: R$ "))
            if gasto_diario < 0:
                break
            total_gasto += gasto_diario
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")
    

excedente = total_gasto - orçamento
    
print(f"\nTotal gasto: R$ {total_gasto:.2f}")
if excedente > 0:
    print(f"Valor excedente: R$ {excedente:.2f}")
else:
    print("Não houve excedente do orçamento.")
