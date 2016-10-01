import json
config = None

def initialize():
    global config
    if config == None:
        # loads the config and stores it in a global dictionary
        with open("/home/pi/.irpconfig") as config_file:
            config = json.load(config_file)
        print('config_initialize')

def get_value(name):
    # returns a value from config
    return config[unicode(name)]


if __name__ == '__main__':
    initialize()
    print(get_value("mail_account"))

