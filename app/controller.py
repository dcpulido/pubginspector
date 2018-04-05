import sys
sys.path.insert(0, './')
import json
import time

class Controller:
    def __init__(self,
                 general):
        self.conf = general
    def parse_message(self,
                      message,
                      client):
        print(client)
        msg = message.content
        author = message.author
        print(msg)
        if msg.startswith("!hello"):
            return author.mention + "\'s ass is so wet"

if __name__ == '__main__':
    pass
