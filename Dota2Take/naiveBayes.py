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

	def estimar(self, X,Y, estat):

		estimativa = pd.DataFrame()

		if estat == "media":
			estimativa = estimativa.append(X.mean(), ignore_index=True)

			for c in self.classe:
				estimativa = estimativa.append(X[Y==c].mean(), ignore_index=True)

			estimativa.index = ["geral"] + self.classe
			return estimativa

		elif estat == "variancia":
			estimativa = estimativa.append(X.var(), ignore_index=True)
			
			for c in self.classe:
				estimativa = estimativa.append(X[Y==c].var(), ignore_index=True)
			
			estimativa.index = ["geral"] + self.classe
			return estimativa

	def faz_X_N(self, linha ):

		hero_1 = list( linha[linha == 1].index )
		if 'modo_jogo' in hero_1:
			hero_1.remove('modo_jogo')
		X_N = []
		for h in hero_1:
			X_N.append( h + "_xp_per_min" )
			X_N.append( h + "_gold_per_min" )

		return linha[X_N]

	def calc_prob_Bernoulli(self, classe, X):

		prob = [ fdpBernoulli(X[i] , self.parametros["Media"][i][classe] ) for i in x.index]
		prob = np.array(prob)
		prob = prob.prod()
		return prob

	def calc_prob_Normal( self, classe, X):
		prob = [ fdpNormal(X[i] , self.parametros["Media"][i][classe], self.parametros["Variancia"][i] ) for i in x.index]
		prob = np.array(prob)
		prob = prob.prod()
		return prob

	def calc_prob(self, X_B, X_N):

		prob_X_B = { c: calc_prob_Bernoulli( c, X_B) for c in self.classe }
		prob_X_N = { c: calc_prob_Bernoulli( c, X_N) for c in self.classe }

	def ajuste(self, dados, X_B, X_N, Y):

		self.classe = list(set(dados[Y]))

		medias = self.estimar( dados[X_B + X_N], dados[Y], "media" )
		variancias = self.estimar( dados[ X_N ], dados[Y], "variancia" )

		self.parametros = { "Media":medias  , "Variancia": variancias}
		return None

	def predicao(self, X_B , X_N):

		return None
