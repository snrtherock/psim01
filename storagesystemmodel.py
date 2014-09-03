# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 12:35:16 2014
@description: storagesystemmodel model library file
@author: christopherupkes
@owner: Stratatron,LLC

"""
#==============================================================================
#  Network interface wrapper class
#==============================================================================
class Interface( object ) :
    def _init_(self, name, ifType, physName, address=None) :
        self._name = name
        self._ip4_address = address
        self._physName = physName
        self._ifType
        
    @property
    def ip4_address(self) :
        return self._ip4_address

    @ip4_address.setter
    def ip4_address(self, value) :
        self._ip4_address = value

    @ip4_address.deleter
    def ip4_address(self) :
        del self._ip4_address


    @property
    def name(self) :
        return self._name

    @name.setter
    def name(self, value) :
        self._name = value

    @name.deleter
    def name(self) :
        del self._name
        

    @property
    def ifType(self) :
        return self._ifType

    @ifType.setter
    def ifType(self, value) :
        self._ifType = value

    @ifType.deleter
    def ifType(self) :
        del self._ifType


    @property
    def physName(self) :
        return self._physName

    @physName.setter
    def physName(self, value) :
        self._physName = value

    @physName.deleter
    def physName(self) :
        del self._physName
        
#==============================================================================
#  Network interface list collection wrapper class
#==============================================================================

class NodeInterfaceList( object ) :
    def _init_( self, interfaceList) :
        self._interfaces = interfaceList

    @property
    def interfaces( self ) :
        return self._interfaces

#    @interfaces.setter
#    def interfaces( self, value) :
#        self._interfaces = value

    @interfaces.deleter
    def interfaces( self ) :
        del self.interfaces

    def removeInterface( self, value ) :
        self._interfaces.remove(value) # add exception handling

    def addInterface( self, value ) :
        self._interfaces.append(value) # add exception handling

#==============================================================================
#  JbodNode model class
#==============================================================================

class JbodNode :
    def _init_( self, wwn, nodeType, capacity=None, mfgr=None, shelf=None, slot=None) :
        self._wwn = wwn
        self._capacty = capacity
        self._mfgr = mfgr
        self._nodeType = nodeType
        self._shelf = shelf
        self._slot = slot

    @property
    def nodeId( self ) :
        return self._wwn
# default property value needs to be dynamically assigned
    @property
    def capacity( self ) :
        if self.nodeType == 'SSD' :
            self._capacity = 200
        else: self._capacity = 300000
        return self._capacity

    @property
    def mfgr( self ) :
        return self._mfgr

    @property
    def nodeType( self ) :
        return self._nodeType
    
    @property
    def shelf( self ) :
        return self._shelf
        
    @shelf.setter
    def shelf( self, value ) :
        self._shelf = value
    
    @property
    def slot( self ) :
        return self._slot
        
    @slot.setter
    def slot( self, value ) :
        self._slot = value
        
#==============================================================================
# jbodNode collection wrapper class
#==============================================================================

class JbodNodeList( object ) :
    def _init_( self , nodes) :
        self._nodes = nodes

    @property
    def nodes( self ) :
        return self._nodes

    def addNode( self, value ) :
        self._nodes.append(value)

    def removeNode( self, value ) :
        self._nodes.remove(value)
        
#==============================================================================
#  clusterNode model classs
#==============================================================================

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
        
#==============================================================================
#  cluster model class
#==============================================================================

class Cluster :
    def _init_( self, nodeList, name ) :
        self._nodeList = nodeList
        self._name = name
        
    @property
    def nodeList( self ) :
        return self._nodeList
    
    def addNode( self, node ) :
        self._nodeList.append( node )
    
    def removeNode( self, node ) :
        self._nodeList.remove( node )

#==============================================================================
#  Storage Controller model class
#==============================================================================




