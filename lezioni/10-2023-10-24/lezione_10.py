# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:22:44 2023

@author: Gianluca
"""

def find_ceters(N, P):
    '''
    Parameters
    ----------
    N : list di caratteri, i nomi dei punti
    P : list di interi, posizioni dei punti sulla retta
    
    Returns
    -------
    C: list dei nomi dei centri di P
    '''   
    n = len(N)
    
    # calcoliamo l'eccentricità  
    E  = []  # O(1)
    
    for x in P:
        ecc_x = 0
        for y in P:
            if abs(x-y) > ecc_x:
                ecc_x = abs(x-y)
        E.append(ecc_x) # O(1) nel 'caso medio'
        
    # ^ Theta(n*n) ^
        
    C = [] # i nomi dei punti centrali di P, costo O(1)
    
    m = None
    # in C tengo i punti con eccentricità pari ad m
    
    i = 0
    while i < len(E):
        e = E[i] # O(1)
        if e == m: 
            C.append(N[i]) 
        elif m == None or e < m:
            m = e
            C = [ N[i] ] # O(1) nel caso peggiore
        i += 1
    # ^ Theta(n)
    
    return C

def draw(N, P, C):
    '''
    Parameters
    ----------
    N : list di caratteri, i nomi dei punti
    P : list di interi, posizioni dei punti sulla retta
    C : list dei nomi dei centri di P

    Returns
    -------
    str che codifica le posizioni dei punti in P e di quelli in N
    '''
    
    # n = len(N)
    # r = max(P)-min(P)
    
    linea = ''
    
    for x in range(min(P), max(P)+1): # per r volte
        if x in P: # O(n)
            i = P.index(x) # O(n)
            nome = N[i]    # O(1)
            if nome in C:  # O(1) sulla linea i centri sono al più 2
                linea += '*' # O(r)
            else:
                linea += '+' # O(r)
        else:
            linea += ' ' # O(r)
            
    return linea
            
    # complessità temporale è
    # O(r*(n+r)) = O(r(r+r) perché n <= r
    # = O(r*r)
    
    
def draw(N, P, C):
    '''
    Parameters
    ----------
    N : list di caratteri, i nomi dei punti
    P : list di interi, posizioni dei punti sulla retta
    C : list dei nomi dei centri di P

    Returns
    -------
    str che codifica le posizioni dei punti in P e di quelli in N
    '''
    
    
    # n = len(N)
    # r = max(P)-min(P)
    
    linea = []
    
    for x in range(min(P), max(P)+1): # per r volte
        if x in P: # O(n)
            i = P.index(x) # O(n)
            nome = N[i]    # O(1)
            if nome in C:  # O(1) sulla linea i centri sono al più 2
                linea.append('*') # O(1)
            else:
                linea.append('+') # O(1)
        else:
            linea.append(' ') # O(1)
     
    #linea_str = ''
    #for x in linea:
    #    linea_str += x
    #
    # Theta(r*r)
    
    linea_str = ''.join(linea) # Theta(r)
     
    return linea_str
            
    # complessità temporale è
    # O(r*n)
        
    
# input
N = ['B', 'A', 'D', 'F', 'E', 'C', 'G']
P = [2, 0, 6, 9, 7, 3, 16]

C = find_ceters(N, P)

print(draw(N, P, C))

