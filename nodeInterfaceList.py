# file: wrapper class for list of interface object
# Author:  Christopher Upkes
# Owner: Stratatron, LLLC
#
import interface

class NodeInterfaceList( object ) :
    def _init_( self, interfaceList=None) :
        self._interfaces = interfaceList

    @property
    def interfaces( self ) :
        retrn self._interfaces

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

        
        
        
        
