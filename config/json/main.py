import json

def reader():
    with open('config.json', 'r') as file:
        data = file.read()
    obj = json.loads(data)
    ip = obj['ip']
    port = str(obj['port'])
    api = obj['api']
    print("IP is {0}, port is {1}, api is {2}".format(ip, port, api))

if __name__ == "__main__":
    reader()
