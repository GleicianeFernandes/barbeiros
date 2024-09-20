from xmlrpc.server import SimpleXMLRPCServer
from threading import Lock
import time

class Barbeiro:
    def __init__(self):
        self.lock = Lock() #pra q apenas um cliente use o barbeiro por vez

    def ctCabelo(self):
        with self.lock: 
            print("Barbeiro: Cortando cabelo...")
            time.sleep(3)  
            print("Barbeiro: Cabelo cortado!")
            return "Cabelo cortado!"

    def ctBarba(self):
        with self.lock:
            print("Barbeiro: Cortando barba...")
            time.sleep(4) 
            print("Barbeiro: Barba cortada!")
            return "Barba cortado!"

    def ctBigode(self):
        with self.lock:
            print("Barbeiro: Cortando bigode...")
            time.sleep(5)  
            print("Barbeiro: Bigode cortado!")
            return "Bigode cortad!"

def startServ():
    serv = SimpleXMLRPCServer(("localhost", 8000))
    barbeiro = Barbeiro() 

    serv.register_instance(barbeiro) #registrando o barbeiro no servidor p/ q os clientes possam usar os métodos
    
    print("Servidor Barbeiro ativo, aguardando clientes...")
    serv.serve_forever()  

if __name__ == "__main__":
    startServ()
