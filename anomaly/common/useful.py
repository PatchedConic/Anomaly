from os.path import exists

USERPATH = '$HOME/.config/anomaly/config.toml'
DEVPATH = './config/config.toml'

def check_for_config():
    if exists(USERPATH):
        return USERPATH
    elif exists(DEVPATH):
        return DEVPATH
    else: return False