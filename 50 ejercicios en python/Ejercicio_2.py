#2.leer un numero entero y determinar si tiene 3 digitos

n1 = int(input('Ingrese un número entero: '))
if n1 > 100 and n1 < 1000 :
    print('El número tiene 3 digitos')
else :
    print('El número no tiene 3 digitos')
