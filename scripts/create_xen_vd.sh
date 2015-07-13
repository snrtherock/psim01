#!/bin/bash
#
# script for creating a virtual disk from a xen SR
###########################################################
# name of the Storage Repository
storage_name="Local storage"
# name of the Virtual Machine
vm_name="test"
# position of the Virtual Disk
position=6
# get the UUID of the local Storage Repository (SR): xe sr-list
srlist=$(xe sr-list name-label=$storage_name | awk '{print $5;}')
SR=$(echo $srlist | awk '{print $1;}')
# Get the UUID of the VM you want to attach the disk to: xe vm-list
vmlist=$(xe vm-list name-label=$vm_name | awk '{print $5;}')
VM=$(echo $vmlist | awk '{print $1;}')
# Create the Virtual Disk (VDI) xe vdi-create
VDI=$(xe vdi-create sr-uuid=$SR | awk '{print $1;}')
# Create the Virtual Block Device (VBD) that the connects the VDI to the VM. xe vbd-create
VBD=$(xe vbd-create vm-uuid=$VM device=$position vdi-uuid=$VDI bootable=false mode=RW type=Disk | awk '{print $1;}')
# Plug the VBD into the VM. aka "Activate". xe vbd-plug
# At this point, the new disk will show up in XenCenter, but "Active" will say "No" and the Activate button will be available.
# You should be able to activate just fine here. This actually runs the xe vbd-plug command. You could run this command manually too.
# uncomment line below to run manually.
# xe vbd-plug uuid=$VBD

