# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:16:21 2023

@author: gianluca
"""

# In[]

def intersezione_liste( a, b ):
    '''
    input: a, b: liste
    output: lista c contenente gli elementi che sono sia in a che in b, senza ripetizioni
    '''
    c = []
    
    for e in a: # n iterazioni
        if e in b and not e in c: # O(m) + O(n)
            c.append(e) # O(1)
            
    return c


    # Costo computazionale
    # - spazio O(1)
    # - tempo: assumiamo che len(a) = n; len(b) = m
    #    nel caso peggiore O(n(n+m))
    
# In[]

def intersezione_liste( a, b ):
    '''
    input: a, b: liste
    output: lista c contenente gli elementi che sono sia in a che in b, senza ripetizioni
    '''
    d, c = {}, {} # O(1)
    
    for e in b:  # m iterazioni
        d[e] = None  # O(1)
    
    for e in a: # n iterazioni
        if e in d: # O(1) + O(1)
            c[e] = None # O(1)
            
    c = [ k for k in c ] # O( min(n, m) )
            
    return c


    # Costo computazionale
    # - spazio O(1)
    # - tempo: assumiamo che len(a) = n; len(b) = m
    #    nel caso peggiore O( n+m )





a = [2, 3, 4, 1, 6, 7, 6]
b = [5, 7, 8, 4, 0, 7, 4]

c = intersezione_liste( b, a )

print(c)

# In[]

def intersezione_dizionari( d0, d1, f = lambda x, y: x+y ):
    '''
    input: d0 e d1 dizionari che mappano stringhe in numeri
    output: un dizionario c tale che:
        - le chiavi di c sono quelle comuni in d0 che in d1
        - se k è una chiave di c allora c[k] = f(d0[k], d1[k]) 
    '''
    
    n, m = len(d0), len(d1)
    
    
    dt0, dt1 = (d1, d0) if n > m else (d0, d1) # alias costo O(1)
    
    # equivalente a...
    # if n > m:
    #     dt0, dt1 = d1, d0 # alias costo O(1)
    # else:
    #     dt0, dt1 = d0, d1 # alias costo O(1)
        
    c = {}
    
    for e in dt0: # n iterazioni
        if e in dt1:
            c[e] = f(dt0[e], dt1[e]) # O(1)
            
    return c

    # Complessità temporale: min( Theta(n), Theta(m) )
    
a = {'uno':1, 'due': 2, 'quattro':4, 'sei':6}
b = {'uno':10,  'quattro':40, 'zero':0}

c = intersezione_dizionari(a, b, f=max)

print(c)

# In[]

def rmax( x ):
    if type(x) in [int, float]:
        return x
    m = None   # massimo corrente
    for e in x:
        c = rmax(e)
        if m == None or c > m:
            m = c
    return m

# In[]


def rmax( x ):
    if type(x) in [int, float]:
        return x
    for e in x:
        c = rmax(e)
        try:
            if c > m:
                m = c
        except UnboundLocalError:
            m = c
    return m

# In[]


def rmax( x ):
    try:
        for e in x:
            c = rmax(e)
            try:
                if c > m:
                    m = c
            except UnboundLocalError:
                m = c
        return m
    except TypeError:
        return x

a = [3, 9, [9, 0, [1, 2], 3], 7, [11, [2, 8], 9], 5 ]
print(rmax(a))


# In[]

d = {}

x = 'a'

try:
    d[x] = d[x]+1
except KeyError:
    d[x] = 9
    
# In[]

def anagrammi(a, b):
    '''
        Input: a, b due stringhe
        Return: True se e solo se a e b sono anagrammi
    '''
    
    if len(a) != len(b):
        return False
    
    # n = len(a) = len(b)
    
    return ''.join(sorted(a)) == ''.join(sorted(b))

    # complessità temporale è O(n log n)
    # complessitò spaziale O(n)

# In[]

def anagrammi(a, b):
    '''
        Input: a, b due stringhe
        Return: True se e solo se a e b sono anagrammi
    '''
    
    if len(a) != len(b):
        return False
    
    # n = len(a) = len(b)
    
    da, db = {}, {}
    for x in a:
        da[x] = None
    for x in b:
        db[x] = None
        
    print(da)
    print(db)
        
    # ritornare True se e solo se da == db



print(anagrammi('panee', 'nepaa'))