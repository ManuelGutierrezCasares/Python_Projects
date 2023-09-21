from time import time
from datetime import datetime
from os import path
import inspect


"""
Timer usage...

You will call 2 functions:
startTimer and endTimer

1) startTimer will return a float number that must be saved into a variable
    - startTimer takes 1 optional argument (name). If no name is passed, it will default to the script's file name
    - Prints the starting time at the moment of usage
    
2) endTimer will return the elapsed time (float number)
    - endTimer takes 2 variables. 1 mandatory (startTimer return value) and 1 optional (name). If no name is passed, it will default to the script's file name
    - Prints the ending time at the moment of usage
    - Prints the difference between starting and ending time at the moment of usage

    
"""


def getFileName():
    fileName = path.basename(__file__)
    for x in inspect.stack():
        if fileName not in x.filename and "<frozen" not in  x.filename:
            callerName = path.basename(x.filename)
            return callerName



def startTimer(program=None):

    if program == None:
        program = getFileName()

    start_time = time()
    print("Start time of " + program + ": " + str(datetime.now()))
    return start_time


def endTimer(start_time, program=None):

    if program == None:
        program = getFileName()

    end_time = time()
    print("End time of " + program + ": " + str(datetime.now()))
    
    elapsed_time = end_time - start_time
    print("Elapsed time in " + program + ": " + str(elapsed_time))
    return elapsed_time
    
# if __name__ == "__main__":
#     fileName = path.basename(__file__)
#     for x in inspect.stack():
#         print(x.filename)
#         if fileName not in x.filename and "<frozen" not in  x.filename:
#             callerName = path.basename(x.filename)
#             break