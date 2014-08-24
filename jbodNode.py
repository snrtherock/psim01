# File:  jbodNode.py defining the jbodNode class
# Author:  Christopher Upkes
# Owner:  Stratatron, LLC
#
class jbodNode :
    def _init_( self, wwn, capacity, mfgr, nodeType ) :
        self._wwn = wwn
        self._capacty = capacity
        self._mfgr = mfgr
        self._nodeType = nodeType

    @property
    def nodeId( self ) :
        return self._wwn

    @property
    def capacity( self ) :
        return self._capacity

    @property
    def mfgr( self ) :
        return self._mfgr

    @property
    def nodeType( self ) :
        return self._nodeType
    

    
