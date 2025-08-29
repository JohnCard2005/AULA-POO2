class ListaDeTarefas:
    def __init__(self):
        self._tarefas = []

    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)

    def remover(self, indice):
        if 0 <= indice < len(self._tarefas):
            del self._tarefas[indice]
        else:
            print("Índice inválido!")

    def listar(self):
        if not self._tarefas:
            print("Nenhuma tarefa na lista.")
            return
        for i, tarefa in enumerate(self._tarefas):
            print(f"{i}. {tarefa}")

    def __len__(self):
        return len(self._tarefas)

    def __getitem__(self, index):
        return self._tarefas[index]

    def __iter__(self):
        return iter(self._tarefas)


def menu():
    lista = ListaDeTarefas()

    while True:
        print("\n=== MENU ===")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Listar tarefas")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            lista.adicionar(tarefa)
            print("Tarefa adicionada!")

        elif escolha == "2":
            if len(lista) == 0:
                print("Nenhuma tarefa para remover.")
                continue
            lista.listar()
            try:
                indice = int(input("Digite o número da tarefa para remover: "))
                lista.remover(indice)
                print("Tarefa removida!")
            except ValueError:
                print("Por favor, digite um número válido.")

        elif escolha == "3":
            print("\nTarefas:")
            lista.listar()

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
