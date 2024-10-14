data = input()

dia = 0
mes = 0
ano = 0

i = 0

while i < 2:
    dia = dia * 10 + int(data[i])
    i += 1

i += 1

while i < 5:
    mes = mes * 10 + int(data[i])
    i += 1

i += 1

while i < 10:
    ano = ano * 10 + int(data[i])
    i += 1

soma = dia + mes + ano

if soma % 2 == 0:
    print("par")
else:
    print("impar")
