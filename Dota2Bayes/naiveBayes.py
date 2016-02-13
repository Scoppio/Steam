import pandas as pd
import numpy as np
import scipy.stats as ss

class naiveBayes():

	def __init__(self, dados, colunas, resposta):
		self.dados = dados
		self.colunas = colunas
		self.resposta = resposta

	def estimar(self):
		estimativa = {"medias":pd.DataFrame(columns = self.colunas) , "variancia" :pd.DataFrame(columns = self.colunas) }

		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas].mean(), ignore_index=True)
		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas][dados[self.resposta]==1].mean(), ignore_index=True)
		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas][dados[self.resposta]==0].mean(), ignore_index=True)
		estimativa["medias"].index = ["geral", 0, 1]



		return estimativa


### EXEMPLO ###
path = "/home/teo/Documentos/Meus Documentos/Steam/DADOS_RASPI/dados_dota/dota_raspi12.csv"

dados = pd.DataFrame.from_csv(path)

NB = naiveBayes(dados, colunas=["RH_1" , "DH_1"], resposta="radiant_win")
print(NB.estimar()["medias"])