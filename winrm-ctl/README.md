
#Prepare CentOS7 management server for winRM access (Master configuration):
---------------------------------------------------
sudo su

yum install python-pip

sudo yum install gcc krb5-devel krb5-workstation

pip install pywinrm

pip install pywinrm[kerberos]

# Prepare Windows Server to open winRM connections (Salve configuraiton):

Open Powershell as admin:

PS C:\> Set-Item WSMan:\localhost\Client\TrustedHosts -Force -Concatenate -Value 10.6.5.3,10.5.2.4

PS C:\> Set-Service WinRM -StartMode Automatic

PS C:\> Restart-Service -Force WinRM

PS C:\> Get-Item WSMan:\localhost\Client\TrustedHosts

Open cmd as admin:

winrm set winrm/config/client/auth @{Basic="true"}

winrm set winrm/config/service/auth @{Basic="true"}

winrm set winrm/config/service @{AllowUnencrypted="true"}

# Test the connection from CentOS7 to Windows server:

python

import winrm

session = winrm.Session('10.1.1.1', auth=('administrator', 'Pa$$w0rd'))

command = session.run_cmd('ipconfig', ['/all'])

output = command.std_out

print(output)
