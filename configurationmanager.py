# configurationmanager class
# Author:  Christopher Upkes
# property of Stratatron, LLC

# manager class for parsing config file values
import ConfigParser
from configfilepointer import ConfigFilePointer

# initialize the manager class by passing a pointer to a confguration file.
class ConfigurationManager :
    def __init__(self, cfpointer) :
        self.configFile = cfpointer
        self.config = ConfigParser.ConfigParser()
        self.config.read(cfpointer.fileName)         

    def validateConfigFiles(self) :
        None # this exception catch requires app specific exceptions to be thrown
        
    def updateConfig(self, configFileName, configFile) :
        None

    def deleteConfig(self, configFileName) :
        None

    def addConfig(self, configFile) :
        None
    # parse configuration key value pairs into section collection class
    def getSectionParameter(self, section, key) :
        return self.config.get(section,key)




        
        
        

    
        
