#Leer un numero de dos digitos y determinar si ambos digitos son pares.
n1 = int(input('Ingrese un número de dos digitos '))
if n1 > 9 and n1 < 100:
    d1 = int(n1/10)
    d2 = n1%10
    if d1 % 2 == 0 and d2 % 2 == 0: 
        print('Los dos números ingresados son pares')
    elif d1 % 2 == 0:
        print('Solo el número',d1,'es par')
    elif d2 % 2 == 0:
        print('Solo el número ',d2,'es par')
    else:
        print('Ningun digito es par')