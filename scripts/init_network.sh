#!/bin/bash -e
#
# Script for initializing cluster networking
##################################################
#
#  TODO:  check command line arguments
##################################################
# place code here
#
# TODO:  check for existing networking
##################################################
# place code here
#
# TODO:  ask if user wants to destroy current configuration
##################################################
# place code here
#
# Search for 1gb or 10/100 physical connected links
##################################################
# place code here
#
# Initialize Management 
##################################################
THISHOST = $(hostname)
echo "Available 1Gb management ports for $THISHOST: "
dladm show-phys > /opt/stratatron/etc/networks.temp
grep -w 1000 /opt/stratatron/etc/networks.temp | awk '{ print $1 }'
read -p "please type name of port: "  PORT
if grep -w $PORT  /opt/stratatron/etc/networks.tempech
then
	echo "Port : $PORT validated, creating management IP"
	# dladm create-aggr
	netadm enable -p ncp DefaultFixed
	ipadm create-ip $PORT
	ipadm create-addr -a 192.168.1.5/24 $PORT
	route -p add default 192.168.1.1
	echo "# STRATATRON" >> /etc/hosts
	echo "192.168.1.5		$THISHOST" >> /etc/hosts
	echo "# END STRATATRON" >> /etc/hosts
	DONE
else
	echo "Port not validated, aborting"
fi
##################################################
# place code here
#
# Initialize Heartbeat 
##################################################
sed -e '/$PORT/d' < /opt/stratatron/etc/networks.temp > opt/stratatron/etc/networks.temp
echo "Available 1Gb heartbeat ports for $THISHOST: "
grep -w 1000 /opt/stratatron/etc/networks.temp | awk '{ print $1 }'
read -p "please type name of port: "  PORT
if grep -w $PORT  /opt/stratatron/etc/networks.tempech
then
	echo "Port : $PORT validated, creating heartbeat IP"
	# dladm create-aggr
	# netadm enable -p ncp DefaultFixed
	ipadm create-ip $PORT
	ipadm create-addr -a 192.168.5.1/24 $PORT
	echo "# STRATATRON" >> /etc/hosts
	echo "192.168.5.1/24		$THISHOST" >> /etc/hosts
	echo "# END STRATATRON" >> /etc/hosts
	DONE
	cp /etc/hosts /opt/stratatron/etc/clusteronehosts
else
	echo "Port not validated, aborting"
fi
##################################################
# place code here
#
# Initialize Heartbeat 
##################################################
sed -e '/$PORT/d' < /opt/stratatron/etc/networks.temp > opt/stratatron/etc/networks.temp
echo "Available 10gb storage ports for $THISHOST : "
grep -w 10000 /opt/stratatron/etc/networks.temp | awk '{ print arr[$1], $2}' > opt/stratatron/etc/aggports.temp
PORT1 = $(sed -e '1p' /opt/stratatron/etc/aggports.temp)
PORT1 = ${PORT1:?"Expected aggregate port missing."}
PORT2 = $(sed -e '2p' /opt/stratatron/etc/aggports.temp)
PORT2 = ${PORT2:?"Expected aggregate port missing."}
echo "Creating aggregate"
# dladm create-aggr
dladm create-aggr -L active -l $PORT1 -l $PORT2 aggr0
ipadm create-addr -a 192.168.3.5/24 aggr0
echo "# STRATATRON" >> /etc/hosts
echo "192.168.3.5		$THISHOST" >> /etc/hosts
echo "# END STRATATRON" >> /etc/hosts



#