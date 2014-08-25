#!/bin/bash -e
#
# Script for creating hostpool02
##################################################
logger -p local5.debug creating zpool hostpopol02
zpool create hostpool02 mirror c15t50011731002AD49Ad0 c15t50011731002AD506d0
echo "zpool hostpool02 created"
zpool add hostpool02 mirror c14t50011731002ACD95d0 c14t50011731002ACB69d0
echo "vdev 1 created"
zpool add hostpool02 mirror c13t50011731002AD2F6d0 c13t50011731002ACB79d0
echo "vdev 2 created"
zpool add hostpool02 mirror c16t50011731002AD452d0 c16t50011731002ACCDEd0
echo "vdev 3 created"
zpool add hostpool02 mirror c15t50011731002AD5E6d0 c15t50011731002AD45Ad0
echo "vdev 4 created"
zpool add hostpool02 mirror c14t50011731002ACDF9d0 c14t50011731002ACBB5d0
echo "vdev 5 created"
zpool add hostpool02 mirror c13t50011731002ACF7Ad0 c13t50011731002ACEC9d0
echo "vdev 6 created"
zpool add hostpool02 mirror c16t50011731002ACC0Ed0 c16t50011731002AD1AEd0
echo "vdev 7 created"
zpool add hostpool02 log mirror c13t5000A72A30097E08d0 c16t5000A72B30097E14d0
echo "slog created"
logger -p local5.debug hostpool02 creation complete
zpool status -v hostpool02 > /opt/stratatron/etc/hostpoolstatus.log

