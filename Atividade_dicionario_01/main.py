""" Crie um programa que inicializa um dicionario zerado, e o usuario adiciona e insere os seguintes dados:
# Nome, DT nascimento, CPF, E-mail, Genero, Telefone, Altura, Peso, tipo sanguineo:
# Ao final, o programa exibe os dados do usuario e informa se IMC."""
# NOTE: o usuário deverá informar o valor apenas dessas chaves.

import os
# dicionario
dados = {}

try:
    
    print("Para realizar um cadastro, favor informe os seguintes dados: ")
    
    while True:
        
        # exibe os dados do dicionario
        for chave in dados:
            print(f'{chave.title()}: {dados.get(chave)}.')

        # usuário informa se deseja inserir nova chave ou encerrar
        prosseguir = input("Deseja inserir novos dados? (s/n): ")
        match prosseguir:
                case "s":
                    # usuário informa o nome da chave adicional que deseja cadastrar
                    nova_chave = input("\nInforme o nome da nova chave: ")
                    dados[nova_chave] = input(f'Informe o valor de {nova_chave}: ')
                    os.system("cls")
                    continue
                case "n":
                    break
                case _:
                    print("Opção invalida.")
        

except Exception as e:
    print(f'Não foi possivel inserir a nova chave. {e}.')

finally:
     print ("Bem vindo a Calculadora de IMC")

pergunta_nome = input("Qual é o seu nome? " )
nome = ("Olá" , pergunta_nome)
idade = input (f"Qual sua idade? ")
peso = float(input("Qual seu peso (em KG)? "))
altura = float(input("Qual sua Altura (em metros e usando ponto)? "))

print("Vamos calcular seu IMC")

imc = (peso / (altura * altura))

print(pergunta_nome , (f"seu IMC é: {imc:.2f}"))

if imc < 16:
	print("Seu estado é de Magreza grave\nProcure um médico ou nutricionista.")
elif imc < 17:
	print("Seu estado é de Magreza moderada\nPrecisa rever sua alimentação.")
elif imc < 18.5:
	print("Seu estado é de Magreza leve\nPrecisa rever sua alimentação.")
elif imc < 25:
	print("Você está Saudável.\nParabéns!")
elif imc < 30:
	print("Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.")
elif imc < 35:
	print("Seu estado é de Obesidade Grau I\nProcure um médico ou nutricionista.")
elif imc < 40:
	print("Seu estado é de Obesidade Grau II (severa)\nProcure um médico ou nutricionista.")
else:
	print("Seu estado é de Obesidade Grau III (mórbida)\nProcure um médico ou nutricionista.")