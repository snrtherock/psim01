# class:  inteface.py
# description:  wrapper class for network interface
# Author: Christopher Upkes
# Owner:  Stratatron, LLC
#
class Interface( object ) :
    def _init_(self, name, address=None) :
        self._name = name
        self_ip4_address = address
        
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
        
        
        


