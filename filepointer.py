# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:19:27 2014
@description:  base file pointer class
@author: christopherupkes
@owner: Stratatron,LLC

"""

class FilePointer  :
    def __init__(self, name, path) :
        self._filePath = path
        self._fileName = name
        
    @property     
    def filePath(self) :
        return self._filePath
        
    @property
    def fileName(self) :
        return self._fileName

