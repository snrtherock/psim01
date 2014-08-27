#!/bin/bash -e
#
# Script for creating archivepool01
##################################################
logger -p local5.debug creating zpool archivepool01
zpool create archivepool01 raidz2 c0t5000C50057B04167d0 c0t5000C50057B040FBd0 c0t5000C50057B0AC57d0 c0t5000C50057AE4617d0 c0t5000C50057AE68CBd0 c0t5000C50057AF7B7Bd0 c0t5000C50057BBE863d0 c0t5000C50057BC696Fd0
echo "zpool archivepool01 created"
zpool add -f archivepool01 raidz2 c0t5000C50057AE26B7d0 c0t5000C50057B0AC7Fd0 c0t5000C50057B03FF7d0 c0t5000C50057AE49F3d0 c0t5000C50057B0448Bd0 c0t5000C50057B038A3d0 c0t5000C50057AE30FFd0 c0t5000C50057AE4AA3d0
echo "zpool vdev1 created"
zpool add -f archivepool01 raidz2 c0t5000C50057AE5F3Fd0 c0t5000C50057B059BFd0 c0t5000C50057B0463Fd0 c0t5000C50057AE4323d0 c0t5000C50057B05597d0 c0t5000C50057B056EFd0 c0t5000C50057AE2CDBd0 c0t5000C50057AE277Bd0
echo "zpool vdev2 created"
zpool add -f archivepool01 raidz2 c0t5000C50057B03417d0 c0t5000C50057B05557d0 c0t5000C50057B092F7d0 c0t5000C50057B086EBd0 c0t5000C50057B044B7d0 c0t5000C50057B0449Fd0 c0t5000C50057AF7B4Fd0 c0t5000C50057B02F8Bd0
echo "zpool vdev3 created"
zpool add -f archivepool01 raidz2 c0t5000C50057B0375Bd0 c0t5000C50057AFF32Bd0 c0t5000C50057B054C3d0 c0t5000C50057B03F63d0 c0t5000C50057AE6A43d0 c0t5000C50057B0500Bd0 c0t5000C50057AE1FA7d0 c0t5000C50057AE49D3d0
echo "zpool vdev4 created"
zpool add -f archivepool01 raidz2 c0t5000C50057B043CFd0 c0t5000C50057B0412Bd0 c0t5000C50057B04717d0 c0t5000C50057B03D27d0 c0t5000C50057AE6787d0 c0t5000C500579D25DFd0 c0t5000C50057B03AFFd0 c0t5000C50057B086FBd0
echo "zpool vdev5 created"
zpool add -f archivepool01 raidz2 c0t5000C50057B093E7d0 c0t5000C50057AE6F77d0 c0t5000C50057B046B3d0 c0t5000C50057AE464Fd0 c0t5000C50057AE697Bd0 c0t5000C50057B05053d0 c0t5000C50057B0886Fd0 c0t5000C50057B0338Bd0
echo "zpool vdev6 created"
zpool add -f archivepool01 raidz2 c0t5000C50057B046FFd0 c0t5000C50057AE1B8Fd0 c0t5000C50057B03FE3d0 c0t5000C50057AE47EBd0 c0t5000C50057AE4967d0 c0t5000C50057B06733d0 c0t5000C50057B0AC6Fd0 c0t5000C50057B05D53d0
echo "zpool vdev6 created"
zpool add -f archivepool01 raidz2 c0t5000C50057AE436Fd0 c0t5000C50057B09553d0 c0t5000C50057AE22FFd0 c0t5000C50057AE467Bd0 c0t5000C50057B034ABd0 c0t5000C50057B094A7d0 c0t5000C50057B04553d0 c0t5000C50057B03DB7d0
echo "zpool vdev7 created"
logger -p local5.debug archivepool01 created
zpool status -v archivepool01 > /opt/stratatron/etc/archivepoolstatus.logging
ls 