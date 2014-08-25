#!/bin/bash
#
# script for creating samba storage on storagegateway02
###########################################################
echo "enabling samba service"
svcadm enable -r smb/server
sleep 5
logger -p local5.debug started samba service
#################################################
# uncomment below if windows workgroup is different from WORKGROUP
# smbadm join -w workgroup-name
echo "updating pam config file"
echo password required	pam_smb_passwd.so.1	nowarn >> /etc/pam.d/other
logger -p local5.debug added password line to /etc/pam.d/other file
echo "creating pam file for tron"
# passwd tron
# logger -p local5.debug created pam file for user tron
echo "creating zfs dataset smb01"
zfs create -o nbmand=on archivepool03/smb01
sleep 5
zfs set quota=10T archivepool03/smb01
logger -p local5.debug created zfs dataset archivepool03/smb01
echo "dataset created"
echo "setting dataset share properties"
zfs set share.smb=on archivepool03/smb01
zfs set share.smb.csc=auto archivepool03/smb01
# comment below if you want strict user access to samba shares
zfs set share.smb.guestok=on archivepool03/smb01
chmod 777 /archivepool03/smb01
echo "smb01 done"
echo "creating zfs dataset smb02"
zfs create -o nbmand=on archivepool04/smb02
sleep 5
zfs set quota=10T archivepool04/smb02
logger -p local5.debug created zfs dataset archivepool04/smb02
echo "dataset created"
echo "setting dataset share properties"
zfs set share.smb=on archivepool04/smb02
zfs set share.smb.csc=auto archivepool04/smb02
# comment below if you want strict user access to samba shares
zfs set share.smb.guestok=on archivepool04/smb02
chmod 777 /archivepool04/smb02
echo "smb01 done"
zfs get all > /opt/stratatron/etc/zfsdatasetproperties.log
