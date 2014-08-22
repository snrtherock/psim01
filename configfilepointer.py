
class ConfigFilePointer  :
    def __init__(self, fileName, fileType, configType, filePath=None) :
        self.filePath = filePath
        self.fileName = fileName
        self.fileType = fileType
        self.configType = configType

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
