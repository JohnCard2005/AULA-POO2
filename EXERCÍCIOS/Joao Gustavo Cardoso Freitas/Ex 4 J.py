from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Exemplo de uso
if __name__ == "__main__":
    q = Quadrado(5)
    print(f"Área do quadrado: {q.area()}")
