import getpass
import sys
from tkinter import *
import telnetlib
import time

root = Tk()
ws = root.winfo_screenwidth()  # считываем текущую ширину экрана
hs = root.winfo_screenheight()  # считываем текущую высоту экрана
root.geometry('%dx%d+%d+%d' % (640, 480, (ws / 2) - 320, (hs / 2 - 240)))  # расположение по центру экрана
root.title("CISCO configuration check")
root.resizable(0, 0)  # запрещаем изменять размер окна

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

root.mainloop()

