import sys
import winrm

session = winrm.Session('10.1.1.1', auth=('administrator', 'Pas$$w0rd'))

def list_service():
    list = session.run_ps('Get-Service')
    output = list.std_out
    print(output)

def stop_service():
    stop = session.run_ps('Stop-Service -name %s' % service)
    output = stop.std_out
    print(output)

def start_service():
    start = session.run_ps('Start-Service -name %s' % service)
    output = start.std_out
    print(output)

def restart_service():
    restart = session.run_ps('Restart-Service -name %s' % service)
    output = restart.std_out
    print(output)

def check_ip():
    ipcheck = session.run_cmd('ipconfig', ['/all'])
    output = ipcheck.std_out
    print(output)

def main():
    command = sys.argv[1]
    if command == 'check_ip':
        check_ip()
    if command == 'list_service':
        list_service()
    else:
        print("The script should run with arguments")

main()
