# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa(tarefas, nome):
    # Cria um dicionário com o nome da tarefa e status de completada como False
    tarefas.append({"tarefa": nome, "completada": False})
    # Exibe mensagem de confirmação
    print(f"Tarefa '{nome}' adicionada com sucesso!")

# Função para exibir todas as tarefas
def ver_tarefas(tarefas):
    print("\n Lista de Tarefas:")
    # Percorre a lista de tarefas com índice começando em 1
    for i, tarefa in enumerate(tarefas, 1):
        # Define o símbolo de status como ✓ se a tarefa estiver completa
        status = "✓" if tarefa["completada"] else " "
        # Exibe o número da tarefa, status e nome
        print(f"{i}. [{status}] {tarefa['tarefa']}")

# Função para atualizar o nome de uma tarefa
def atualizar_tarefa(tarefas, indice, novo_nome):
    i = indice - 1  # Ajusta o índice para começar do zero
    # Verifica se o índice é válido
    if 0 <= i < len(tarefas):
        tarefas[i]["tarefa"] = novo_nome  # Atualiza o nome da tarefa
        print(f"Tarefa {indice} atualizada para '{novo_nome}'")
    else:
        print("Índice inválido.")

# Função para marcar uma tarefa como completada
def completar_tarefa(tarefas, indice):
    i = indice - 1  # Ajusta o índice
    # Verifica se o índice é válido
    if 0 <= i < len(tarefas):
        tarefas[i]["completada"] = True  # Marca como completada
        print(f"Tarefa {indice} marcada como completada.")
    else:
        print("Índice inválido.")

# Função para deletar todas as tarefas que estão marcadas como completadas
def deletar_completadas(tarefas):
    # Filtra a lista mantendo apenas tarefas não completadas
    tarefas[:] = [t for t in tarefas if not t["completada"]]
    print("Tarefas completadas foram deletadas.")

# Função principal que exibe o menu e controla o fluxo do programa
def menu():
    tarefas = []  # Lista que armazenará as tarefas
    while True:
        # Exibe o menu de opções
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Atualizar tarefa")
        print("4. Completar tarefa")
        print("5. Deletar tarefas completadas")
        print("6. Sair")

        # Recebe a escolha do usuário
        escolha = input("Escolha uma opção: ")

        # Adiciona uma nova tarefa
        if escolha == "1":
            nome = input("Nome da tarefa: ")
            adicionar_tarefa(tarefas, nome)

        # Exibe todas as tarefas
        elif escolha == "2":
            ver_tarefas(tarefas)

        # Atualiza o nome de uma tarefa
        elif escolha == "3":
            ver_tarefas(tarefas)
            try:
                indice = int(input("Número da tarefa a atualizar: "))
                novo_nome = input("Novo nome: ")
                atualizar_tarefa(tarefas, indice, novo_nome)
            except ValueError:
                print("Entrada inválida.")

        # Marca uma tarefa como completada
        elif escolha == "4":
            ver_tarefas(tarefas)
            try:
                indice = int(input("Número da tarefa a completar: "))
                completar_tarefa(tarefas, indice)
            except ValueError:
                print("Entrada inválida.")

        # Remove tarefas completadas
        elif escolha == "5":
            deletar_completadas(tarefas)
            ver_tarefas(tarefas)

        # Encerra o programa
        elif escolha == "6":
            print("Programa finalizado.")
            break

        # Caso o usuário digite uma opção inválida
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal para iniciar o programa
menu()