import getpass
import sys
import telnetlib
import time

Host = "vpn.kansk-tc.ru"

user = "cisco"
password = "cisco"

tn = telnetlib.Telnet(Host, 32771)
tn.write(b"\r")
tn.read_until(b"Username:")
tn.write(user.encode() + b"\r")
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode()+b"\r")
tn.write(b"enable\n")
tn.write(b"show run\n")
line = tn.read_until(b'bratishka', 1)
tn.write(b"\n")
tn.write(b"quit\n")
print(line)

