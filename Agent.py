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
    def __init__(self, agentName, configfilepointer, start=False) :
        self._name = agentName
        self.configManager = configurationmanager.ConfigurationManager(configfilepointer)
        self.start = start
        self.initEnvironment()

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