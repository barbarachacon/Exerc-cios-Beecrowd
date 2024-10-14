N = int(input("Digite um número natural (0 <= N <= 10): "))


if 0 <= N <= 10:
    i = 1
    while i <= 10:
        resultado = N * i
        print(f"{N} x {i} = {resultado}")  
        i += 1
