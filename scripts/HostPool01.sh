#!/bin/bash -e
# script to create ZPool
###############################################################################
set -e # exit on command errors (so you MUST handle exit codes properly!)

zpool create HostPool01 mirror c15t50011731002AD5E6d0 c15t50011731002AD49Ad0
echo "Zpool created"
zpool add HostPool01 mirror c14t50011731002ACDF9d0 c15t50011731002AD45Ad0
echo "Zpool vdev2 created"
zpool add HostPool01 mirror c15t50011731002ACF22d0 c15t50011731002AD1BEd0
echo "zpool vdev3 created"
zpool add HostPool01 mirror c15t50011731002AD286d0 c15t50011731002AD182d0
echo "zpool vdev4 created"
zpool add HostPool01 log mirror c13t5000A72A30097E08d0 c13t5000A72A30097E03d0
echo "zpool log device added"


    