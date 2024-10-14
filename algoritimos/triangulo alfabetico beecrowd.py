def triângulo_alfabético(N):
    linha = 1
    
    while linha <= N:
        resultado = ""
        
        if linha == 1:
            letra = 'A'
        elif linha == 2:
            letra = 'B'
        elif linha == 3:
            letra = 'C'
        elif linha == 4:
            letra = 'D'
        elif linha == 5:
            letra = 'E'
        elif linha == 6:
            letra = 'F'
        elif linha == 7:
            letra = 'G'
        elif linha == 8:
            letra = 'H'
        elif linha == 9:
            letra = 'I'
        elif linha == 10:
            letra = 'J'
        elif linha == 11:
            letra = 'K'
        elif linha == 12:
            letra = 'L'
        elif linha == 13:
            letra = 'M'
        elif linha == 14:
            letra = 'N'
        elif linha == 15:
            letra = 'O'
        elif linha == 16:
            letra = 'P'
        elif linha == 17:
            letra = 'Q'
        elif linha == 18:
            letra = 'R'
        elif linha == 19:
            letra = 'S'
        elif linha == 20:
            letra = 'T'
        elif linha == 21:
            letra = 'U'
        elif linha == 22:
            letra = 'V'
        elif linha == 23:
            letra = 'W'
        elif linha == 24:
            letra = 'X'
        elif linha == 25:
            letra = 'Y'
        elif linha == 26:
            letra = 'Z'

        coluna = 1
        while coluna <= linha:
            resultado += letra
            coluna += 1
        
        print(resultado)
        
        linha += 1

N = int(input())

if N >= 1 and N <= 26:
    triângulo_alfabético(N)

