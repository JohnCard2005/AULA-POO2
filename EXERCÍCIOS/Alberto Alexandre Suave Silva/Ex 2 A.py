class Relogio:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"


def menu_relogio():
    while True:
        print("\n=== Relógio Interativo ===")
        try:
            h = int(input("Digite a hora (0-23): "))
            m = int(input("Digite os minutos (0-59): "))
            if not (0 <= h <= 23) or not (0 <= m <= 59):
                print("⚠️ Hora ou minuto inválido!")
                continue
            r = Relogio(h, m)
            print(f"🕒 Horário formatado: {r}")
        except Exception as e:
            print(f"⚠️ Erro: {e}")
        sair = input("Deseja testar outro horário? (s/n): ").lower()
        if sair != 's':
            break


if __name__ == "__main__":
    menu_relogio()