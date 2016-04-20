import pandas as pd
from naiveBayes import naiveBayes
from menus import faz_colunas_herois
from menus import faz_colunas_infos
#### TESTE ####

colunas_herois = faz_colunas_herois()
colunas_infos = faz_colunas_infos( colunas_herois , ["xp_per_min", "gold_per_min"])

path = "/home/teo/Documentos/Meus Documentos/Steam/DADOS_RASPI/dados_dota/dota_raspi25_6.csv"
BASE = pd.DataFrame.from_csv( path )

print(BASE.head())

