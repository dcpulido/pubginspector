import sys
sys.path.insert(0, './')
import json
import time
from wrapper import PubgWrapper
from dataParser import Filter


class Controller:
    def __init__(self,
                 general,
                 tokens,
                 players):
        self.conf = general
        self.tokens = tokens
        self.players = players
        self.wp = PubgWrapper(tokens["pubg_token"],
                              self.conf)
        self.fl = Filter()

    def parse_message(self,
                      message,
                      client):
        print(client)
        msg = message.content
        author = message.author
        print(msg)
        if msg.startswith("!hello"):
            return author.mention + "\'s ass is so wet"

    def get_player(self, name):
        plsp = self.fl.filter_player(self.wp.get_player(self.players[name]))


if __name__ == '__main__':
    pass
