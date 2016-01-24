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
        return ["id", "radiant_win", "tempo", "modo_jogo"]

    def faz_colunas_time(self, time="RH"):
        colunas = [time + "_" + str(i) for i in self.herois.id]
        return colunas

    def faz_colunas_herois(self):
        self.colunas_RH = self.faz_colunas_time("RH")
        self.colunas_DH = self.faz_colunas_time("DH")
        colunas = self.colunas_RH + self.colunas_DH
        return colunas

    def faz_colunas_infos(self, colunas):
        colunas_infos = []
        for j in self.info_heroi:
            colunas_infos += [i + "_" + j for i in colunas]
        return colunas_infos

    def faz_todas_colunas(self):
        col_herois = self.faz_colunas_herois()
        colunas = self.faz_colunas_partida() + col_herois + self.faz_colunas_infos(col_herois)
        return colunas

    #### FUNCAO PARA BUSCAR AS ULTIMAS 100 PARTIDAS ####
    def pega_ids(self):
        try:
            partidas = api.get_match_history(skill=self.skill, game_mode=self.game_mode, min_players=10)
            ids = [i["match_id"] for i in partidas["result"]["matches"] ]
            return ids

        except requests.RequestException as erro:
            print(erro)
            return None

    #### COLETA TODAS INFORMAÇÕES DE UMA UNICA PARTIDA ####
    def info_partida(self,num):
        try:
            match = api.get_match_details(num)["result"]

        except requests.RequestException as erro:
            print("\n *********************************\n")
            print(erro)
            print("\n Problema na coleta desta partida... O procedimento continua.")
            print(" \n*********************************\n")
            return pd.DataFrame()

        info = {"id":[match["match_id"]],
                "radiant_win":[match["radiant_win"]],
                "tempo":[ match["duration"]/60 ],
                "modo_jogo":[match["game_mode"]]}
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

        print(" Arrumandos o dados coletados...")

        ## TIRA DUPLICATAS ##
        dados = dados.drop_duplicates()

        ## TIRA PARTIDAS INCONSISTENTES ##
        dados_columns = dados.keys()
        fora = ["RH_0","DH_0"]
        for f in fora:
            if f in dados_columns:
                dados = dados[ dados[f]!= 1 ]
                del dados[f]
        dados = dados[self.colunas]

        ## SUBSTIRUI NA`s ##
        dados[self.colunas_DH + self.colunas_RH] = dados[self.colunas_DH + self.colunas_RH].fillna(0)

        ## REMOVE PARTIDAS COM POUCA DURAÇÃO ##
        dados = dados[ dados["tempo"]>=15 ]

        return dados

    #### ESTRUTURA TODAS INFORMAÇÕES DAS PARTIDAS COLETADAS ####
    def faz_coleta(self):
        ids =  self.pega_ids()
        dados = pd.DataFrame(columns=self.colunas)

        for i in tqdm(ids):
            dados = dados.append( self.info_partida(i), ignore_index=True)

        dados = self.arruma_dados(dados)
        return dados

    ### FUNCAO PARA SALVAR OS DADOS ###
    def salvamento(self):
        self.salva = input(" Deseja salvar os dados a cada iteração? [S/n] ")

        if self.salva.upper() == "S":
           self.endereco = input(" Entre com o endereço do arquivo: ")

           if self.endereco[-3:] != "csv":
               self.endereco = self.endereco + ".csv"
        return None

    ### PROCEDIMENTOS DURANTE A COLETA RECURSIVA ###
    def coletando(self, tempo, i):
        print("\n "+ str(i)+"a coleta iniciada.")
        self.dados = self.dados.append( self.faz_coleta(), ignore_index=True).drop_duplicates()
        if self.salva == "S":
            self.dados.to_csv(self.endereco)

        return None

    ### COOLETA RECURSIVA AUTOMATICA ###
    def coleta_recursiva(self, tempo, quantidade=False):
        self.salvamento()
        os.system("clear")
        print("\n Iniciando coleta recursiva...")

        if quantidade:
            for i in range(1,quantidade+1):
                self.coletando(tempo, i)
                funcoes.dormindo(tempo, i)

        else:
            i=1
            while True:
                self.coletando(tempo, i)
                funcoes.dormindo(tempo, i)
                i+=1

        print("\n Foram realizadas "+str(i) + " coletas de dados.")
        return None