import pandas as pd
import numpy as np
import math

class naiveBayes():

	def __init__(self):
		print("None")


	def fdpBernoulli(self, x ,p):

		fdp = ( p**x ) *( (1-p) ** (1-x) )
		return fdp

	def fdpNormal(self, x, media, variancia):

		fdp = ( 1 / math.sqrt( 2 * math.pi * variancia ) ) * ( math.e ** ( (-1/2) * ( (x - media) ** 2 ) / variancia 	) )
		return fdp

	def estimar_media(self, X, Y):

		estimativa = pd.DataFrame(columns = X)
		estimativa = estimativa.append(X.mean(), ignore_index=True)
		estimativa = estimativa.append(X[Y==1].mean(), ignore_index=True)
		estimativa = estimativa.append(X[Y==0].mean(), ignore_index=True)
		estimativa.index = ["geral", 0, 1]
		return estimativa

	def estimar_variancia( self, X, Y):

		estimativa = pd.DataFrame(columns = X)
		estimativa = estimativaa.ppend(X.var(), ignore_index=True)
		estimativa = estimativa.append(X[Y==1].var(), ignore_index=True)
		estimativa = estimativa.append(X[Y==0].var(), ignore_index=True)
		estimativa.index = ["geral", 0, 1]
		return estimativa

	def ajuste(self, dados, X_B, X_N, Y):

		medias = estimar_media( dados[X_B + X_N] )
		variancias = estimar_variancia( dados[ X_N ] )

		self.parametros = { "Media":medias  , "Variancia": variancias}
		return None

	def predicao(self, X_B , X_N):

		return None


### EXEMPLO ###
'''
path = "/home/teo/Documentos/Meus Documentos/Steam/DADOS_RASPI/dados_dota/dota_raspi12.csv"

dados = pd.DataFrame.from_csv(path)

NB = naiveBayes(dados, colunas=["RH_1" , "DH_1"], resposta="radiant_win")
'''