# -*- encoding: utf-8 -*-

class Rule(object):
    """
    R = A --> B
    
    support(R) = sup_count(A^B) / num_transactions
    confidence(R) = sup_count(A^B) / sup_count(A)
    """
    
    def __init__(self, ant, cons, rule_supcount, num_transactions):
        self._ant = ant
        self._cons = cons
        self._support = round(rule_supcount / num_transactions, 2)
        self._confidence = round(rule_supcount / float(ant.support_count), 2)
    
    @property
    def support(self):
        return self._support
    
    @property
    def confidence(self):
        return self._confidence

    def __str__(self):
        ant = ' ^ '.join(map(str, self._ant.items))
        cons = ' ^ '.join(map(str, self._cons.items))
        met =  '(Sop: ' + str(self.support) + '; Conf: '+ str(self.confidence) +'): '
        return met + ant + ' -> ' + cons
