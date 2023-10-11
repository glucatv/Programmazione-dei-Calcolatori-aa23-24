# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:04:47 2023

@author: gianluca
"""

# In[Esercizio 1]

# scrivere un test che verifica se una stringa possa essere convertita in float

x = input('Digita un numero ')

# la stringa x rappresenta un numero se:
# - se è composta da cifre decimali (0, 1, ...., 9)
# - contiene al massimo un '.'

numero_punti = 0

# for c in x:
#     if c in '0123456789':
#         # accettiamo il carattere
#     elif c == '.':
#         # accettiamo il carattere solo se numero_punti è 0 ed incrementiamo numero_punti


i = 0
while i < len(x) and ( (x[i] in '0123456789') or (x[i] == '.' and numero_punti == 0) ):
    if x[i] == '.':
        numero_punti += 1
    i += 1
    
# esco dal while se i < len(x) non è più vera oppure
# ( (x[i] in '0123456789') or (x[i] == '.' and numero_punti == 0) ) non è più vera
if i == len(x):
    # tutti i caratteri di x sono stati accettati
    x = float(x)
else:
    x = 0
    
print(x)

# In[Esercizio 2 bis]

x = input('Digita un numero ')

numero_punti = 0

i = 0
while i < len(x) and ( (x[i] >= '0' and x[i] <= '9') or (x[i] == '.' and numero_punti == 0) ):
    if x[i] == '.':
        numero_punti += 1
    i += 1
    

if i == len(x):

    x = float(x)
else:
    x = 0
    
print(x)

# In[Esercizio 2]

x = input('Digita la prima parola (caratteri minuscoli) ')
y = input('Digita la second parola (caratteri minuscoli) ')

# scrivere un programma che stampi vero se x precede y
# nell'ordinamento alfabetico

i = 0

# cerco il primo i tale che x[i] != y[i], concludo che x precede y se e solo se x[i] < y[i]

if len(x) < len(y):
    n = len(x)
else:
    n = len(y)
    
while i < n  and x[i] == y[i]:
    i += 1
    
# se termino perché i == n che succede?
if i == n:
    if len(x) == len(y):
        print('le stringhe sono uguali')
    elif len(x) < len(y):
        print(x, 'precede', y)
    else:
        print(y, 'precede', x)
else:
    if x[i] < y[i]:
        print(x, 'precede', y)
    else:
        print(y, 'precede', x)
        
# In[]
    
# operatori relazionali tra stringhe <=, =>, < , >, ==
# esito definito dall'ordinamento lessicografico

# In[Funzioni]

def test_function( a ):
    print(a)
    
test_function('programma')
test_function(4)

# In[]

def f(n):
    n += 1
    return n

m = f(4)
print(m)

# In[]

def is_float( x ):
    numero_punti = 0
    i = 0
    
    while i < len(x) and ( (x[i] >= '0' and x[i] <= '9') or (x[i] == '.' and numero_punti == 0) ):
        if x[i] == '.':
            numero_punti += 1
        i += 1
        

    if i == len(x):
        return True
    else:
        return False
    
a = input('Digita un numero ')

if is_float(a):
    a = float(a)
else:
    a = 0
    
print(a)