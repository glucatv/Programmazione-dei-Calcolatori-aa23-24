# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:18:33 2023

@author: Gianluca
"""

# In[]

def conta_parole( a ):
    # a è una stringa che rappresenta una frase
    # (parole separate da punteggiatura)
    # return numero di parole in a
    # i separatori sono: spazio, virgola e punto
    
    m = len(a) # 1 o 2 o 5... operazioni, dipende da len?
    
    n = 0 # numero di parole  # 1 operazione
    in_parola = False # 1 operazione
    
    for c in a:
        if c in ' .,': # 4 5 oppure 3 oppure...
            if in_parola: # 2 ops
                in_parola = False # 1 op
        else: # c è una lettera
            if not in_parola: # 2 ops  # nega il valore di in_parola
                in_parola = True # 1 op
                n += 1 # 3 ops 
                
    return n # 1 op

# costo complessivo al massimo 7 + m*8 + 1
# elimino le costanti additive
# costo 8*m meglio dire k*m dove k è una costante
# k non dipende da a (o da m)
# 
# 8*m
# 6*m
# 10*m
#
# si tratta di funzioni lineari in m
# introduco una notazione asintotica,
# il numero di operazioni eseguite dall'algoritmo è
# è in  O(m)
#
# in generale sia f(m) il numero di operazioni eseguite
# da un algoritmo su input di dimensione m
# l'algoritmo ha complessità temporale O(g(m)) se
# f(m) è in O(g(m))
#
# nel nostro caso f(m) = 7+8*m+1
# g(m) = m
#
# osservazione: la nostra f(m) è in O(m*m)
# f(m) è anche in O(m) e in Theta(m)
# O(m) contiene anche le funzioni 'più piccole'
# p.e. log(m) è in O(m) ma log(m) non è in Theta(m)


f = '. programmazione dei   calcolatori .  con,   laboratorio'
print(conta_parole(f))
# In[]

a = input('inserisci un testo ')

# voglio sapere la compl. temporale da qui in poi

n = len(a)

if 'A' in a:
    print('Si')
else:
    print('No')
    
# complessità è Theta(n) nel caso peggiore, 'A' non in a
# è Theta(n) anche nel caso medio.

# In[]

def conta_occorrenze(x, y):
    '''
    Input: x, e y sono due str len(y) < len(x)
    Ritorna: il numero di volte in cui y compare in x
    '''
    n, m = len(x), len(y)
    
    occ = 0
    i = 0 # la prima posizione della sottostringa di x in esame
    while i < n-m:
        if x[i:i+m] == y: # Theta(m) operazioni 
            occ += 1 # O(1) tempo costante
        i += 1 # O(1)
        
    return occ 

print(conta_occorrenze('prtghydfjuy7dfkiu', 'df'))
    
# Complessità temporale
#
# per n-m volte eseguo Theta(m) operazioni, in totale
# Theta(m(n-m))


