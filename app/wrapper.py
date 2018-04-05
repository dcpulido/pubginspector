import requests
import json


class PubgWrapper:
    def __init__(self, key, conf):
        self.key = key
        self.conf = conf
        self.url = 'https://api.playbattlegrounds.com/shards/' + \
            self.conf["shard"]
        self.headers = dict(accept="application/vnd.api+json",
                            Authorization="Bearer " + self.key)

    def get_player_name(self, name):
        pass

    def get_player(self, iid):
        return json.loads(requests.get(self.url + "/players/" + iid,
                                       headers=self.headers).text)

    def get_match(self, iid):
        return json.loads(requests.get(self.url + "/matches/" + iid,
                                       headers=self.headers).text)

    def get_telemetry(self, iid):
        pass

if __name__ == "__main__":
    print (json.dumps(json.loads(r.text), indent=4))

    print (len(data["data"]["relationships"]["matches"]["data"]))
