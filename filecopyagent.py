# FileCopyAgent.py class
# Author:  Christopher Upkes
# property of Stratatron, LLC


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
        self.name = agentName
        self.configManager = configurationmanager.ConfigurationManager(configfilepointer)
        self.start = start
        self.initEnvironment()

    def getName(self) :
        return self.name

    def setName(self, name) :
        self.name = name

    def updateInitFile(self,configfilepoiner) :
        self.configManager.updateConfig(configfilepointer)

    def startAgent(self) :
        # start and initialize agent
        reportFile = open(self.reportFile, 'w')
        todayNow = datetime.datetime.now()
        reportFile.write('Agent Test Report ' + todayNow.strftime('%Y-%m-%d %H:%M'))
        reportFile.write('\nInitiating file copy ...\n')
        timeStart = datetime.datetime.now()
        shutil.copy2(self.copyFile, self.destFile)
        timeStop = datetime.datetime.now()
        copyDuration = timeStop - timeStart
        fileSizeInBytes = os.path.getsize(self.copyFile)
        fileSize = fileSizeInBytes / 1048576
        copySpeed = fileSize / copyDuration.seconds
        reportFile.write('File copy started @ ' + str(timeStart) + ' \n')
        reportFile.write('File copy completed @ ' + str(timeStop) + ' \n')
        reportFile.write('Test duration was ' + str(copyDuration.seconds) + ' seconds ')
        reportFile.write('and ' + str(copyDuration.microseconds) + ' microseconds\n')
        reportFile.write('Copy throughput was ' + str(copySpeed) + ' MBs per second\n')
        reportFile.close()

    def initEnvironment(self) :
        self.platform = sys.platform
        self.copyFile = self.configManager.getSectionParameter('filecopyparams','copyfile')
        self.destFile = self.configManager.getSectionParameter('filecopyparams','destfile')
        self.reportFile = self.configManager.getSectionParameter('reportparams','reportfile')
            
        

    def stopAgent(self) :
        # stop agent  Needs to be implemented
        None


    
        

    
