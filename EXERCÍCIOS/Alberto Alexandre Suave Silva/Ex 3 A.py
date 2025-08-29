class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def __len__(self):
        return len(self.tarefas)

    def __getitem__(self, index):
        return self.tarefas[index]

    def __iter__(self):
        return iter(self.tarefas)


def menu_lista():
    lista = ListaDeTarefas()
    while True:
        print("\n=== Lista de Tarefas ===")
        print("1 - Adicionar tarefa")
        print("2 - Ver todas as tarefas")
        print("3 - Sair")
        opc = input("Escolha uma opção: ")
        if opc == "1":
            tarefa = input("Digite a tarefa: ")
            lista.adicionar(tarefa)
            print("✅ Tarefa adicionada!")
        elif opc == "2":
            if len(lista) == 0:
                print("📭 Nenhuma tarefa cadastrada.")
            else:
                print("📋 Tarefas:")
                for i, t in enumerate(lista):
                    print(f"{i+1}. {t}")
        elif opc == "3":
            print("👋 Saindo da lista de tarefas...")
            break
        else:
            print("⚠️ Opção inválida.")


if __name__ == "__main__":
    menu_lista()