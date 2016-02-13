import pandas as pd
import numpy as np
import scipy.stats as ss

class naiveBayes():

	def __init__(self, dados):
		self.dados = dados
		self.colunas = colunas
		self.resposta = resposta

	def estimar(self, colunas, resposta):

		estimativa = {"medias":pd.DataFrame(columns = self.colunas) , "variancia" :pd.DataFrame(columns = self.colunas) }

		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas].mean(), ignore_index=True)
		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas][dados[self.resposta]==1].mean(), ignore_index=True)
		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas][dados[self.resposta]==0].mean(), ignore_index=True)
		estimativa["medias"].index = ["geral", 0, 1]

		estimativa["variancia"] = estimativa["variancia"].append(dados[self.colunas].var(), ignore_index=True)
		estimativa["variancia"] = estimativa["variancia"].append(dados[self.colunas][dados[self.resposta]==1].var(), ignore_index=True)
		estimativa["variancia"] = estimativa["variancia"].append(dados[self.colunas][dados[self.resposta]==0].var(), ignore_index=True)
		estimativa["variancia"].index = ["geral", 0, 1]
		
		return estimativa

	def distr_bernnouli(self, colunas, resposta):

		estimacao_bernnouli = estimar(colunas, resposta)

	def predicao(self, novo_dado):


### EXEMPLO ###
path = "/home/teo/Documentos/Meus Documentos/Steam/DADOS_RASPI/dados_dota/dota_raspi12.csv"

dados = pd.DataFrame.from_csv(path)

NB = naiveBayes(dados, colunas=["RH_1" , "DH_1"], resposta="radiant_win")
print(NB.estimar()["medias"])