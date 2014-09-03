# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:08:09 2014
@description:  Base OS Agent class
@author: christopherupkes
@owner: Stratatron,LLC

"""

import configfilepointer
import configurationmanager
import os
import sys
import datetime
import string
import shutil

# basic os agent class
class Agent:
    def __init__(self, agentName, configfilepointer, fileType='config', start=False) :
        self._name = agentName
        if fileType == 'config' :
            self.configManager = configurationmanager.ConfigurationManager(configfilepointer) 
        else :
            self.configManager = None
        self.initEnvironment()
        self.reportFile = 'AgentReport.txt'

    @property
    def name(self) :
        return self._name
        
    @name.setter
    def name(self, value) :
        self._name = value

    def updateInitFile(self,configfilepoiner) :
        self.configManager.updateConfig(configfilepointer)

    def startAgent(self) :
        # start and initialize agent
        reportFile = open(self.reportFile, 'w')
        todayNow = datetime.datetime.now()
        reportFile.write('Agent Init Test Report ' + todayNow.strftime('%Y-%m-%d %H:%M'))
        reportFile.close()

    def initEnvironment(self) :
        self.platform = sys.platform                 
        

    def stopAgent(self) :
        # stop agent  Needs to be implemented
        None
        
    def fileScanner(self, counter, fileName, function):
        file = open(fileName, 'r')
        while True:
            line = file.readline()
            if not line: break
            function(counter, line)
            counter =  counter + 1
            if counter > 5: break
        file.close()
