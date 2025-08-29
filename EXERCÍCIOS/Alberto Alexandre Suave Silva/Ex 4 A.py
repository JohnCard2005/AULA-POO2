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


def menu_quadrado():
    while True:
        print("\n=== Calculadora de Quadrado ===")
        try:
            lado = float(input("Digite o tamanho do lado do quadrado: "))
            if lado < 0:
                print("⚠️ Lado não pode ser negativo!")
                continue
            q = Quadrado(lado)
            print(f"🔲 Área do quadrado: {q.area()}")
        except Exception as e:
            print(f"⚠️ Erro: {e}")
        sair = input("Deseja calcular outro quadrado? (s/n): ").lower()
        if sair != 's':
            break


if __name__ == "__main__":
    menu_quadrado()