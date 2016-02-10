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

def selecao(tamanho = 60):
	system("clear")
	print()
	print(" MENU DE OPÇÕES ".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	print("| Visualizar Base de Herois |  1  |".center(tamanho))
	print("|    Previsão de Partida    |  2  |".center(tamanho))
	print("|            Sair           |  3  |".center(tamanho))
	print("+---------------------------+-----+".center(tamanho))
	
def mostra_herois():

	print(herois[ ["id", "heroi"] ])
	input(" Aperte qualquer tecla para retornar")

def inicio(tamanho=60):

	system("clear")
	print("\n" + "Seja bem vindo".center(tamanho)+"\n")
	print_dota2bayes(tamanho)
	input("Aperte qualquer tecla para iniciar")
	selecao()
	escolha = input("\nEntre com o valor da opção desejada: ")
	if escolha == "1":
		mostra_herois()



def linha_heroi(heroi, i_heroi):

	linha = " | " + ("HEROI " + str(i_heroi) + ": ").ljust(10) + heroi.center(19) + " |"
	linha = linha.center(len(linha))
	return linha

def todos_herois(herois):
	tamanho_heroi = max([len(h) for h in herois])
	linhas = []
	i=1
	for h in herois:
		linhas.append( linha_heroi(h, i) )
		i+=1
	return linhas

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

inicio()
mostra_time("RADIANT", ["Tedoro Calvo", "Emanuel Alvares", "Lara Calvo"])
print()
mostra_time("DIRE", ["Natália Ataide", "Maria Carolina", "Beatriz Ataide"])


