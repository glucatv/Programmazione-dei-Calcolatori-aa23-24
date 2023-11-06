# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:24:27 2023

@author: Gianluca
"""
# In[Esercizio]

# prima
a = [ 3.14, 'python', 2, 'programma', 12, 0, 'corso' ]

# dopo la corretta invocazione di bubble_sort...

#dopo
a = [0, 2, 3.14, 'corso', 'programma', 'python']

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
        
# In[Confronto tra sequenze]
print( (3, 2) < (1, 6, 9) )
print( (3, 2) < (3, 6, 9) )
print( (3, 6) < (3, 6, 9) )
print( (3, 'python') < (3, 'programma', 9) )
print( (2, 6) < (3, 'programma', 9) )

# In[]


def numeristringhe( e ):
    if type(e) == str:
        return (1, e)
    else:
        return (0, e)
    
def numeristringhe( e ):
    # espressione condizionale
    z = (1, e) if type(e) == str else (0, e) 
    return z

    
a = [ 3.14, 'python', 2, 'programma', 12, 0, 'corso' ]

bubble_sort(a, key=numeristringhe)

print(a)

# In[]

a = [ 3.14, 'python', 2, 'programma', 12, 0, 'corso' ]

b = sorted(a, key=numeristringhe)

print(b)

a.sort(key=numeristringhe)

print(a)

# In[]

a = [ 3.14, 'python', 2, 'programma', 12, 0, 'corso' ]



b = sorted(a, key= lambda e: len(e) if type(e) == str else e)

print(b)

# In[]

a = [(1,2), (3, 0), (1, 8)]

a.sort(key = lambda e: e[1])

print(a)

# In[]

a = [ 3.14, 'python', 2, 'programma', 12, 0, 'corso' ]

b = a # alias
c = a[:] # clone

# In[]

a = [3, [4, 5, 6], 7, 8]
b = a[:]

b[0] = 10
b[1][0] = 9
print(a)
print(b)






