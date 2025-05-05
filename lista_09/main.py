# Importa biblioteca

import os

# declaração de lista
nomes = ['Fulano', 'Cicrano', 'Beltrano', 'João', 'Maria', 'José']

# tratamento de exceção
try:
    # loop infinito
    while True:
        #exibe a lista
        for i in range(len(nomes)):
            print(f'Nome de código {i}: {nomes[i]}.')
        # usuário informa se deseja excluir item
        opção = input('Deseja excluir item da lista? (s/n)')
        match opção:
            case 's':
                posicao = int(input('Informe o código do nome a ser alterado: '))
                del(nomes[posicao])
                # limpar o terminal
                os.system('cls')
                print('Item excluido com sucesso!\n')
            case 'n':
                break
            case _:
                print('Opção inválida')
                continue

except Exception as e:
    print(f'Não foi possivel deletar item da lista. {e}.')