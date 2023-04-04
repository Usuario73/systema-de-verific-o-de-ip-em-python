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
                classe = "Público"
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

        # Exibe o resultado na interface
        self.label_resultado.config(text=resultado)

# Cria a janela principal
root = tk.Tk()

# Cria o verificador de IP
verificador = VerificadorIP(root)

# Inicia o loop da interface gráfica
root.mainloop()
