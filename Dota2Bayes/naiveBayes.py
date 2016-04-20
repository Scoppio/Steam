import pandas as pd
import numpy as np
import math

class naiveBayes():

	def __init__(self):
		print("None")

	def fdpBernoulli(self, x ,p):

		fdp = ( p ** x ) * ( (1-p) ** (1-x) )
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

	def ajuste(self, X_B, X_N, Y):

		self.classe = list(set(Y))
		X = X_B.append(X_N)

		medias = self.estimar( X, Y, "media" )
		variancias = self.estimar( X_N, Y, "variancia" )

		self.parametros = { "Media":medias  , "Variancia": variancias}
		return None

	def predicao(self, X_B , X_N):

		return None
