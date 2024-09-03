"Crie um programa para ajudar o usuário a acompanhar suas metas de estudo. O usuário define uma meta de horas de estudo e o programa deve permitir que o usuário insira o número de horas estudadas até que o total atinja ou exceda a meta. O programa deve  exibir o total de horas estudadas e o valor excedente."

import os
os.system("cls || clear")

meta = float(input("Digite sua meta de horas de estudo: "))
total_horas = 0

while total_horas < meta:
    horas_estudadas = float(input("Digite o número de horas estudadas hoje: "))
    total_horas += horas_estudadas
    excedente = total_horas - meta
    if excedente > 0:
        print(f"Parabéns! Você atingiu sua meta e ainda estudou {excedente:.2f} horas a mais.")
    else:
        print(f"Você atingiu sua meta de {meta} horas de estudo!")