# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:17:13 2023

@author: Gianluca
"""



# le stringhe sono immutabili, questa operazione
# non è consentita
# 
# x[14] = '_'

# concatenazione

a,b  = 'prima', 'seconda'
c = a+b
print(c)

# In[Problema: sostituire spazi di x con '_']

# Concatenazione

x = 'programmazione python e c'

y = '' # stringa

n = len(x)

for c in x:
    if c == ' ':
        y = y+'_'
    else:
        y = y+c
        
print(y)

# esegue un numero quadratico di operazioni rispetto ad n perché per ogni
# nuovo carattere aggiunto deve essere creata una copia della stringa precedente

# In[Ripetizione]

a = '012'

b = a*4 # equivalente a b = 4*a

print(b)

# In[Palindromi]

def palindromo( a ):
    b = ''
    for c in a:
        b = c+b
        
    # b è inversa rispetto ad a

    return a == b


print(palindromo('radar'))    
print(palindromo('rAdar'))    

    
# se n = len(a), richiede circa n^2 operazioni, vedere sopra
# e b occupa spazio

# In[]

def palindromo( a ):
    i, n = 0, len(a)
    
    while i < n//2:
        if a[i] != a[n-1-i]:
            return False
        i += 1
    return True

print(palindromo('radar'))    
print(palindromo('rAdar')) 

# richiede circa n operazioni, non usa
# memoria supplementare

# In[]

# indici negativi: a[-1] è l'ultimo carattere
# a[-2] il penultimo e così via

def palindromo( a ):
    i, n = 0, len(a)
    
    while i < n//2:
        if a[i] != a[-i-1]:
            return False
        i += 1
    return True

print(palindromo('radar'))    
print(palindromo('rAdar')) 

# richiede circa n operazioni, non uso
# memoria supplementare

# In[slicing]

a = '0123456789'

b = a[2:5]

print(b)

b = a[5:2]
print(b)

b = a[1:8:2]
print(b)

b = a[1:8:-1]
print(b)

b = a[8:1:-1]
print(b)

b = a[:4:2]
print(b)

b = a[1::2]
print(b)

b = a[::-1]
print(b)

# In[]
def palindromo( a ):
    return a == a[::-1]


# richiede circa n operazioni (creazione nuova
# stringa). Richiede memoria supplementare


print(palindromo('radar'))    
print(palindromo('rAdar')) 