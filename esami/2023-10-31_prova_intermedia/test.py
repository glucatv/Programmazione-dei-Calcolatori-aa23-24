#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:11:48 2022

@author: gianluca
"""

# In[1]

def f(condizione0, condizione1):
    if condizione0 and not condizione1:
        return condizione1
    elif condizione1:
        return False
    return True

print(f(True, True))
print(f(True, False))
print(f(False, True))
print(f(False, False))

# In[2]

n = 100


i, j = 0, 2*n
while i < j:
    i += 1
    j -= 1
    
print(i+j)

# In[3]

k = 13

n = 2*k+1
a, b = n/2, n/2

print(int(a)+int(b) < int(a+b))

# In[4]

def m( a ):
    if a[0] > max( a[1:] ):
        return a[0]
    else:
        return max( a[1:] )


print(m([3,4,5,3,1]))

# In[5]

def f(a, b, c):
    return a*b+c

print(f( (1,), 2, (1,2) ))

# In[6]

a = 'python'
t = ('x', 'y', (1, 2, 3), 'z', a)
        
print(len(t))

# In[7]
n = 10


def f(a):
    b = a/2
    if a > 0:
        b = a
    return b*b

b = n
x = f(b)
print(b)

# In[10]

x, y, z, w = 1,2,3