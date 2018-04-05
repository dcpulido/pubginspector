import sys
sys.path.insert(0, "./app")
import json
import logging
import configparser
import discord
from controller import Controller


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


generalconf = get_general_conf('GENERAL')
tokens = get_general_conf('TOKENS')
client = discord.Client()
controller = Controller(generalconf, tokens)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0] == "!":
        msg = controller.parse_message(message, client)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


if __name__ == "__main__":
    if generalconf["log"]=="1":
        logging.basicConfig(
            format='%(asctime)s %(levelname)s:%(message)s',
            level=logging.DEBUG)
        logging.info('INSSMG')
    client.run(tokens["discord_token"])

    # print(json.dumps(wp.get_match("1b4a8dfe-5d4f-47e3-bbad-8200c9861463"), indent=4))
