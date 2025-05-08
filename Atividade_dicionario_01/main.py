""" Crie um programa que inicializa um dicionario zerado, e o usuario adiciona e insere os seguintes dados:
# Nome, DT nascimento, CPF, E-mail, Genero, Telefone, Altura, Peso, tipo sanguineo:
# Ao final, o programa exibe os dados do usuario e informa se IMC."""
# NOTE: o usuário deverá informar o valor apenas dessas chaves.

import os
# dicionario
usuario = {}

try: 
    usuario["nome"] = input('Informe o nome: ')
    usuario["data de nascimento"] = input('Informe a data de nascimento: ')
    usuario["cpf"] = input('Informe o cpf: ')
    usuario["email"] = input('Informe o email: ')
    usuario["gênero"] = input('Informe o gênero: ')
    usuario["telefone"] = input('Informe o telefone: ')
    usuario["altura"] = float(input('Informe a altura: ').replace(",", "."))
    usuario["peso"] = float(input('Informe o peso: ').replace(",", "."))
    usuario["tipo sanguinêo"] = input('Informe o tipo sanguinêo: ')

    # exibe os dados do usuário
    for chave in usuario:
          print(f'{chave.title()}: {usuario.get(chave)}')

    # exibindo o imc do usuario
    imc = usuario.get("peso")/usuario.get('altura')**2

    # exibe o valor do imc
    print(f'\nIMC de {usuario.get('nome')}: {imc:,.2f}')

    # escolhe o diagnostico do usuario co, base no valor do imc
    if imc <= 18.5:
        print(f"{usuario.get('nome')} está abaixo do peso.")
    elif imc < 25:
        print(f"{usuario.get('nome')} está no peso ideal. PARABENS!!!")
    elif imc < 30:
        print(f"{usuario.get('nome')} está acima do peso ideal.")
    elif imc < 35:
        print(f"{usuario.get('nome')} está obeso.")
    elif imc < 40:
        print(f"{usuario.get('nome')} está com obesidade nevel II.")
    else:
        print(f"{usuario.get('nome')} está com obesidade morbida. PROCURE UM MÉDICO.")

except Exception as e:
      print(f"Não foi possivel inserir os dados. {e}.")