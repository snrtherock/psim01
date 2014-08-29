# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 10:57:49 2014
@description:  System Data Collector os agent subclass
@author: christopherupkes
@owner: Stratatron,LLC

"""
from Agent import Agent

class SystemDataCollector( Agent ):
    def __init__(self, agentName, configfilepointer, fileType='report', start=False):
        self._diskDataReport = None
        
        Agent.__init__(self, agentName, configfilepointer, fileType, start)
        self._records = []
        self._record = []
        
                
        
        
    def collectReportData(self):
        pass
        
    def fileScanner(self, counter, fileName, function) :
        Agent.fileScanner(self, counter, fileName, function)
    
    @property
    def records ( self ):
        return self._records
    
    @property
    def record ( self ) :
        return self._record
        
