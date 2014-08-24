# file:  jbodNodeList.py wrapper class for list of jbodNodes
# Author:  Christopher Upkes
# Owner:  Stratatron, LLC

import jbodNode

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


