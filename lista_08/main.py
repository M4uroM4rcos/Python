# importa biblioteca
import os

# declaração de lista
cidades = ['Brasília', 'São Paulo', 'Rio de Janeiro', 'Curitiba', 'Recife', 'Fortaleza']

# tratamento de exceção
try:
    #loop infinito
    while True:
        #exibe a lista
        for i in range(len(cidades)):
            print(f'Cidade de código {i}: {cidades[i]}.')
        # usuário informa se deseja alterar algum valor
        alterar = input('\nDeseja alterar algum valor? (s/n)')
        match alterar:
            case "s":
                # usuário informa a posição do valor que deseja alterar
                codigo_cidade = int(input('\nInforme o código da ciade que deseja mudar: '))
                # usuário informa o novo valor
                nova_cidade = input('Informe o novo nome da cidade: ')
                # troca o valor
                cidades[codigo_cidade] = nova_cidade
                os.system('cls')

            case "n":
                break
            case _:
                print('Opção inválida')
                break

except Exception as e:
    print(f'Não foi possivel alterar valor da lista. {e}')