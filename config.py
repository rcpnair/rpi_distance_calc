import configparser

# read config and store values
config = configparser.ConfigParser()


def readConf(confFile):
    config.read(confFile)

# Check if the section and key are available


def isConfAvail(section, key):
    if config.has_option(section, key):
        return True

    return False

# Get the value from config. Assign none if default value is not provided
# Args : section name, key, default value


def getVal(section, key, default=None):
    if isConfAvail(section, key):
        return config.get(section, key)
    return default


def getValInt(section, key, default=0):
    if isConfAvail(section, key):
        return config.getint(section, key)
    return defult


def getValBool(section, key, default=False):
    if isConfAvail(section, key):
        return config.getboolean(section, key)
    return defult
