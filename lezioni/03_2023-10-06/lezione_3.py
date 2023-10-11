# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:19:16 2023

@author: Gianluca
"""

# Sintassi if
#
#  if condizione:
#    blocco_if
#  else:
#    blocco_else
#
#
#  if condizione0:
#       blocco_0
#  elif condizione1:
#       blocco_1
#  ....
#  else:
#       default
#

x = input('Digita un intero: ')
x = int(x)

if x%2 == 0: 
    print(x, 'è parti e', x,  '= 2*', x//2)
else:
    print(x, 'è dispari e', x,'= 2*', x//2, '+ 1')
    
# Operatori relazionali

# < minore  > maggiore
# == uguale
# <= minore-uguale >= maggiore uguale
# != Diverso

# In[Contare le vocali in un testo]

x = input('Digita un testo: ')

i, numero_vocali = 0, 0
# per ogni valore legale di i, valuta x[i]

while i < len(x):
    # esiste il carattere x[i]
    # x[i] è una vocale?
    if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or\
        x[i] == 'o' or x[i] == 'u':
            numero_vocali = numero_vocali+1
    i += 1 # equivalente a i = i+1

print(numero_vocali)

# In[Contare le vocali in un testo]

x = input('Digita un testo: ')

i, numero_vocali = 0, 0
# per ogni valore legale di i, valuta x[i]

while i < len(x):
    # esiste il carattere x[i]
    # x[i] è una vocale?
    if x[i] in 'aeiouAEIOU':
            numero_vocali = numero_vocali+1
    i += 1 # equivalente a i = i+1

print(numero_vocali)

# In[Istruzione for]

x = 'una stringa'

for c in x:
    print(c)

# In[Contare le vocali in un testo]

x = input('Digita un testo: ')

numero_vocali = 0

# per ogni carattere c in x
for c in x:
    if c in 'aeiouAEIOU':
        numero_vocali = numero_vocali+1

print(numero_vocali)

# In[]



