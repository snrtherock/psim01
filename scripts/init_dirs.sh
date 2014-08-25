#!/bin/bash -e
#
# Script for initializing strataron directories
##################################################
cd /
mkdir /opt/stratatron
mkdir /opt/stratatron/etc
mkdir /opt/stratatron/bin
chmod 777 /opt/stratatron/etc/
chmod 777 /opt/stratatron/bin/

#logger -p local5.debug stratatron directories created

