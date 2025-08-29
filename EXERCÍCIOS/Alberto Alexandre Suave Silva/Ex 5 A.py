class Registro:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def __enter__(self):
        self.f = open(self.arquivo, "a")
        self.f.write("=== Início do registro ===\n")
        return self.f

    def __exit__(self, tipo, valor, traceback):
        self.f.write("=== Fim do registro ===\n\n")
        self.f.close()


def menu_registro():
    while True:
        print("\n=== Registro de Atividades ===")
        nome = input("Digite o nome do arquivo de registro: ")

        with Registro(nome) as f:
            print("Digite as mensagens que deseja registrar (uma por vez).")
            print("Quando terminar, digite 'sair'.")
            while True:
                msg = input("> ")
                if msg.lower() == "sair":
                    break
                f.write(f"{msg}\n")
            print(f"✅ Registro salvo no arquivo '{nome}'!")

        sair = input("Deseja registrar em outro arquivo? (s/n): ").lower()
        if sair != 's':
            break


if __name__ == "__main__":
    menu_registro()