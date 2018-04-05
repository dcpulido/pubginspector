import requests
import json


class PubgWrapper:
    def __init__(self, key, conf):
        self.key = key
        self.conf = conf
        self.url = 'https://api.playbattlegrounds.com/shards/pc-eu/players/'
        self.headers = dict(accept="application/vnd.api+json",
                            Authorization="Bearer " + self.key)

    def get_player_name(self, name):
        pass

    def get_player_id(self, iid):
        r = requests.get(self.url+iid,
                         headers=self.headers)
        return json.loads(r.text)


if __name__ == "__main__":

    # idBoc = "account.fdddd9dfa3954ad78458e9e9c1172bbb"
    # iid = "account.d0e19381ceea42a6bd59497fac789943"

    print json.dumps(json.loads(r.text), indent=4)

    print len(data["data"]["relationships"]["matches"]["data"])
