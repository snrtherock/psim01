#!/bin/bash -e
#
# Script for initializing logging
##################################################
cd /
mkdir /opt/stratatron
mkdir /opt/stratatron/etc
mkdir /opt/stratatron/bin
chmod 777 /opt/stratatron/etc/
chmod 777 /opt/stratatron/bin/
mkdir /var/log/strata_logs
touch /var/log/strata_logs/init.log
cat <<ENDOC >>/etc/syslog.conf
# STRATATRON MODIFICATION
local5.debug	/var/log/strata_logs/init.log
# END STRATATRON MODIFICATION
ENDOC
svcadm refresh system/system-log
# introduce wait code for refresh process
sleep 10
logger -p local5.debug stratatron
LOG =g$(grep stratatron /var/log/strata_logs/init.log/strata_logs)
LOGENTRY=${LOG:?"Expected log entry missing."}
LOGVALUE=$(awk '{print $10} $LOGENTRY')
if [ $LOGVALUE == "stratatron" ]
then
	echo "logging initialized"
else
	echo "error initializing logging"
fi
