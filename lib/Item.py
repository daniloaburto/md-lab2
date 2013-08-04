# -*- encoding: utf-8 -*-

class Item(object):
    """
    Un ítem está compuesto por un atributo y un valor para dicho atributo
    """
    
    def __init__(self, attribute, value, is_class=False):
        self._attribute = attribute
        self._value = value
        self._is_class = is_class
    
    @property
    def attribute(self):
        return self._attribute
    
    @property
    def value(self):
        return self._value
    
    @property
    def is_class(self):
        """Define si un item es una clase"""
        return self._is_class
    
    def __str__(self):
        return '(%s, %s)' % (self._attribute, self._value)
    
    def __repr__(self):
        return '(%s, %s)' % (self._attribute, self._value)
    
    def __hash__(self):
        return hash((self._attribute, self._value))
    
    def __eq__(self, other):
        return (self.attribute == other.attribute) and (self.value == other.value)