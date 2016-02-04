#! /usr/bin/python

from infos_partidas import infos_partidas
import pandas as pd
import time
from funcoes import dormindo
from tqdm import tqdm

def coleta_recursiva(chave, endereco = False, tempo=0, nlinhas=10000):

    minha_coleta = infos_partidas(chave)
    dados = pd.DataFrame(columns = minha_coleta.colunas)

    print("\n Iniciando coleta recursiva...")
    i = 1
    j = 1
    while True:
        print("\n Iniciando "+ str(i) + " coleta.")
        dados = dados.append( minha_coleta.faz_coleta(ids=minha_coleta.pega_ids()) )
        dados = dados.drop_duplicates()

        if dados.shape[0] > nlinhas:
            end_salvar = endereco[:-4] + "_" + str(j) +".csv"
            print("Os dados estão sendo salvos no arquivo:" + end_salvar)
            dados.to_csv(end_salvar)
            del dados
            dados = pd.DataFrame(columns=minha_coleta.colunas)
            j+=1

        dormindo(tempo, i)
        i+=1

    return None

#### CHAVE DA STEAM PARA ACESSO ####
chave = input(" Entre com a chave do desenvolvedor: ")
tempo = int(input("\n Defina um intervalo de tempo para coleta (em segundos): "))
nlinhas = int(input("\n Entre com o número maximo de linahs: "))
salvar = input("\n Deseja salvar a base de dados?[S/n]: ").upper()


endereco=False
if salvar == "S":
    endereco = input("\n Entre com o endereco para salvar a base de dados: ")
    if "csv" not in endereco:
        endereco= endereco + ".csv"

coleta_recursiva(chave = chave, endereco = endereco, tempo = tempo, nlinhas=nlinhas)



