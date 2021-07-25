import nmap
import ipaddress
from datetime import datetime
from database import Database


class HostDiscovery:

    db = Database()

    def insertData (self, resultData):

        # UPDATE DATA IN SQLITE DATABASE
        self.db.insertData(resultData)
        print("New host connected!")
        #print(resultData)

    def updateTimeStamp (self, resultData):

        # UPDATE TIME STAMP OF LAST SEEN
        self.db.updateData(resultData)
        print("IP: %s - Time stamp: %s" %(resultData["ipAddress"], resultData["timeStamp"]))
        #print(resultData)

    def checkDatabase (self, ipAddress):
        return self.db.checkHost(ipAddress)

    # HOST DISCOVERY USING PING SCAN
    def discoverHostDaemon (self, subnet):

        nm = nmap.PortScanner()

        while True:

            # SCAN NETWORK FOR LIVE HOSTS
            result = nm.scan(subnet, arguments="-sn -T5 --min-parallelism 100")

            # IF ANY HOST IS UP, STORE/UPDATE DATA
            if bool(result["scan"]):

                for ipAddress in result["scan"]:

                    # GET CURRENT DATE TIME
                    now = datetime.now()
                    timeStamp = now.strftime("%d-%m-%Y %I-%M-%S %p")

                    # EXTRACT REQUIRED DATA FROM RESULT
                    hostName = result["scan"][ipAddress]["hostnames"][0]["name"]
                    if hostName == "": hostName = "NONE"

                    # CHECK IF MAC ADDRESS OF DEVICE IS HIDDEN
                    macAddress = "HIDDEN"
                    if "mac" in result["scan"][ipAddress]["addresses"]:
                        macAddress = result["scan"][ipAddress]["addresses"]["mac"]

                    # CHECK DATABASE IF DATA WAS PREVIOUSLY INSERTED
                    if not self.checkDatabase(ipAddress):

                        resultData = {
                            "ipAddress": ipAddress,
                            "hostName": hostName,
                            "macAddress": macAddress,
                            "state": "up",
                            "osName": "NULL",
                            "osFamily": "NULL",
                            "osVersion": "NULL",
                            "osAccuracy": "NULL",
                            "timeStamp": timeStamp
                        }
                        
                        self.insertData(resultData)
                    
                    else:

                        # UPDATE ITS LAST SEEN TIME STAMP
                        resultData = {
                            "ipAddress": ipAddress,
                            "timeStamp": timeStamp,
                            "state": "up"
                        }
                        
                        self.updateTimeStamp(resultData)
                
            else:
                print("No hosts detected")


def main ():

    hsd = HostDiscovery()
    subnet = "192.168.29.1/24"
    hsd.discoverHostDaemon(subnet)


if __name__ == "__main__":
    main()