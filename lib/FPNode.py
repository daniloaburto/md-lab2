# -*- encoding: utf-8 -*-

class FPNode(object):
    """
    Un nodo puede ser usado como lista enlazada o árbol
    """
    
    def __init__(self, item):
        self._item = item
        self._support_count = 1
        self._parent = None
        self._next = None
        self._children = {}
    
    def increment(self, count=1):
        self._support_count += count
    
    def add(self, child):
        child.parent = self
        self._children[child.item] = child
    
    def add_linkedlist(self, node):
        temp = self
        while temp.next:
            temp = temp.next
        temp.next = node
    
    @property
    def children(self):
        return self._children
    
    @property
    def item(self):
        return self._item
    
    @property
    def support_count(self):
        return self._support_count
    
    def next():
        doc = "Retorna el siguiente nodo de la lista enlazada o None"
        
        def fget(self):
            return self._next
        
        def fset(self, node):
            self._next = node
            
        return locals()
    next = property(**next())
    
    def parent():
        doc = "Retorna el nodo padre o None"
        
        def fget(self):
            return self._parent
        
        def fset(self, parent):
            self._parent = parent
        
        return locals()
    parent = property(**parent())
    
    def __str__(self):
        return '(%s, %s)' % (str(self._item), self._support_count)
    
    def __repr__(self):
        return '(%s, %s)' % (str(self._item), self._support_count)