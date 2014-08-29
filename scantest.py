# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 13:06:28 2014
@description:  
@author: christopherupkes
@owner: Stratatron,LLC

"""

from storagesystemmodel import jbodNode
from storagesystemmodel import JbodNodeList
class UnknownCommand(Exception) : pass
    
#==============================================================================
# TO_DO add code to process the line byte by byte and extract all data
#==============================================================================
def processLine(counter, line):
    # parse line    
    parsedLine = line.split(":")
    diskInfo = str(parsedLine[1])
    if 'c' in diskInfo[0] and 't' in diskInfo[3] :
        print("diskID " + str(parsedLine[1]))
        print("diskType " + str(parsedLine[2]))
        # save disk ID value
        # parse diskType from parsedLine[2]
    elif '<SHELF' in diskInfo :
        print("shelf " + str(parsedLine[1]))
        print("location " + str(parsedLine[2]))
        print("slot " + str(parsedLine[3]))
    else:
        print("not a disk")

    
def fileScanner(counter, fileName, function):
    
    file = open(fileName, 'r')
    while True:
        line = file.readline()
        if not line: break
        function(counter, line)
        counter =  counter + 1
        if counter > 5: break
    file.close()

def formatFileParser(disks, counter):
    fileScanner(counter, filename, processLine)
    
disks = JbodNodeList()

counter = 0    
filename = './data/AllDiskInfo.txt'
fileScanner(counter, filename, processLine)