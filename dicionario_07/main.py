# NOTA: esse programa vai mostrar como deletar um item.
# impotação de biblioteca
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
        prosseguir = input("Deseja excluir uma chave? (s/n): ")
        match prosseguir:
            case "s":
                chave_escolhida = input("Informe o nome da chave que deseja excluir: ")
                if chave_escolhida in chaves:
                    usuario.pop(chave_escolhida, None)
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
