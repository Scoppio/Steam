from os import system
from termcolor import colored
import pandas as pd

herois = pd.DataFrame.from_csv("Herois.csv")

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

def mostra_selecao(tamanho = 60):
	system("clear")
	print()
	print(" MENU DE OPÇÕES ".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	print("|     Visualizar Herois     |  1  |".center(tamanho))
	print("|    Previsão de Partida    |  2  |".center(tamanho))
	print("|            Sair           |  3  |".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))

def faz_selecao(tamanho = 60):
	mostra_selecao(tamanho)
	escolha = input("\nEntre com o valor da opção desejada: ")
	return escolha

def todos_herois(herois):
	tamanho_heroi = max([len(h) for h in herois])
	linhas = []
	i=1
	for h in herois:
		linhas.append( linha_heroi(h, i) )
		i+=1
	return linhas

def base_herois(base_herois):
	print(" +---------------------------+")
	print(" | " + "ID".center(3) + " | " + "HEROI".center(19) + " |")
	print(" +---------------------------+")

	for h in range(base_herois.shape[0]):
		print(" | " + str(herois.loc[h]["id"]).rjust(3) + " | " + str(herois.loc[h]["heroi"]).center(19) + " |" )
	
	print(" +---------------------------+")
	input(" Aperte qualquer tecla para retornar")

def linha_heroi(heroi, i_heroi):

	linha = " | " + ("HEROI " + str(i_heroi) + ": ").ljust(10) + heroi.center(19) + " |"
	linha = linha.center(len(linha))
	return linha

def mostra_time(time, herois):
	
	linhas_herois = todos_herois(herois)
	tamanho = len( linhas_herois[0] )

	if time.lower() == "radiant":
		print(colored( "RADIANT".center(tamanho), "green"))
		for l in linhas_herois:
			print( colored( l, "green") )

	if time.lower() == "dire":
		print( colored( "DIRE".center(tamanho), "red" ) )
		for l in linhas_herois:
			print( colored(l, "red") )

	return None

def coleta_time(base_herois,time):
	system("clear")
	herois = []
	for i in range(1,6):
		heroi = 150
		while (not (base_herois["id"].min() <= heroi <= base_herois["id"].max())) or (heroi in herois): 
			heroi = int(input("Entre com o " + str(i) + "o Heroi do time " + time + ": ") )
		if heroi != '':
			herois.append(heroi)
		else:
			herois.sort()
			return herois
	herois.sort()
	return herois

def coleta_times():
	herois_radiant = coleta_time("RADIANT")
	herois_dire = coleta_time("DIRE")
