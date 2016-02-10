from menus import *
import pandas as pd

def main(tamanho=60):

	herois = pd.DataFrame.from_csv("Herois.csv")
	system("clear")
	print("\n" + "Seja bem vindo".center(tamanho)+"\n")
	print_dota2bayes(tamanho)
	input("Aperte qualquer tecla para iniciar")
	while True:
		escolha = faz_selecao()
		if escolha == "1":
			base_herois(herois)
		if escolha == "2":
			print(coleta_time(herois, "radiant"))
			input(" Aperte qualquer tecla para retornar")
		if escolha == "3":
			break

main()
mostra_time("RADIANT", ["Tedoro Calvo", "Emanuel Alvares", "Lara Calvo"])
print()
mostra_time("DIRE", ["Natália Ataide", "Maria Carolina", "Beatriz Ataide"])


