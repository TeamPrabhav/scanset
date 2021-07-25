import nmap
from database import Database

class OSScanner:

    def updateData (self, resultData):

        db = Database()
        db.updateOSInfo(resultData)
        print("IP: %s - OS: %s" %(resultData["ipAddress"], resultData["osName"]))

    # RETRIEVE OS DATA OF INPUT IP ADDRESS
    def osScanDaemon (self):

        db = Database()
        ipList = db.getIPList()

        while True:

            for ipAddress in ipList:

                ipAddress = ipAddress[0]
                detectedOS = db.getOS(ipAddress)
                detectedOS = detectedOS[0]
                
                if detectedOS == "NULL":

                    print("Scanning %s..." % ipAddress)

                    nm = nmap.PortScanner()
                    result = nm.scan(ipAddress, arguments="-O")

                    if bool(result["scan"]):

                        for ipAddress in result["scan"]:

                            osName = "NULL"
                            osFamily = "NULL"
                            osVersion = "NULL"
                            osAccuracy = "NULL"

                            if bool(result["scan"][ipAddress]["osmatch"]):
                                osName = result["scan"][ipAddress]["osmatch"][0]["name"]
                                osFamily = result["scan"][ipAddress]["osmatch"][0]["osclass"][0]["osfamily"]
                                osVersion = result["scan"][ipAddress]["osmatch"][0]["osclass"][0]["osgen"]
                                osAccuracy = result["scan"][ipAddress]["osmatch"][0]["accuracy"]

                            resultData = {
                                "ipAddress": ipAddress,
                                "osName": osName,
                                "osFamily": osFamily,
                                "osVersion": osVersion,
                                "osAccuracy": osAccuracy
                            }
                        
                            self.updateData(resultData)

                else:
                    print("IP: %s - OS: %s" %(ipAddress, detectedOS))


def main ():

    osc = OSScanner()
    osc.osScanDaemon()


if __name__ == "__main__":
    main()