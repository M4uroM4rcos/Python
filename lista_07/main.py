# importar biblioteca
import os

# declaração da lista
cidades = ['Brasília', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Goiânia', 'Palmas', 'Brasília', 'Brasília', 'Goiânia']

# Tratamento de exceção
try:
    # loop infinito
    while True:
        #limpeza do terminal
        os.system('cls')

        #usuário informa valor a ser pesquisado
        pesquisa = input('Informe a cidade a ser pesquisada: ').title() # title coloca a primeira letra como maiúscula

        # retorna quantidade de valores encontrados
        result = cidades.count(pesquisa)

        # mostra resultado na lisra
        if result != 0:
            print(f'{pesquisa} foi encontrado na lista {result} vezes.')
        else:
            print(f'{pesquisa} não foi encotrado na lista.')

        # perguntar se o usuário deseja continuar
        continuar = input('Deseja continuar? (s/n): ')

        # verificar ser o usuário deseja continuar
        match continuar:
            case "s":
                continue
            case "n":
                break
            case _:
                print('Opção inválida.')


except Exception as e:
    print(f'Não foi possível realizar a busca. {e}.')