# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:38:05 2014
@description:  file scanning routine calling delegate
@author: christopherupkes
@owner: Stratatron,LLC

"""
def fileScaner(fileName, function):
    file = open(fileName, 'r')
    while True:
        line = file.readline()
        if not line: break
        function(line)
    file.close()
