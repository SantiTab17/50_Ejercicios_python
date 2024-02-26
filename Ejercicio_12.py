#13. Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par.
n1 = int(input('Ingrese un número de dos digitos '))
n2 = int(input('Ingrese otro número de dos digitos '))
if n1 > 9 and n1 < 100 and n2 > 9 and n2 < 100:
    sum = n1 + n2
    if sum %2 == 0:
        print('La suma de los números origina un par')
    else:print('La suma de los números no origina un par')