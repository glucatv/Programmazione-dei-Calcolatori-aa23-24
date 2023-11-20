# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:23:29 2023

@author: Gianluca
"""
def anagrammi(a, b):
    '''
        Input: a, b due stringhe
        Return: True se e solo se a e b sono anagrammi
    '''
    
    if len(a) != len(b): # O(1)
        return False
    
    # n = len(a) = len(b)
    
    da, db = {}, {} # O(1)
    
    for x in a: # per n volte
        da[x] = da.get(x, 0) + 1 # O(1)
    for x in b:
        db[x] = db.get(x, 0) + 1 # O(1)
        
    return da == db # O(n)
        
    # Complessità temporale è O(n)
    # Complessità spaziale è O(n)

# In[]

def anagrammi(a, b):
    '''
        Input: a, b due stringhe
        Return: True se e solo se a e b sono anagrammi
    '''
    
    if len(a) != len(b): # O(1)
        return False
    
    # n = len(a) = len(b)
    
    # da =  db = {} # NO! da è alias di db
    da, db = {}, {}
      
    for x,y in zip(a, b):
        da[x] = da.get(x, 0) + 1
        db[y] = db.get(y, 0) + 1
    
    return da == db # O(n)
        
    # Complessità temporale è O(n)
    # Complessità spaziale è O(n)

# funzione incorporata id()
    
print(anagrammi('paxee', 'nepaae'))