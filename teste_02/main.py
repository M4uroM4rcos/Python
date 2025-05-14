import os

# Lista para armazenar os cadastros
pessoas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar():
    pessoa = {}
    pessoa['nome'] = input("Nome: ")
    pessoa['cpf'] = input("CPF (chave única): ")
    pessoa['email'] = input("Email: ")
    pessoa['telefone'] = input("Telefone: ")
    pessoa['data_nasc'] = input("Data de Nascimento: ")
    pessoa['genero'] = input("Gênero: ")

    pessoas.append(pessoa)
    print(f"{pessoa['nome']} cadastrado com sucesso!")

def listar():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
    else:
        for pessoa in pessoas:
            print("\n" + "-"*20)
            for chave, valor in pessoa.items():
                print(f"{chave.title()}: {valor}")

def alterar():
    cpf = input("Informe o CPF da pessoa que deseja alterar: ")
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            print("Pessoa encontrada. Informe os novos dados:")
            pessoa['nome'] = input("Nome: ")
            pessoa['email'] = input("Email: ")
            pessoa['telefone'] = input("Telefone: ")
            pessoa['data_nasc'] = input("Data de Nascimento: ")
            pessoa['genero'] = input("Gênero: ")
            print("Dados atualizados com sucesso!")
            return
    print("Pessoa com esse CPF não foi encontrada.")

def excluir():
    cpf = input("Informe o CPF da pessoa que deseja excluir: ")
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            pessoas.remove(pessoa)
            print("Pessoa excluída com sucesso!")
            return
    print("Pessoa com esse CPF não foi encontrada.")

# Menu principal
while True:
    print("\n--- MENU ---")
    print("[1] Cadastrar")
    print("[2] Listar")
    print("[3] Alterar")
    print("[4] Excluir")
    print("[5] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        alterar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida.")

    input("\nPressione Enter para continuar...")
    limpar_tela()
