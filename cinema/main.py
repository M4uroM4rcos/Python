## Crie um algoritmo que receba o nome do usuário e sua idade e informe o nome de 5 filmes, e suas respectivas salas (sala 1 a sala 5),
## e também suas respectivas classificaçoes indicativas. O usuário deverá escolher o filme e o programa ira verificar se o usuário tem
## a idade minima para ver o filme. Caso tenha. o programa imprime o bilhete e encerra, Caso não tenha idade minima, o programa retorná
## para a tela de seleção de filmes, permitindo que o escolha outro filme.

# declaração de variveis
try:
    # repetição de algoritmo
    while True:
        # declaração de variaveis
        nome = input('Informe seu nome: ')
        idade = int(input('Informe sua idade: '))

        # saída de dados
        print(nome, 'é maior de idade.' if idade >= 18 else 'é menor de idade.')

        # mostre o menu
        print('Escolha a operação:')
        print('Sala 1 - Noite dos mortos vivos CL 18')
        print('Sala 2 - Efeito colateral CL 18')
        print('Sala 3 - Filme Músical CL 14')
        print('Sala 4 - Chapeuzinho Vermelho CL 13')
        print('Sala 5 - Casa Verde CL 10 -')

# ususário escolhe o operação
operador = input('Informe a operação desejada: ')

# estrutura match
match operador:
    case '1':
        print(f'Resultado da soma: {x+y}.')
    case '2':
        print(f'Resultado da subtração: {x-y}.')
    case '3':
        print(f'Resultado da multiplicação: {x*y}.')
    case '4':
        print(f'Resultado da divisão: {x/y}.')
    case '5':
        print(f'Resto da divisão: {x%y}.')
    case _:
        print('Operador inválido')
except Exception as e:
    print(f'Dados informados invalidos. {e}.')
finally:
    print('Programa finalizado com sucesso.')