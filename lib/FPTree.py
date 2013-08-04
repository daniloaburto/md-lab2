# -*- encoding: utf-8 -*-

from FPNode import FPNode
from Itemset import Itemset

class FPTree(object):
    
    def __init__(self, conditional_itemset=None, minimum_support_count=2):
        """
        root representa la raíz del árbol y su item es None
        
        nodes_shortcut es un diccionario que mantiene una lista
        enlazada para todos los elementos, la cabeza de dicha lista
        enlazada es un nodo que mantiene el contador de soporte acumulado
        de dicho elemento
        
        condiciontal_itemset es usado cuando un FPTree es condicional a 
        un itemset específico
        """
        self._root = FPNode(None)
        self._nodes_shortcut = {}
        self._conditional_itemset = conditional_itemset
        self._minimum_support_count = minimum_support_count
    
    def add_transaction(self, items):
        """Agrega los items de una transacción"""
        node = self._root
        for item in items:
            
            new_node = FPNode(item)
            
            # bandera
            node_in_children = False
            
            # agregar el nodo al árbol
            if not item in node.children:
                node.add(new_node)
                node = node.children[item]
            else:
                node = node.children[item]
                node.increment()
                node_in_children = True
                
            # agrega el nodo a la lista de atajo
            if item in self._nodes_shortcut:
                head = self._nodes_shortcut[item]
                
                # el nodo es agregado solo si no existe previamente
                # en la lista enlazada
                if not node_in_children:
                    head.add_linkedlist(new_node)
                head.increment()
            else:
                head = FPNode(item)
                self._nodes_shortcut[item] = head
                head.add_linkedlist(new_node)

    def extract_itemsets(self, itemsets, support_counts):
        
        for item in self._nodes_shortcut:
            
            node = self._nodes_shortcut[item]
            if node.support_count < self._minimum_support_count:
                continue
            
            # para cada item guardar un itemset más largo
            if self._conditional_itemset:
                larger_itemset = self._conditional_itemset.join(item, node.support_count)
            else:
                larger_itemset = Itemset([node.item], node.support_count)
            
            # se guarda el itemset más largo y su contador de soporte
            itemsets.append(larger_itemset)
            support_counts[larger_itemset] = larger_itemset.support_count

            # se obtienen todos los caminos a un item
            paths = []
            
            while node.next:
                path = []
                node = node.next

                # cuantas veces el camino existe a este nodo?
                q = node.support_count

                child = node.parent
                while child.parent:
                    
                    # se agregan solo items frecuentes
                    global_sup_count = self._nodes_shortcut[child.item].support_count
                    if global_sup_count >= self._minimum_support_count:
                        path.append(child.item)

                    # siguiente nodo
                    child = child.parent

                if path:
                    path.reverse()
                    paths.append((path,q))

            # Se obtienen los itemsets de los subarboles
            if paths:
                conditional_tree = FPTree(larger_itemset, minimum_support_count=self._minimum_support_count)
                for path, q in paths:
                    for i in range(0, q):
                        conditional_tree.add_transaction(path)
                conditional_tree.extract_itemsets(itemsets, support_counts)
