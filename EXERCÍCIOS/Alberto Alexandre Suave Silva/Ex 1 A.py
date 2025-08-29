class Livro:
    def __init__(self, titulo: str, estoque: int):
        self.titulo = str(titulo)
        self._estoque = 0
        self.estoque = estoque

    @property
    def estoque(self) -> int:
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if isinstance(valor, bool):
            raise TypeError("Estoque deve ser um inteiro >= 0, não booleano.")
        if not isinstance(valor, int):
            try:
                valor = int(valor)
            except:
                raise TypeError("Estoque deve ser um inteiro >= 0.")
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo.")
        self._estoque = valor

    def __repr__(self):
        return f"📚 Livro: {self.titulo} | Estoque: {self.estoque}"


def menu_livro():
    livro = None
    while True:
        print("\n=== Sistema de Estoque de Livros ===")
        print("1 - Criar livro")
        print("2 - Consultar estoque")
        print("3 - Alterar estoque")
        print("4 - Sair")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            titulo = input("Digite o título do livro: ")
            try:
                estoque = int(input("Digite o estoque inicial: "))
                livro = Livro(titulo, estoque)
                print(f"✅ Livro criado: {livro}")
            except Exception as e:
                print(f"⚠️ Erro: {e}")
        elif opc == "2":
            if livro:
                print(f"📦 Estoque atual de '{livro.titulo}': {livro.estoque}")
            else:
                print("⚠️ Nenhum livro cadastrado ainda!")
        elif opc == "3":
            if livro:
                try:
                    novo_estoque = int(input("Digite o novo valor de estoque: "))
                    livro.estoque = novo_estoque
                    print(f"✅ Estoque atualizado: {livro.estoque}")
                except Exception as e:
                    print(f"⚠️ Erro: {e}")
            else:
                print("⚠️ Nenhum livro cadastrado ainda!")
        elif opc == "4":
            print("👋 Saindo do sistema de livros...")
            break
        else:
            print("⚠️ Opção inválida.")


if __name__ == "__main__":
    menu_livro()