import threading
from host_discovery import HostDiscovery
from os_scanner import OSScanner
from save_data import SaveData
from database import Database


# MAIN FUNCTION
def main ():

    osc = OSScanner()
    hsd = HostDiscovery()
    db = Database()

    # subnet = str(input("Enter subnet address: "))
    subnet = "192.168.29.1/24"
    hsd.discoverHostDaemon(subnet)
    thread_discoverHostDaemon = threading.Thread(target=hsd.discoverHostDaemon(subnet), daemon=True)
    thread_discoverHostDaemon.start()

    thread_showDBDaemon = threading.Thread(target=db.showDBDaemon(), daemon=True)
    thread_showDBDaemon.start()

    thread_osScanDaemon = threading.Thread(target=osc.osScanDaemon(subnet), daemon=True)
    thread_osScanDaemon.start()

    """
    while True:

        print("Select an option -")
        print("1. Show Data")
        print("2. OS Scan")
        print("3. Exit")

        option = int(input(": "))
        
        if option == 1:
            thread_showDBDaemon = threading.Thread(target=db.showDBDaemon(), daemon=True)
            thread_showDBDaemon.start()
            exitInput = str(input())

            if exitInput == 0:
                thread_showDBDaemon.stop()

        elif option == 2:
            ip = input("Enter IPv4 address: ")
            result = osc.osScan(ip)
            s = SaveData()
            s.saveData(result)
            print(result)

        elif option == 3:
            break

        else:
            print("Invalid option!")
    """


if __name__ == "__main__":
    main()