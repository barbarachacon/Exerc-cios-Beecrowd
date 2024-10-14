compra = input()
prazo = int(input())

if compra == 'domingo':
    if prazo == 0:
        dias = 'domingo'
    elif prazo == 1:
        dias = 'segunda'
    elif prazo == 2:
        dias = 'terca'
    elif prazo == 3:
        dias = 'quarta'
    elif prazo == 4:
        dias = 'quinta'
    elif prazo == 5:
        dias = 'sexta'
    elif prazo == 6:
        dias = 'sabado'
elif compra == 'segunda':
    if prazo == 0:
        dias = 'segunda'
    elif prazo == 1:
        dias = 'terca'
    elif prazo == 2:
        dias = 'quarta'
    elif prazo == 3:
        dias = 'quinta'
    elif prazo == 4:
        dias = 'sexta'
    elif prazo == 5:
        dias = 'sabado'
    elif prazo == 6:
        dias = 'domingo'
elif compra == 'terca':
    if prazo == 0:
        dias = 'terca'
    elif prazo == 1:
        dias = 'quarta'
    elif prazo == 2:
        dias = 'quinta'
    elif prazo == 3:
        dias = 'sexta'
    elif prazo == 4:
        dias = 'sabado'
    elif prazo == 5:
        dias = 'domingo'
    elif prazo == 6:
        dias = 'segunda'
elif compra == 'quarta':
    if prazo == 0:
        dias = 'quarta'
    elif prazo == 1:
        dias = 'quinta'
    elif prazo == 2:
        dias = 'sexta'
    elif prazo == 3:
        dias = 'sabado'
    elif prazo == 4:
        dias = 'domingo'
    elif prazo == 5:
        dias = 'segunda'
    elif prazo == 6:
        dias = 'terca'
elif compra == 'quinta':
    if prazo == 0:
        dias = 'quinta'
    elif prazo == 1:
        dias = 'sexta'
    elif prazo == 2:
        dias = 'sabado'
    elif prazo == 3:
        dias = 'domingo'
    elif prazo == 4:
        dias = 'segunda'
    elif prazo == 5:
        dias = 'terca'
    elif prazo == 6:
        dias = 'quarta'
elif compra == 'sexta':
    if prazo == 0:
        dias = 'sexta'
    elif prazo == 1:
        dias = 'sabado'
    elif prazo == 2:
        dias = 'domingo'
    elif prazo == 3:
        dias = 'segunda'
    elif prazo == 4:
        dias = 'terca'
    elif prazo == 5:
        dias = 'quarta'
    elif prazo == 6:
        dias = 'quinta'
elif compra == 'sabado':
    if prazo == 0:
        dias = 'sabado'
    elif prazo == 1:
        dias = 'domingo'
    elif prazo == 2:
        dias = 'segunda'
    elif prazo == 3:
        dias = 'terca'
    elif prazo == 4:
        dias = 'quarta'
    elif prazo == 5:
        dias = 'quinta'
    elif prazo == 6:
        dias = 'sexta'


if prazo == 0:
    print("chega hoje!")
else:
    print(f"sera entregue {dias}")
