from datetime import datetime
import os
import sys

LOG_CODE = {
    '-1' : "Unknown Error",
    '0' : "Success",
    '1' : "Operand Input Error",
    '2' : "Operator Selection Error",
    '3' : "Zero Division Error",
    '4' : ""
}

class logManager:
    def __init__(self):
        self.errLogFile = createLogFile("errlog")
        self.opLogFile = createLogFile("oplog")

    def errorLogWrite(self, code, opstr):
        logWrite(code, opstr, self.errLogFile)
    def opLogWrite(self, code, opstr):
        logWrite(code, opstr, self.opLogFile)

    def __del__(self):
        self.errLogFile.close()
        self.opLogFile.close()

def createLogFile(filename):
    path = os.path.dirname(os.path.abspath(__file__))

    try:
        tempP=open(path+"/"+filename+".log", "a")
    except:
        print("Can't create log file.", file=sys.stderr)
        exit(1)
    else:
        return tempP

def logWrite(code, opstr, filename):
    try:
        filename.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " <%s>" % LOG_CODE[code] + " : " + opstr + "\n")
    except:
        print("*.log doesn't exist | unknown")
        exit(1)

