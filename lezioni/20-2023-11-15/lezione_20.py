# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:03:09 2023

@author: Gianluca
"""

# In[]

def minuscolo( x ):
    '''
    Parameters
    ----------
    x : lettera maiuscola

    Returns
    -------
    la miuscola di x
    '''
    return chr(ord(x) + ord('a') - ord('A'))

# In[]

f = open('promessi_sposi.txt')
d = {}

for line in f:
    for x in line:
        if x in ['è', 'é']:
            x = 'e'
        elif x in ['ò']:
            x = 'O'
        if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
            if (x >= 'A' and x <= 'Z'):
                x = minuscolo(x)
            if x in d:
                d[x] += 1 # modifica
            else:
                d[x] = 1 #inserimento

# In[]

lista_d = []
for k in d:
    lista_d.append( (k, d[k]) )
    
lista_d.sort(key = lambda t: t[1], reverse=True)

# In[Diagrammi a barre]

lm = 60 # lunghezza massima delle barre
m = lista_d[0][1] # massima occorrenza

for k, v in lista_d:
    print(k, '#'*(v*lm//m))

# e: ######################
# a: ##################
# i: ##########

# In[Costruzione del dizionario con get() ]

f = open('promessi_sposi.txt')
d = {}

for line in f:
    for x in line:
        if x in ['è', 'é']:
            x = 'e'
        elif x in ['ò']:
            x = 'O'
        if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
            if (x >= 'A' and x <= 'Z'):
                x = minuscolo(x)
            d[x] = d.get(x,0) + 1
            
# In[Costruzione della lista con items]

lista_d = []
for t in d.items():
    lista_d.append( t )
    
# In[Costruzione della lista con list comprehension]

lista_d = [ t for t in d.items() ]

# In[E' necessario lista_d se non devo ordinare?]

lm = 60 # lunghezza massima delle barre
m = max(d.items(), key = lambda t: t[1])[1]

for k, v in d.items():
    print(k, '#'*(v*lm//m))

# In[Complessità operazioni su dizionari]

d = {}  # O(1)

n = len(d)

d['k'] = 10 # O(1) caso medio sia inserimento che sia aggiornamento, caso peggiore O(n)

'k' in d # O(1) nel caso medio, caso peggiore O(n)

del(d['k']) # O(1) nel caso medio, caso peggiore O(n)

d.get(k) # O(1) nel caso medio, caso peggiore O(n)

for x in d:    # Theta(n)
    print(x)

for x in d.items():    # Theta(n)
    print(x)

for x in d.keys():    # Theta(n)
    print(x)

for x in d.values():    # Theta(n)
    print(x)

# In[]

d1 = d # alias 
d2 = d.copy() # clonazione

