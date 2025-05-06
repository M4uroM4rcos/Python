# dicionario
import os
dados = {
    'nome': "Mauro Marcos",
    'idade': 39,
    'cpf': "666.666.666-66"
}

# exibe os dados do dicionario
for chave in dados:
    print(f'{chave.title()}: {dados.get(chave)}.')

# usuario insere novo chave (e-mail)
dados['email'] = input("\nInforme o e-mail do usuário: ")

# limpa terminal e re-exibe a lista
os.system('cls')
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}.")