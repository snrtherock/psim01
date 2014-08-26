# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 08:48:56 2014
@description:  clusterNode class file
@author: christopherupkes
@owner: Stratatron,LLC

"""
class ClusterNode :
    def _init_( self, number, nodeID, name, nodeInterfaceList=None, peer=None ) :
        self._number = number
        self._nodeId = nodeID
        self._name = name
        self._nodeInterfaceList = nodeInterfaceList
        self._peer = peer
        
    @property
    def number( self ) :
        return self._number
    
    @property
    def nodeId( self ) :
        return self._nodeID
        
    @property
    def name( self ) :
        return self._name
        
    @property
    def nodeInterfaceList( self ) :
        return self._nodeInterfaceList
        
    @property
    def peer( self ) :
        return self._peer
        
    @peer.setter
    def peer( self, value ) :
        self._peer = value
    
    @peer.deleter
    def peer( self ) :
        del self._peer
        
    def validateHeartbeat( self ) :
        None
        # TO_DO validate heartbeat ips to ensure in same subnet
    
    
        
    
