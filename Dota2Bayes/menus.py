#-*- coding: utf-8 -*-

from os import system
from termcolor import colored
import pandas as pd

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
	print("|     VISUALIZAR HEROIS     |  1  |".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	print("|    PREVISÃO DE PARTIDAS   |  2  |".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	print("|      VERIFICAR HEROIS     |  3  |".center(tamanho))
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

def mostra_tabela_herois(base_herois):
	
	print(" +---------------------------+")
	print(" | " + "ID".center(3) + " | " + "HEROI".center(19) + " |")
	print(" +---------------------------+")

	for h in range(base_herois.shape[0]):
		print(" | " + str(base_herois.loc[h]["id"]).rjust(3) + " | " + str(base_herois.loc[h]["heroi"]).center(19) + " |" )
	
	print(" +---------------------------+")

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

def coleta_time(tabela_herois,time):

	cor = "green" if time.lower()=="radiant" else "red"

	herois = []
	for i in range(1,6):
		heroi = ""
		while ( (heroi not in set(tabela_herois["heroi"]) ) or (heroi in herois) ): 
			heroi = input(colored( "Entre com o " + str(i) + "o Heroi do time " + time + ": " , cor ) )
			if heroi == '':
				herois.sort()
				return herois
		herois.append( heroi )
	herois.sort()
	return herois

def coleta_times(tabela_herois):
	
	system("clear")
	herois_radiant = coleta_time(tabela_herois, "RADIANT")
	print()
	herois_dire = coleta_time(tabela_herois, "DIRE")
	times = {"radiant":herois_radiant, "dire":herois_dire}
	mostra_times( times )
	return times
