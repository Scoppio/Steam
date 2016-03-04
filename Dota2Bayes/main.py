#-*- coding: utf-8 -*-

from menus import *
import pandas as pd

def main(tamanho=60):

	abertura(tamanho)
	times={"radiant":[], "dire":[]}
	
	while True:
		escolha = escolha_menu()
		if escolha == "1":
			modelo = ajusta_modelo()
			input(" Aperte 'ENTER' para retornar ")
		if escolha == "2":
			times = coleta_times(times)
			faz_predicao(times, modelo)
			input(" Aperte 'ENTER' para retornar ")
		if escolha == "3":
			print( faz_predicao(times, modelo) )
			input(" Aperte 'ENTER' para retornar ")
		if escolha == "4":
			break

main()


