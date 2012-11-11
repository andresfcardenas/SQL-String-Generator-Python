#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Andres F. Cardenas (Andrewnix)
# Email: akardenasjimenez@gmail.com
import random

instructions = (
    'SELECT',
    'INSERT',
    'UPDATE',
    'DELETE',
    'WHERE',
    'FROM',
)

def select(table_name, columns=None, value=None):
    """This method represent the select instruction.
    """

    if columns == None:
        return '{0} * {1} {2}'.format(
            instructions[0],
            instructions[5],
            table_name
        )

    elements = extract_elements_list(columns)

    if value != None:
        column = random.randrange(0, len(columns))
        return '{0} {1} {2} {3} {4} {5}{6}'.format(
            instructions[0],
            elements,
            instructions[5],
            table_name,
            instructions[4],
            columns[column],
            value,
        )


    return '{0} {1} {2} {3}'.format(
        instructions[0],
        elements,
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

def extract_elements_list(lst):
    """This function extract the elements list
    """
    elements = ''

    for element in lst:
        if element == lst[-1]:
            elements = elements + element
        else:
            elements = elements + element + ', '

    return elements