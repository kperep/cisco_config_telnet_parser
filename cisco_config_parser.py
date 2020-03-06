import getpass
import sys
import telnetlib
import time

Host = "vpn.kansk-tc.ru"

# user=input("Enter User name")
# password=getpass.getpass()

tn = telnetlib.Telnet(Host, 32771, 5)
# tn.read_until("Username: ")
# tn.write(user.encode('ascii') + b"\n")

# if password:
# tn.read_until(b”Password: “)
# tn.write(password.encode(‘ascii’)+b”\n”)
tn.write(b"\n")
time.sleep(2)
tn.write(b"enable\n")
time.sleep(2)
tn.write(b"show run\n")
time.sleep(2)
line = tn.read_until(b'no mmi auto-configure')
print(line)
