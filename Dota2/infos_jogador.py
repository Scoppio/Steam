import pandas
from dota2py import api
from tqdm import tqdm
import os
import funcoes
import time
import requests

class infos_jogador():
    def __init__(self, chave, account_id, game_mode=(1,2), info_heroi=("gold_per_min", "xp_per_min")):
        api.set_api_key(chave)
        self.info_heroi=info_heroi
        self.account_id=account_id
        self.game_mode = game_mode
        self.ids = []

    def busca_ids(self):
        try:
            if len(self.ids) < 1:
                partidas = api.get_match_history(game_mode=self.game_mode, account_id=self.account_id, min_players=10 )
                ids = [i["match_id"] for i in partidas["result"]["matches"] ]
            else:
                partidas = api.get_match_history(game_mode=self.game_mode, account_id=self.account_id, min_players=10, start_at_match_id=min(self.ids) )
                ids += [i["match_id"] for i in partidas["result"]["matches"] ]
        except requests.HTTPError as erro:
            print(erro)
            pass
        return ids
