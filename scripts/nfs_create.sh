#!/bin/bash -e
#
# Script for creating hostpool01/hostnfs01
##################################################
logger -p local5.debug creating hostnfs01
# check for existence of pool and any conflicting dataset
#hostpool = $(zpool list $1 | grep $1 | awk ' { print $1 }'
#pool = ${hostpool:?"Hostpool $1 not found"}
zfs create hostpool01/hostnfs01
echo "dataset hostnfs01 created"
zfs set share.nfs=on hostpool01/hostnfs01
echo "dataset shostnfs01 shared"
chmod 777 /hostpool01/hostnfs01
# test value from showmount -e for completion