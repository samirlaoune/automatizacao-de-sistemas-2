# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer Login
# Passo 3: Pegar/Importar a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time 
import pandas as pd

pyautogui.PAUSE = 1

# Passo 1 - Entrar no sistema

# abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer Login

pyautogui.click(x=859, y=561)
pyautogui.write("empresa@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.click(x=957, y=806)

time.sleep(3)


# Passo 3 - Importar a base de dados

tabela = pd.read_csv("produtos.csv")
print(tabela)


# Passo 4 - Cadastrar um produto

# para cada linha da minha tabela:
for linha in tabela.index:
    # código
    pyautogui.doubleClick(x=594, y=385)
    
    codigo = str(tabela.loc[linha, "codigo"]) # string = texto
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    # clicar no botao de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    time.sleep(1)

    pyautogui.scroll(5000)





# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - combinação de teclas
# pyautogui.scroll - rolar a tela para cima ou para baixo