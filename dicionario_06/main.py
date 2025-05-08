# importar biblioteca
import os
# usando tupla dentro de biblioteca
chaves = ("nome", "idade", "cpf", "telefone", "email", "profissão")
usuario = {
    chaves[0]: "Mauro Marcos",
    chaves[1]: 39,
    chaves[2]: "666.666.666-66",
    chaves[3]: "(61) 96666-6666",
    chaves[4]: "mauro@gmail.com",
    chaves[5]: "Programador"
}

try:
    while True:
    
        for chave in usuario:
            print(f"{chave}: {usuario.get(chave)}.")
        prosseguir = input("Deseja alterar o dado de alguma chave? (s/n): ")
        match prosseguir:
            case "s":
                chave_escolhida = input("Informe o name da chave que deseja alterar: ")
                if chave_escolhida in chaves:
                    usuario[chave_escolhida] = input("Informe o novo valor da chave escolhida: ")
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print(f"{chave_escolhida} não existe.")
            case "n":
                break
            case _:
                print("Opção invalida.")
                continue
except Exception as e:
    print(f"Não foi possivel atualizar as chaves. {e}.")
