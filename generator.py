#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Andres F. Cardenas (Andrewnix)
# Email: akardenasjimenez@gmail.com
instructions = (
    'SELECT',
    'INSERT',
    'UPDATE',
    'DELETE',
    'WHERE',
    'FROM',
)

def select(table_name, columns=None, table_esp=None, sign=None, value=None):
    """This method represent the select instruction.
    """

    if type(columns) == type(None):
        return '{0} * {1} {2}'.format(
            instructions[0],
            instructions[5],
            table_name
        )
    elif type(columns) == type(''):
        pass
    elif type(columns) == type([]):
        columns = ', '.join(columns)
    else:
        raise NameError('Data structure invalid, only string or list type')

    if value != None:
        if sign == None:
            sign = '='

        return '{0} {1} {2} {3} {4} {5}{6}{7}'.format(
            instructions[0],
            columns,
            instructions[5],
            table_name,
            instructions[4],
            table_esp,
            sign,
            value,
        )

    return '{0} {1} {2} {3}'.format(
        instructions[0],
        columns,
        instructions[5],
        table_name
    )

def insert():
    """This method represent the insert instruction.
    """
    pass

def update():
    """This method represent the update instruction.
    """
    pass

def delete():
    """This method represent the delete instruction.
    """
    pass
