# configfilepointer class
# Author:  Christopher Upkes
# property of Stratatron, LLC

# configuration file wrapper class
class ConfigFilePointer  :
    def __init__(self, fileName, fileType, configType, filePath=None) :
        self.filePath = filePath
        self.fileName = fileName
        self.fileType = fileType # needs to be enumeration
        self.configType = configType # needs to be enumeration

    # no setter functions.  Initilization popluates all properties

    def getFilePath(self) :
        return self.filePath

    def setFilePath(self, filePath) :
        self.filePath = filePath

    def getFileName(self) :
        return self.fileName

    def getFileType(self) :
        return self.fileType

    def getConfigType(self) :
        return self.configType
