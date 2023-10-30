# 1

Per quali valori di `condizione0` e `condizione1` la funzione restituisce `True`?

```python
def f(condizione0, condizione1):
    if condizione0 and not condizione1:
        return condizione1
    elif condizione1:
        return False
    return True
```

## Risposte

- [ ] `True`, `True`
- [ ] `True`, `False`
- [ ] `False`, `True`
- [x] `False`, `False`

# 2

Sia `n` un intero positivo, qual è il valore di `i+j` al termine del seguente frammento di codice?

```python
i, j = 0, 2*n
while i < j:
    i += 1
    j -= 1
```

## Risposte

- [ ] `2n-1`
- [ ] `0`
- [ ] `n-1`
- [x] `2n`
- [ ] `n`

# 3

Sia `k` un intero positivo, cosa viene stampato dal seguente frammento di codice?

```python
n = 2*k+1
a, b = n/2, n/2

print(int(a)+int(b) < int(a+b))
```

## Risposte

- [ ] `False`
- [ ] `0`
- [ ] `n`
- [x] `True`
- [ ] una stringa

# 4

Sia `L` una lista di `n`scalari: qual è la complessità temporale e spaziale di `m(L)`?

```python
def m( a ):
    if a[0] > max( a[1:] ):
        return a[0]
    else:
        return max( a[1:] )
```

## Risposte

- [x] `Theta(n)` tempo e `Theta(n)` spazio
- [ ] `Theta(n)` tempo e `O(1)` spazio
- [ ] `Theta(n*n)` tempo e `O(1)` spazio
- [ ] `O(n)` tempo e `O(1)` spazio
- [ ] `Theta(n*n)`tempo e`Theta(n)` spazio

# 5

Si consideri il seguente frammento di codice. Per quali tipi di `a`, `b`  e `c` il valore di `x` non è definito?

```python
x =  a*b+c
```

## Risposte

- [ ] `type(a) == int`,`type(b) == str`, `type(c) == str`
- [ ] `type(a) == int`,`type(b) == tuple`, `type(c) == tuple`
- [ ] `type(a) == tuple`,`type(b) == int`, `type(c) == tuple`
- [ ] `type(a) == float`,`type(b) == int`, `type(c) == int`
- [ ] `type(a) == int`,`type(b) == int`, `type(c) == tuple`
- [ ] `type(a) == str`,`type(b) == int`, `type(c) == str`

# 6

Qual è il valore di  `len(t)` alla fine del seguente frammento di codice?

```python
a = 'python'
t = ('x', 'y', (1, 2, 3), 'z', a)
```

## Risposte

- [ ] 7
- [ ] 12
- [x] 5
- [ ] 10
- [ ] 1

# 7

Sia `n` un intero positivo, cosa viene stampato dal seguente programma?

```python
def f(a):
    b = a/2
    if a > 0:
        b = a
    return b*b

b = n
x = f(b)
print(b)
```

## Risposte

- [ ] `n-1`
- [ ] `(n-1)**2`
- [x] `n`
- [ ] `(n/2)**2`
- [ ] `(n//2)**2`

# 8

Siano `a` e `b` due stringhe, in quale caso tra quelli proposti `a < b`?

## Risposte

- [ ] se `a` è più corta di `b`
- [x] se `a` inizia con `'f'` e `b` con `'q'`
- [ ] se `a` è `'90'` e `b` è `'100'`
- [ ] se `a` ha meno spazi di `b`
- [ ] mai

# 9

Per quale tipo di dato è consentito aggiungere ma non cancellare elementi?

## Risposte

- [ ] liste
- [ ] tuple
- [ ] stringhe
- [x] in nessuno dei tre

# 10

Sia `t` una tupla di `n` elementi e si consideri la seguente operazione di assegnazione

```python
x0, x1, ... = t
```

dove a sinistra dell'uguale compaiono `k` variabili. In quale caso questo tipo di operazione è legale?

## Risposte

- [ ] solo se `k` è uguale a `n`
- [ ] solo se `k` è uguale a 1
- [x] se `k` è uguale a `n` oppure a 1
- [ ] se `k` è maggiore o uguale a `n` 
- [ ] se `k` è minore o uguale a `n`
