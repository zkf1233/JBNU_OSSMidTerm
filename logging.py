import os
import sys

def init(logFileName):
    path = os.path.dirname(os.path.abspath(__file__))

    try:
        tempP=open(path+"/"+logFileName+".log", "a")
    except:
        print("Can't create log file.", file=sys.stderr)
        exit(1)
    else:
        return tempP

def errorLogWrite(errorCode):
    int1 = 2

def operationLogWrite():
    int3 = 3