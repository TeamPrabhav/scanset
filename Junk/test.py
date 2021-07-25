import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP

t_host = str(input("Enter the host name: "))
t_port = int(input("Enter Port: "))

sock.connect((t_host,t_port))
sock.send('GET HTTP/1.1 \r\n')

ret = sock.recv(1024)
print('[+]' + str(ret))