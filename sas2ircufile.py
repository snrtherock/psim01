# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:24:10 2014
@description:  Sas2ircu file wrapper
@author: christopherupkes
@owner: Stratatron,LLC

"""
import filepointer
import sys
import shutil
import re
import fileScanner

class UnknownDataException( Exception ): pass

class Sas2ircuFile (filepointer):
    def _init_(self):
        self._enclosers = None
        self._controllers = None
        self.parseSystemData()
        
    @property
    def enclosers(self):
        return self._enclosers
    
    def initPatternObjects(self):
        # update compile methods with functionl regex
        self._controllerPatObj = re.compile('controller')
        self._enclosurePatObj = re.compile('enclosure')
        
#==============================================================================
# the parseSystemData routine will parse the Sas2Ircu output  
# and then populate the enclosures and controllers lists
#==============================================================================
    def parseSystemData(self, line):
        # TO_DO:  Include controller and enclosure parsing logic
        matchobj = self._controllerPatObj.match(line[0])
        if matchobj.group(1) == 'x' : print('success')
        else:
            raise UnknownDataException(line)
        self.delegate(Sas2ircuFile.parseSystemData)

#==============================================================================
# we use a delegate function to complete initiate the file scan
#==============================================================================
    def delegate(delegator):
            fileScanner(filepointer.fileName,delegator)
            
            
        
        