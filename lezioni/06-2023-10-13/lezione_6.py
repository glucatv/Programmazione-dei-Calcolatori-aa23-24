# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:20:19 2023

@author: Gianluca
"""

def radice_quadrata( x ):
    g = x

    while abs(g*g - x) > 0.00001 :
        # inizio del testo indentato, inizio blocco
        g = 0.5*(g+x/g)
        
    return g

def radice_quarta( x ):
    # x è un numero (int o float)
    # return y t.c. y*y*y*y ==  x
    y = radice_quadrata( radice_quadrata(x) )
    return y

# programma principale o main
x = input('Inserisci un  numero ')
x = float(x)
y = radice_quarta(x)
print(y)

# In[]

def conta_parole( a ):
    # a è una stringa che rappresenta una frase (parole separate da punteggiatura)
    # return numero di parole in a
    # i separatori sono: spazio, virgola e punto
    
    n = 0 # numero di parole
    in_parola = False
    
    for c in a:
        if c in ' .,':
            if in_parola:
                in_parola = False
        else: # c è una lettera
            if not in_parola: # nega il valore di in_parola
                in_parola = True
                n += 1
                
    return n

f = '. programmazione dei   calcolatori .  con,   laboratorio'
print(conta_parole(f))