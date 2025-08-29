import time

class RegistroProcesso:
    def __init__(self, arquivo, nome_processo):
        self.arquivo = arquivo
        self.nome_processo = nome_processo

    def __enter__(self):
        self.f = open(self.arquivo, 'a')
        self.inicio = time.time()
        self.f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Começo do processo: {self.nome_processo}\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duracao = time.time() - self.inicio
        self.f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Fim do processo: {self.nome_processo}. Duração: {duracao:.2f} segundos\n")
        self.f.close()

# Exemplo de uso real:

if __name__ == "__main__":
    with RegistroProcesso("processos.log", "Backup Diário") as processo:
        # Simulando tarefa demorada
        time.sleep(3)
        print("Executando backup...")

    with RegistroProcesso("processos.log", "Envio de Relatórios") as processo:
        time.sleep(2)
        print("Enviando relatórios...")