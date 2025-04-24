habitos = {}

def carregar_habitos():
    try:
        with open("habitos.txt", "r") as f:
            for linha in f:
                nome, vezes = linha.strip().split(":")
                habitos[nome] = int(vezes)
    except FileNotFoundError:
        pass

def salvar_habitos():
    with open("habitos.txt", "w") as f:
        for nome, vezes in habitos.items():
            f.write(f"{nome}:{vezes}\n")

def adicionar_habito():
    nome = input("Digite o nome do hábito que deseja acompanhar: ")
    if nome in habitos:
        print("Esse hábito já existe.")
    else:
        habitos[nome] = 0
        print("Hábito adicionado com sucesso.")

def marcar_feito():
    nome = input("Digite o nome do hábito que você realizou hoje: ")
    if nome in habitos:
        habitos[nome] += 1
        print(f"Hábito '{nome}' marcado como feito!")
    else:
        print("Esse hábito ainda não foi adicionado.")

def listar_habitos():
    if not habitos:
        print("Nenhum hábito registrado ainda.")
    else:
        print("\nSeu progresso:")
        for nome, vezes in habitos.items():
            print(f"- {nome}: {vezes} dia(s) feito(s)")

def menu():
    carregar_habitos()
    while True:
        print("\n--- Diário de Hábitos Saudáveis ---")
        print("1. Adicionar hábito")
        print("2. Marcar hábito como feito")
        print("3. Ver progresso")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_habito()
        elif opcao == "2":
            marcar_feito()
        elif opcao == "3":
            listar_habitos()
        elif opcao == "4":
            salvar_habitos()
            print("Progresso salvo. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
