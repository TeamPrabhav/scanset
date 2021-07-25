import nmap
import time

nm = nmap.PortScanner()

start = time.perf_counter()

result = nm.scan("192.168.29.2/24", arguments="-sn")

for ip in result["scan"]:
    print(result["scan"][ip])

print(time.perf_counter() - start)