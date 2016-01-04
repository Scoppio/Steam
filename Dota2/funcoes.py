import os
import time

def dormindo(tempo, i):
    for t in range(tempo):
        minutos = int( (tempo - t) / 60 )
        segundos = (tempo - t) % 60
        os.system("clear")
        print("\n " + str(i) + "a Coleta realizada e salva com sucesso!!\n")
        print("\n A próxima coletá será em : "+str(minutos)+ " minutos e " + str(segundos) + " segundos" )
        time.sleep(1)
    os.system("clear")
    return None
