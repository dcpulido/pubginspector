import sys
sys.path.insert(0, "./app")
import json
import logging
import configparser
from wrapper import PubgWrapper
from dataParser import Filter


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
    Config.read("./conf/config.conf")
    myprior = {}
    for sec in Config.sections():
        if sec == name:
            myprior = ConfigSectionMap(sec, Config)
    return myprior


def get_key():
    with open("./conf/key", "r") as key:
        return key.read()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(message)s',
        level=logging.DEBUG)
    logging.info('INSSMG')

    generalConf = get_general_conf("GENERAL")
    key = get_key()

    wp = PubgWrapper(key, generalConf)

    print json.dumps(wp.get_match("1b4a8dfe-5d4f-47e3-bbad-8200c9861463"), indent=4)
