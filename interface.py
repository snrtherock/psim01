# class:  inteface.py
# description:  wrapper class for network interface
# Author: Christopher Upkes
# Owner:  Stratatron, LLC
#
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
        
        


