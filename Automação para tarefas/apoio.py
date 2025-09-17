from time import sleep
import pyautogui
import pandas

sleep(5)
# posição_mouse = pyautogui.position()
tabela = pandas.read_csv("tarefas_diarias.csv")

print(tabela)