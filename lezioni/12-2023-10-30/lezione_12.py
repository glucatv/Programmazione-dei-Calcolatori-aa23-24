# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:13:42 2023

@author: Gianluca
"""
# In[ORDINAMENTO]

# Input una sequenza di numeri a
# Output gli elementi di a ordinati dal più piccolo al
# più grande

def bubble_sort( a ):
    n = len(a)
    
    for c in range(n-1):
        for i in range(n-1-c):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

    # ancora Theta(n*n) ma risparmio la metà delle operazioni
    # riduco la costante moltiplicativa
    
# In[]

def bubble_sort( a ):
    n = len(a)
    
    for c in range(n-1):
        ordinata = True
        for i in range(n-1-c):
            if a[i] > a[i+1]:
                ordinata = False
                a[i], a[i+1] = a[i+1], a[i]
        if ordinata:
            break # esco dal ciclo più interno

    # complessità temporale è O(n*n)
    
# In[]

def bubble_sort( a ):
    n = len(a)
    
    ordinata = False
    c = 0
    
    while not ordinata:
        ordinata = True
        for i in range(n-1-c):
            if a[i] > a[i+1]:
                ordinata = False
                a[i], a[i+1] = a[i+1], a[i]
        c += 1
    
    # complessità temporale è O(n*n)

# In[]
x = [20, 10, 9, 8, 7, 6, 5, 4, 3, 100]

bubble_sort(x)

print(x)

# In[]

# In[]

def bubble_sort( a ):
    '''
    a: lista di n tuple (nome, posizione) dove nome è un
        str di lunghezza 1, e posizione un intero
        
    ordina a rispetto alle posizioni
    '''
    n = len(a)
    
    ordinata = False
    c = 0
    
    while not ordinata:
        ordinata = True
        for i in range(n-1-c):
            if a[i][1] > a[i+1][1]:
                ordinata = False
                a[i], a[i+1] = a[i+1], a[i]
        c += 1
    
    # complessità temporale è O(n*n)

# In[]

x = [ ('a', 9), ('b', 4), ('c', 0), ('d', 2) ]
bubble_sort(x)
print(x)

# In[]

def draw(N, P):
    '''
    Parameters
    ----------
    N : list di caratteri, i nomi dei punti
    P : list di interi, posizioni dei punti sulla retta,
        
        P[i] è la posizine di N[i]

    Returns
    -------
    str che codifica le posizioni dei punti in P e di quelli in N
    '''
    
    n = len(N)
    # r = max(P)-min(P)
    
    # TODO
    # ordina P, e N di conseguenza
    x = []
    for i in range(n):
        t = N[i], P[i]
        x.append( t )
        
    bubble_sort( x )
    
    # x è ordinata rispetto il secondo elemento delle
    # coppie che lo compongono
    
    P, N = [], [] #  non bene, modifichiamo input
    for i in range(n):
        P.append(x[i][1])
        N.append(x[i][0])

    
    linea = []
    
    #for i in range(0, n): # da 0 a n-1 inclusi
    for i in range(n): # da 0 a n-1 inclusi
        linea.append(N[i])
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
    
# In[]       
# input
N = ['B', 'A', 'D', 'F', 'E', 'C']
P = [13, 7, 19, 20, 1, 3]

print(draw(N, P))