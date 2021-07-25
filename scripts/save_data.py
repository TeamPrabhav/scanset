import json
import pandas as pd
from datetime import datetime

class SaveData:

    hostInfo = pd.DataFrame(columns=[
        "IP Address", "Host Name", "Mac Address", "OS Name",
        "OS Family", "OS Version", "Accuracy", "Last Seen"])


    # SAVE GATHERED DATA AS JSON FILE
    def saveData (self, resultData):

        now = datetime.now()
        dateTime = now.strftime("%I-%M-%S %p")
        fileName = "scan_result_" + str(dateTime) + ".json"

        out_file = open(fileName, "w")
        json.dump(resultData, out_file)