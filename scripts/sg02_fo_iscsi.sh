#!/bin/bash
#
# script for creating iscsi storage for gateway02
###########################################################
#
# create volume section
#
HG=xpool-archive3-4hg
echo "hostgroup name is: $HG"
#
zfs create -V 10T archivepool03/vols/vol2
echo "volume created"
logger -p local5.debug archivepool03/vols/vol2 volume created at 10 TB
#
# create LUN section
#
output=$(sbdadm create-lu /dev/zvol/rdsk/archivepool03/vols/vol2 | awk '{print $1;}')
uuid=$(echo $output | awk '{print$4;}')
#
# remember to create the view with a reference to the host group
#
stmfadm add-view -h $HG $uuid
#
# stmfha update archivepool03 # use this if RSF-1 is installed and running
#
logger -p local5.debug lun uuid $uuid created
echo lun uuid is $uuid