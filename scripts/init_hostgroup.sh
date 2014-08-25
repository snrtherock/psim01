#!/bin/bash
#
# script for creating xenpool hostgroup
###########################################################
#
# create host group section
#
HG = xenpoolhg
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