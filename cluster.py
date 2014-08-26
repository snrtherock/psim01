# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:29:47 2014
@description:  
@author: christopherupkes
@owner: Stratatron,LLC

"""

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
        
    
    
    
        
        