#-*- coding: utf-8 -*-

from menus import *
import pandas as pd

def main(tamanho=60):

	abertura(tamanho)
	times={"radiant":[], "dire":[]}
	modelo = None
	
	while True:
		escolha = escolha_menu()
		if escolha == "1":
			modelo = ajusta_modelo()
			input("\n Aperte 'ENTER' para retornar ")
		if escolha == "2":
			times = coleta_times(times)
			if modelo:
				faz_predicao(times, modelo)
			else:
				print("\n\n NAO HÁ NENHUM MODELO AJUSTADO, POR FAVOR FAÇA O AJUSTE DO MODELO! \n\n")
			input("\n Aperte 'ENTER' para retornar ")
		if escolha == "3":
			mostra_times(times)
			if modelo:
				faz_predicao(times, modelo)
			input("\n Aperte 'ENTER' para retornar ")
		if escolha == "4":
			break

main()


