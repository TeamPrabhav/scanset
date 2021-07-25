import socket
from IPy import IP
#multiple targets
targets = input('Enter target/s use comma to split target: ') #type in ip address

#use nslookup to find ip address of website and use www. nslookup (www.gb.facebook.com/)

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + 'Scanning Targer' + ' ' +str(target) )
    for port in range(75,81):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip) #converts to ip address
        return ip
    except ValueError:
        return socket.gethostbyname(ip) #converts website name to ip address     
        
def get_banner(s, target):
    # target is dns host name, ie "testphp.vulweb.com"
    headers = \
        "GET / HTTP/1.1\r\n" \
        f"Host: {target}\r\n" \
        "User-Agent: python-custom-script/2.22.0\r\n" \
        "Accept-Encoding: gzip, deflate\r\nAccept: */*\r\n" \
        "Connection: keep-alive\r\n\r\n"
    print("\n\n" + headers)

    s.send(headers.encode())  # send request
    resp = s.recv(2048)  # receive response
    return resp

def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.settimeout(10)#this is how long to look for the port however the accuracy of the port will be low
        sock.connect((ip_address,port)) #connect to ip address
        try:
            banner = get_banner(sock, ip_address)
            
            print('port'+ str(port)  +'is open and banner is open' + str(banner.decode().strip('\n')))
        except:
            print('port'+ str(port)  +'is open')
      
    except:
        pass
    
#converted_ip = check_ip(ip_address)

if ',' in targets:
    for ip_add in targets.spilt(','): #words spilt with comma
        scan(ip_add.strip(' ')) #removes empty spaces
else:
    scan(targets)