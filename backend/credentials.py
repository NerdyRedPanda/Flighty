import configparser
from os.path import exists

keys = configparser.ConfigParser()

# Loads API keys from file


def loadKeys(configFile):
    if (not exists(configFile)):
        print("No credentials file found")
        return
    else:
        print("Loading keys...")
        keys.read(configFile)

# Gets a key from the config file


def getKey(keyName):
    try:
        return keys['KEYS'][keyName]
    except:
        return ""
