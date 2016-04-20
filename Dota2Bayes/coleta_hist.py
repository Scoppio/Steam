from infos_partidas import infos_partidas

def coleta_historica(min_id, max_id):
    chave = input(" Entre com a chave do desenvolvedor: ")
    Obj_coleta = infos_partidas(chave)
    ids = []
    ultimo_id = max_id
    while min_id in ids:
        ids += Obj_coleta.pega_ids(hist=ultimo_id)
        ultimo_id = min(ids) - 1
    return ids



