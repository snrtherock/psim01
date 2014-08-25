#!/bin/bash -e
#
# Script for creating archivepool01 vols
##################################################
logger -p local5.debug creating vols iscsi subdirectory
# check for existence of pool and any conflicting dataset
#hostpool = $(zpool list $1 | grep $1 | awk ' { print $1 }'
#pool = ${hostpool:?"Hostpool $1 not found"}
zfs create archivepool01/vols
echo "dataset vols created"
logger -p local5.debug vols subdirectory created
# test value from showmount -e for completion