from datetime import datetime

class Relogio:
    def __init__(self, hora=None, minuto=None):
        if hora is None or minuto is None:
            agora = datetime.now()
            hora = agora.hour
            minuto = agora.minute

        if not (0 <= hora < 24):
            raise ValueError("Hora deve estar entre 0 e 23.")
        if not (0 <= minuto < 60):
            raise ValueError("Minuto deve estar entre 0 e 59.")
        
        self.hora = hora
        self.minuto = minuto

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"

if __name__ == "__main__":
    relogio = Relogio()
    print("Hora atual:", relogio)
