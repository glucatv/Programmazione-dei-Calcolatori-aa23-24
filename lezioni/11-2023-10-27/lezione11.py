# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:23:13 2023

@author: Gianluca
"""
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
    P : list di interi, posizioni dei punti sulla retta,
        P[i] <= P[i+1] per i = 0, 1, 2,...
        
        P[i] è la posizine di N[i]
    C : list dei nomi dei centri di P

    Returns
    -------
    str che codifica le posizioni dei punti in P e di quelli in N
    '''
    
    n = len(N)
    # r = max(P)-min(P)
    
    linea = []
    
    #for i in range(0, n): # da 0 a n-1 inclusi
    for i in range(n): # da 0 a n-1 inclusi
        p = N[i]
        if p in C: #O(1)
            linea.append('*')
        else:
            linea.append('+')
        if i < n-1: # i non è l'ultimo punto
            spazi = P[i+1]-P[i]-1
            linea.extend([' ']*spazi) #O(r_i)
        # ^equivalente a 
        # for s in [' ']*spazi:
        #   linea.append(s)
     
    # num operazioni Sum_i r_i = r
    # costo del ciclo  Theta(r)
    
    linea_str = ''.join(linea) # Theta(r)
     
    
    
    return linea_str


def draw(N, P, C):
    '''
    Parameters
    ----------
    N : list di caratteri, i nomi dei punti
    P : list di interi, posizioni dei punti sulla retta,
        
        P[i] è la posizine di N[i]
    C : list dei nomi dei centri di P

    Returns
    -------
    str che codifica le posizioni dei punti in P e di quelli in N
    '''
    
    n = len(N)
    # r = max(P)-min(P)
    
    # TODO
    # ordina P e N di conseguenza
    
    linea = []
    
    #for i in range(0, n): # da 0 a n-1 inclusi
    for i in range(n): # da 0 a n-1 inclusi
        p = N[i]
        if p in C: #O(1)
            linea.append('*')
        else:
            linea.append('+')
        if i < n-1: # i non è l'ultimo punto
            spazi = P[i+1]-P[i]-1
            linea.extend([' ']*spazi) #O(r_i)
        # ^equivalente a 
        # for s in [' ']*spazi:
        #   linea.append(s)
     
    # num operazioni Sum_i r_i = r
    # costo del ciclo  Theta(r)
    
    linea_str = ''.join(linea) # Theta(r)
     
    # Costo totale: Theta(r) + costo sorting
    # = Theta(r) + Theta(n*n)
    
    return linea_str
    
         
# input
N = ['B', 'A', 'D', 'F', 'E', 'C']
P = [3, 7, 9, 10, 13, 20]

C = find_ceters(N, P)

print(draw(N, P, C))

# In[ORDINAMENTO]

# Input una sequenza di numeri a
# Output gli elementi di a ordinati dal più piccolo al
# più grande

def bubble_sort( a ):
    n = len(a)
    
    for c in range(n-1):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            
    #return a

    # Costo Theta(n*n)

# In[]
x = [3, 9, 0, 11, 7, 4]

bubble_sort(x)

print(x)




