import xmlrpc.client

# Função que simula o cliente pedindo os serviços do barbeiro
def solicitar_servicos():
    servidor = xmlrpc.client.ServerProxy("http://localhost:8000/")
    
    for ciclo in range(20):  # Cada cliente repetirá 20 vezes o ciclo de corte
        print(f"Iniciando ciclo {ciclo + 1} do cliente...")
        print(servidor.cortarCabelo())
        print(servidor.cortarBarba())
        print(servidor.cortarBigode())
        print(f"Ciclo {ciclo + 1} concluído!\n")
        
if __name__ == "__main__":
    solicitar_servicos()
