# -*- encoding: utf-8 -*-

import argparse
from lib.FPTree import FPTree
from lib.Preprocesado import get_transactions
from lib.Rule import Rule
from math import ceil

VERBOSE = True

def _print(e):
    if VERBOSE:
        print(e)

# Rutina main
if __name__ == '__main__':
    
    # Arguments
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("fnames", help="Ruta al archivo de extensión '.names'.",type=str)
    parser.add_argument("fdata", help="Ruta al archivo de extensión '.names'.",type=str)
    parser.add_argument("num_rules", help="Número de mejores reglas.",type=int)
    parser.add_argument("support", help="Soporte mínimo de las reglas",type=float)
    parser.add_argument("--classes", help="Indica si los consecuentes de las reglas son clases.",type=bool)
    args = parser.parse_args()
    
    _print('\nReading files...')

    # Get transactions from files
    transactions = get_transactions(args.fnames, args.fdata)
    num_transactions = float(len(transactions))
    
    # Minimum support count = support * Nº transactions
    supcount = max(int(ceil(num_transactions * args.support)), 1)
    base_tree = FPTree(minimum_support_count=supcount) 
    
    _print('Building FP Tree...')

    # Adding all transactions
    for transaction in transactions:
        base_tree.add_transaction(transaction)
    
    _print('   Support count: ' + str(supcount))
    _print('   Num transactions: ' + str(int(num_transactions)))

    itemsets = []
    support_counts = {}

    _print('Extracting itemsets from FP Tree...')

    # Extract itemsets recursively
    base_tree.extract_itemsets(itemsets, support_counts)
    itemsets.sort(key=lambda itemset: itemset.length)

    #for itemset in itemsets:
    #    print(itemset)
    
    _print('Generating rules...')

    # Rules list
    rules = []
    for itemset in itemsets:
        if itemset.length > 1:
            for single, group in itemset.pairs():
                
                # find support counts in a hash table
                single.support_count = support_counts[single]
                group.support_count = support_counts[group]

                # --clasess?
                if args.classes:
                    if single.items[0].is_class:
                        rule = Rule(group, single, itemset.support_count, num_transactions)                
                        rules.append(rule)
                else:
                    # creating rules
                    rule1 = Rule(single, group, itemset.support_count, num_transactions)
                    rules.append(rule1)
                    
                    # prevents duplicated rules
                    if itemset.length > 2:
                        rule2 = Rule(group, single, itemset.support_count, num_transactions)                
                        rules.append(rule2)
    
    rules.sort(key=lambda rule: (rule.support, rule.confidence), reverse=True)

    _print('Showing ' + str(min(args.num_rules, len(rules))) + ' of ' + str(len(rules)) + ' rules:')
    
    i = 0
    while i < len(rules) and i < args.num_rules:
        print(rules[i])
        i += 1
    
    if not i:
        print("No se han encontrado reglas con el soporte mínimo indicado")
        if args.support != 0:
            print("Por favor, inténtelo nuevamente con un soporte menor")

    print('')

    #rules.sort(key=lambda item: items[item], reverse=True)
    
    