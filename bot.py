import pyperclip
import pyautogui as py
import time
import random

rodando = True

def parar_envio():
    global rodando
    rodando = False

def carregar_grupos(arquivo="grupos.txt"):
    with open(arquivo, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]

def pausa_interrompivel(segundos):
    for _ in range(segundos):
        if not rodando:
            return False
        time.sleep(1)
    return True

def enviar_mensagens():
    global rodando
    rodando = True

    print("Enviando mensagens")
    py.PAUSE = 1

    linhas = [
        "✨ Lustre Pendente em Madeira ✨",
        "Peça artesanal em madeira tratada, com iluminação aconchegante e estilo rústico/industrial.",
        "Ideal para varandas, salas, cozinhas e áreas gourmet.",
        "Produto feito à mão, acabamento de qualidade e fácil instalação.",
        "🌿 Iluminação que transforma o ambiente."
    ]

    imagens = r'"C:\Python2\assets\img1.jpeg" "C:\Python2\assets\img2.jpeg" "C:\Python2\assets\img3.jpeg"'

    grupos = carregar_grupos()
  
    for nome_grupo in grupos:
        if not rodando:
            print("Envio interrompido pelo usuário")
            break

        try:
            print("Enviando:", nome_grupo)
            #Clica na área de pesquisa 
            py.click(187, 166)
            pausa_interrompivel(1)

            #Limpa a barra de pesquisa
            py.hotkey("ctrl", "a")
            py.press("backspace")

            #Busca o nome do grupo
            pyperclip.copy(nome_grupo)
            py.hotkey("ctrl", "v")
            pausa_interrompivel(1)

            #Entra no grupo
            py.press("enter")
            pausa_interrompivel(3)           

            posicao1 = py.locateCenterOnScreen('botao1.png')
            pausa_interrompivel(5)   

             #Clica no icone Anexar
            if posicao1:                
                print("Imagem encontrada:", posicao1)
                py.click(posicao1[0], posicao1[1])
            else:
                print("Imagem não encontrada")
            pausa_interrompivel(2)           
           
            posicao2 = py.locateCenterOnScreen('botao2.png')
            pausa_interrompivel(5) 
            
            #Clica no icone ducumentos            
            if posicao2:
                print("Imagem encontrada:", posicao2)
                py.click(posicao2[0], posicao2[1])
            else:
                print("Imagem não encontrada, clicando pela posição")
                py.click(611, 492)
            pausa_interrompivel(2)  

        
            pyperclip.copy(imagens)
            py.hotkey("ctrl", "v")
            pausa_interrompivel(2)
            py.press("enter")
            pausa_interrompivel(4)

            for linha in linhas:
                if not rodando:
                    break
                pyperclip.copy(linha)
                py.hotkey("ctrl", "v")
                py.hotkey("shift", "enter")

            py.press("enter")

            print(f"Mensagem enviada para: {nome_grupo}")
            print("--------------------------------")


            pausa_interrompivel(random.randint(15, 20))

        except Exception as e:
            print(f"Erro no grupo {nome_grupo}: {e}")
            continue

    print("Finalizado envio")
