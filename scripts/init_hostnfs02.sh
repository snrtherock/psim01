#!/bin/bash -e
#
# Script for creating hostpool01/hostnfs01
##################################################
logger -p local5.debug creating hostnfs02
# check for existence of pool and any conflicting dataset
#hostpool = $(zpool list $1 | grep $1 | awk ' { print $1 }'
#pool = ${hostpool:?"Hostpool $1 not found"}
zfs create hostpool02/hostnfs02
echo "dataset hostnfs02 created"
zfs set share.nfs=on hostpool02/hostnfs02
echo "dataset hostnfs02 shared"
chmod 777 /hostpool02/hostnfs02
# test value from showmount -e for completion