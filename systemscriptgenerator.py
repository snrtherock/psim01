# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:39:48 2014
@description:  System Script Generator agent subclass
@author: christopherupkes
@owner: Stratatron,LLC

"""
import Agent

#==============================================================================
# This class generates bash shell scripts from object data
#==============================================================================
class SystemScriptGenerator( Agent ):
    def _init_( self, sciptDir='../scripts', templateDir='../templates' ):
        self._scriptDir = scriptDir
        self._templateDir = templateDir
    # default directories are the scripts and templates directories
    @property
    def scriptDir( self ):
        return self._scriptDir
    
    @scriptDir.setter
    def scriptDir( self, value ):
        self._scriptDir = value
        
    @property
    def templateDir( self ):
        self._templateDir
    
    @templateDir.setter
    def templateDir( self, value ):
        self._templateDir = value
        
    # load the template and generate the creation scripts based on cluster data    
    def genClusterScript( self, cluster ):
        # TO_DO implement cluster scripting code
        # TO_DO use delegate pattern for template value replacement
        None
    
    def genStorageSystemScript( self, storageSystem ):
        # TO_DO implement storage system scripting code
        # TO_DO use delegate pattern for template value replacement
        None
        
