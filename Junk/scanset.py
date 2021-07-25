#import nmap

#scanner = nmap.PortScanner()
#ip = "192.168.29.1"
#scanner.scan(hosts=ip, ports="80")
#print(scanner[ip].state())

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    print(s.recv(1024))

def main():
    ip = "192.168.29.184"
    port = 80
    banner(ip, port)

main()