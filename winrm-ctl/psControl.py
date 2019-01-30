import argparse
import sys
import winrm
import os

# This code block will use the command arguements - game, path, script:

parser = argparse.ArgumentParser()

parser.add_argument("--game","-g", help="Set the game you'd like to configure. This will add Username,Password and IP of the relevant host to the program", type=str)
parser.add_argument("--cmdlet","-m", help="run only cmdlet", type=str)
parser.add_argument("--path","-p", help="Choose the scripts path", type=str)
parser.add_argument("--script","-s", help="Choose the script name", type=str)
parser.add_argument("--cmd", "-c", help="Run only command line scripts", type=str)

args = parser.parse_args()

cmdlet = args.cmdlet
path = args.path
script = args.script
game = args.game
command = args.cmd

# These are the Username\Password and IP stored as env. variable and build the winRM session:

user = str(os.environ[game + '_user'])
password = str(os.environ[game + '_pass'])
ip = str(os.environ[game + '_ip'])

# Define the session for winRM:

session = winrm.Session('%s' % ip, auth=('%s' % user, '%s' %password))

# Main function will execute the commd:

def main():
    if args.path and args.script:
    	ps_script = 'cd %s; ./%s' % (path, script)
	runscript = session.run_ps('%s' % ps_script)
    	output = runscript.std_out
    	print(output)
    elif args.cmdlet:
    	commandlet = '%s' % cmdlet
        runcmdlet = session.run_ps('%s' % commandlet)
	output = runcmdlet.std_out
        print(output)
    elif args.cmd:
	commandline = '%s' % command
	runcmd = session.run_cmd('%s' % commandline)
        output = runcmd.std_out
        print(output)

main()
