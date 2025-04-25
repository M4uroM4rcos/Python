# Crie um programa que receba do usuario uma lista de compras e ordene a lista em ordem alfabetica.
# 1º Obs: só quero os nomes dos itens, deixe os preços e a quantidade de fora.
# 2º Obs: após terminarem, faça o comit no GitHub.

# importar a bibliotexa
import os

# declarar lista
lista = []

# tratamento de execeção
try:
    # loop infinito
    while True:
        # informe os intens de sua compra
        item = input('Informe o nome intem ou deixe em branco para encerrar: ') # input
        os.system('cls') # limpa o terminal

        #verifica se o item está vazio ou não
        if item != "":
            lista.append(item) # insere o item na lista
            print(f'{item} inserido na lista com sucesso!') # mensagem de confirmação
            continue
        else:
            break

    # ordenar lista
    lista.sort()

except Exception as e:
    print(f'Não foi possivel inserir item ma lista. {e}.')

finally:
    print('Lista de itens:\n')
    for item in lista:
        print(item)