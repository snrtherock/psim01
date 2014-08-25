#!/bin/bash
# creation script for vol1 on archivepool03 and vol2 of archivepool04
#
############################################################
# creating vol1 for archivepool03
############################################################
# create dependent file system section
#
zfs create archivepool03/vols
logger -p local5.debug archivepool03/vols created
echo "vols directory created"
#
# create volume section
#
zfs create -V 115T archivepool03/vols/vol1
echo "volume created"
logger -p local5.debug archivepool03/vols/vol1 volume created at 144 TB
#
# create LUN section
#
output=$(sbdadm create-lu /dev/zvol/rdsk/archivepool03/vols/vol1 | awk '{print $1;}')
uuid=$(echo $output | awk '{print$4;}')
#
# remember to create the view with a reference to the host group
#
stmfadm add-view -h xpool-archive3-4hg $uuid
#
# stmfha update archivepool04 # use this if RSF-1 is installed and running
#
logger -p local5.debug lun uuid $uuid created
echo lun uuid is $uuid
############################################################
# creating vol1 for archivepool03
############################################################
# create dependent file system section
#
zfs create archivepool04/vols
logger -p local5.debug archivepool04/vols created
echo "vols directory created"
#
# create volume section
#
zfs create -V 130T archivepool04/vols/vol1
logger -p local5.debug archivepool04/vols/vol1 volume created at 155 TB
echo "volume created"
#
# create LUN section
#
output2=$(sbdadm create-lu /dev/zvol/rdsk/archivepool04/vols/vol1 | awk '{print $1;}')
uuid2=$(echo $output2 | awk '{print$4;}')
#
# remember to create the view with a reference to the host group
#
stmfadm add-view -h xpool-archive3-4hg $uuid2
#
# stmfha update archivepool04 # use this if RSF-1 is installed and running
#
logger -p local5.debug lun uuid $uuid2 created
echo lun uuid is $uuid2
