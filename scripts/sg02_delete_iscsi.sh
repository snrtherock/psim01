#!/bin/bash
#
# script for creating iscsi storage for gateway02
###########################################################
stmfadm list-lu  | awk '{ print $3 }' > luns.temp
while read LUN
do
	stmfadm delete-lu $LUN
	logger -p local5.debug deleting lun $LUN
	echo "deleting lun $LUN"
done < luns.temp
HG=$(stmfadm list-hg | awk '{ print $3 }')
if [ -n $HG ]
then
	stmfadm delete-hg $HG
	logger -p local5.debug deleting hg $HG
	echo "deleting hostgroup $HG"
fi
zfs destroy -r archivepool03/vols
logger -p local5.debug destroying archivepool03/vols
echo "destroying archivepool03/vols/"
zfs destroy -r archivepool04/vols
logger -p local5.debug destroying archivepool03/vols
echo "destroying archivepool03/vols"


