import tkinter as tk
import os
import threading
from bot import enviar_mensagens, parar_envio

PASTA = r"C:\whatsapp-bot\Grupos.txt"
PASTA_IMAGENS = r"C:\whatsapp-bot"

janela = tk.Tk()
janela.title("Bot WhatsApp")
janela.geometry("400x300")
janela.resizable(False,False)

status = tk.StringVar(value="Status de Envio: Parado")

def envio():
    try:
        enviar_mensagens()
    finally:
        janela.after(0, finalizado)

def iniciar():
    status.set("Enviando...")
    janela.update_idletasks()

    threading.Thread(
        target=envio,
        daemon=True
    ).start()
    

def parar():
    status.set("Status de Envio: Parado")
    threading.Thread(
        target=parar_envio,
        daemon=True
    ).start()

def finalizado():
    status.set("Enviado com sucesso")
    
    janela.deiconify()
    janela.lift()
    janela.focus_force()

def abrir_pasta():
    os.startfile(PASTA)

def abrir_pasta_imagens():
    os.startfile(PASTA_IMAGENS)

tk.Button(
    janela,
    text="Abrir Arquivo",
    command=abrir_pasta
).pack(pady=10)

tk.Button(
    janela,
    text="Abrir pasta dos arquivos",
    command=abrir_pasta_imagens
).pack(pady=10)

# Botões -------------------------
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=30)

tk.Button(
    frame_botoes,
    text="Iniciar Envio",
    bg="green",
    fg="white",
    width=15,
    command=iniciar    
).pack(side="left", padx=10)

tk.Button(
    frame_botoes,
    text="Parar Envio",
    bg="red",
    fg="white",
    width=15,
    command=parar
).pack(side="left", padx=10)

#----------------------------------

tk.Label(
    janela,
    textvariable=status,
    font=("Arial", 12)
).pack(pady=10)

janela.mainloop()
