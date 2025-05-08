# declaração tupla
chaves = ("nome", "idade", "cpf", "telefone", "email", "profissão")
usuario = {
    chaves[0]: "Mauro Marcos",
    chaves[1]: 39,
    chaves[2]: "666.666.666-66",
    chaves[3]: "(61) 96666-6666",
    chaves[4]: "mauro@gmail.com",
    chaves[5]: "Programador"
}
for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}.")