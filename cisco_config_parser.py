import getpass
import sys
import telnetlib
import time

Host = "vpn.kansk-tc.ru"

user = 'cisco'
password = 'cisco'

tn = telnetlib.Telnet(Host, 32771, 5)
tn.write(b"\n")
time.sleep(2)
#tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

time.sleep(2)
if password:
#    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii')+b"\n")
time.sleep(1)
tn.write(b"enable\n")
time.sleep(1)
tn.write(b"show run\n")
time.sleep(1)
line = tn.read_until(b'aaa authorization console')
print(line)
tn.write(b"exit\n")
