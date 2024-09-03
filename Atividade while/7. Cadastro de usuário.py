"CADASTRO DE USUÁRIO COM CONFIRMAÇÃO DE SENHA"
import os
os.system("cls || clear")

senha = input("Crie sua senha: ")

while True:
    confirmacao = input("Confirme sua senha: ")

    if senha == confirmacao:
        print("Acesso concedido...")
        break

    if senha != confirmacao:
        os.system("cls || clear")
        print("Senha incorreta")
        
        

