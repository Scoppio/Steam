#! /usr/bin/python

from infos_partidas import infos_partidas
import time

#### CHAVE DA STEAM PARA ACESSO ####
chave = input(" Entre com a chave do desenvolvedor: ")
int_tempo = int(input("\n Defina um intervalo de tempo para coleta (em segundos): "))

minha_coleta = infos_partidas(chave)
minha_coleta.coleta_recursiva(int_tempo)

