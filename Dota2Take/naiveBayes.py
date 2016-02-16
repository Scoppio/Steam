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

	def estimar(self, X, Y, estat):

		classes = Y.unique()
		classes.sort()
		estimativa = pd.DataFrame(columns = X)

		if estat == "media":
			estimativa = estimativa.append(X.mean(), ignore_index=True)
			for c in classes:
				estimativa = estimativa.append(X[Y==c].mean(), ignore_index=True)
			estimativa.index = ["geral"] + list(classes)
			return estimativa

		elif estat == "variancia":
			estimativa = estimativa.append(X.var(), ignore_index=True)
			for c in classes:
				estimativa = estimativa.append(X[Y==c].var(), ignore_index=True)
			estimativa.index = ["geral"] + list(classes)
			return estimativa

	def faz_X_N( linha ):
		
		hero_1 = list( linha[linha == 1].index )
		if 'modo_jogo' in hero_1:
			hero_1.remove('modo_jogo')
		X_N = []
		for h in hero_1:
			X_N.append( h + "_xp_per_min" )
			X_N.append( h + "_gold_per_min" )

		return linha[X_N]


	def ajuste(self, dados, X_B, X_N, Y):

		medias = estimar( dados[X_B + X_N], Y, "media" )
		variancias = estimar( dados[ X_N ], Y, "variancia" )

		self.parametros = { "Media":medias  , "Variancia": variancias}
		return None

	def predicao(self, X_B , X_N):

		return None
