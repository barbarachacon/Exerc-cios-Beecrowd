total = 0.0
qtd = 0

while qtd < 5:
    preco = float(input('Preço ?'))
    total += preco
    qtd += 1

print(f'Total = R$ {total:.2f}')
