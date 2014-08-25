#!/bin/bash
#
# script for creating iscsi storage for gateway02
###########################################################
#
# create host group section
#
HG=xpool-archive3-4hg
echo "hostgroup name is: $HG"
stmfadm create-hg $HG
echo "created hostgroup $HG"
#
# add initiators to new host group
while read IQN
do
stmfadm add-hg-member -g $HG $IQN
logger -p local5.debug $IQN added to $HG
echo "added $IQN to $HP"
done < iqns.dat
logger -p local5.debug hostgroup $HG init complete
echo "done"
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
logger -p local5.debug archivepool03/vols/vol1 volume created at 115 TB
#
# create LUN section
#
output=$(sbdadm create-lu /dev/zvol/rdsk/archivepool03/vols/vol1 | awk '{print $1;}')
uuid=$(echo $output | awk '{print$4;}')
#
# remember to create the view with a reference to the host group
#
stmfadm add-view -h $HG $uuid
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
logger -p local5.debug archivepool04/vols/vol1 volume created at 130 TB
echo "volume created"
#
# create LUN section
#
output2=$(sbdadm create-lu /dev/zvol/rdsk/archivepool04/vols/vol1 | awk '{print $1;}')
uuid2=$(echo $output2 | awk '{print$4;}')
#
# remember to create the view with a reference to the host group
#
echo "executing the command stmfadm add-view -
stmfadm add-view -h $HG $uuid2
#
# stmfha update archivepool04 # use this if RSF-1 is installed and running
#
logger -p local5.debug lun uuid $uuid2 created
echo lun uuid is $uuid2
