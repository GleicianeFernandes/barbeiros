from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread, Lock
import time

class Barbeiro:
    def __init__(self):
        self.lock = Lock()

    def realizarCorte(self, tipo_corte):
        with self.lock:
            if tipo_corte == "cabelo":
                print("Cortando cabelo...")
                time.sleep(3)
                print("Cabelo cortado!")
                return "Cabelo cortado com sucesso!"
            elif tipo_corte == "barba":
                print("Cortando barba...")
                time.sleep(4)
                print("Barba cortada!")
                return "Barba cortada com sucesso!"
            elif tipo_corte == "bigode":
                print("Cortando bigode...")
                time.sleep(5)
                print("Bigode cortado!")
                return "Bigode cortado com sucesso!"
            else:
                return "Serviço não disponível."

def startServidor():
    servidor = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
    barbeiro = Barbeiro()
    
    servidor.register_function(barbeiro.realizarCorte, "realizarCorte")
    
    print("Servidor ativo, aguardando clientes...")
    
    for i in range(5):
        thread = Thread(target=servidor.serve_forever)
        thread.start()
        print(f"Thread {i+1} iniciada para atender um cliente.")

if __name__ == "__main__":
    startServidor()
