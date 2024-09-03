"Desenvolva um programa que solicite ao usuário inserir um código de promoção para obter um desconto. O código correto é 'PROMO2024'. O usuário tem 3 tentativas para acertar o código. Se o código estiver correto, exiba uma mensagem de 'Código aceito' e o desconto. Se o usuário errar o código nas 3 tentativas, exiba uma mensagem de 'Código inválido'."
import os 
os.system("cls || clear")

contador = 0
tentativa = 3
promocao = "PROMO2024"

while True:
    codigo = input("Digite o código promocional: ")
    if promocao == codigo:
        print("Desconto concedido")
        break

    else:
        contador += 1
        print("Tente novamente")
    if contador == tentativa:
        print("Número de tentativas excedidas")
        break
        
        