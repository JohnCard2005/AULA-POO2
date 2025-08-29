class Livro:
    def __init__(self, titulo, estoque):
        self.titulo = titulo
        self._estoque = 0
        self.estoque = estoque

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo.")
        self._estoque = valor

if __name__ == "__main__":
    print("Executando joao.py")
    livro = Livro("Python para Iniciantes", 10)
    print(f"Título: {livro.titulo}")
    print(f"Estoque: {livro.estoque}")
