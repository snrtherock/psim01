# script for automating local and remote file copy operations and capture of metrics
#
#
# PerfMonitory invocation script
# Author:  Christopher Upkes
# property of Stratatron, LLC


import os
import sys
import datetime
import string
import shutil

copyFile = 'CopyTestFile.pmf'
destinationFile = 'CopyTestDestinationFile.pmf'

# initialize all global variables based on platform value
def setGlobals(platform) :
    global localCopyDestination
    global remoteCopyDestination
    if platform == 'darwin' :
        localCopyDestination = '/tmp/'
        remoteCopyDestination = '/export/'
    elif platform == 'win32' :
        localCopyDestination = 'c:\\temp\\'
        remoteCopyDestination = 'e:\\'
    elif platform == 'win64' :
        localCopyDestination = 'c:\\temp\\'
        remoteCopyDestination = 'e:\\temp\\'

# capture platform information
def whereami():
    print ('Setting globals for: ' + sys.platform)
    return sys.platform

# ensure copy file is available
def envCheck() :
    fullFilePath = os.getcwd() + '/' + copyFile
    print (fullFilePath)
    try :
        CopyFileCheck = open(fullFilePath, 'r')
    except :
        print('Could not open copy test file')
        return False
    else :
        CopyFileCheck.close()
        return True
    
# initialize report file for update
def initReportFile(reportFileName):
    if reportFileName == '':
        print ('invalid filename')
        return False
    else :
        return True
    
    
# initialize process for particular platform
def init(platform):
    setGlobals(platform)
    reportFileName = str()
    if platform == 'darwin':
        pid = str(os.getpid())
        print ('PerfMonitor Daemon started.  PID: ' + pid)
        print ('Curent working directory is: ' + os.getcwd())
        fileOk = False
        while not fileOk :
            reportFileName = input('Enter report file name or q to quit => ')
            if reportFileName.capitalize() == 'Q':
                break
            else :
                fileOk = initReportFile(reportFileName)
                reportFileName += '.pmr'
                reportFile = open(reportFileName, 'w')
                reportFile.write('Performance Monitor Report ' +  str(datetime.datetime.now()))
                reportFile.write('\n')
                reportFile.close()
                return reportFileName
    elif platform == 'win32' :
        print ('Hooray for Windows')
    elif platform == 'win64':
        print ('win64')
    else :
        print ('Sorry, unsupported platform')
    return fileName

# make sure remote copy destination is accessible
def validateRemoteDestination(remoteCopyDestination) :
    try:
        remoteDirs = os.listdir(remoteCopyDestination)
    except:
        return False
    else :
        return True
    
# execute local copy test procuedure
# local is defined as copy without using protocol (NFS, iSCSI, etc...)
def runLocalCopyTest(reportFileName) :
    try:
        reportFile = open(reportFileName, 'a')
    except :
        print ('Could not open report file')
    else :
        print ('good to go')
        print ('Copying file to: ' + localCopyDestination)
        now = datetime.datetime.now()
        reportFile.write('File copy starting ' + now.strftime("%Y-%m-%d %H:%M") + '\n')
        timeStart = datetime.datetime.now()
        shutil.copy2(copyFile, localCopyDestination + destinationFile)
        timeStop = datetime.datetime.now()
        copyDuration = timeStop - timeStart
        print (str(copyDuration))
        fileSizeInBytes = os.path.getsize(copyFile)
        fileSize = fileSizeInBytes / 1048576 # default display KB or GB
        print (str(fileSize) + 'MB')
        copySpeed = fileSize / copyDuration.seconds
        print ('Copy speed was ' + str(copySpeed) + ' MB per second\n')
        reportFile.write('File copy test duration = ' + str(copyDuration.seconds) + ' seconds\n')
        reportFile.write('and ' + str(copyDuration.microseconds) + ' microseconds\n')
        reportFile.write('Copy throughput was ' + str(copySpeed) + ' MBs per Second\n')
        reportFile.close()
        
# execute remote copy test procedure
def runRemoteCopyTest(reportFileName) :
    if validateRemoteDestination(remoteCopyDestination) :
        try:
            reportFile = open(reportFileName, 'a')
        except :
            print ('Could not open report file')
        else :
            print ('good to go')
            print ('Copying file to: ' + remoteCopyDestination)
            now = datetime.datetime.now()
            reportFile.write('File copy starting ' + now.strftime("%Y-%m-%d %H:%M") + '\n')
            timeStart = datetime.datetime.now()
            shutil.copy2(copyFile, remoteCopyDestination + destinationFile)
            timeStop = datetime.datetime.now()
            copyDuration = timeStop - timeStart
            print (str(copyDuration))
            fileSizeInBytes = os.path.getsize(copyFile)
            fileSize = fileSizeInBytes / 1048576
            print (str(fileSize) + 'MB')
            copySpeed = fileSize / copyDuration.seconds
            print ('Copy speed was ' + str(copySpeed) + ' MB per second\n')
            reportFile.write('File copy test duration = ' + str(copyDuration.seconds) + ' seconds\n')
            reportFile.write('and ' + str(copyDuration.microseconds) + ' microseconds\n')
            reportFile.write('Copy throughput was ' + str(copySpeed) + ' MBs per Second\n')
            reportFile.close()
    else :
        print ('Could not validate remote copy destination' )

# main method
if envCheck() :
    reportFileName = init(whereami())
    runLocalCopyTest(reportFileName)
    print('Test Complete')
else :
    print ('Configuration error')
