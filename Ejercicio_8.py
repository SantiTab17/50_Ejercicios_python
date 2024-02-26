#Leer un numero de dos digitos y determinar si sus dos digitos son primos.

n1 = int(input('Ingrese un número de dos digitos '))
if n1 > 9 and n1 < 100:
    cont = 0
    i = 2
    while i < n1 and cont == 0:
        rest = n1%i
        if rest == 0:
            cont+=1
        i+=1
        if cont == 0:
            print('Los dos digitos son primos')
        else: print('Uno de los digitos no es primo')
