import tkinter as tk
import ping3
import socket

def pingar_servidor(ip, porta):
    # Ping para o IP
    resposta_ping = ping3.ping(ip)
    
    # Verificar a conexão na porta
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(porta)))
        conexao = True
    except Exception as e:
        conexao = False
    finally:
        s.close()
    
    return resposta_ping, conexao

def get_input(): 
    ip_servidor = entry_ip.get()
    porta = entry_porta.get()
    
    resposta_ping, conexao = pingar_servidor(ip_servidor, porta)
    
    if resposta_ping is not None and conexao:
        resultado = "Servidor online. Tempo de ping: {:.2f} ms".format(resposta_ping * 1000)
    else:
        resultado = "Servidor offline ou porta fechada."
    
    resultado_label.config(text=resultado)

# Criação de tela 

janela = tk.Tk()
janela.title("PING")
# Configurações da janela
janela.geometry("380x250")

texto_top = tk.Label(janela, text="Verificador de Servidor")
texto_top.grid(row=0, column=1)

texto_orientacao = tk.Label(janela, text="IP do servidor:")
texto_orientacao.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="e") 

texto_orientacao2 = tk.Label(janela, text="Porta:")
texto_orientacao2.grid(row=2, column=0, padx=(10, 5), pady=10, sticky="e") 

# Criar campos de entrada para IP e porta
entry_ip = tk.Entry(janela, width=30)
entry_ip.grid(row=1, column=1, padx=0, pady=5)

entry_porta = tk.Entry(janela, width=10)
entry_porta.grid(row=2, column=1, padx=(0, 5), pady=5, sticky="w")  # Adicionando espaço apenas à direita da entrada da porta

# Criar um botão para obter o texto digitado
button = tk.Button(janela, text="Pingar Servidor", command=get_input)
button.grid(row=3, column=1, padx=10, pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.grid(row=4, column=0, columnspan=2)

janela.mainloop() # Manter a janela aberta 
