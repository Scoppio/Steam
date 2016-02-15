from infos_partidas import infos_partidas
import time
import pandas as pd
from tqdm import tqdm 
from threading import Thread

def coleta_historica(ids, coleta, j):

    dados = pd.DataFrame()
    for i in tqdm(ids):
        dados = dados.append( coleta.info_partida(i), ignore_index=True )
        print(" Salvando dados do "+ str(j) + "o Thread")
        dados.to_csv("/home/teo/GRANDE" + str(j) + ".csv")
    
obj = infos_partidas(input(" Entre com a chave: "))

ids = [ i for i in range(2142996589, 2154193222+1) ]
intervalo_inf = 0
intervalo_sup = int( ( max(ids) - min(ids) ) / 6 )
for j in range(6):
    t = Thread( target=coleta_historica , args= ( ids[intervalo_inf:intervalo_sup], obj, j, ) )
    t.start()
    intervalo_inf = intervalo_sup
    intervalo_sup += intervalo_sup


