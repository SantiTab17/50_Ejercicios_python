#Leer un numero de dos digitos menor que 20 y determinar si es primo.
n1 = int(input('Ingrese un número de dos digitos '))
i= 0
cont = 1
if n1 > 9 and n1 < 20:
    if n1 == 11 or n1 == 13 or n1 == 17 or n1 == 19:
        print(f'El número {n1} es primo')
    else:
        print(f'El número {n1} no es primo')

