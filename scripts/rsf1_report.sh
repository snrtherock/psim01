#!/bin/bash
#
# script for creating rsf-1 info for any gateway
###########################################################
HOSTID=$(hostid)
HOSTN=$(hostname)
RSFREPORT=RSF1-$HOSTN-$HOSTID.info
touch $RSFREPORT
echo "Report file for hostid : $HOSTID\n" >> $RSFREPORT
echo "Hostname : $HOSTN\n" >> $RSFREPORT
echo "------pool info------\n" >> $RSFREPORT
zpool status -v >> $RSFREPORT
echo "------network hosts info-----\n" >> $RSFREPORT
cat /etc/hosts >> $RSFREPORT
echo "------ipadm output info------\n" >> $RSFREPORT
ipadm show-addr >> $RSFREPORT
echo "------end report-------\n" >> $RSFREPORT

