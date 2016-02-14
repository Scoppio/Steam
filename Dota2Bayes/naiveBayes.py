import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import bernoulli
import math

class naiveBayes():

	def __init__(self, dados):
		self.dados = dados
		self.colunas = colunas
		self.resposta = resposta

	def fdp_bernoulli(x ,p):

		fdp = ( p**x ) *( (1-p) ** (1-x) )

		return fdp

	def fdp_normal(x, media, variancia):

		fdp = ( 1 / math.sqrt( 2 * math.pi * variancia ) ) * ( math.e ** ( (-1/2) * ( (x - media) ** 2 ) / variancia 	) )
		
		return fdp

	def estimar_media(self, colunas, resposta):

		estimativa = {"medias":pd.DataFrame(columns = self.colunas) , "variancia" :pd.DataFrame(columns = self.colunas) }

		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas].mean(), ignore_index=True)
		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas][dados[self.resposta]==1].mean(), ignore_index=True)
		estimativa["medias"] = estimativa["medias"].append(dados[self.colunas][dados[self.resposta]==0].mean(), ignore_index=True)
		estimativa["medias"].index = ["geral", 0, 1]
	 
	 	return estimativa

	 def estimar_variancia( self, colunas, resposta):

		estimativa["variancia"] = estimativa["variancia"].append(dados[self.colunas].var(), ignore_index=True)
		estimativa["variancia"] = estimativa["variancia"].append(dados[self.colunas][dados[self.resposta]==1].var(), ignore_index=True)
		estimativa["variancia"] = estimativa["variancia"].append(dados[self.colunas][dados[self.resposta]==0].var(), ignore_index=True)
		estimativa["variancia"].index = ["geral", 0, 1]
		
		return estimativa

	def NBB(self, colunas, resposta):

		estimativa = estimar(colunas, resposta)

		distribuicao_geral = { i: bernoulli( estimativa["medias"][i]["geral"] ) for i in colunas }
		distribuicao_1 = { i: bernoulli( estimativa["medias"][i][1] ) for i in colunas }
		distribuicao_0 = { i: bernoulli( estimativa["medias"][i][0] ) for i in colunas }

		ajuste = { "geral": distribuicao_geral , 1: distribuicao_1, 0:distribuicao_0 }

		return ajuste

	def NBN(self, colunas, resposta):

		estimativa = estimar(colunas, resposta)

		return 

	def predicao(self, novo_dado):


### EXEMPLO ###
path = "/home/teo/Documentos/Meus Documentos/Steam/DADOS_RASPI/dados_dota/dota_raspi12.csv"

dados = pd.DataFrame.from_csv(path)

NB = naiveBayes(dados, colunas=["RH_1" , "DH_1"], resposta="radiant_win")
