""" Crie um programa que inicializa um dicionario zerado, e o usuario adiciona e insere os seguintes dados:
# Nome, DT nascimento, CPF, E-mail, Genero, Telefone, Altura, Peso, tipo sanguineo:
# Ao final, o programa exibe os dados do usuario e informa se IMC."""
# NOTE: o usuário deverá informar o valor apenas dessas chaves.

import os
# dicionario
dados = {}

try:
    
    print("Para realizar um cadastro, favor informe os seguintes dados: \nNome, \nDta Nascimento, \nCPF, \nE-mail, \nGenero, \nTelefone, \nAltura, \nPeso, \nTipo Sanguineo")
    
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