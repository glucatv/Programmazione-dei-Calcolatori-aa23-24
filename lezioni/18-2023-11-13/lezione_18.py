# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:12:46 2023

@author: Gianluca
"""

def bin_search( a, k ):
    '''
    Parameters
    ----------
    a : una lista ordinata
    k : una chiave di ricerca

    Returns
    -------
    Un int p
     - Se k è in a restituisce p tale che a[p] == k
     - Se k non è in a restituisce -1
    '''
    #n = len(a)
    sx, rx = 0, len(a)
    # ricerco k in a[sx:rx]
    
    while rx > sx:
        cx = (sx+rx)//2
        if a[cx] == k:
            return cx
        if k < a[cx]:
            rx = cx
        else:
            sx = cx+1
            
    return -1

    # Complessità spaziale: O(1)
    # Complessità temporale: O(log n)
    
# In[]

def bin_search( a, k ):
    '''
    Parameters
    ----------
    a : una lista ordinata
    k : una chiave di ricerca

    Returns
    -------
    Un int p
     - Se k è in a restituisce il massimo p tale
         che a[p] == k
     - Se k non è in a restituisce -1
    '''
    #n = len(a)
    sx, rx = 0, len(a)
    # ricerco k in a[sx:rx]
    
    while rx > sx:
        cx = (sx+rx)//2
        if a[cx] == k and (cx == rx-1 or a[cx+1] != k):
            return cx
        if k < a[cx]:
            rx = cx
        else:
            sx = cx+1
            
    return -1

    # Complessità spaziale: O(1)
    # Complessità temporale: O(log n)
    
# In[]

def bin_search( a, k ):
    '''
    Parameters
    ----------
    a : una lista ordinata
    k : una chiave di ricerca

    Returns
    -------
    la posizione che dovrebbe occupare l'istanza di
    k più a destra in a
    
    ovvero
    
    a[i] <= k per i <= p
    a[i] > k per i > p
    '''
    
    # TODO
    

    # Complessità spaziale: O(1)
    # Complessità temporale: O(log n)
        
a = [2,4, 6, 7, 7, 10, 10, 10, 10, 14, 16, 17, 20, 23, 23]

print(bin_search(a, 10))

# In[]

# Dizionario

d = {} # dizionario vuoto
d = { 'python':5, 3:3.14, 2:'programmazione', 'pi':3.14 }

print(len(d))
print(d['pi'])
# print(d['PI']) # KeyError
d['pi'] = 3.1416  # aggiornamento
print(d['pi'])
d ['PI'] = d['pi'] # inserimento
del(d['pi'])
print(d)

