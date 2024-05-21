from pyautogui import click
from time import sleep as sp
import pyautogui
import wmi
import subprocess
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# Requisições
login = "login.png"
senha = "senha.png"
entrar = "entrar.png"
abrir_lol = "abrir_lol.png"
jogar = "jogar.png"
f = wmi.WMI()
flag = 0
processo_desejado = "RiotClientUx.exe"
processo_aberto = False
now = datetime.now()
data = now.date()
hora = now.time()
hora_formatada = hora.strftime("%H:%M:%S")

# =======FUNÇÕES========
def clicklogin():
    clicar1 = pyautogui.locateCenterOnScreen(login)
    click(clicar1)
def clicksenha():
    clicar2 = pyautogui.locateCenterOnScreen(senha)
    click(clicar2)
def clickentrar():
    clicar3 = pyautogui.locateCenterOnScreen(entrar)
    click(clicar3)
def abrirlol():
    clicar4 = pyautogui.locateCenterOnScreen(abrir_lol)
    click(clicar4)
def clickjogar():
    clicar5 = pyautogui.locateCenterOnScreen(jogar)
    click(clicar5)
def print_temporary_message(message, duration=2):
    print(message, end='', flush=True)
    sp(duration)
    print('\r' + ' ' * len(message) + '\r', end='', flush=True)
def elo(elo_conta1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    elo1 = elo_conta1
    requisicao = requests.get(elo1, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    busca = site.find("div", class_="tier")
    if busca:
        return busca.text
    else:
        return "Unranked"
def nivel(lvl_conta1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    conta1 = lvl_conta1
    requisicao = requests.get(conta1, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    busca = site.find("span", class_="level")
    if busca:
        return busca.text
    else:
        return None

for processo in f.Win32_Process():
    if processo_desejado.lower() in processo.Name.lower():
        processo_aberto = True
        break

if not processo_aberto:
    print_temporary_message(f"O Serviço {processo_desejado} não está aberto, iniciando...")
    sp(0.8)
    subprocess.run(["C:\\Riot Games\\Riot Client\\RiotClientServices.exe"])
else:
    print_temporary_message(f"O Serviço {processo_desejado} está aberto.")

sp(1)
print_temporary_message("CARREGANDO A LISTA DE CONTAS ATUALIZADA...", duration=2)
# Estrutura de escolha das contas
mane = 'https://www.op.gg/summoners/br/Man%C3%A9%20Galinha%20157-157'
vulgo = 'https://www.op.gg/summoners/br/vulgo%20trash-BR1'
lottus = 'https://www.op.gg/summoners/br/LottusKiller07-BR1'
print(f'''Lista de contas:
   [1] Mané Galinha 157 | Nível: {nivel(mane)} | Elo: {elo(mane).capitalize()}
   [2] Vulgo Trash | Nível: {nivel(vulgo)} | Elo: {elo(vulgo).capitalize()}
   [3] Lottus Killer07 | Nível: {nivel(lottus)} | Elo: {elo(lottus).capitalize()}
   
                                                  ATUALIZADO EM : {data} / {hora_formatada}

''')
resp = int(input("Selecione a conta: "))
while True:
    if resp == 1:
        clicklogin()
        sp(0.4)
        pyautogui.write("conta1")
        sp(0.4)
        clicksenha()
        sp(0.4)
        pyautogui.write("senha1*")
        clickentrar()
        sp(7)
        abrirlol()
        sp(1)
        click(x=217, y=273)
        break
    if resp == 2:
        clicklogin()
        sp(0.4)
        pyautogui.write("conta2")
        sp(0.4)
        clicksenha()
        sp(0.4)
        pyautogui.write("senha2")
        clickentrar()
        sp(7)
        abrirlol()
        sp(1)
        click(x=217, y=273)
        break
    if resp == 3:
        clicklogin()
        sp(0.4)
        pyautogui.write("conta3")
        sp(0.4)
        clicksenha()
        sp(0.4)
        pyautogui.write("senha3")
        clickentrar()
        sp(7)
        abrirlol()
        sp(1)
        click(x=217, y=273)
        break

