import pyautogui
import time

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas (pyautogui.hotkey("win", "shift", "s"))

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=513, y=433)

# Digitar o site
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")

# Esperar 5 segundos
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=390, y=376)
pyautogui.write("l.pinheiro.w@gmail.com")
pyautogui.press("tab")
pyautogui.write("Senha1234")
pyautogui.click(x=680, y=535)

# Espera 5 segundos
time.sleep(3)

# Passo 3: Importar a base de dados
# pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv") # Ler e armazenar a base de dados

# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir para todos os produtos

for linha in tabela.index: # Para cada linha da tabela:

    pyautogui.click(x=388, y=256)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))

    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))

    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan" :
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")

    # pyautogui.scroll(8000)
    pyautogui.press("home")

# pyautogui -> fazer automações com python (pip install pyautogui)

