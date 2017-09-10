import sys
import socket
import os
import argparse
def getIP(host):
    try:
       IP = socket.gethostbyname(host)
       return IP
    except Exception:
       return False
DescriptionX = '''
Dnsenum created by Saber Guenichi -- saberguenichi92@gmail.com
'''
parser = argparse.ArgumentParser(description=DescriptionX)
parser.add_argument('-d','--domain', help='the target main domain name', required=True)
parser.add_argument('-n','--name', help='the target name', required=True)
parser.add_argument('-f','--file', help='the filename that contains subs', required=True)
args = vars(parser.parse_args())
domain = args['domain']
name = args['name']
filex = args['file']
command00 = 'mkdir targets'
os.system(command00)
command = 'mkdir targets/' + name
os.system(command)
ips = []
hosts = []
with open(filex, "r") as ins:
    for line in ins:
        full = line.strip() + '.' + domain
        ip = getIP(full)
        if ip != False:
            hosts.append(full)
            ips.append(ip)
            string = full + ' - ' + ip
            print string
count1 = len(hosts)
i = 0
while i < count1:
    command = 'echo ' + hosts[i] + ' >> targets/' + name + '/hosts.txt'
    os.system(command);
    i = i + 1
count2 = len(ips)
j = 0
limit = 0
uniqueips = []
while j < count2:
    isnew = True
    k = 0
    while k < limit:
        if ips[j] == uniqueips[k]:
            isnew = False
        k = k + 1
    if isnew == True:
        uniqueips.append(ips[j])
        command = 'echo ' + ips[j] + ' >> targets/' + name + '/ips.txt'
        os.system(command)
    limit = len(uniqueips)
    j = j + 1
