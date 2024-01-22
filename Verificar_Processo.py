import wmi
import subprocess


f = wmi.WMI()


processo_desejado = "RiotClientUx.exe"


processo_aberto = False
for processo in f.Win32_Process():
    if processo.Name == processo_desejado:
        processo_aberto = True
        break

if processo_aberto:
    print("O processo está aberto.")
else:
    resposta = input("O Aplicativo RiotGames não está aberto, você deseja abrir? [S/N]").upper()
    if resposta == "S":
        subprocess.run(["C:\Riot Games\Riot Client\RiotClientServices.exe"])
    else:
        print("Você optou por não abrir o aplicativo RiotGames.")
