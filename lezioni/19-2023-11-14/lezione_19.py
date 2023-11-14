# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:03:09 2023

@author: Gianluca
"""
def bin_search( a, k ):
    '''
    Parameters
    ----------
    a : una lista ordinata
    k : una chiave di ricerca

    Returns
    -------
    la posizione del primo elemento più grande di k
    
    ovvero
    
    0 se k < a[0]
    n se k >= a[n-1]
    
    a[p] > k e a[p] <= k
    '''
    
    n = len(a)
    sx, rx = 0, len(a)
    
    if k < a[0]:
        return 0
    if k >= a[-1]:
        return n
          
    while True:
        cx = (sx+rx)//2
        if a[cx] > k and a[cx-1] <= k:
            return cx
        if k < a[cx]:
            rx = cx
        else:
            sx = cx+1

    # Complessità spaziale: O(1)
    # Complessità temporale: O(log n)
    
a = [2,4, 6, 7, 7, 10, 10, 10, 10, 14, 16, 17, 20, 23, 23]

print(bin_search(a, 23))

# In[]


d = { 'python':5, 3:3.14, 2:'programmazione', 'pi':3.14 }

for k in d:
    print(k, d[k])
    
if 'Pi' in d:
    x = d['Pi']
else:
    x = 0
    
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
                d[x] += 1
            else:
                d[x] = 1

lista_d = []
for k in d:
    lista_d.append((k, d[k]))
    
lista_d.sort(key = lambda t: t[1], reverse=True)



# e: ######################
# a: ##################
# i: ##########



