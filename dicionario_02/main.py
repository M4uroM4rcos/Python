# declaração de dicionário
usuario = dict(nome="Fulano de Tal", idade=46, email="fulano@gmail.com")

# exibindo os dados do dicionario
for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}.")