#!/bin/bash -e
#
# Script for creating hostpool01
##################################################
logger -p local5.debug creating zpool hostpopol01
zpool create hostpool01 mirror c14t50011731002ACF21d0 c14t50011731002AD181d0
echo "zpool hostpool01 created"
zpool add hostpool01 mirror c13t50011731002ACD4Ad0 c13t50011731002ACE12d0
echo "vdev 1 created"
zpool add hostpool01 mirror c12t50011731002ACF05d0 c12t50011731002AD592d0
echo "vdev 2 created"
zpool add hostpool01 mirror c15t50011731002AD299d0 c15t50011731002ACFB5d0
echo "vdev 3 created"
zpool add hostpool01 mirror c14t50011731002AD285d0 c14t50011731002AD1BDd0
echo "vdev 4 created"
zpool add hostpool01 mirror c13t50011731002AD482d0 c13t50011731002ACC42d0
echo "vdev 5 created"
zpool add hostpool01 mirror c12t50011731002ACBFDd0 c12t50011731002AD546d0
echo "vdev 6 created"
zpool add hostpool01 mirror c15t50011731002ACC5Dd0 c15t50011731002AD44Dd0
echo "vdev 7 created"
zpool add hostpool01 log mirror c14t5000A72A30097E1Ad0 c13t5000A72B30097E03d0
echo "slog created"
logger -p local5.debug hostpool01 creation complete
zpool status -v hostpool01 > /opt/stratatron/etc/hostpoolstatus.log
