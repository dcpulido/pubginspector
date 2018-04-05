""" clase para filtrar los json de ntrada y crear diccionarios con xeito
filtrando los campos q no son necesarios"""
class Filter:
    def __init__(self):
        pass

    def filter_player(self, player):
        print(json.dumps(player, indent=4))
        return player

    def filter_match(self, match):
        pass