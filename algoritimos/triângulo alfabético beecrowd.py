N = int(input())

if 1 <= N <= 26:
    linha = 1
    while linha <= N:
        letra = 'A'
        resultado = ''
        contagem = 1
        
        while contagem <= linha:
            resultado += letra
            contagem += 1
        
        print(resultado)
        linha += 1
