a = int(input())

b = int(input())

c = int(input())

d = int(input())

e = int(input())
 
qtd_pares = 0
 
if a % 2 == 0:

    qtd_pares += 1
 
if b % 2 == 0:

    qtd_pares += 1
 
if c % 2 == 0:

    qtd_pares += 1
 
if d % 2 == 0:

    qtd_pares += 1
 
if e % 2 == 0:

    qtd_pares += 1
 
print(f'{qtd_pares} valores pares')
