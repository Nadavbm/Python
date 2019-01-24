import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-path","-p", help="Choose the scripts path", type=str, required=True)
parser.add_argument("-script","-s", help="Choose the script name", type=str, required=True)

args = parser.parse_args()

print(args.path)
print(args.script)
