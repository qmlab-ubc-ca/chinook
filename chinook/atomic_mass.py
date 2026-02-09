# -*- coding: utf-8 -*-

#Created on Mon Aug 14 09:32:57 2017

#@author: ryanday
#MIT License

#Copyright (c) 2018 Ryan Patrick Day

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import linecache
from chinook.resource_loader import load_text_lines


a_file = 'atomic_mass.txt'

def _lines():
    return load_text_lines('chinook', a_file)

def get_mass_from_number(N_at):
    '''

    Pull atomic mass for the indicated atomic number
    
    *args*:

        - **N_at**: int, atomic number
        
    *return*:

        - float, atomic mass, in atomic mass units
    
    ***
    '''
    try:
        fields = _lines()[int(N_at) - 1].split('\t')
        return float(fields[2])
    except IndexError:
        print('ERROR: Invalid atomic number, returning mass = 0.')
        return 0.0

def get_el_from_number(N_at):
    
    '''
    Get symbol for element, given the atomic number
    
    *args*:

        - **N_at**: int, atomic number
    
    *return*:

        - string, symbol for element
    
    ***
    '''
    
    try:
        return _lines()[int(N_at) - 1].split('\t')[1]
    except IndexError:
        print('ERROR: Invalid atomic number, returning empty string.')
        return ''

def get_num_from_el(el):
    
    '''

    Get atomic number from the symbol for the associated element. Returns 0 for
    invalid entry.
    
    *args*:

        - **el**: string, symbol for element    
    
    *return*:

        - **Z**: int, atomic number.
    
    '''
    Z  = -1
    for l in _lines():
        line = l.split('\t')
        if line[1] == el:
            Z = int(line[0])
    if Z == -1:
        print('WARNING!! Invalid symbol passed. Returning with Z = 0')
        Z = 0
        
    return Z