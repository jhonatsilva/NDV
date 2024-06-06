from banco import app as banco_app
from seletor import app as seletor_app
from validador import app as validador_app
import threading

def run_banco():
    banco_app.run(port=5001)

def run_seletor():
    seletor_app.run(port=5002)

def run_validador():
    validador_app.run(port=5003)

if __name__ == '__main__':
    banco_thread = threading.Thread(target=run_banco)
    seletor_thread = threading.Thread(target=run_seletor)
    validador_thread = threading.Thread(target=run_validador)

    banco_thread.start()
    seletor_thread.start()
    validador_thread.start()

    banco_thread.join()
    seletor_thread.join()
    validador_thread.join()
