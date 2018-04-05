import requests
import json
import configparser


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
        print(iid)
        print(self.url + "/players/" + iid)
        return json.loads(requests.get(self.url + "/players/" + iid,
                                       headers=self.headers).text)

    def get_match(self, iid):
        return json.loads(requests.get(self.url + "/matches/" + iid,
                                       headers=self.headers).text)

    def get_telemetry(self, iid):
        pass


if __name__ == "__main__":
    def ConfigSectionMap(section, Config):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    logging.info("skip: %s" % option)
            except:
                logging.info("exception on %s!" % option)
                dict1[option] = None
        return dict1

    def get_general_conf(name):
        Config = configparser.ConfigParser()
        Config.read("../conf/config.conf")
        myprior = {}
        for sec in Config.sections():
            if sec == name:
                myprior = ConfigSectionMap(sec, Config)
        return myprior
    generalconf = get_general_conf('GENERAL')
    tokens = get_general_conf('TOKENS')
    pw = PubgWrapper(tokens["pubg_token"], generalconf)
    pw.get_match("1b4a8dfe-5d4f-47e3-bbad-8200c9861463")
