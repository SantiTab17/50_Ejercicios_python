#15. Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos.
#//100 //10 parte entera de parte en dos %10
n1 = int(input('Ingrese un número entero de 3 digitos '))
primerDigito = n1 // 100
parteEntera = n1 // 10
segundoDigito = parteEntera % 10
tercerDigito = n1 % 10
if n1 > 100 and n1 < 1000:
    sum = primerDigito + segundoDigito + tercerDigito
    print('La suma de sus dígitos es igual a',sum)