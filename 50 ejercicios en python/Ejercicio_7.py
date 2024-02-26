#Leer un numero entero de dos digitos y determinar si es primo y ademas si es negativo.

n1 = int(input('Ingrese un número de dos digitos '))
primos = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
if n1 < 0:
    print('El número',n1,'es negativo')
else:
    if n1 > 9 and n1 < 100:
        if n1 in primos:
            print('El número',n1,'es primo')
        else:
            print('El número',n1,'no es primo')
