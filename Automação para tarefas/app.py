import pandas as pd  # Tratamento de dados
import pyautogui  # Automação de teclado e mouse
from time import sleep  # Controle de tempo

# Funções úteis do pyautogui:
# pyautogui.click() → Clica em uma posição
# pyautogui.scroll() → Rola a tela
# pyautogui.hotkey("ctrl", "c") → Atalhos de teclado
# pyautogui.position() → Posição atual do mouse
# pyautogui.moveTo(x, y) → Move o mouse
# pyautogui.press() → Pressiona tecla
# pyautogui.write() → Digita texto

# Passo 1: Alternar para o Chrome e clicar na posição desejada
pyautogui.hotkey("alt", "tab")
sleep(1)
pyautogui.moveTo(x=785, y=584)
pyautogui.click()
sleep(2)

# Passo 2: (opcional) Garantir que está na tela correta

# Passo 3: Importar arquivo CSV
try:
    tabela = pd.read_csv("tarefas_diarias.csv", sep=";")
except FileNotFoundError:
    print("Arquivo CSV não encontrado. Verifique o nome e o caminho.")
    exit()

# Passo 4: Laço para registrar cada tarefa
for linha in tabela.index:
    Tarefa = tabela.loc[linha, "Tarefa"].capitalize()
    pyautogui.press("tab")
    sleep(2)
    pyautogui.write(f"{Tarefa}")

    sleep(2)
    pyautogui.write(" ")
    Data = tabela.loc[linha, "Data"]
    pyautogui.write(f"{Data}")

    sleep(2)
    pyautogui.write(" ")
    Horario = tabela.loc[linha, "Hora"]
    pyautogui.write(f"{Horario}")

    # Passo 5: Registrar na To-do List

    pyautogui.press("enter")
    sleep(3)
