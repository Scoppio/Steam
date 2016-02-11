#-*- coding: utf-8 -*-

from menus import *
import pandas as pd

def main(tamanho=60):

	abertura(tamanho)

	tabela_herois = pd.DataFrame.from_csv("Herois.csv")
	escolha_herois = []
	
	while True:
		escolha = escolha_menu()
		if escolha == "1":
			mostra_tabela_herois(tabela_herois)
			input(" Aperte 'ENTER' para retornar ")
		if escolha == "2":
			escolha_herois = coleta_times(tabela_herois)
			print(escolha_herois)
			input(" Aperte 'ENTER' para retornar ")
		if escolha == "3":
			print(nomes_herois)
			input(" Aperte 'ENTER' para retornar ")
		if escolha == "4":
			break

main()


