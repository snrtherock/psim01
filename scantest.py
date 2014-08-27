# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 13:06:28 2014
@description:  
@author: christopherupkes
@owner: Stratatron,LLC

"""


class UnknownCommand(Exception) : pass
    
#==============================================================================
# TO_DO add code to process the line byte by byte and extract all data
#==============================================================================
def processLine(line):
    if line[0] == 'x':
        print("success")
    else:
        raise UnknownCommand(line)
def fileScanner(fileName, function):
    file = open(fileName, 'r')
    while True:
        line = file.readline()
        if not line: break
        function(line)
    file.close()
    
filename = './data/AllDiskInfo.txt'
fileScanner(filename, processLine)