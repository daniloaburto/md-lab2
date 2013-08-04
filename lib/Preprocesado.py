# -*- encoding: utf-8 -*-
from Item import Item

class Interval(object):
    """
    Representa 
    """
    
    def __init__(self, _min, _max, steps):
        step = (_max - _min) / steps

        self._min = _min
        self._max = _max
        self.steps = steps
        self._intervals = []

        current = _min
        for i in range(0, steps):
            current = current + step
            self._intervals.append(current)
    
    def get_range(self, value):
        value = float(value)
        if value >= self._min and value <= self._max:
            i = 0
            for val in self._intervals:
                if value > val:
                    i = i + 1
            return i
        else:
            return -1


def get_transactions(fnames, fdata):
    """
    Se lee el archivo de extensión .names
    """

    try:
        f = open(fnames, 'r')
    except Exception:
        exception('Error: No es posible abrir "' + fnames + '".')
    
    # Mantiene los nombres de atributos
    attributes = []
    
    # Indica si un atributo es numerico y además
    # mantiene un objeto que permite obtener su intervalo
    is_numeric = []

    # La primera linea contiene los nombres de lcases
    row = f.readline()

    # Se leen los nombres de atributos
    row = f.readline()
    while row != "":
        
        data = row.strip().split(':')
        
        # Se guardan los nombres de atributos
        attributes.append(data[0])

        # Se obtienen los valores
        row_values = data[1].split(',')

        # Es numérico?
        numeric = True
        for val in row_values:
            try:
                number = float(val)
            except ValueError, TypeError:
                numeric = False
                break
        if numeric:
            obj = Interval(float(row_values[0]), float(row_values[-1]), 10)
            is_numeric.append((True, obj))
        else:
            is_numeric.append((False, None))

        row = f.readline()
    f.close()
    
    attributes.append('class')
    
    """
    Se lee el archivo de extensión .data
    """

    items = {}
    transactions = []
    
    try:
        f = open(fdata, 'r')
    except Exception:
        exception('Error: no es posible abrir "' + fdata + '".')
    
    row = f.readline()
    while row != "":
        
        transaction = []
        values = row.strip().split(',')
        
        for i in range(0, len(values)):

            # Es el nuevo item una clase?
            is_class = False
            if i == (len(values) - 1):
                is_class = True
            else:
                # Es numérico?
                if is_numeric[i][0]:
                    values[i] = 'Interv ' + str(is_numeric[i][1].get_range(values[i]))

            new_item = Item(attributes[i], values[i], is_class)
            transaction.append(new_item)

            if new_item in items:
                items[new_item] += 1
            else:
                items[new_item] = 0
        transactions.append(transaction)
        row = f.readline()
    f.close()
    
    # Se ordenan las transacciones de acuerdo
    # a su cantidad de items
    for transaction in transactions:
        transaction.sort(key=lambda item: items[item], reverse=True)

    return transactions