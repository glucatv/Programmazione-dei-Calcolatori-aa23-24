# In[ESERCIZIO]

a = [3, [4, 5, 6, [10, 11]], 7, 8, [12, 13, [2,3]]]
a = []
a = [('ricorsione', 1), 3, [3, 3.14, (3, True)]]

# Data una lista a,
# scrivere una funzione che ritorni il numero di
# interi contenuti in a ed in tutte le sue liste
# annidate

def count_int( x ):
    c = 0
    for e in x:
        if type(e) == int:
            c += 1
        elif type(e) in [list, tuple]:
            c += count_int( e )
    return c

print(count_int(a))
            
# In[]


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

# In[]

def merge(a, sx, cx, dx):
    '''
    Parameters
    ----------
    a : una lista t.c per ogni coppia di elementi in a è
        definito l'operatore <
    sx, cx, dx : int

    Assunzione
    a[sx:cx] è ordinata
    a[cx:dx] è ordinata

    Returns
    -------
    None.
    Garantiamo che a[sx:dx] sarà ordinata
    '''   
    c = []
    i, j = sx, cx
    
    while i < cx and j < dx: # O(n+m)
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    
    if i == cx: # O(n+m)
        c.extend(a[j:dx])
    else:
        c.extend(a[i:cx])
    
    for i in range(len(c)):
        a[sx+i] = c[i]

def merge_sort( a, sx=0, dx=None ):
    '''
    Parameters
    ----------
    a : una lista t.c per ogni coppia di elementi in a è
        definito l'operatore <
    sx : intero
    dx : intero

    Returns
    -------
    None.
    Ordina a[sx:dx] in loco
    '''
    if dx == None:
        dx = len(a)
    
    n = dx-sx
    if n >= 2:
        cx = (sx+dx)//2
        merge_sort(a, sx, cx)
        merge_sort(a, cx, dx)
        merge(a, sx, cx, dx)
        
    # complessità temporale Theta(n log n)
    # complessità spaziale Theta(n) per la lista c in merge 
    #   + log(n) che è la profondità della ricorsione
    #   ovvero Theta(n)        
a = [3,7,3,9,8,1,4,2,1,0,9,3,1,4,5]
merge_sort(a)
print(a)