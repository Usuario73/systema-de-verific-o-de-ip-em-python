import ipaddress
import socket
import struct
import tkinter as tk

class VerificadorIP:
    def __init__(self, master):
        self.master = master
        master.title("Verificador de IP")
        master.minsize(300, 150)  # Definir tamanho mínimo para a janela
        master.geometry("400x200")  # Definir tamanho padrão para a janela
        
        # Criação dos widgets
        self.label_ip = tk.Label(master, text="Insira o endereço IP:")
        self.label_ip.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_ip = tk.Entry(master, width=20)
        self.entry_ip.grid(row=0, column=1, padx=10, pady=10)
        
        self.botao_verificar = tk.Button(master, text="Verificar", command=self.verificar)
        self.botao_verificar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.ip_history = []
    
    def verificar(self):
        ip = self.entry_ip.get()
        
        try:
            # Verifica se o IP é válido
            ipaddress.ip_address(ip)

            # Verifica a classe do IP
            if ipaddress.ip_address(ip).is_private:
                classe = "Privado"
            elif ipaddress.ip_address(ip).is_reserved:
                classe = "Reservado"
            elif ipaddress.ip_address(ip).is_global:
                # Verifica a classe do IP (A, B ou C)
                ip_bin = bin(struct.unpack('!I', socket.inet_aton(ip))[0])[2:].zfill(32)
                if ip_bin[0] == '0':
                    classe = "Classe A"
                elif ip_bin[1] == '0':
                    classe = "Classe B"
                else:
                    classe = "Classe C"
            else:
                classe = "Desconhecido"

            # Verifica a máscara de sub-rede
            rede = ipaddress.ip_network(ip, strict=False)
            mk = rede.netmask

            # Verifica o endereço de broadcast
            bc = str(rede.broadcast_address)

            resultado = f"A classe do IP {ip} é {classe}.\nA máscara de sub-rede é {mk}.\nO endereço de broadcast é {bc}."
                
        except ValueError:
            resultado = f"O IP {ip} é inválido."
        
        self.ip_history.append(ip) # Adiciona o IP à lista de histórico

        # Exibe o resultado na interface
        self.label_resultado.config(text=resultado)

    def mostrar_historico(self):
        historico = "Histórico de IPs:\n\n"
        for ip in self.ip_history:
            historico += ip + "\n"
        self.label_resultado.config(text=historico)

# Cria a janela principal
root = tk.Tk()

# Cria o verificador de IP
verificador = VerificadorIP(root)

# Cria o botão para mostrar o histórico
botao_historico = tk.Button(root, text="Mostrar histórico", command=verificador.mostrar_historico)
botao_historico.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



root.tk()
