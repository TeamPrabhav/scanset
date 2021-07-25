import os
import sqlite3


class Database:

    conn = None
    c = None

    def __init__(self):

        os.chdir("..")
        if not os.path.isdir("databases"):
            os.mkdir("databases")

        os.chdir("databases")

        self.conn = sqlite3.connect("hostInfo.db")
        self.c = self.conn.cursor()
        with self.conn:
            self.c.execute("""CREATE TABLE IF NOT EXISTS 
                host_data (
                    ipAddress TEXT,
                    hostName TEXT,
                    macAddress TEXT,
                    state TEXT,
                    osName TEXT,
                    osFamily TEXT,
                    osVersion TEXT,
                    osAccuracy TEXT,
                    timeStamp TEXT
            )""")

    
    def insertData (self, data):

        with self.conn:
            self.c.execute("""INSERT INTO host_data VALUES (
                :ipAddress,
                :hostName,
                :macAddress,
                :state,
                :osName,
                :osFamily,
                :osVersion,
                :osAccuracy,
                :timeStamp)""", data)


    def updateData (self, data):

        with self.conn:
            self.c.execute("""UPDATE host_data SET timeStamp = :timeStamp
                WHERE ipAddress = :ipAddress""", data)


    def updateOSInfo (self, data):

        with self.conn:
            self.c.execute("""UPDATE host_data SET
                osName = :osName, osFamily = :osFamily,
                osVersion = :osVersion, osAccuracy = :osAccuracy
                WHERE ipAddress = :ipAddress""", data)

    def checkHost (self, ipAddress):

        with self.conn:
            self.c.execute("""SELECT count(*) FROM host_data
                WHERE ipAddress = :ipAddress""", {"ipAddress": ipAddress})
            data = self.c.fetchone()[0]

            if data == 0:
                return False
            else:
                return True


    def getIPList (self):
        with self.conn:
            self.c.execute("SELECT ipAddress FROM host_data")
            return self.c.fetchall()

    def getOS (self, ipAddress):
        with self.conn:
            self.c.execute("""SELECT osName FROM host_data
                WHERE ipAddress = :ipAddress""", {"ipAddress":ipAddress})
            return self.c.fetchone()
    
    def showDBDaemon (self):
        
        while True:
            with self.conn:
                self.c.execute("SELECT ipAddress, state, timeStamp FROM host_data")
                for data in self.c.fetchall():
                    print(data)


def main ():

    db = Database()
    # db.showDBDaemon()


if __name__ == "__main__":
    main()