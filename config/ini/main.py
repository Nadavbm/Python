import configparser

config = configparser.ConfigParser()

def reader():
    config.read('config.ini')
    net = config['network']
    ip = net['ip']
    port = net['port']
    api = config['api']
    key = api['key']
    print("IP is '{0}', Port is '{1}', Key is '{2}'".format(ip, port, key))

if __name__ == "__main__":
    reader()
