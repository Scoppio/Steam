import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import bernoulli
import math

class naiveBayes():

	def __init__(self):
		print("None")


	def fdp_bernoulli(self, x ,p):

		fdp = ( p**x ) *( (1-p) ** (1-x) )

		return fdp

	def fdp_normal(self, x, media, variancia):

		fdp = ( 1 / math.sqrt( 2 * math.pi * variancia ) ) * ( math.e ** ( (-1/2) * ( (x - media) ** 2 ) / variancia 	) )
		
		return fdp

	def estimar_media(self, colunas, resposta):

		estimativa = pd.DataFrame(columns = colunas)
		estimativa = estimativa.append(dados[colunas].mean(), ignore_index=True)
		estimativa = estimativa.append(dados[colunas][dados[resposta]==1].mean(), ignore_index=True)
		estimativa = estimativa.append(dados[colunas][dados[resposta]==0].mean(), ignore_index=True)
		estimativa.index = ["geral", 0, 1]
		return estimativa

	def estimar_variancia( self, colunas, resposta):

		estimativa = pd.DataFrame(columns = colunas)
		estimativa = estimativaa.ppend(dados[colunas].var(), ignore_index=True)
		estimativa = estimativa.append(dados[colunas][dados[resposta]==1].var(), ignore_index=True)
		estimativa = estimativa.append(dados[colunas][dados[resposta]==0].var(), ignore_index=True)
		estimativa.index = ["geral", 0, 1]
		return estimativa

	def ajuste(self, dados, X, Y):

		return None

	def NBB(self, colunas, resposta):

		estimativa = estimar(colunas, resposta)

		distribuicao_geral = { i: bernoulli( estimativa["medias"][i]["geral"] ) for i in colunas }
		distribuicao_1 = { i: bernoulli( estimativa["medias"][i][1] ) for i in colunas }
		distribuicao_0 = { i: bernoulli( estimativa["medias"][i][0] ) for i in colunas }

		ajuste = { "geral": distribuicao_geral , 1: distribuicao_1, 0:distribuicao_0 }

		return ajuste

	def NBN(self, colunas, resposta):

		estimativa = estimar(colunas, resposta)

		return None

	def predicao(self, novo_dado):

		return None


### EXEMPLO ###
'''
path = "/home/teo/Documentos/Meus Documentos/Steam/DADOS_RASPI/dados_dota/dota_raspi12.csv"

dados = pd.DataFrame.from_csv(path)

NB = naiveBayes(dados, colunas=["RH_1" , "DH_1"], resposta="radiant_win")
'''