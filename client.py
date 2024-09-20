import xmlrpc.client
from threading import Thread

def usar_servicos(cliente_id):
    servidor = xmlrpc.client.ServerProxy("http://localhost:8000/") #conectando ao server q está rodando na porta 8000
    
    # Cada cliente realiza 20 ciclos de corte
    for ciclo in range(20):
        print(f"Cliente {cliente_id}: Iniciando ciclo {ciclo + 1}...")
        
        print(f"Cliente {cliente_id}: {servidor.ctCabelo()}")
        
        print(f"Cliente {cliente_id}: {servidor.ctBarba()}")
        
        print(f"Cliente {cliente_id}: {servidor.ctBigode()}")
        
        print(f"Cliente {cliente_id}: Ciclo {ciclo + 1} concluído!\n")

if __name__ == "__main__":
    threads = []  #lista q armazena as threads dos cliente
    
    for i in range(5):
        thread = Thread(target=usar_servicos, args=(i+1,))
        threads.append(thread)
        thread.start() #depois q é iniciado, o cliente começa a competir pelo barbeiro
        
    for thread in threads:
        thread.join()
