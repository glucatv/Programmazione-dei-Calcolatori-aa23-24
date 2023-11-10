
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

# In[]

def deep_copy( a ):
    '''
    Parameters
    ----------
    a : una lista

    Returns
    -------
    b, una copia profonda di a

    '''

    b = []
    
    for e in a:
        if type(e) == list:
            b.append( deep_copy(e) )
        else:
            b.append( e )
    
    return b


# In[]

a = [3, [4, 5, 6, [10, 11]], 7, 8, [12, 13, [2,3]]]

b = deep_copy(a)

print(b)

# In[]

def rmax( a ):
    '''
    a: lista non vuota di numeri
    return: il massimo in a
    '''
    
    if len(a) == 1:
        return a[0]
    else:
        m = rmax(a[1:])
        if m > a[0]:
            return m
        else:
            return a[0]
        
print(rmax([3,2,6, 2, 1, 9, 0]))

# Tempo e spazio quatratici

# In[]

def rmax( a, p ):
    '''
    Parameters
    ----------
    a : una lista di numeri
    p : un indice in a

    Returns: il massimo in a[p:]
    -------
    '''
        
    if p == len(a)-1:
        return a[p]
    else:
        m = rmax(a, p+1)
        if m > a[p]:
            return m
        else:
            return a[p]      
    
print(rmax([3,2,6, 2, 1, 9, 0], 0))

# Complessità temporale Theta(n)
# Complessità spaziale Theta(n)

# In[ESERCIZIO]

a = [3, [4, 5, 6, [10, 11]], 7, 8, [12, 13, [2,3]]]

# Data una lista a,
# scrivere una funzione che ritorni il numero di
# interi contenuti in a ed in tutte le sue liste
# annidate

# In[]

a = [3, 5, 7, 9, 10, 21]
b = [1, 2, 6, 14, 16, 23]

# siano a e b due liste ordinate
# scrivere una funzione che ordini gli elementi 
# di a e b in una nuova lista

def merge( a, b ):
    n, m = len(a), len(b)
    
    c = []
    i, j = 0, 0
    
    while i < n and j < m: # O(n+m)
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    if i == n: # O(n+m)
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    
    return c

# Costo è Theta(n+m) in quanto l'ottimale è almeno
# lineare in n+m

print(merge())