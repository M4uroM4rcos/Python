# importar biblioteca
import os
# dicionario
dados = {
    'nome': "Mauro Marcos",
    'idade': 39,
    'cpf': "666.666.666-66"
}

try:
    while True:
        os.system('cls')
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
                    continue
                case "n":
                    break
                case _:
                    print("Opção invalida.")

except Exception as e:
    print(f'Não foi possivel inserir a nova chave. {e}.')