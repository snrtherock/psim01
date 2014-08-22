import configparser
from configfilepointer import ConfigFilePointer


class ConfigurationManager :
    def __init__(self, cfpointer) :
        self.configFile = cfpointer
        self.config = configparser.ConfigParser()
        self.config.read(cfpointer.fileName)         

    def validateConfigFiles(self) :
        None
        
    def updateConfig(self, configFileName, configFile) :
        None

    def deleteConfig(self, configFileName) :
        None

    def addConfig(self, configFile) :
        None

    def getSectionParameter(self, section, key) :
        return self.config.get(section,key)


        
        
        

    
        
