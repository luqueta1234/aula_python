import time
def obter_hora_atual():
    # Retorna a hora atual no formato HH:MM:SS.
    hora_atual = time.localtime()
    return time.strftime("%H:%M:%S", hora_atual)

def exibir_relogio():
    # Exibe a hora atual no console a cada segundo.
    try:
        while True:
            hora = obter_hora_atual()
            print(hora, end="\r") # \r retorna o cursor para o início
            time.sleep(1) # Pausa por 1 segundo
    except KeyboardInterrupt:
        print("\/Relógio encerrado.")


# Inicia o relógio
exibir_relogio()