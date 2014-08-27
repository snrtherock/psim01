# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:59:47 2014
@description:  Template Scanner delegate function
@author: christopherupkes
@owner: Stratatron,LLC

"""

def templateScanner( templateName, function):
    file = open(templateName, 'r')
    while True:
        line = file.readline()
        if not line: break
        function(line)
    file.close()