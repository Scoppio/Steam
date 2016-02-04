#! /usr/bin/python

#### IMPORTA TODAS BIBLIOTECAS NECESSÁRIAS ###
import pandas as pd
from dota2py import api
from tqdm import tqdm
import os
import funcoes
import time
import requests

class infos_partidas():

    def __init__(self, chave, game_mode=(1,2), skill=3, info_heroi=("gold_per_min", "xp_per_min")):
        api.set_api_key(chave)
        self.info_heroi = info_heroi
        self.game_mode = game_mode
        self.skill = skill
        self.herois = self.tabela_herois()
        self.colunas = self.faz_todas_colunas()
        self.dados = pd.DataFrame()

    #### FUNCAO QUE BUSCA OS HEROIS ####
    def tabela_herois(self):
        herois = pd.DataFrame.from_dict(api.get_heroes()["result"]["heroes"])
        herois.columns = ["id","heroi", "nome" ]
        return herois

     #### CRIA AS COLUNAS DESEJADAS PARA BASE DE DADOS ####
    def faz_colunas_partida(self):
        return ["id", "radiant_win", "tempo", "modo_jogo", "data_inicio"]

    def faz_colunas_time(self, time="RH"):
        colunas = [time + "_" + str(i) for i in self.herois.id]
        return colunas

    def faz_colunas_herois(self):
        colunas = self.faz_colunas_time("RH") + self.faz_colunas_time("DH")
        return colunas

    def faz_colunas_infos(self, colunas):
        colunas_infos = []
        for j in self.info_heroi:
            colunas_infos += [i + "_" + j for i in colunas]
        return colunas_infos

    def faz_todas_colunas(self):
        self.colunas_herois = self.faz_colunas_herois()
        colunas = self.faz_colunas_partida() + self.colunas_herois + self.faz_colunas_infos(self.colunas_herois)
        return colunas

    #### FUNCAO PARA BUSCAR AS ULTIMAS 100 PARTIDAS ####
    def pega_ids(self, hist=False):

        ids = []

        while len(ids)<=1:

            try:
                if not hist:
                    partidas = api.get_match_history(skill=self.skill, game_mode=self.game_mode, min_players=10)
                else:
                    partidas = api.get_match_history(skill=self.skill, game_mode=self.game_mode, min_players=10, start_at_match_id=hist )
                ids = [i["match_id"] for i in partidas["result"]["matches"] ]

            except requests.RequestException as erro:
                print(erro)

        return ids

    #### COLETA TODAS INFORMAÇÕES DE UMA UNICA PARTIDA ####
    def info_partida(self,id):
        try:
            match = api.get_match_details(id)["result"]

        except requests.RequestException as erro:
            print("\n *********************************\n")
            print(erro)
            print("\n Problema na coleta desta partida... O procedimento continua.")
            print(" \n*********************************\n")
            return pd.DataFrame()

        info = {"id":[match["match_id"]],
                "radiant_win":[match["radiant_win"]],
                "tempo":[ match["duration"]/60 ],
                "modo_jogo":[match["game_mode"]],
                "data_inicio":[match["start_time"]]}
        leaver = 0

        for p in match["players"]:

            if p["player_slot"] <= 4:
                info[ "RH_" + str(p["hero_id"])]=[1]
                leaver += int(p["leaver_status"])
                for j in self.info_heroi:
                    info["RH_" + str(p["hero_id"]) +"_"+ j] =p[j]

            else:
                info[ "DH_" + str(p["hero_id"])]=[1]
                leaver += int(p["leaver_status"])
                for j in self.info_heroi:
                    info["DH_" + str(p["hero_id"]) +"_"+ j] =p[j]

        if leaver>0:
            return pd.DataFrame()
        else:
            return pd.DataFrame.from_dict(info)

    #### ARRUMA OS DADOS CAPTURADOS REALIZANDO LIMPEZA NECESSÁRIA ####
    def arruma_dados(self, dados):
        print("\n Arrumandos o dados coletados...")

        ## TIRA PARTIDAS INCONSISTENTES ##
        dados_columns = dados.keys()
        fora = ["RH_0","DH_0"]
        for f in fora:
            if f in dados_columns:
                dados = dados[ dados[f]!= 1 ]
                del dados[f]
        dados = dados[self.colunas]

        ## SUBSTIRUI NA`s ##
        dados[self.colunas_herois] = dados[self.colunas_herois].fillna(0)

        ## REMOVE PARTIDAS COM POUCA DURAÇÃO ##
        dados = dados[ dados["tempo"]>=15 ]

        print(" Processo de arrumar os dados finalizado...")

        return dados

    #### ESTRUTURA TODAS INFORMAÇÕES DAS PARTIDAS COLETADAS ####
    def faz_coleta(self, ids):

        dados = pd.DataFrame(columns=self.colunas)

        for i in tqdm(ids):
            dados = dados.append( self.info_partida(i), ignore_index=True)

        dados = self.arruma_dados(dados)
        return dados