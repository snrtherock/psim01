# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:38:05 2014
@description:  file scanning routine calling delegate
@author: christopherupkes
@owner: Stratatron,LLC

"""
class UnknownToken(Exception) : pass
    
def processLine(line):
    if line[0] != 'x':
        print("success")
    else:
        raise UnknownToken(line)
def fileScanner(fileName, function):
    file = open(fileName, 'r')
    while True:
        line = file.readline()
        print(line)
        if not line: break
        function(line)
    file.close()
    
filename = '../psim01/data/data.txt'
fileScanner(filename, processLine)
