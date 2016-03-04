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
	print("|    PREVISÃO DE PARTIDAS   |  2  |".center(tamanho))
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

	dados = importa_base()
	colunas_herois = faz_colunas_herois()
	modelo = BernoulliNB()
	modelo.fit( dados[colunas_herois], dados["radiant_win"])
	estimativa = modelo.predict( dados[colunas_herois] )
	print(" O modelo está ajusatado.\n"+
	 " O mo possui uma taxa de " + str( 100 * sum(estimativa == dados["radiant_win"]) / dados.shape[0]  ), "porcento de acerto.")
	return modelo

def mostra_time(time, herois):
	
	linhas = linhas_herois(herois)
	tamanho = 19

	if time.lower() == "radiant":
		print(colored( "RADIANT".center(tamanho), "green"))
		for l in linhas:
			print( colored( l, "green") )

	if time.lower() == "dire":
		print( colored( "DIRE".center(tamanho), "red" ) )
		for l in linhas:
			print( colored(l, "red") )

	return None

def mostra_times( times ):

	print()
	for time in times.keys():
		mostra_time( time , times[time])
		print()

	return None

def coleta_time(time):

	cor = "green" if time.lower()=="radiant" else "red"

	herois = []
	for i in range(1,6):
		heroi = ""
		while ( (heroi not in set(HEROIS["heroi"]) ) or (heroi in herois) ): 
			heroi = input(colored( "Entre com o " + str(i) + "o Heroi do time " + time + ": " , cor ) )
			if heroi == '':
				herois.sort()
				return herois
		herois.append( heroi )
	herois.sort()
	return herois

def coleta_times():
	
	system("clear")
	herois_radiant = coleta_time("RADIANT")
	print()
	herois_dire = coleta_time("DIRE")


	times = {"radiant":herois_radiant, "dire":herois_dire}
	mostra_times( times )
	return times

###########################################################################

HEROIS = pd.DataFrame.from_csv("Herois.csv")
