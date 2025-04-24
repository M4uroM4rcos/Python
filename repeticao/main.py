# tramento de exceção
try:
    # repetição de algoritmo
    while True:
        # declaração de variaveis
        nome = input('Informe seu nome: ')
        idade = int(input('Informe sua idade: '))

        # saída de dados
        print(nome, 'é maior de idade.' if idade >= 18 else 'é menor de idade.')

        # decisão
        continuar = input('Deseja continuar? (s/n)')
        match continuar:
            case 's':
                continue
            case 'n':
                break
            case _:
                print('Não foi possivél computar sua decissão.')
except Exception as e:
    print(f'Dados informados invalidos. {e}.')
finally:
    print('Programa finalizado com sucesso.')