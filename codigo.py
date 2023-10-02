import pyautogui
import time
import pandas


pyautogui.PAUSE = 0.5



pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=675, y=363, clicks = 1)
pyautogui.write("teste@bol.com.br")
pyautogui.press("tab")
pyautogui.write("teste") #senha
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("esc")
pyautogui.click(x=735, y=249)


time.sleep(2)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
  pyautogui.click(x=735, y=249)
  codigo = tabela.loc[linha, "codigo"]
  marca = tabela.loc[linha, "marca"]
  tipo = tabela.loc[linha, "tipo"]
  categoria = tabela.loc[linha, "categoria"]
  preco = tabela.loc[linha, "preco_unitario"]
  custo = tabela.loc[linha, "custo"]


  pyautogui.write(str(codigo))
  pyautogui.press('tab')
  pyautogui.write(str(marca))
  pyautogui.press('tab')

  pyautogui.write(str(tipo))
  pyautogui.press('tab')
  pyautogui.write(str(categoria))
  pyautogui.press('tab')
  pyautogui.write(str(preco))
  pyautogui.press('tab')
  pyautogui.write(str(custo))
  pyautogui.press('tab')
  pyautogui.press('tab')

  pyautogui.press("enter")

  pyautogui.scroll(5000)


