#-*- coding: utf-8 -*-

from os import system
from termcolor import colored
import pandas as pd
from sklearn.naive_bayes import BernoulliNB


def print_dota2bayes(tamanho=60):

	print("#######    ########   ########     ####      #####  ".center(tamanho))
	print("##    ##   ##    ##      ##       ##  ##    ##  ### ".center(tamanho))
	print("##    ##   ##    ##      ##      ##    ##      ###  ".center(tamanho))
	print("##    ##   ##    ##      ##      ########     ###   ".center(tamanho))
	print("##    ##   ##    ##      ##      ##    ##    ###    ".center(tamanho))
	print("#######    ########      ##      ##    ##   ########".center(tamanho))
	print()
	print("#######     ####    ##    ##  ########   #######".center(tamanho))
	print("##   ###   ##  ##    ##  ##   ##        #####   ".center(tamanho))
	print("##   ###  ##    ##    ####    ########   ####   ".center(tamanho))
	print("#######   ########     ##     ########     #### ".center(tamanho))
	print("##   ###  ##    ##    ##      ##           #####".center(tamanho))
	print("#######   ##    ##   ##       ########  ####### ".center(tamanho))
	print()
	return None

def abertura(tamanho):
	
	system("clear")
	print("\n" + "Seja bem vindo".center(tamanho)+"\n")
	print_dota2bayes(tamanho)
	input("Aperte qualquer tecla para iniciar ")

def mostra_menu(tamanho = 60):
	system("clear")
	print()
	print(" MENU DE OPÇÕES ".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	print("|       AJUSTAR MODELO      |  1  |".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	print("|     SELECIONAR HEROIS     |  2  |".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	print("|          PREDIÇÃO         |  3  |".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	print("|            SAIR           |  4  |".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))

def escolha_menu(tamanho = 60):

	mostra_menu(tamanho)
	escolha = input("\nEntre com o valor da opção desejada: ")
	return escolha

def linha_heroi(heroi, i_heroi):

	linha = " | " + ("HEROI " + str(i_heroi) + ": ").ljust(10) + heroi.center(19) + " |"
	linha = linha.center(len(linha))
	return linha

def linhas_herois(herois):
	
	linhas = [ linha_heroi(h, (i+1) ) for i,h in enumerate(herois) ]	
	return linhas

def importa_base():
	
	path = input(" Entre com o endereço da base de treinamento: ")
	print("\n Impotando base de treinamento...")
	dados = pd.DataFrame.from_csv(path)
	return dados

def faz_colunas_herois():
	colunas = []
	for h in HEROIS["id"]:
		colunas.append("RH_"+ str(h))
		colunas.append("DH_"+ str(h))
	return colunas

def ajusta_modelo():

	system("clear")
	dados = importa_base()
	colunas_herois = faz_colunas_herois()
	modelo = BernoulliNB()
	print("\n Fazendo ajuste do modelo...")
	modelo.fit( dados[colunas_herois], dados["radiant_win"])
	estimativa = modelo.predict( dados[colunas_herois] )
	taxa = round( 100 * sum(estimativa == dados["radiant_win"]) / dados.shape[0] , 2)
	print("\n O modelo está ajustado.\n O modelo possui uma taxa de " + str(taxa) + "%" + " de acerto.\n\n")

	return modelo

def faz_predicao(times, modelo):
	
	colunas = {}
	for time in times:
		for heroi in times[time]:
			
			if time == "radiant":
				colunas["RH_"+ str(HEROIS['id'][HEROIS["heroi"]==heroi].values[0]) ] = [1]
			
			else:
				colunas["DH_"+ str(HEROIS['id'][HEROIS["heroi"]==heroi].values[0]) ] = [1]

	partida = pd.DataFrame( columns = faz_colunas_herois() ).append( pd.DataFrame( colunas ) ).fillna(0)
	
	predicao = modelo.predict(partida)[0]

	if predicao:
		proba = round( 100 * modelo.predict_proba( partida )[0][1] , 2)
		print(colored(" Vitória do time RADIANT com " + str(proba) + " de chance.", "green") )
	else:
		proba = round( 100 * modelo.predict_proba( partida )[0][0] , 2)
		print(colored(" Vitória do time DIRE com " + str(proba) + "%" + " de chance.", "red") )

	return None

def mostra_time(time, herois):
	
	linhas = linhas_herois(herois)
	tamanho = 19

	if time.lower() == "radiant":
		print(colored( "radiant".upper().center(tamanho), "green"))
		for l in linhas:
			print( colored( l, "green") )

	if time.lower() == "dire":
		print( colored( "dire".upper().center(tamanho), "red" ) )
		for l in linhas:
			print( colored(l, "red") )

	return None

def mostra_times( times ):

	system("clear")
	print()
	mostra_time( 'radiant' , times['radiant'])
	print()
	mostra_time( 'dire' , times['dire'])
	print()

	return None

def coleta_time(time, herois):

	cor = "green" if time.lower()=="radiant" else "red"

	escolhidos = len(herois)

	for i in range(escolhidos+1,6):
		heroi = ""
		while ( (heroi not in set(HEROIS["heroi"]) ) or (heroi in herois) ): 
			heroi = input(colored( "Entre com o " + str(i) + "o Heroi do time " + time.upper() + ": " , cor ) )
			if heroi == '':
				herois.sort()
				return herois
		herois.append( heroi )
	herois.sort()
	return herois

def coleta_times(times):
	
	herois_radiant = times["radiant"]
	herois_dire = times["dire"]

	if len(herois_radiant) > 0 or len(herois_dire) > 0:
		if input(" Deseja limpar os herois já selecionados anteriormente? [S/n]").lower() == "s":
			herois_radiant = []
			herois_dire = []

	system("clear")
	herois_radiant = coleta_time("radiant", herois_radiant)
	print()
	herois_dire = coleta_time("dire", herois_dire)
	times = {"radiant":herois_radiant, "dire":herois_dire}
	mostra_times( times )

	return times

###########################################################################

HEROIS = pd.DataFrame.from_csv("Herois.csv")
