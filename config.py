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
# Args : section name, key, default value , bool
# bool is used to identify and convert if the value is a boolean
# By default, value is considered as string
# Need to extend in case other data types are used


def getVal(section, key, default=None, bool=False):

    if isConfAvail(section, key):
        if bool:
            return config.getboolean(section, key)
        return config.get(section, key)

    return default
