# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:34:52 2023

@author: Gianluca
"""
# In[]

def conta_occorrenze(x, y):
    '''
    Input: x, e y sono due str len(y) < len(x)
    Ritorna: il numero di volte in cui y compare in x
    '''
    n, m = len(x), len(y)
    
    occ = 0
    i = 0 # la prima posizione della sottostringa di x in esame
    while i <= n-m:
        if x[i:i+m] == y: # Theta(m) operazioni 
            occ += 1 # O(1) tempo costante
        i += 1 # O(1)
        
    return occ 

print(conta_occorrenze('prtghydfjuy7dfkiudf', 'df'))
    
# Complessità temporale
#
# per n-m volte eseguo Theta(m) operazioni, in totale
# Theta(m(n-m))
#
# Complessità spaziale
#
# Usa Theta(m) spazio aggiuntivo rispetto all'I/O
#
# 

# In[]

def conta_occorrenze(x, y):
    '''
    Input: x, e y sono due str len(y) < len(x)
    Ritorna: il numero di volte in cui y compare in x
    '''
    
    n, m = len(x), len(y) # O(1)
    
    occ = 0
    i = 0 # la prima posizione della sottostringa di x in esame
    while i <= n-m:
        j = 0
        while j < m and y[j] == x[i+j]:
            j += 1
        if j == m:
            occ += 1
        i += 1 # O(1)
        
    return occ 

print(conta_occorrenze('prtghydfjuy7dfkiudf', 'df'))

# Complessità temporale
#
# per n-m volte eseguo O(m) operazioni. Quindi la
# complessità temporale è
#
# O((n-m)*m)
#
# Complessità spaziale
#
# Usa O(1) spazio aggiuntivo rispetto all'I/O
#
#

# In[Tuple]

n, m = 1, 2.3

t = 1, 2.3
t = (1, 2.3)

for x in (3, 4,1,5,7):
    print(x)
    
t = ('python', 3, True, (3.14, 9))

print(t[2])
t0 = t[1::2]
print(t0)

t0 = (1,2,3)
t1 = ('uno', 2, 'III')
t = t0+t1
print(t)

t = 2*t0
print(t)

# la tuple è immutabile
# t[0] = 'ciao' #NO!

t = ('python', 'programma',  'c')

print(t[0][1])

x, y, z = t # unpacking

print(x, y, z)

a = x, y, z  # packing

n = 1

t = (n, n+1)

print(t)

n += 1

print(t)

print(len(t))

# In[Lista]

a = [0, 1.2, True, (1,2,3), 'python', [1,9] ]
print(len(a))
# valgono indicizzazione, slicing, concatenazione, ripetizione

print(a[2])

a[2] = 'una stringa'

print(a)

b = a[1:]
print(b)

del(a[1])

print(a)

a.append('xxxxxx')
print(a)
print(len(a))

t = (1,2,3,4)

a = list(t)

print(a)

t = tuple(a)

a = str(3.14)

a = list('abcdefd')

print(a)
