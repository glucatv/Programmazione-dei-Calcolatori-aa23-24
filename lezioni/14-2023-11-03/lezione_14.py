# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:21:16 2023

@author: gianluca
"""

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

a = [3, 4, 5, 6]
b = ['tre', 'quattro', 'cinque', 'sei']

for e in zip(a, b):
    print(e)
    
# In[]

a = [3, 4, 5]
b = ['tre', 'quattro', 'cinque', 'sei']

for e in zip(a, b):
    print(e)

    
# In[]

x = list(zip(a,b))

print(x)
    
# In[]

a = [0,1,2,3]
b = [10, 11, 12, 13]

x = list(zip(a, b))

print(x)

y = list(zip(*x))

print(y)


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
    
    x = list(zip(N,P))
    bubble_sort( x )
    
    # x è ordinata rispetto il secondo elemento delle
    # coppie che lo compongono
            
    N, P = list(zip(*x))

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


# In[]

def bubble_sort( a, key ):
    '''
    a: lista di n tuple (nome, posizione) dove nome è un
        str di lunghezza 1, e posizione un intero
    key: una funzione che assegna valori agli elementi di a
        
    ordina a rispetto ai valori di key, dal più piccolo al più grande
    '''
    n = len(a)
    
    ordinata = False
    c = 0
    
    while not ordinata:
        ordinata = True
        for i in range(n-1-c):
            if key(a[i]) > key(a[i+1]):
                ordinata = False
                a[i], a[i+1] = a[i+1], a[i]
        c += 1
        
# In[]

a = [ (1, 2, 4), (1, 2), (3, ) , (4,), (0, 1)]

bubble_sort(a, sum)

print(a)

# In[]

N = ['B', 'A', 'D', 'F', 'E', 'C']
P = [13, 7, 19, 20, 1, 3]

x = list(zip(N, P))

print(x)

def t(e):
    return e[1]

bubble_sort(x, t)

print(x)

# In[]

x = [3, 5, 3, 1, 8, 0]

def ident(e):
    return e

bubble_sort(x, ident)

print(x)

# In[]

def bubble_sort( a, key=None ):
    '''
    a: lista di n tuple (nome, posizione) dove nome è un
        str di lunghezza 1, e posizione un intero
    key: una funzione che assegna valori agli elementi di a. Se non indicato,
        è la funzione identità
        
    ordina a rispetto ai valori di key, dal più piccolo al più grande
    '''
    def ident(e): # funzione locale
        return e

    if key == None:
        key = ident
    
    n = len(a)
    
    ordinata = False
    c = 0
    
    while not ordinata:
        ordinata = True
        for i in range(n-1-c):
            if key(a[i]) > key(a[i+1]):
                ordinata = False
                a[i], a[i+1] = a[i+1], a[i]
        c += 1

# In[]

x = [3, 5, 3, 1, 8, 0]


bubble_sort(x)

print(x)

# In[]

x = [ (1, 2, 4), (1, 2), (3, ) , (4,), (0, 1)]

bubble_sort(key=sum, a=x) # per nome
# bubble_sort(a, key=sum) # mista
# bubble_sort(a, sum) # per posizione

print(a)

# In[Esercizio]

# prima
a = [ 3.14, 'python', 2, 'programma', 12, 0, 'corso' ]

# dopo la corretta invocazione di bubble_sort...

#dopo
a = [0, 2, 3.14, 'corso', 'programma', 'python']



