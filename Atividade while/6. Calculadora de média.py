"CALCULADORA DE MÉDIA DE NOTAS"
import os
os.system("cls || clear")

soma = 0
soma_adicional = 0
num_notas = int(input("Digite a quantidade de notas: "))

for i in range(num_notas):
    while True:
        nota = float(input(f"Digite {i + 1}º nota: "))
        soma += nota 

        if nota < 0 or nota > 10:
            os.system("cls || clear")
            print("Nota inválida, digite novamente.")

        else:
            break
    
    media = soma / num_notas

print(f"\nMédia: {media:.2f}")

if media >= 7:
    print("Parabéns, você está aprovado!")
elif media >= 5 and media < 7:
    print("Infelizmente você não conseguiu a atingir a nota esperada. Recuperação")
elif media < 5:
    print("Sinto muito. Reprovado")