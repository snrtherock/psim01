# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 13:06:28 2014
@description:  
@author: christopherupkes
@owner: Stratatron,LLC

"""


class UnknownCommand(Exception) : pass
    
def processLine(line):
    if line[0] == 'x':
        print("success")
    else:
        raise UnknownCommand(line)
def fileScaner(fileName, function):
    file = open(fileName, 'r')
    while True:
        line = file.readline()
        if not line: break
        function(line)
    file.close()
    
filename = '../data/data.txt'
fileScanner(filename, processLine)