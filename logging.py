from datetime import datetime
import os
import sys

# String for error or operation write log file
LOG_CODE = {
    '-1' : "Unknown Error",
    '0' : "Success",
    '1' : "Operand Input Error",
    '2' : "Operator Selection Error",
    '3' : "Zero Division Error",
    '4' : "..."
}

class logManager:
    def __init__(self):
        # print("Logmanager init")
        self.errLogFile = createLogFile("errlog")
        self.opLogFile = createLogFile("oplog")

    def errorLogWrite(self, code, opstr):
        self.errLogFile = createLogFile("errlog")
        logWrite(code, opstr, self.errLogFile)
    def opLogWrite(self, code, opstr):
        self.opLogFile = createLogFile("oplog")
        logWrite(code, opstr, self.opLogFile)

    def __del__(self):
        # print("Logmanager close")
        self.errLogFile.close()
        self.opLogFile.close()

# Create *.log file in folder *.py is running
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
        # print("write.............")
        filename.write("{0} <{1}> : {2}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S") , str(LOG_CODE[code]), opstr))
        filename.close()
    except:
        print("*.log doesn't exist | unknown")
        exit(1)

