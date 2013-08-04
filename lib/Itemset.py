# -*- encoding: utf-8 -*-

class Itemset(object):
    def __init__(self, items, support_count):
        self._items = items
        self._support_count = support_count
    
    def join(self, item, support_count):
        return Itemset(self._items + [item], support_count)
    
    def pairs(self):
        for i in range(0, len(self.items)):
            x = Itemset([self._items[i]], -1)
            y = Itemset(self._items[0:i] + self._items[i+1:], -1)
            yield (x, y)
    
    
    def support_count():
        doc = "Retorna el contador de soporte"
        
        def fget(self):
            return self._support_count
        
        def fset(self, supcount):
            self._support_count = supcount
        
        return locals()
    support_count = property(**support_count())
    
    @property
    def items(self):
        return self._items
    
    @property
    def length(self):
        return len(self._items)

    def __hash__(self):
        item_hashes = []
        for item in self._items:
            item_hashes.append(hash(item))
        return hash(tuple(item_hashes))
    
    def __str__(self):
        return '{' + ', '.join([str(item) for item in self._items]) + ': ' + str(self._support_count) + '}'
    
    def __eq__(self, other):
        return self._items == other.items
    
