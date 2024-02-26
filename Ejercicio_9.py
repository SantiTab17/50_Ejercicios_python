#Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
n1 = int(input('Ingrese un número de dos digitos '))
d1 = n1//10
d2 = n1%10
if n1 > 9 and n1 < 100: 
    if d1 == d2:
        print('Los dos digitos son iguales')
    else:print('Los dos digitos no son iguales')