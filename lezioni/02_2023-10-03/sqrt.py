

x = input('Immetti un numero ')

#x = int(x)

x = float(x)

g = x

print(type(g)) # mostra il tipo di g

while abs(g*g - x) > 0.00001 :
    # inizio del testo indentato, inizio blocco
    print (g)
    g = 0.5*(g+x/g)
    # fine del testo indentato, fine blocco

mess = 'la radice quadrata di x è'

print( mess, g)

print(type(mess))

print('la radice quadrata di', x, 'è', g)

